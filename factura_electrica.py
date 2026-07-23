"""
FACTURA ELÉCTRICA - Calcula factura real según estructura chilena
Basado en CNE (Comisión Nacional de Energía)
"""

from dataclasses import dataclass
from parametros import Parametros, TarifaType


@dataclass
class DetalleFactura:
    """Desglose completo de la factura eléctrica"""

    # Componentes principales
    costo_energia_clp: float  # Energía consumida (kWh × precio)
    costo_potencia_clp: float  # Potencia contratada/máxima
    costo_potencia_punta_clp: float  # Recargo por demanda en punta (si aplica)
    costo_recargo_factor_potencia_clp: float  # Multa por factor bajo
    costo_distribucion_clp: float  # VAD (Valor Agregado Distribución)

    # Totales
    subtotal_clp: float
    impuestos_clp: float  # IVA típicamente
    total_mes_clp: float

    # Información adicional
    tarifa: TarifaType
    periodo_aplicado: str  # "Normal" o "Punta" (abril-septiembre)


class CalculadoraFactura:
    """
    Calcula factura eléctrica mensual según estructura chilena
    Compatible con BT2, BT3 y BT4
    """

    # Constantes CNE
    ALIQUOTA_IVA = 0.19  # 19% en Chile

    # VAD (Valor Agregado Distribución) - referencia
    # Estos valores son aproximados; varían por distribuidor y zona
    VAD_BT2_CLIENTES_POR_KWMES = 30  # $30 por kWh consumido
    VAD_BT3_CLIENTES_POR_KWMES = 25  # BT3 suele ser más barato
    VAD_BT4_CLIENTES_POR_KWMES = 20

    def __init__(self, parametros: Parametros):
        self.p = parametros
        self.es_periodo_punta = True  # Simulamos siempre con punta

    def calcular_factura(self) -> DetalleFactura:
        """
        Calcula factura completa mensual
        """

        # Costo por energía consumida
        costo_energia = self.p.energia_mensual_kwh * self.p.precio_energia_clp_per_kwh

        # Costo por potencia contratada o medida
        costo_potencia = self.p.demanda_maxima_kw * self.p.precio_potencia_clp_per_kw

        # Costo por demanda punta (solo si hay demanda punta >0 y tarifa aplica)
        if self.p.demanda_punta_kw > 0 and self.p.precio_potencia_punta_clp_per_kw > 0:
            costo_potencia_punta = (
                self.p.demanda_punta_kw * self.p.precio_potencia_punta_clp_per_kw
            )
        else:
            costo_potencia_punta = 0

        # Recargo por factor de potencia bajo
        costo_recargo_factor = costo_energia * (
            self.p.recargo_factor_potencia_pct / 100
        )

        # VAD (Valor Agregado Distribución)
        if self.p.tarifa == TarifaType.BT2:
            vad_por_kwmes = self.VAD_BT2_CLIENTES_POR_KWMES
        elif self.p.tarifa == TarifaType.BT3:
            vad_por_kwmes = self.VAD_BT3_CLIENTES_POR_KWMES
        else:
            vad_por_kwmes = self.VAD_BT4_CLIENTES_POR_KWMES

        costo_distribucion = self.p.energia_mensual_kwh * vad_por_kwmes

        # Subtotal
        subtotal = (
            costo_energia
            + costo_potencia
            + costo_potencia_punta
            + costo_recargo_factor
            + costo_distribucion
        )

        # Impuestos (IVA)
        impuestos = subtotal * self.ALIQUOTA_IVA

        # Total
        total = subtotal + impuestos

        periodo = (
            "Punta (Abr-Sep 18:00-22:00)"
            if self.es_periodo_punta
            else "Normal (Oct-Mar)"
        )

        return DetalleFactura(
            costo_energia_clp=costo_energia,
            costo_potencia_clp=costo_potencia,
            costo_potencia_punta_clp=costo_potencia_punta,
            costo_recargo_factor_potencia_clp=costo_recargo_factor,
            costo_distribucion_clp=costo_distribucion,
            subtotal_clp=subtotal,
            impuestos_clp=impuestos,
            total_mes_clp=total,
            tarifa=self.p.tarifa,
            periodo_aplicado=periodo,
        )

    def imprimir_factura(self) -> str:
        """
        Genera reporte de factura formateado
        """
        factura = self.calcular_factura()

        lineas = []
        lineas.append("\n" + "=" * 80)
        lineas.append(f"FACTURA ELÉCTRICA - {self.p.nombre_cliente}")
        lineas.append(f"Tarifa: {factura.tarifa.value} | Período: {factura.periodo_aplicado}")
        lineas.append("=" * 80)

        lineas.append(f"\n📊 CONSUMO Y DEMANDA:")
        lineas.append(f"  Energía consumida:         {self.p.energia_mensual_kwh:>10,.0f} kWh/mes")
        lineas.append(f"  Demanda máxima:            {self.p.demanda_maxima_kw:>10,.1f} kW")
        if self.p.demanda_punta_kw > 0:
            lineas.append(f"  Demanda punta:             {self.p.demanda_punta_kw:>10,.1f} kW")

        lineas.append(f"\n⚡ FACTOR DE POTENCIA:")
        lineas.append(f"  Factor actual:             {self.p.factor_potencia_actual:>10,.2f}")
        if self.p.factor_potencia_actual < 0.93:
            lineas.append(
                f"  ⚠️  BAJO: Recargo de {self.p.recargo_factor_potencia_pct:.1f}%"
            )
        else:
            lineas.append(f"  ✅ CORRECTO: Sin recargo")

        lineas.append(f"\n💰 DESGLOSE DE FACTURA MENSUAL:")
        lineas.append(f"  Costo energía:             ${factura.costo_energia_clp:>14,.0f} CLP")
        lineas.append(f"  Costo potencia:            ${factura.costo_potencia_clp:>14,.0f} CLP")
        if factura.costo_potencia_punta_clp > 0:
            lineas.append(
                f"  Costo demanda punta:       ${factura.costo_potencia_punta_clp:>14,.0f} CLP"
            )
        lineas.append(
            f"  Recargo factor potencia:   ${factura.costo_recargo_factor_potencia_clp:>14,.0f} CLP"
        )
        lineas.append(
            f"  VAD (distribución):        ${factura.costo_distribucion_clp:>14,.0f} CLP"
        )
        lineas.append("-" * 80)
        lineas.append(f"  Subtotal:                  ${factura.subtotal_clp:>14,.0f} CLP")
        lineas.append(f"  IVA (19%):                 ${factura.impuestos_clp:>14,.0f} CLP")
        lineas.append("=" * 80)
        lineas.append(f"  TOTAL MES:                 ${factura.total_mes_clp:>14,.0f} CLP")
        lineas.append("=" * 80)

        # Análisis de composición
        pct_energia = (factura.costo_energia_clp / factura.total_mes_clp) * 100
        pct_potencia = (
            (factura.costo_potencia_clp + factura.costo_potencia_punta_clp)
            / factura.total_mes_clp
        ) * 100
        pct_recargo = (factura.costo_recargo_factor_potencia_clp / factura.total_mes_clp) * 100

        lineas.append(f"\n📈 ANÁLISIS DE COMPOSICIÓN:")
        lineas.append(f"  Energía:                   {pct_energia:>10.1f}%")
        lineas.append(f"  Potencia (incl. punta):    {pct_potencia:>10.1f}%")
        lineas.append(f"  Recargo factor:            {pct_recargo:>10.1f}%")

        lineas.append(f"\n💡 PROYECCIONES ANUALES:")
        lineas.append(f"  Factura anual:             ${factura.total_mes_clp * 12:>14,.0f} CLP")
        lineas.append(
            f"  Costo energía anual:       ${factura.costo_energia_clp * 12:>14,.0f} CLP"
        )
        lineas.append(
            f"  Costo potencia anual:      ${(factura.costo_potencia_clp + factura.costo_potencia_punta_clp) * 12:>14,.0f} CLP"
        )

        # Estimación de "dinero desperdiciado" por factor bajo
        if self.p.factor_potencia_actual < 0.93:
            desperdicio_anual = (
                factura.costo_recargo_factor_potencia_clp * 12
            )
            lineas.append(f"\n⚠️  COSTO DE INEFICIENCIA (factor potencia bajo):")
            lineas.append(
                f"  Recargo mensual por ineficiencia: ${factura.costo_recargo_factor_potencia_clp:>10,.0f} CLP"
            )
            lineas.append(
                f"  Recargo ANUAL por ineficiencia:   ${desperdicio_anual:>10,.0f} CLP"
            )
            lineas.append(f"  Nota: Esto se puede ELIMINAR con condensadores")

        lineas.append("\n" + "=" * 80 + "\n")

        return "\n".join(lineas)


def comparar_facturas(params_lista: list) -> str:
    """
    Compara facturas de múltiples clientes
    """
    lineas = []
    lineas.append("\n" + "=" * 100)
    lineas.append("COMPARATIVA DE FACTURAS ELÉCTRICAS MENSUALES")
    lineas.append("=" * 100)

    # Encabezados
    lineas.append(
        f"{'Cliente':<30} {'Tarifa':<8} {'Total $':<15} {'Energía':<12} {'Potencia':<12} {'Recargo':<12}"
    )
    lineas.append("-" * 100)

    resultados = []
    for params in params_lista:
        calc = CalculadoraFactura(params)
        factura = calc.calcular_factura()
        resultados.append((params, factura))

        lineas.append(
            f"{params.nombre_cliente:<30} {factura.tarifa.value:<8} "
            f"${factura.total_mes_clp:>13,.0f} "
            f"${factura.costo_energia_clp:>10,.0f} "
            f"${factura.costo_potencia_clp + factura.costo_potencia_punta_clp:>10,.0f} "
            f"${factura.costo_recargo_factor_potencia_clp:>10,.0f}"
        )

    lineas.append("-" * 100)

    # Totales
    total_general = sum(f.total_mes_clp for _, f in resultados)
    lineas.append(f"{'TOTAL':<30} {'':<8} ${total_general:>13,.0f}")
    lineas.append("=" * 100 + "\n")

    return "\n".join(lineas)
