#!/usr/bin/env python3
"""
MD A PDF - Convierte los documentos Markdown del repositorio a PDF

Genera un PDF por cada archivo .md de la raíz del repositorio y los deja en
`docs_pdf/` (directorio de SALIDA; no confundir con `fuentes_pdf/`, que guarda
las fuentes externas de respaldo).

Sin dependencias externas: usa solo la biblioteca estándar y genera el PDF
directamente (fuentes base-14 de PDF, sin incrustar). Por eso no requiere npm,
pip, reportlab ni pandoc.

Uso:
    python3 md_a_pdf.py                 # convierte todos los .md de la raíz
    python3 md_a_pdf.py 09_PRICING_CANONICO.md   # convierte archivos puntuales
    python3 md_a_pdf.py --salida otra_carpeta

Limitaciones conocidas (por diseño, para no depender de librerías):
- Los emoji y caracteres de dibujo de caja se traducen a equivalentes ASCII
  (las fuentes base-14 solo cubren Latin-1 / WinAnsi).
- Las tablas se renderizan en monoespaciado con ancho de columna proporcional.
- No hay imágenes ni resaltado de sintaxis.
"""

import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field

# ============ CONFIGURACIÓN DE PÁGINA (A4 en puntos) ============

ANCHO_PAGINA = 595.28
ALTO_PAGINA = 841.89
MARGEN_IZQ = 56.0
MARGEN_DER = 56.0
MARGEN_SUP = 56.0
MARGEN_INF = 52.0

ANCHO_UTIL = ANCHO_PAGINA - MARGEN_IZQ - MARGEN_DER

# Fuentes disponibles (base-14, no requieren incrustación)
F_NORMAL = "F1"      # Helvetica
F_BOLD = "F2"        # Helvetica-Bold
F_ITALIC = "F3"      # Helvetica-Oblique
F_MONO = "F4"        # Courier
F_MONO_BOLD = "F5"   # Courier-Bold (encabezados de tabla: debe alinear con F_MONO)

TAM_CUERPO = 9.8
INTERLINEADO = 1.42          # múltiplo del tamaño de fuente
TAM_MONO = 8.0
TAM_TABLA = 7.6

# Tamaños por nivel de encabezado
TAM_TITULOS = {1: 17.0, 2: 13.5, 3: 11.5, 4: 10.4, 5: 10.0, 6: 10.0}


# ============ ANCHOS DE CARACTER (unidades/1000 del tamaño de fuente) ============
# Métricas oficiales AFM de Helvetica / Helvetica-Bold para ASCII imprimible.

_HELV = (
    "278 278 355 556 556 889 667 191 333 333 389 584 278 333 278 278 "
    "556 556 556 556 556 556 556 556 556 556 278 278 584 584 584 556 "
    "1015 667 667 722 722 667 611 778 722 278 500 667 556 833 722 778 "
    "667 778 722 667 611 722 667 944 667 667 611 278 278 278 469 556 "
    "333 556 556 500 556 556 278 556 556 222 222 500 222 833 556 556 "
    "556 556 333 500 278 556 500 722 500 500 500 334 260 334 584"
)

_HELV_BOLD = (
    "278 333 474 556 556 889 722 238 333 333 389 584 278 333 278 278 "
    "556 556 556 556 556 556 556 556 556 556 333 333 584 584 584 611 "
    "975 722 722 722 722 667 611 778 722 278 556 722 611 833 722 778 "
    "667 778 722 667 611 722 667 944 667 667 611 333 278 333 584 556 "
    "333 556 611 556 611 556 333 611 611 278 278 556 278 889 611 611 "
    "611 611 389 556 333 611 556 778 556 556 500 389 280 389 584"
)


def _tabla_anchos(serie: str) -> dict:
    """Convierte la serie AFM (desde el carácter espacio) en un dict char->ancho."""
    valores = [int(v) for v in serie.split()]
    return {chr(32 + i): v for i, v in enumerate(valores)}


ANCHOS = {
    F_NORMAL: _tabla_anchos(_HELV),
    F_BOLD: _tabla_anchos(_HELV_BOLD),
    F_ITALIC: _tabla_anchos(_HELV),  # Oblique comparte métricas con Helvetica
}
ANCHO_MONO = 600  # Courier es de ancho fijo


def ancho_texto(texto: str, fuente: str, tam: float) -> float:
    """Ancho en puntos de un texto para la fuente y tamaño dados."""
    if fuente in (F_MONO, F_MONO_BOLD):
        return len(texto) * ANCHO_MONO * tam / 1000.0
    tabla = ANCHOS.get(fuente, ANCHOS[F_NORMAL])
    total = 0
    for ch in texto:
        # Los acentuados no están en la tabla ASCII: se aproximan con su letra base
        total += tabla.get(ch, tabla.get(_letra_base(ch), 556))
    return total * tam / 1000.0


def _letra_base(ch: str) -> str:
    """Devuelve la letra sin tilde ('é' -> 'e') para estimar anchos."""
    descompuesto = unicodedata.normalize("NFD", ch)
    return descompuesto[0] if descompuesto else ch


# ============ TRADUCCIÓN DE CARACTERES NO SOPORTADOS ============
# Las fuentes base-14 usan WinAnsi (cp1252): emoji y dibujo de caja no existen.

MAPA_CARACTERES = {
    # Emoji frecuentes en la documentación del repo
    "⚠": "[!]", "✅": "[OK]", "❌": "[X]", "✔": "[v]", "✓": "[v]",
    "⏳": "[...]", "🔴": "[!]", "⭐": "*", "❗": "!",
    "📊": "", "💰": "", "💸": "", "📈": "", "🎯": "", "🚀": "", "⚡": "",
    "💡": "", "📌": "", "📂": "", "📖": "", "🔍": "", "📚": "", "🎓": "",
    "🏆": "", "🔧": "", "⚙": "", "📦": "", "🌟": "", "ℹ": "i", "👋": "",
    "🤖": "", "📄": "", "📁": "", "🔒": "", "🧭": "", "🧪": "", "🔬": "",
    # Dibujo de caja (los diagramas ASCII de las Zonas 00 y 04b)
    "│": "|", "├": "+", "└": "+", "─": "-", "┌": "+", "┐": "+", "┘": "+",
    "┤": "+", "┬": "+", "┴": "+", "┼": "+",
    "═": "=", "║": "|", "╔": "+", "╗": "+", "╚": "+", "╝": "+",
    "╠": "+", "╣": "+", "╦": "+", "╩": "+", "╬": "+",
    # Flechas y símbolos matemáticos
    "→": "->", "←": "<-", "↑": "^", "↓": "v", "⇒": "=>", "⇐": "<=",
    "≥": ">=", "≤": "<=", "≠": "!=", "≈": "~", "∞": "inf", "±": "+/-",
    # Griegas usadas en factor de potencia (cos phi)
    "ϕ": "phi", "φ": "phi", "Φ": "PHI", "Δ": "Delta", "α": "alpha", "β": "beta",
    # Subíndices (CO2)
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
}


def limpiar_texto(texto: str) -> str:
    """Traduce caracteres no representables en WinAnsi y descarta el resto."""
    # Quita selectores de variación y uniones de emoji
    texto = texto.replace("️", "").replace("‍", "").replace("⁩", "")
    salida = []
    for ch in texto:
        if ch in MAPA_CARACTERES:
            salida.append(MAPA_CARACTERES[ch])
            continue
        try:
            ch.encode("cp1252")
            salida.append(ch)
        except UnicodeEncodeError:
            # Último intento: versión sin tilde; si tampoco sirve, se descarta
            plano = unicodedata.normalize("NFKD", ch).encode("ascii", "ignore").decode()
            salida.append(plano)
    return "".join(salida)


# ============ MODELO DE CONTENIDO ============

@dataclass
class Fragmento:
    """Trozo de texto con un estilo homogéneo."""
    texto: str
    fuente: str = F_NORMAL
    tam: float = TAM_CUERPO
    gris: float = 0.0  # 0 = negro, 1 = blanco


@dataclass
class Bloque:
    """Unidad de maquetación ya lista para dibujar."""
    tipo: str                      # parrafo | codigo | tabla | regla | espacio
    lineas: list = field(default_factory=list)   # lista de listas de Fragmento
    sangria: float = 0.0
    espacio_antes: float = 0.0
    espacio_despues: float = 0.0
    fondo: bool = False


# ============ PARSEO DE MARKDOWN ============

RE_INLINE = re.compile(
    r"`([^`]+)`"                       # código
    r"|\*\*(.+?)\*\*"                  # negrita
    r"|__(.+?)__"                      # negrita alternativa
    r"|(?<!\*)\*([^*\n]+?)\*(?!\*)"    # cursiva
    r"|\[([^\]]+)\]\(([^)]+)\)"        # enlace
)


def parsear_inline(texto: str, fuente_base: str, tam: float) -> list:
    """Convierte marcas inline de Markdown en una lista de Fragmentos."""
    fragmentos = []
    pos = 0
    for m in RE_INLINE.finditer(texto):
        if m.start() > pos:
            fragmentos.append(Fragmento(texto[pos:m.start()], fuente_base, tam))
        codigo, neg1, neg2, cursiva, enlace_txt, enlace_url = m.groups()
        if codigo is not None:
            fragmentos.append(Fragmento(codigo, F_MONO, tam * 0.92))
        elif neg1 is not None or neg2 is not None:
            fragmentos.append(Fragmento(neg1 or neg2, F_BOLD, tam))
        elif cursiva is not None:
            fragmentos.append(Fragmento(cursiva, F_ITALIC, tam))
        elif enlace_txt is not None:
            fragmentos.append(Fragmento(enlace_txt, fuente_base, tam, gris=0.0))
            # La URL se conserva: el PDF es para leer/imprimir y las fuentes importan
            fragmentos.append(Fragmento(f" ({enlace_url})", F_ITALIC, tam * 0.85, gris=0.45))
        pos = m.end()
    if pos < len(texto):
        fragmentos.append(Fragmento(texto[pos:], fuente_base, tam))
    return [f for f in fragmentos if f.texto]


def parsear_markdown(md: str) -> list:
    """Convierte el Markdown completo en una lista de Bloques."""
    bloques = []
    lineas = md.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        despojada = linea.strip()

        # --- Bloque de código cercado ---
        if despojada.startswith("```"):
            cuerpo = []
            i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                cuerpo.append(lineas[i])
                i += 1
            i += 1
            bloques.append(_bloque_codigo(cuerpo))
            continue

        # --- Tabla ---
        if despojada.startswith("|") and despojada.endswith("|"):
            filas = []
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                filas.append(lineas[i].strip())
                i += 1
            bloques.append(_bloque_tabla(filas))
            continue

        # --- Línea horizontal ---
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", despojada):
            bloques.append(Bloque("regla", espacio_antes=6, espacio_despues=8))
            i += 1
            continue

        # --- Línea en blanco ---
        if not despojada:
            bloques.append(Bloque("espacio", espacio_despues=TAM_CUERPO * 0.5))
            i += 1
            continue

        # --- Encabezado ---
        m = re.match(r"^(#{1,6})\s+(.*)$", despojada)
        if m:
            nivel = len(m.group(1))
            tam = TAM_TITULOS.get(nivel, TAM_CUERPO)
            frags = parsear_inline(m.group(2), F_BOLD, tam)
            for f in frags:
                if f.fuente == F_NORMAL:
                    f.fuente = F_BOLD
            bloques.append(Bloque(
                "parrafo", [frags],
                espacio_antes=tam * (1.0 if nivel <= 2 else 0.7),
                espacio_despues=tam * 0.35,
            ))
            if nivel <= 2:
                bloques.append(Bloque("regla", espacio_despues=5))
            i += 1
            continue

        # --- Cita ---
        if despojada.startswith(">"):
            cuerpo = []
            while i < len(lineas) and lineas[i].strip().startswith(">"):
                cuerpo.append(lineas[i].strip().lstrip(">").strip())
                i += 1
            texto = " ".join(c for c in cuerpo if c)
            frags = parsear_inline(texto, F_ITALIC, TAM_CUERPO)
            for f in frags:
                if f.fuente == F_NORMAL:
                    f.fuente = F_ITALIC
                f.gris = max(f.gris, 0.25)
            bloques.append(Bloque("parrafo", [frags], sangria=14,
                                  espacio_antes=3, espacio_despues=4))
            continue

        # --- Lista (viñeta o numerada) ---
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", linea)
        if m:
            sangria_md, marca, contenido = m.groups()
            nivel = len(sangria_md) // 2
            i += 1
            # Juntar líneas de continuación del mismo ítem (texto envuelto en el
            # fuente): así un span **negrita** partido en dos líneas no se rompe.
            while i < len(lineas):
                cont = lineas[i]
                pelada = cont.strip()
                if (not pelada or pelada.startswith(("#", ">", "|", "```"))
                        or re.match(r"^(\s*)([-*+]|\d+[.)])\s+", cont)
                        or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", pelada)):
                    break
                contenido += " " + pelada
                i += 1
            vineta = "\x95" if marca in "-*+" else marca  # \x95 = bullet en cp1252
            frags = [Fragmento(f"{vineta}  ", F_NORMAL, TAM_CUERPO)]
            frags += parsear_inline(contenido, F_NORMAL, TAM_CUERPO)
            bloques.append(Bloque("parrafo", [frags],
                                  sangria=12 + nivel * 14, espacio_despues=1.5))
            continue

        # --- Párrafo normal (junta líneas hasta un corte) ---
        cuerpo = []
        while i < len(lineas):
            actual = lineas[i]
            pelada = actual.strip()
            if (not pelada or pelada.startswith(("#", ">", "|", "```"))
                    or re.match(r"^(\s*)([-*+]|\d+[.)])\s+", actual)
                    or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", pelada)):
                break
            cuerpo.append(pelada)
            i += 1
        texto = " ".join(cuerpo)
        if texto:
            bloques.append(Bloque("parrafo", [parsear_inline(texto, F_NORMAL, TAM_CUERPO)],
                                  espacio_despues=3))
    return bloques


def _bloque_codigo(cuerpo: list) -> Bloque:
    """Bloque monoespaciado con fondo gris; corta líneas demasiado largas."""
    max_chars = int((ANCHO_UTIL - 12) / (ANCHO_MONO * TAM_MONO / 1000.0))
    lineas = []
    for cruda in cuerpo:
        texto = cruda.rstrip()
        if not texto:
            lineas.append([Fragmento(" ", F_MONO, TAM_MONO)])
            continue
        while len(texto) > max_chars:
            lineas.append([Fragmento(texto[:max_chars], F_MONO, TAM_MONO)])
            texto = texto[max_chars:]
        lineas.append([Fragmento(texto, F_MONO, TAM_MONO)])
    return Bloque("codigo", lineas, sangria=6, espacio_antes=4,
                  espacio_despues=6, fondo=True)


def _bloque_tabla(filas: list) -> Bloque:
    """Renderiza la tabla en monoespaciado con columnas de ancho proporcional."""
    matriz = []
    for fila in filas:
        celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
        # Fila separadora (|---|---|)
        if all(re.fullmatch(r":?-{2,}:?", c) for c in celdas if c):
            continue
        # Quita marcas inline para que el ancho monoespaciado sea predecible
        celdas = [re.sub(r"[*`]", "", c) for c in celdas]
        celdas = [re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", c) for c in celdas]
        matriz.append(celdas)

    if not matriz:
        return Bloque("espacio")

    n_col = max(len(f) for f in matriz)
    for f in matriz:
        f.extend([""] * (n_col - len(f)))

    total_chars = int((ANCHO_UTIL - 8) / (ANCHO_MONO * TAM_TABLA / 1000.0))
    naturales = [max(len(f[c]) for f in matriz) for c in range(n_col)]
    suma = sum(naturales) + 3 * n_col
    if suma <= total_chars:
        anchos = naturales
    else:
        disponible = total_chars - 3 * n_col
        anchos = [max(8, int(n * disponible / sum(naturales))) for n in naturales]

    lineas = []
    for idx, fila in enumerate(matriz):
        # Cada celda se parte en varias líneas físicas si no cabe
        envueltas = [_envolver(fila[c], anchos[c]) for c in range(n_col)]
        alto = max(len(e) for e in envueltas)
        for n in range(alto):
            partes = []
            for c in range(n_col):
                trozo = envueltas[c][n] if n < len(envueltas[c]) else ""
                partes.append(trozo.ljust(anchos[c]))
            fuente = F_MONO_BOLD if idx == 0 else F_MONO
            lineas.append([Fragmento(" | ".join(partes), fuente, TAM_TABLA)])
        if idx == 0:
            regla = "-+-".join("-" * anchos[c] for c in range(n_col))
            lineas.append([Fragmento(regla, F_MONO, TAM_TABLA)])
    return Bloque("tabla", lineas, sangria=4, espacio_antes=4, espacio_despues=6)


def _envolver(texto: str, ancho: int) -> list:
    """Parte un texto en líneas de a lo más `ancho` caracteres."""
    if not texto:
        return [""]
    palabras, lineas, actual = texto.split(), [], ""
    for palabra in palabras:
        while len(palabra) > ancho:  # palabra sola más larga que la columna
            if actual:
                lineas.append(actual)
                actual = ""
            lineas.append(palabra[:ancho])
            palabra = palabra[ancho:]
        if not actual:
            actual = palabra
        elif len(actual) + 1 + len(palabra) <= ancho:
            actual += " " + palabra
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas or [""]


# ============ GENERACIÓN DEL PDF ============

def _escapar(texto: str) -> bytes:
    """Escapa la cadena para un literal de PDF y la codifica en WinAnsi."""
    texto = texto.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")
    return texto.encode("cp1252", "replace")


class DocumentoPDF:
    """Constructor mínimo de PDF con fuentes base-14."""

    def __init__(self, titulo: str):
        self.titulo = titulo
        self.paginas = []      # cada página es una lista de operadores (bytes)
        self.actual = None
        self.y = 0.0
        self.nueva_pagina()

    # -- manejo de páginas --------------------------------------------------
    def nueva_pagina(self):
        self.actual = []
        self.paginas.append(self.actual)
        self.y = ALTO_PAGINA - MARGEN_SUP

    def espacio_disponible(self) -> float:
        return self.y - MARGEN_INF

    # -- primitivas de dibujo ----------------------------------------------
    def texto(self, x: float, y: float, frag: Fragmento):
        if not frag.texto.strip():
            return
        gris = f"{frag.gris:.2f} g\n" if frag.gris else "0 g\n"
        self.actual.append(
            gris.encode()
            + f"BT /{frag.fuente} {frag.tam:.2f} Tf 1 0 0 1 {x:.2f} {y:.2f} Tm (".encode()
            + _escapar(frag.texto)
            + b") Tj ET\n"
        )

    def rectangulo(self, x, y, ancho, alto, gris=0.94):
        self.actual.append(
            f"{gris} g {x:.2f} {y:.2f} {ancho:.2f} {alto:.2f} re f 0 g\n".encode()
        )

    def linea(self, x1, y1, x2, y2, grosor=0.5, gris=0.75):
        self.actual.append(
            f"{gris} G {grosor} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S 0 G\n".encode()
        )

    # -- serialización ------------------------------------------------------
    def guardar(self, ruta: str):
        objetos = []           # lista de bytes (cuerpo de cada objeto)

        def agregar(cuerpo: bytes) -> int:
            objetos.append(cuerpo)
            return len(objetos)  # los números de objeto parten en 1

        # Fuentes base-14
        fuentes = {
            F_NORMAL: "Helvetica",
            F_BOLD: "Helvetica-Bold",
            F_ITALIC: "Helvetica-Oblique",
            F_MONO: "Courier",
            F_MONO_BOLD: "Courier-Bold",
        }
        ids_fuentes = {}
        for alias, nombre in fuentes.items():
            ids_fuentes[alias] = agregar(
                f"<< /Type /Font /Subtype /Type1 /BaseFont /{nombre} "
                f"/Encoding /WinAnsiEncoding >>".encode()
            )

        recursos = "<< /Font << " + " ".join(
            f"/{alias} {ids_fuentes[alias]} 0 R" for alias in fuentes
        ) + " >> >>"

        id_paginas = agregar(b"")  # se rellena al final (necesita los hijos)

        ids_pagina = []
        for contenido in self.paginas:
            flujo = b"".join(contenido)
            id_flujo = agregar(
                f"<< /Length {len(flujo)} >>\nstream\n".encode() + flujo + b"\nendstream"
            )
            ids_pagina.append(agregar(
                f"<< /Type /Page /Parent {id_paginas} 0 R "
                f"/MediaBox [0 0 {ANCHO_PAGINA:.2f} {ALTO_PAGINA:.2f}] "
                f"/Resources {recursos} /Contents {id_flujo} 0 R >>".encode()
            ))

        hijos = " ".join(f"{i} 0 R" for i in ids_pagina)
        objetos[id_paginas - 1] = (
            f"<< /Type /Pages /Count {len(ids_pagina)} /Kids [{hijos}] >>".encode()
        )

        id_info = agregar(
            b"<< /Title (" + _escapar(self.titulo) + b") /Producer (md_a_pdf.py) >>"
        )
        id_catalogo = agregar(f"<< /Type /Catalog /Pages {id_paginas} 0 R >>".encode())

        # Ensamblado con tabla xref
        salida = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = [0] * (len(objetos) + 1)
        for numero, cuerpo in enumerate(objetos, start=1):
            offsets[numero] = len(salida)
            salida += f"{numero} 0 obj\n".encode() + cuerpo + b"\nendobj\n"

        inicio_xref = len(salida)
        salida += f"xref\n0 {len(objetos) + 1}\n".encode()
        salida += b"0000000000 65535 f \n"
        for numero in range(1, len(objetos) + 1):
            salida += f"{offsets[numero]:010d} 00000 n \n".encode()
        salida += (
            f"trailer\n<< /Size {len(objetos) + 1} /Root {id_catalogo} 0 R "
            f"/Info {id_info} 0 R >>\nstartxref\n{inicio_xref}\n%%EOF\n".encode()
        )

        with open(ruta, "wb") as fh:
            fh.write(bytes(salida))


# ============ MAQUETACIÓN ============

def _envolver_fragmentos(frags: list, ancho_max: float) -> list:
    """Reparte los fragmentos en líneas que quepan en `ancho_max`."""
    lineas, actual, x = [], [], 0.0
    for frag in frags:
        # Se conserva el espaciado separando por palabras
        piezas = re.split(r"(\s+)", frag.texto)
        for pieza in piezas:
            if not pieza:
                continue
            ancho = ancho_texto(pieza, frag.fuente, frag.tam)
            if x + ancho > ancho_max and actual and pieza.strip():
                lineas.append(actual)
                actual, x = [], 0.0
                if not pieza.strip():
                    continue
            actual.append(Fragmento(pieza, frag.fuente, frag.tam, frag.gris))
            x += ancho
    if actual:
        lineas.append(actual)
    return lineas


def dibujar(doc: DocumentoPDF, bloques: list):
    """Dibuja los bloques paginando automáticamente."""
    for bloque in bloques:
        if bloque.tipo == "espacio":
            doc.y -= bloque.espacio_despues
            continue

        doc.y -= bloque.espacio_antes

        if bloque.tipo == "regla":
            if doc.espacio_disponible() < 12:
                doc.nueva_pagina()
            doc.linea(MARGEN_IZQ, doc.y, ANCHO_PAGINA - MARGEN_DER, doc.y)
            doc.y -= bloque.espacio_despues
            continue

        x0 = MARGEN_IZQ + bloque.sangria
        ancho_max = ANCHO_UTIL - bloque.sangria

        # Los párrafos se re-envuelven; código y tablas ya vienen en líneas
        if bloque.tipo == "parrafo":
            lineas = []
            for frags in bloque.lineas:
                lineas.extend(_envolver_fragmentos(frags, ancho_max))
        else:
            lineas = bloque.lineas

        for linea in lineas:
            tam = max((f.tam for f in linea), default=TAM_CUERPO)
            alto = tam * INTERLINEADO
            if doc.espacio_disponible() < alto:
                doc.nueva_pagina()
            if bloque.fondo:
                doc.rectangulo(MARGEN_IZQ, doc.y - alto + tam * 0.28,
                               ANCHO_UTIL, alto)
            x = x0
            base = doc.y - tam
            for frag in linea:
                doc.texto(x, base, frag)
                x += ancho_texto(frag.texto, frag.fuente, frag.tam)
            doc.y -= alto

        doc.y -= bloque.espacio_despues


def pie_de_pagina(doc: DocumentoPDF, nombre: str):
    """Escribe nombre del documento y número de página en cada hoja."""
    total = len(doc.paginas)
    for indice, contenido in enumerate(doc.paginas, start=1):
        doc.actual = contenido
        doc.linea(MARGEN_IZQ, MARGEN_INF - 10, ANCHO_PAGINA - MARGEN_DER,
                  MARGEN_INF - 10, grosor=0.4, gris=0.8)
        doc.texto(MARGEN_IZQ, MARGEN_INF - 21,
                  Fragmento(nombre, F_ITALIC, 7.5, gris=0.45))
        etiqueta = f"pág. {indice} de {total}"
        ancho = ancho_texto(etiqueta, F_ITALIC, 7.5)
        doc.texto(ANCHO_PAGINA - MARGEN_DER - ancho, MARGEN_INF - 21,
                  Fragmento(etiqueta, F_ITALIC, 7.5, gris=0.45))


def convertir(ruta_md: str, dir_salida: str) -> str:
    """Convierte un .md a PDF y devuelve la ruta del PDF generado."""
    with open(ruta_md, encoding="utf-8") as fh:
        contenido = fh.read()

    nombre = os.path.basename(ruta_md)
    bloques = parsear_markdown(limpiar_texto(contenido))

    doc = DocumentoPDF(titulo=nombre)
    dibujar(doc, bloques)
    pie_de_pagina(doc, nombre)

    destino = os.path.join(dir_salida, os.path.splitext(nombre)[0] + ".pdf")
    doc.guardar(destino)
    return destino


def main(argv: list) -> int:
    dir_base = os.path.dirname(os.path.abspath(__file__))
    dir_salida = os.path.join(dir_base, "docs_pdf")

    argumentos = list(argv)
    if "--salida" in argumentos:
        idx = argumentos.index("--salida")
        dir_salida = os.path.abspath(argumentos[idx + 1])
        del argumentos[idx:idx + 2]

    if argumentos:
        archivos = [os.path.abspath(a) for a in argumentos]
    else:
        archivos = sorted(
            os.path.join(dir_base, n)
            for n in os.listdir(dir_base)
            if n.lower().endswith(".md")
        )

    if not archivos:
        print("No se encontraron archivos .md que convertir.")
        return 1

    os.makedirs(dir_salida, exist_ok=True)
    print(f"Convirtiendo {len(archivos)} documento(s) a PDF")
    print(f"Destino: {dir_salida}\n")

    fallidos = 0
    for ruta in archivos:
        nombre = os.path.basename(ruta)
        try:
            destino = convertir(ruta, dir_salida)
            tam_kb = os.path.getsize(destino) / 1024
            print(f"  OK  {nombre:<38} -> {os.path.basename(destino):<38} {tam_kb:>7.1f} KB")
        except Exception as exc:  # noqa: BLE001 - queremos seguir con los demás
            fallidos += 1
            print(f"  ERROR {nombre:<36} -> {exc}")

    print(f"\nListo: {len(archivos) - fallidos} generado(s), {fallidos} con error.")
    return 0 if fallidos == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
