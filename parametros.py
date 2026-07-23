"""
PARAMETROS - Definición y documentación de parámetros para simulación
Mercado eléctrico chileno

Cada parámetro tiene:
- Nombre: identificador único
- Tipo: qué tipo de dato es
- Rango: valores válidos/típicos
- Unidad: en qué se mide
- Descripción: qué es y cómo obtenerlo
- Ejemplo: caso real típico
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List


class TarifaType(Enum):
    """Opciones tarifarias en Chile según CNE"""
    BT1 = "BT1"  # Baja tensión simple (residencial, <10kW)
    BT2 = "BT2"  # Medición energía + contratación potencia (comercio)
    BT3 = "BT3"  # Medición energía + demanda máxima (manufactura pequeña)
    BT4 = "BT4"  # Medición energía + demanda punta + máxima (industria)


@dataclass
class Parametros:
    """
    Parámetros que DEFINES TÚ para simular un cliente específico
    Basados en datos reales del mercado eléctrico chileno
    """

    # ============ IDENTIFICACIÓN DEL CLIENTE ============
    nombre_cliente: str
    # Descripción: Nombre o descripción de tu cliente
    # Ejemplo: "Tienda de congelados Pastelería La Merced"
    # Cómo obtenerlo: Es tu cliente específico

    tarifa: TarifaType
    # Descripción: Opción tarifaria en la que está clasificado
    # Opciones válidas: BT1, BT2, BT3, BT4
    # Cómo obtenerlo: Ver factura eléctrica o llamar a tu distribuidor
    # BT2: Pequeños comercios (tiendas, oficinas, call centers)
    # BT3: Pequeña manufactura con medición de demanda
    # BT4: Industria con demanda punta

    # ============ CONSUMO ENERGÉTICO MENSUAL ============
    energia_mensual_kwh: float
    # Descripción: Kilovatios-hora consumidos en un mes típico
    # Unidad: kWh/mes
    # Rango típico BT2: 1,500 - 15,000 kWh/mes
    # Rango típico BT3: 5,000 - 50,000 kWh/mes
    # Cómo obtenerlo: Revisar última factura eléctrica, línea "energía consumida"
    # Ejemplos reales:
    #   - Tienda congelados pequeña: 3,000 kWh/mes
    #   - Call center 30 puestos: 2,500 kWh/mes
    #   - Taller/manufactura: 8,000 kWh/mes

    # ============ DEMANDA DE POTENCIA ============
    demanda_maxima_kw: float
    # Descripción: Máxima potencia instantánea que consume en el mes
    # Unidad: kW
    # Rango típico BT2: 10-50 kW
    # Rango típico BT3: 40-150 kW
    # Cómo obtenerlo: Revisar factura, línea "demanda máxima medida"
    # Nota: En BT2 puede ser contratada; en BT3+ es medida
    # Ejemplos:
    #   - Tienda congelados: 40-60 kW (refrigeración es la mayor demanda)
    #   - Call center: 15-25 kW (computadores + aire acondicionado)
    #   - Manufactura: 80-150 kW (maquinaria)

    demanda_punta_kw: float
    # Descripción: Potencia durante horas punta (solo BT4, opcional para BT3)
    # Unidad: kW
    # Rango: Suele ser 60-80% de demanda máxima
    # Período punta en Chile: abril-septiembre, 18:00-22:00 hrs
    # Cómo obtenerlo: Si factura muestra "demanda punta medida", úsalo
    # Si no aparece, estimar como 70% de demanda_maxima_kw
    # Impacto: Genera recargos significativos en periodos punta

    # ============ FACTOR DE POTENCIA ============
    factor_potencia_actual: float
    # Descripción: Eficiencia de uso de energía (ratio potencia real/aparente)
    # Unidad: Sin unidad (0 a 1)
    # Rango típico: 0.75 - 0.95
    # Límite legal: 0.93 (bajo esto genera recargos)
    # Cómo obtenerlo: Revisar factura, línea "factor de potencia"
    #
    # Casos típicos:
    #   - Tienda con refrigeración: 0.80-0.85 (equipos inductivos)
    #   - Call center/oficina: 0.88-0.92 (menos cargas inductivas)
    #   - Manufactura con motores: 0.75-0.85 (muchos equipos inductivos)
    #
    # Por qué importa:
    # - Factor <0.93 → recargo de 1% POR CADA 0.01 bajo 0.93
    # - Ejemplo: Factor 0.85 → recargo de 8% en la factura
    # - Ejemplo: Factor 0.80 → recargo de 13% en la factura

    recargo_factor_potencia_pct: float
    # Descripción: Porcentaje de recargo por factor de potencia bajo
    # Unidad: %
    # Cálculo: (0.93 - factor_potencia_actual) * 100
    # Ejemplo: Si factor=0.85, recargo = (0.93-0.85)*100 = 8%
    # Impacto: Afecta directamente a la factura total
    # Nota: En factura aparece como línea separada o incluida en energía

    # ============ INFORMACIÓN TARIFARIA (DEL DISTRIBUIDOR) ============
    precio_energia_clp_per_kwh: float
    # Descripción: Precio unitario de energía según distribuidor
    # Unidad: CLP/kWh
    # Rango actual Chile (2026): $180-220 CLP/kWh (varía por zona)
    # Cómo obtenerlo: Revisar factura, línea "precio unitario energía"
    # Varía por: distribuidor (Enel, CGE, Saesa, etc.), zona, temporada
    # Nota: CNE actualiza precios cada año (abril típicamente)

    precio_potencia_clp_per_kw: float
    # Descripción: Precio unitario de potencia contratada/medida
    # Unidad: CLP/kW/mes
    # Rango actual Chile (2026): $12,000-18,000 CLP/kW/mes
    # Cómo obtenerlo: Revisar factura, línea "precio potencia"
    # Nota: Este cargo se multiplica por tu demanda máxima cada mes
    # Impacto: Factura mensual = (energía × precio_energía) + (demanda × precio_potencia)

    precio_potencia_punta_clp_per_kw: float
    # Descripción: Precio adicional para demanda en horas punta (si aplica)
    # Unidad: CLP/kW/mes (durante período punta)
    # Rango: Suele ser similar o mayor que precio_potencia normal
    # Cuándo aplica: En BT4 obligatorio; en BT3 opcional según distribuidor
    # Período: Abril-septiembre, 18:00-22:00 hrs
    # Nota: Si no tienes este dato, dejar en 0


# ============ PARÁMETROS TÍPICOS REALES CHILENOS ============

EJEMPLO_TIENDA_CONGELADOS = Parametros(
    nombre_cliente="Tienda de Congelados - Pequeña",
    tarifa=TarifaType.BT2,
    energia_mensual_kwh=3500,
    demanda_maxima_kw=55,
    demanda_punta_kw=45,  # ~80% de la máxima
    factor_potencia_actual=0.83,  # Refrigeración típicamente baja
    recargo_factor_potencia_pct=10.0,  # (0.93 - 0.83) * 100
    precio_energia_clp_per_kwh=195,  # Precio promedio 2026
    precio_potencia_clp_per_kw=14500,
    precio_potencia_punta_clp_per_kw=18000,
)

EJEMPLO_CALL_CENTER = Parametros(
    nombre_cliente="Call Center - 30 Puestos",
    tarifa=TarifaType.BT2,
    energia_mensual_kwh=2800,  # Menos que tienda (sin refrigeración industrial)
    demanda_maxima_kw=22,  # Computadores + aire acondicionado
    demanda_punta_kw=18,  # ~80% de máxima
    factor_potencia_actual=0.90,  # Mejor que tienda (equipos más simples)
    recargo_factor_potencia_pct=3.0,  # (0.93 - 0.90) * 100
    precio_energia_clp_per_kwh=195,
    precio_potencia_clp_per_kw=14500,
    precio_potencia_punta_clp_per_kw=18000,
)

EJEMPLO_MANUFACTURA_PEQUENA = Parametros(
    nombre_cliente="Taller de Manufactura - Pequeño",
    tarifa=TarifaType.BT3,
    energia_mensual_kwh=12000,  # Mayor consumo por maquinaria
    demanda_maxima_kw=95,  # Motores consume mucha potencia
    demanda_punta_kw=80,  # ~85% de máxima
    factor_potencia_actual=0.78,  # Motores generan reactivos
    recargo_factor_potencia_pct=15.0,  # (0.93 - 0.78) * 100 = 15%
    precio_energia_clp_per_kwh=190,  # BT3 suele ser más barato
    precio_potencia_clp_per_kw=13500,  # BT3 tiene mejores precios
    precio_potencia_punta_clp_per_kw=17500,
)

PARAMETROS_TIPICOS: Dict[str, Parametros] = {
    "tienda_congelados": EJEMPLO_TIENDA_CONGELADOS,
    "call_center": EJEMPLO_CALL_CENTER,
    "manufactura": EJEMPLO_MANUFACTURA_PEQUENA,
}


def validar_parametros(p: Parametros) -> List[str]:
    """
    Valida que los parámetros sean coherentes
    Retorna lista de problemas encontrados (vacía si todo está bien)
    """
    problemas = []

    # Validaciones de rango
    if p.energia_mensual_kwh <= 0:
        problemas.append("Energía mensual debe ser positiva")

    if p.demanda_maxima_kw <= 0:
        problemas.append("Demanda máxima debe ser positiva")

    if not (0 < p.factor_potencia_actual <= 1):
        problemas.append("Factor potencia debe estar entre 0 y 1")

    if p.recargo_factor_potencia_pct < 0:
        problemas.append("Recargo no puede ser negativo")

    # Validación de coherencia
    if p.demanda_punta_kw > p.demanda_maxima_kw:
        problemas.append("Demanda punta no puede ser mayor que máxima")

    if p.precio_energia_clp_per_kwh <= 0:
        problemas.append("Precio energía debe ser positivo")

    if p.precio_potencia_clp_per_kw <= 0:
        problemas.append("Precio potencia debe ser positivo")

    # Validación del recargo vs factor potencia
    recargo_calculado = (0.93 - p.factor_potencia_actual) * 100
    if abs(recargo_calculado - p.recargo_factor_potencia_pct) > 1:  # Tolerancia de 1%
        problemas.append(
            f"Recargo {p.recargo_factor_potencia_pct}% no coincide con factor {p.factor_potencia_actual} "
            f"(debería ser ~{recargo_calculado:.1f}%)"
        )

    return problemas


def imprimir_documentacion_parametros():
    """Imprime documentación completa de todos los parámetros"""
    print("""
╔════════════════════════════════════════════════════════════════════════════════╗
║           DOCUMENTACIÓN: PARÁMETROS DEL SIMULADOR                              ║
║                  Mercado Eléctrico Chileno                                     ║
╚════════════════════════════════════════════════════════════════════════════════╝

═══ 1. IDENTIFICACIÓN ═══

nombre_cliente (str)
  Descripción: Identificador del cliente que simulas
  Ejemplo: "Tienda de congelados La Merced"
  Uso: Solo descriptivo, para reportes

tarifa (BT1/BT2/BT3/BT4)
  Descripción: Categoría tarifaria según CNE

  BT1: Baja tensión simple
    → Residencial o muy pequeño comercio
    → Potencia conectada <10 kW
    → Raramente usado en empresas

  BT2: Medición energía + contratación potencia
    → Pequeños comercios y oficinas
    → Demanda típica 10-50 kW
    → NO mide demanda punta
    → EJEMPLOS: tiendas, call centers, consultorios

  BT3: Medición energía + demanda máxima
    → Pequeña manufactura
    → Demanda típica 40-150 kW
    → Mide demanda máxima pero NO demanda punta
    → EJEMPLOS: talleres, pequeñas fábricas

  BT4: Medición energía + demanda máxima + punta
    → Industria mediana/grande
    → Demanda >100 kW
    → Mide demanda punta (horas específicas)
    → EJEMPLOS: plantas industriales, grandes manufacturas

  Cómo saber tu tarifa:
    1. Revisar factura eléctrica
    2. Llamar a tu distribuidor (Enel, CGE, Saesa, etc.)
    3. Revisar contrato de suministro

═══ 2. CONSUMO ENERGÉTICO ═══

energia_mensual_kwh (float)
  Descripción: Total de kWh consumido en mes típico
  Unidad: kWh/mes
  Rango BT2: 1,500 - 15,000 kWh/mes
  Rango BT3: 5,000 - 50,000 kWh/mes

  Ejemplos reales CHILE:
  - Tienda pequeña (100 m²): 2,000-3,000 kWh
  - Tienda congelados (200 m²): 3,500-5,000 kWh
  - Call center (50 puestos): 3,000-4,000 kWh
  - Taller mecánica: 8,000-12,000 kWh
  - Panadería: 5,000-8,000 kWh (horno consume mucho)

  Cómo obtenerlo:
    1. Revisar 3 últimas facturas
    2. Sacar promedio (consumo varía por estación)
    3. Usar para mes "típico" (no incluir picos anormales)

  Nota: Verano vs invierno pueden diferir hasta 30% (aire acondicionado)

═══ 3. DEMANDA DE POTENCIA ═══

demanda_maxima_kw (float)
  Descripción: Máxima potencia instantánea en el mes
  Unidad: kW
  Rango BT2: 10-50 kW
  Rango BT3: 40-150 kW

  Ejemplos reales CHILE:
  - Tienda: 30-50 kW (iluminación + refrigeración)
  - Call center: 15-25 kW (computadores + aire acondicionado)
  - Taller con maquinaria: 80-120 kW
  - Panadería con horno: 40-60 kW

  Cómo obtenerlo:
    1. Revisar factura: línea "demanda máxima medida" o "potencia contratada"
    2. En BT2: tú contratas; en BT3+: se mide automáticamente
    3. Si no aparece, consultar con distribuidor

  Por qué importa:
    - Afecta ~30-40% de la factura en BT2
    - En BT3/BT4 afecta aún más
    - Mayor demanda = mayor recargo aunque no uses
    - Reducir demanda es objetivo de eficiencia energética

demanda_punta_kw (float)
  Descripción: Potencia máxima durante horas punta
  Unidad: kW
  Período punta en Chile: Abril-septiembre, 18:00-22:00 horas
  Rango típico: 60-85% de demanda_maxima

  Por qué aplica:
    - CNE define horas punta para incentivar reducción en picos
    - Tarifa de potencia punta es MÁS CARA
    - Solo aplica en BT4 obligatorio; en BT3 es opcional

  Cómo obtenerlo:
    1. Si tu factura muestra "demanda punta", úsalo directo
    2. Si no, estimar como 70-75% de demanda máxima
    3. Revisar si hay "horas de punta" en tu contrato

  Impacto:
    - Recargo adicional durante 4 meses (abril-septiembre)
    - Típicamente 20-30% más caro que potencia normal

═══ 4. FACTOR DE POTENCIA ═══

factor_potencia_actual (float)
  Descripción: Medida de EFICIENCIA en uso de energía
  Símbolo en Chile: "Fp" o "cos φ"
  Unidad: Decimal (0 a 1)
  Límite legal: 0.93 (por debajo genera MULTAS)

  Rango típico por industria:
  - Tienda/oficina: 0.85-0.92 (bueno)
  - Manufactura sin corrección: 0.75-0.85 (malo)
  - Manufactura con condensadores: 0.92-0.98 (excelente)

  Qué significa:
    0.95 = 95% de energía se convierte en trabajo útil
    0.80 = Solo 80% es trabajo útil; 20% es energía "desperdiciada" reactiva

  Cómo obtenerlo:
    1. Revisar factura: línea "factor de potencia" o "Fp"
    2. Típicamente aparece en forma decimal (ej: 0.83)
    3. Si no aparece, contactar distribuidor

  Por qué es importante:
    - Factor <0.93 genera recargos
    - Recargo = 1% POR CADA 0.01 bajo 0.93
    - Ejemplo: Fp=0.85 → recargo = (0.93-0.85)×100 = 8%
    - Ejemplo: Fp=0.80 → recargo = (0.93-0.80)×100 = 13%

  Quién tiene factor bajo:
    - Equipos con motores (refrigeración, máquinas)
    - Transformadores
    - Hornos industriales
    - Soldadoras

  Cómo mejorarlo:
    - CONDENSADORES (solución más común)
    - Cambiar a equipos más eficientes
    - Instalar filtros armónicos

recargo_factor_potencia_pct (float)
  Descripción: Porcentaje de costo adicional por factor bajo
  Unidad: %

  Cálculo automático:
    recargo = (0.93 - factor_potencia_actual) × 100

  Ejemplos:
    - Factor 0.93: recargo 0% (sin penalidad)
    - Factor 0.90: recargo 3% (legal pero con costo)
    - Factor 0.85: recargo 8% (típico manufactura)
    - Factor 0.80: recargo 13% (muy bajo, muy caro)

  Impacto en factura:
    Si factura es $1M y factor baja a 0.85:
    → Costo adicional = $1M × 8% = $80,000/mes
    → En un año = $960,000 por ineficiencia

═══ 5. PRECIOS TARIFARIOS ═══

precio_energia_clp_per_kwh (float)
  Descripción: Valor unitario de cada kWh consumido
  Unidad: CLP/kWh
  Rango actual CHILE 2026: $180-220 CLP/kWh

  Varía según:
    - Distribuidor: Enel, CGE, Saesa, Edelmag, etc.
    - Zona geográfica: Sur más caro que Centro
    - Temporada: Invierno puede ser 10-20% más caro

  Cómo obtenerlo:
    1. Revisar factura: línea "precio unitario energía"
    2. Dividir: (total energía en $) / (kWh consumidos)
    3. Llamar a distribuidor para precio vigente

  Nota: CNE actualiza precios cada año (típicamente en abril)

precio_potencia_clp_per_kw (float)
  Descripción: Costo mensual de cada kW de potencia demandada
  Unidad: CLP/kW/mes
  Rango actual CHILE 2026: $12,000-18,000 CLP/kW/mes

  Cómo funciona:
    - Es INDEPENDIENTE de cuánto consumas
    - Si contratas 50 kW, pagas 50 × precio_potencia cada mes
    - Incluso si no los usas todos

  Cómo obtenerlo:
    1. Revisar factura: línea "cargo por potencia"
    2. Dividir: (total potencia en $) / (kW contratados)

  Impacto:
    Factura típica BT2 = (energía×precio_e) + (potencia×precio_p)
    Ejemplo 50 kW:
    - Potencia: 50 × $15,000 = $750,000/mes
    - Es ~30% de factura aunque uses solo 60% de capacidad

precio_potencia_punta_clp_per_kw (float)
  Descripción: Cargo adicional para demanda durante horas punta
  Unidad: CLP/kW/mes
  Rango actual: $15,000-22,000 CLP/kW/mes (MÁS CARO)
  Cuándo aplica: Solo abril-septiembre, 18:00-22:00 horas

  Cómo funciona:
    - Es ADICIONAL al cargo de potencia normal
    - Solo se paga en meses con horas punta
    - Si redues demanda en punta, ahorras MUCHO

  Impacto económico:
    Si demanda_punta = 40 kW y precio = $18,000/kW:
    - Costo en punta = 40 × $18,000 × 6 meses = $4,320,000
    - Es el objetivo principal de BESS y otras soluciones

╚════════════════════════════════════════════════════════════════════════════════╝
    """)
