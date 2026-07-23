"""
SIMULADOR DE EFICIENCIA - Proyecta ahorros de soluciones de ahorro energético
"""

from dataclasses import dataclass
from enum import Enum
from parametros import Parametros
from factura_electrica import CalculadoraFactura, DetalleFactura


class SolucionType(Enum):
    """Tipos de soluciones de eficiencia disponibles"""

    CONDENSADORES = "condensadores"  # Corrige factor potencia
    BESS = "bess"  # Battery Energy Storage System - peak shaving
    BESS_THERMAL = "bess_thermal"  # BESS + almacenamiento térmico
    BESS_SOLAR = "bess_solar"  # BESS + generación solar
    COMPLETA = "completa"  # Todas integradas


@dataclass
class Solucion:
    """Define una solución de eficiencia energética"""

    tipo: SolucionType
    nombre: str

    # Inversión requerida
    capex_hardware_clp: float  # Costo de equipamiento
    capex_instalacion_clp: float  # Costo de instalación/labor

    # Qué logra la solución (impacto en parámetros)
    mejora_factor_potencia: float  # A qué FP llega (ej: 0.93)
    reduccion_demanda_punta_pct: float  # % de reducción en demanda punta
    reduccion_energia_pct: float  # % de reducción en energía total

    # Operación
    costo_saas_mensual_clp: float  # Costo de operación/monitoreo
    costo_mantenimiento_anual_clp: float  # Mantenimiento anual


@dataclass
class ProyeccionAhorro:
    """Proyección de 5 años de una solución"""

    solucion: Solucion
    ahorro_mensual_clp: float  # Ahorro promedio por mes
    capex_total_clp: float  # Inversión total inicial

    # Proyecciones a 5 años
    ahorro_total_5anos_clp: float
    costo_operacion_5anos_clp: float  # SaaS + mantenimiento
    beneficio_neto_5anos_clp: float  # Ahorro - costos operación

    # Rentabilidad
    payback_meses: float
    payback_anos: float
    roi_pct: float
    tir_aproximado: float

    # Adicional para tu negocio
    ingreso_tu_margen_hw_instalacion: float
    ingreso_tu_saas_5anos: float
    ingreso_tu_total_5anos: float


class SimuladorEficiencia:
    """
    Simula ahorros y ROI de soluciones de eficiencia
    """

    # Márgenes comerciales (para tu negocio)
    MARGEN_HARDWARE_PCT = 40  # 40% margen en venta de hardware
    MARGEN_INSTALACION_PCT = 40  # 40% margen en labor
    MARGEN_SAAS_PCT = 60  # 60% margen en SaaS recurrente

    def __init__(self, parametros_antes: Parametros):
        """
        Inicializa con parámetros del cliente ANTES de la solución
        """
        self.param_antes = parametros_antes
        self.calc_antes = CalculadoraFactura(parametros_antes)
        self.factura_antes = self.calc_antes.calcular_factura()

    def aplicar_solucion(
        self, solucion: Solucion
    ) -> tuple[Parametros, CalculadoraFactura, DetalleFactura]:
        """
        Simula parámetros DESPUÉS de aplicar la solución
        """
        # Copiar parámetros y modificarlos
        param_despues = Parametros(
            nombre_cliente=self.param_antes.nombre_cliente + f" + {solucion.nombre}",
            tarifa=self.param_antes.tarifa,
            energia_mensual_kwh=self.param_antes.energia_mensual_kwh
            * (1 - solucion.reduccion_energia_pct / 100),
            demanda_maxima_kw=self.param_antes.demanda_maxima_kw,  # No cambia
            demanda_punta_kw=self.param_antes.demanda_punta_kw
            * (1 - solucion.reduccion_demanda_punta_pct / 100),
            factor_potencia_actual=solucion.mejora_factor_potencia,
            recargo_factor_potencia_pct=max(
                0, (0.93 - solucion.mejora_factor_potencia) * 100
            ),
            precio_energia_clp_per_kwh=self.param_antes.precio_energia_clp_per_kwh,
            precio_potencia_clp_per_kw=self.param_antes.precio_potencia_clp_per_kw,
            precio_potencia_punta_clp_per_kw=self.param_antes.precio_potencia_punta_clp_per_kw,
        )

        calc_despues = CalculadoraFactura(param_despues)
        factura_despues = calc_despues.calcular_factura()

        return param_despues, calc_despues, factura_despues

    def proyectar_solucion(self, solucion: Solucion) -> ProyeccionAhorro:
        """
        Proyecta viabilidad y ROI de una solución a 5 años
        """
        # Aplicar solución
        param_despues, calc_despues, factura_despues = self.aplicar_solucion(solucion)

        # Ahorro mensual
        ahorro_mensual = self.factura_antes.total_mes_clp - factura_despues.total_mes_clp

        # CAPEX total
        capex_total = solucion.capex_hardware_clp + solucion.capex_instalacion_clp

        # Proyecciones a 5 años (60 meses)
        meses_proyeccion = 60
        ahorro_total_5anos = ahorro_mensual * meses_proyeccion

        # Costos de operación (SaaS + mantenimiento)
        costo_saas_5anos = solucion.costo_saas_mensual_clp * meses_proyeccion
        costo_mantenimiento_5anos = solucion.costo_mantenimiento_anual_clp * 5
        costo_operacion_total_5anos = costo_saas_5anos + costo_mantenimiento_5anos

        # Beneficio neto (ahorro - costos operación - capex)
        beneficio_neto = ahorro_total_5anos - costo_operacion_total_5anos - capex_total

        # Payback
        if ahorro_mensual > 0:
            payback_meses = capex_total / ahorro_mensual
        else:
            payback_meses = float("inf")
        payback_anos = payback_meses / 12

        # ROI simple (no considera TIR)
        if capex_total > 0:
            roi_pct = ((beneficio_neto + capex_total) / capex_total) * 100
        else:
            roi_pct = 0

        # TIR aproximado (simplificado)
        if payback_anos > 0:
            tir_aproximado = (ahorro_mensual * 12 / capex_total) * 100
        else:
            tir_aproximado = 0

        # Ingresos para tu startup
        margen_hw = solucion.capex_hardware_clp * (self.MARGEN_HARDWARE_PCT / 100)
        margen_instalacion = solucion.capex_instalacion_clp * (self.MARGEN_INSTALACION_PCT / 100)
        ingreso_hw_instalacion = margen_hw + margen_instalacion

        # SaaS recurrente (solo tu margen)
        ingreso_saas_mensual = solucion.costo_saas_mensual_clp * (self.MARGEN_SAAS_PCT / 100)
        ingreso_saas_5anos = ingreso_saas_mensual * meses_proyeccion

        ingreso_total_tu = ingreso_hw_instalacion + ingreso_saas_5anos

        return ProyeccionAhorro(
            solucion=solucion,
            ahorro_mensual_clp=ahorro_mensual,
            capex_total_clp=capex_total,
            ahorro_total_5anos_clp=ahorro_total_5anos,
            costo_operacion_5anos_clp=costo_operacion_total_5anos,
            beneficio_neto_5anos_clp=beneficio_neto,
            payback_meses=payback_meses,
            payback_anos=payback_anos,
            roi_pct=roi_pct,
            tir_aproximado=tir_aproximado,
            ingreso_tu_margen_hw_instalacion=ingreso_hw_instalacion,
            ingreso_tu_saas_5anos=ingreso_saas_5anos,
            ingreso_tu_total_5anos=ingreso_total_tu,
        )

    def imprimir_proyeccion(self, proyeccion: ProyeccionAhorro) -> str:
        """
        Genera reporte formateado de una proyección
        """
        s = proyeccion.solucion
        lineas = []

        lineas.append("\n" + "=" * 90)
        lineas.append(f"SIMULACIÓN DE SOLUCIÓN: {s.nombre.upper()}")
        lineas.append(f"Cliente: {self.param_antes.nombre_cliente}")
        lineas.append("=" * 90)

        # Factura actual vs después
        lineas.append(f"\n📊 COMPARATIVA DE FACTURA:")
        lineas.append(
            f"  Factura ANTES de solución:   ${self.factura_antes.total_mes_clp:>14,.0f} CLP/mes"
        )

        param_despues, calc_despues, factura_despues = self.aplicar_solucion(s)
        lineas.append(
            f"  Factura DESPUÉS de solución: ${factura_despues.total_mes_clp:>14,.0f} CLP/mes"
        )
        lineas.append(
            f"  AHORRO MENSUAL:              ${proyeccion.ahorro_mensual_clp:>14,.0f} CLP"
        )
        pct_ahorro = (proyeccion.ahorro_mensual_clp / self.factura_antes.total_mes_clp) * 100
        lineas.append(f"  Porcentaje ahorro:           {pct_ahorro:>15.1f}%")

        # Cambios en parámetros
        lineas.append(f"\n⚡ MEJORAS TÉCNICAS:")
        if param_despues.factor_potencia_actual != self.param_antes.factor_potencia_actual:
            lineas.append(
                f"  Factor potencia: {self.param_antes.factor_potencia_actual:.2f} → {param_despues.factor_potencia_actual:.2f}"
            )
            lineas.append(
                f"    Recargo anterior: {self.param_antes.recargo_factor_potencia_pct:.1f}%"
            )
            lineas.append(
                f"    Recargo nuevo: {param_despues.recargo_factor_potencia_pct:.1f}%"
            )

        if param_despues.demanda_punta_kw != self.param_antes.demanda_punta_kw:
            reduccion_punta = self.param_antes.demanda_punta_kw - param_despues.demanda_punta_kw
            pct_reduccion_punta = (reduccion_punta / self.param_antes.demanda_punta_kw) * 100
            lineas.append(
                f"  Demanda punta: {self.param_antes.demanda_punta_kw:.1f} kW → {param_despues.demanda_punta_kw:.1f} kW"
            )
            lineas.append(f"    Reducción: {reduccion_punta:.1f} kW ({pct_reduccion_punta:.1f}%)")

        if param_despues.energia_mensual_kwh != self.param_antes.energia_mensual_kwh:
            reduccion_energia = (
                self.param_antes.energia_mensual_kwh - param_despues.energia_mensual_kwh
            )
            pct_reduccion_energia = (reduccion_energia / self.param_antes.energia_mensual_kwh) * 100
            lineas.append(
                f"  Energía: {self.param_antes.energia_mensual_kwh:.0f} → {param_despues.energia_mensual_kwh:.0f} kWh/mes"
            )
            lineas.append(
                f"    Reducción: {reduccion_energia:.0f} kWh ({pct_reduccion_energia:.1f}%)"
            )

        # Inversión
        lineas.append(f"\n💰 INVERSIÓN REQUERIDA:")
        lineas.append(f"  Hardware:                    ${s.capex_hardware_clp:>14,.0f} CLP")
        lineas.append(f"  Instalación (labor):         ${s.capex_instalacion_clp:>14,.0f} CLP")
        lineas.append(f"  CAPEX TOTAL:                 ${proyeccion.capex_total_clp:>14,.0f} CLP")

        # Operación
        lineas.append(f"\n⚙️  COSTOS DE OPERACIÓN (5 años):")
        lineas.append(f"  SaaS/monitoreo:              ${s.costo_saas_mensual_clp * 60:>14,.0f} CLP")
        lineas.append(f"  Mantenimiento:               ${s.costo_mantenimiento_anual_clp * 5:>14,.0f} CLP")
        lineas.append(
            f"  Total operación (5 años):    ${proyeccion.costo_operacion_5anos_clp:>14,.0f} CLP"
        )

        # ROI del cliente
        lineas.append(f"\n✅ ROI DEL CLIENTE (5 años):")
        lineas.append(
            f"  Ahorro total (5 años):       ${proyeccion.ahorro_total_5anos_clp:>14,.0f} CLP"
        )
        lineas.append(
            f"  Menos operación:             ${proyeccion.costo_operacion_5anos_clp:>14,.0f} CLP"
        )
        lineas.append(f"  Beneficio neto (5 años):     ${proyeccion.beneficio_neto_5anos_clp:>14,.0f} CLP")

        if proyeccion.payback_anos < 100:
            lineas.append(f"  PAYBACK:                     {proyeccion.payback_anos:>15.1f} años")
        else:
            lineas.append(f"  PAYBACK:                     > 10 años (NO VIABLE)")

        lineas.append(f"  ROI (5 años):                {proyeccion.roi_pct:>15.1f}%")

        # Viabilidad
        lineas.append(f"\n🎯 ANÁLISIS DE VIABILIDAD:")
        if proyeccion.payback_anos < 3:
            lineas.append(f"  ✅ ALTAMENTE VIABLE - Payback <3 años")
        elif proyeccion.payback_anos < 5:
            lineas.append(f"  ⚠️  BORDERLINE - Payback 3-5 años")
        else:
            lineas.append(f"  ❌ NO VIABLE - Payback >5 años")

        # Tu negocio
        lineas.append(f"\n🚀 INGRESOS PARA TU STARTUP:")
        lineas.append(
            f"  Hardware + instalación:      ${proyeccion.ingreso_tu_margen_hw_instalacion:>14,.0f} CLP (one-time)"
        )
        lineas.append(
            f"  SaaS (5 años, 60% margen):   ${proyeccion.ingreso_tu_saas_5anos:>14,.0f} CLP"
        )
        lineas.append(
            f"  INGRESO TOTAL (5 años):      ${proyeccion.ingreso_tu_total_5anos:>14,.0f} CLP"
        )

        # Ratio viabilidad tu negocio
        ratio_ingresos_capex = (
            proyeccion.ingreso_tu_total_5anos / proyeccion.capex_total_clp
        )
        lineas.append(f"  Ratio ingresos/CAPEX:        {ratio_ingresos_capex:>15.1f}x")
        if ratio_ingresos_capex > 1:
            lineas.append(f"    → Viable: Ingresos > Inversión")
        else:
            lineas.append(f"    → Problema: Ingresos < Inversión")

        lineas.append("\n" + "=" * 90 + "\n")

        return "\n".join(lineas)

    def comparar_soluciones(self, soluciones: list) -> str:
        """
        Compara múltiples soluciones lado a lado
        """
        lineas = []
        lineas.append("\n" + "=" * 140)
        lineas.append(
            f"COMPARATIVA DE SOLUCIONES - {self.param_antes.nombre_cliente}"
        )
        lineas.append("=" * 140)

        proyecciones = [self.proyectar_solucion(s) for s in soluciones]

        # Tabla de comparación
        lineas.append(
            f"{'Solución':<25} {'Payback':<12} {'Ahorro 5Y':<15} {'ROI %':<10} {'Ingreso TÚ':<15} {'Viabilidad':<15}"
        )
        lineas.append("-" * 140)

        for p in sorted(proyecciones, key=lambda x: x.payback_anos):
            viabilidad = (
                "✅ Viable"
                if p.payback_anos < 3
                else "⚠️  Borderline" if p.payback_anos < 5 else "❌ No viable"
            )
            lineas.append(
                f"{p.solucion.nombre:<25} {p.payback_anos:>10.1f}a "
                f"${p.ahorro_total_5anos_clp:>13,.0f} "
                f"{p.roi_pct:>8.1f}% "
                f"${p.ingreso_tu_total_5anos:>13,.0f} "
                f"{viabilidad:<15}"
            )

        lineas.append("=" * 140 + "\n")

        return "\n".join(lineas)
