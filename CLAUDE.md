# CLAUDE.md

Guía para trabajar en este repositorio con Claude Code.

## Qué es este proyecto

Base de conocimiento e investigación + prototipos de simulación para un **sistema de gestión de energía** dirigido al mercado de **pequeñas y medianas empresas (PYMES) en Chile**.

El objetivo de negocio es que las PYMES logren:

- Un **uso eficiente de la energía** (eléctrica primero; térmica más adelante).
- **Cumplimiento de las normas ISO 50001 (Sistemas de Gestión de la Energía) e ISO 50002 (Auditorías Energéticas)**, con miras a la familia ISO 50000 (M&V con ISO 50006/50015).
- **Postular a financiamiento público bajo un modelo ESCO** (Empresa de Servicios Energéticos). Programa ancla verificado (jul 2026): **"Ponle Energía a tu Pyme"** del **Ministerio de Energía + Agencia de Sostenibilidad Energética (AgenciaSE)** — cofinancia hasta 50–80% según tamaño de empresa ([ficha](https://www.agenciase.org/energia-a-tu-pyme/), [plataforma](https://energia.gob.cl/pfinanciamiento)). El modelo ESCO se declara en el **Registro Energético** de AgenciaSE (www.agenciase.cl); gremio de referencia **ANESCO Chile**. Detalle y fuentes en `03_SUBSIDIOS_FINANCIAMIENTO.md`.

El propósito del repositorio es ser **suficientemente robusto y bien fundamentado** para sostener un juicio informado en conversaciones con clientes, inversionistas y partners. Toda afirmación numérica debe poder trazarse a una fuente (CNE, distribuidoras) o marcarse explícitamente como estimación.

## Estructura del repositorio

### Documentación de investigación (Markdown)

Numerada por "zonas" temáticas; leer en orden da la tesis completa del negocio:

| Archivo | Contenido |
|---------|-----------|
| `00_ESTRUCTURA_TARIFARIA_CHILE.md` | Tarifas BT1–BT4, componentes de cobro, dónde está el costo real |
| `01_MERCADO_PYMES_CHILE.md` | Segmento BT2/BT3, TAM, preguntas de mercado abiertas |
| `02_TECNICO_HARDWARE_ARQUITECTURA.md` | Stack: medidor Eastron SDM630, gateway Teltonika RUT956, Railway + Supabase, dashboard (ver stack elegido abajo) |
| `03_SUBSIDIOS_FINANCIAMIENTO.md` | FFEE, BancoEstado, CORFO, Certificados de Eficiencia (CEE) |
| `04b_SERVICIO_INTEGRADO_ESCO.md` | Definición del servicio ESCO, modelo EPC/SaaS/híbrido, ciclo de servicio |
| `05_GOMARKET_ELECTRICISTAS.md` | Go-to-market vía electricistas como canal |
| `06_ROADMAP_TECNICO_MVP.md` | Roadmap de desarrollo (MVP → EPC), 6 meses |
| `07_MODELO_ESI_BID.md` | **Fuente primaria BID (IDB-TN-2038)**: Modelo ESI, mercado potencial PYME, tecnologías, TIR/payback, financiamiento BancoEstado |
| `08_PANORAMA_INDUSTRIA.md` | Contraste oferta/demanda (vs. RENMAD/ATA/ACERA), Net Billing vs. PMGD, fuentes de vigilancia regulatoria |
| `FUENTES_Y_DESPERDICIO.md` | **Fuente clave**: cuantificación del desperdicio + todas las fuentes citadas (CNE, distribuidoras, estudios) |
| `README.md` | Guía rápida y resumen de los 6 casos analizados |
| `fuentes_pdf/` | PDFs oficiales de respaldo (evidencia). **No leerlos** — ver abajo. |

### Simuladores (Python, sin dependencias externas)

Solo biblioteca estándar (`dataclasses`, `enum`, `typing`). No hay `requirements.txt` porque no hace falta. Requiere Python 3.

| Archivo | Rol |
|---------|-----|
| `parametros.py` | Define `TarifaType` (BT1–BT4), `Parametros` (cliente), y 6 clientes reales precargados. Documentación de cada parámetro. |
| `factura_electrica.py` | `CalculadoraFactura` / `DetalleFactura`: calcula la factura mensual según estructura CNE (energía, potencia, punta, recargo factor de potencia, VAD, IVA). |
| `simulador_eficiencia.py` | `SimuladorEficiencia` / `Solucion` / `SolucionType`: proyecta 5 años de ahorro, payback, ROI para condensadores, BESS, thermal, solar. |
| `demo_automatica.py` | **Punto de entrada principal.** Corre 6 casos sin inputs: factura → desperdicio → solución → ROI. |
| `demo_interactivo.py` | Variante que pide inputs por consola. |

Dependencias entre módulos: `demo_*` → `simulador_eficiencia` → `factura_electrica` → `parametros`.

## Ejecutar

```bash
python3 demo_automatica.py     # demo principal, sin inputs
python3 demo_interactivo.py    # versión interactiva
```

## Convenciones y reglas de dominio

- **Idioma**: todo el contenido (docs, comentarios, nombres de variables de dominio, salida de consola) está en **español**. Mantenerlo así.
- **Moneda**: CLP (pesos chilenos). Costos de hardware a veces en USD; indicar siempre la unidad.
- **Regla regulatoria central (CNE)**: el recargo por factor de potencia es **1% por cada 0.01 bajo el límite de 0.93**. Factor ≥ 0.93 = sin recargo. Cualquier cálculo que toque factor de potencia debe respetar esta regla.
- **Tarifas**: BT2 = energía + potencia contratada (comercio, 10–50 kW). BT3 = energía + demanda máxima (manufactura pequeña, >50 kW). Punta = abril–septiembre, 18:00–22:00.
- **Trazabilidad**: los números "reales" provienen de CNE 2026 y distribuidoras (Enel, CGE, Saesa, Edelmag). Los valores marcados con `*` en las tablas son estimaciones. Al agregar cifras nuevas, citar la fuente o marcarlas como estimadas — no inventar precisión.
- **Precisión declarada del simulador**: ~95%; no modela peajes de transmisión variables, contribuciones fiscales especiales ni cargos por atraso. Ver la sección "Advertencias sobre precisión" en `FUENTES_Y_DESPERDICIO.md`.

## Carpeta `fuentes_pdf/` — no leer

La carpeta `fuentes_pdf/` contiene documentos oficiales (Ministerio de Energía, SII)
descargados como **respaldo/evidencia**. **No los leas con herramientas de IA/LLM**: son
extensos y de codificación compleja (fuentes incrustadas, binario comprimido) y su lectura
gasta muchos tokens con baja señal. **Los datos relevantes ya están extraídos y citados**
en los Markdown (`01_MERCADO_PYMES_CHILE.md`, `03_SUBSIDIOS_FINANCIAMIENTO.md`). Usa esos
resúmenes citados; abre los PDF solo si un humano necesita verificar la fuente primaria.
Ver `fuentes_pdf/README.md` para el índice.

## Al hacer cambios

- Si cambias parámetros de cálculo (precios, factores), actualiza también la documentación de fuentes correspondiente para no desincronizar el discurso del negocio con el código.
- Mantén los scripts ejecutables sin dependencias externas salvo justificación explícita.
- Este repo sostiene decisiones y pitches: prioriza la **corrección de los datos y su trazabilidad** por sobre la elegancia del código.
