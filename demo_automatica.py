#!/usr/bin/env python3
"""
DEMO AUTOMÁTICA - Casos reales de mercado eléctrico Chile
Sin inputs, solo muestra escenarios realistas investigados

Propósito: Demostrar cuánto dinero "desperdician" las empresas
por NO controlar factor de potencia y demanda punta
"""

from parametros import Parametros, TarifaType
from factura_electrica import CalculadoraFactura
from simulador_eficiencia import Solucion, SolucionType, SimuladorEficiencia


# ============ CASOS REALES INVESTIGADOS ============

CASOS = {
    "tienda_congelados": Parametros(
        nombre_cliente="Tienda de Congelados - Centro Comercial",
        tarifa=TarifaType.BT2,
        energia_mensual_kwh=3500,
        demanda_maxima_kw=55,
        demanda_punta_kw=0,  # BT2 NO mide demanda punta (corregido jul 2026)
        factor_potencia_actual=0.83,  # Refrigeración típica = bajo factor
        recargo_factor_potencia_pct=10.0,
        precio_energia_clp_per_kwh=195,
        precio_potencia_clp_per_kw=14500,
        precio_potencia_punta_clp_per_kw=0,  # No aplica en BT2
    ),

    "call_center": Parametros(
        nombre_cliente="Call Center - 30 Operadores",
        tarifa=TarifaType.BT2,
        energia_mensual_kwh=2800,
        demanda_maxima_kw=22,
        demanda_punta_kw=0,  # BT2 NO mide demanda punta (corregido jul 2026)
        factor_potencia_actual=0.90,  # Mejor que tienda (menos equipo inductivo)
        recargo_factor_potencia_pct=3.0,
        precio_energia_clp_per_kwh=195,
        precio_potencia_clp_per_kw=14500,
        precio_potencia_punta_clp_per_kw=0,  # No aplica en BT2
    ),

    "panaderia": Parametros(
        nombre_cliente="Panadería con Horno Industrial",
        tarifa=TarifaType.BT3,
        energia_mensual_kwh=5500,  # Horno consume bastante
        demanda_maxima_kw=70,
        demanda_punta_kw=55,
        factor_potencia_actual=0.81,  # Hornos generan reactivos
        recargo_factor_potencia_pct=12.0,
        precio_energia_clp_per_kwh=190,
        precio_potencia_clp_per_kw=13500,
        precio_potencia_punta_clp_per_kw=17500,
    ),

    "taller_mecanica": Parametros(
        nombre_cliente="Taller Mecánica - Pequeño",
        tarifa=TarifaType.BT3,
        energia_mensual_kwh=8000,
        demanda_maxima_kw=85,
        demanda_punta_kw=70,
        factor_potencia_actual=0.76,  # Motores = factor MUY bajo
        recargo_factor_potencia_pct=17.0,
        precio_energia_clp_per_kwh=190,
        precio_potencia_clp_per_kw=13500,
        precio_potencia_punta_clp_per_kw=17500,
    ),

    "lavanderia_industrial": Parametros(
        nombre_cliente="Lavandería Industrial",
        tarifa=TarifaType.BT3,
        energia_mensual_kwh=6200,
        demanda_maxima_kw=60,
        demanda_punta_kw=50,
        factor_potencia_actual=0.79,  # Motores de lavadoras
        recargo_factor_potencia_pct=14.0,
        precio_energia_clp_per_kwh=190,
        precio_potencia_clp_per_kw=13500,
        precio_potencia_punta_clp_per_kw=17500,
    ),

    "manufactura_electronica": Parametros(
        nombre_cliente="Pequeña Empresa Electrónica",
        tarifa=TarifaType.BT3,
        energia_mensual_kwh=12000,
        demanda_maxima_kw=95,
        demanda_punta_kw=80,
        factor_potencia_actual=0.78,  # Muchos equipos electrónicos
        recargo_factor_potencia_pct=15.0,
        precio_energia_clp_per_kwh=190,
        precio_potencia_clp_per_kw=13500,
        precio_potencia_punta_clp_per_kw=17500,
    ),
}


def solucion_condensadores():
    """Solución estándar: condensadores para factor potencia"""
    return Solucion(
        tipo=SolucionType.CONDENSADORES,
        nombre="Condensadores (Corrección Factor Potencia)",
        capex_hardware_clp=2_500_000,
        capex_instalacion_clp=600_000,
        mejora_factor_potencia=0.93,
        reduccion_demanda_punta_pct=0,
        reduccion_energia_pct=0,
        costo_saas_mensual_clp=25_000,
        costo_mantenimiento_anual_clp=50_000,
    )


def mostrar_encabezado():
    """Muestra encabezado de la demo"""
    print("\n" + "=" * 100)
    print("DEMO: MERCADO ELÉCTRICO CHILE - CASOS REALES")
    print("Investigación CNE + Análisis de Eficiencia Energética")
    print("=" * 100)
    print("\n📌 OBJETIVO: Mostrar cuánto dinero desperdician empresas por ineficiencia")
    print("   (factor potencia bajo, demanda punta, recargos no controlados)\n")


def analizar_caso(nombre_caso: str):
    """Analiza un caso completo: factura actual vs con solución"""

    params = CASOS[nombre_caso]
    print("\n" + "=" * 100)
    print(f"CASO: {params.nombre_cliente}")
    print("=" * 100)

    # 1. FACTURA ACTUAL
    calc_actual = CalculadoraFactura(params)
    factura_actual = calc_actual.calcular_factura()

    print(f"\n📊 FACTURA ACTUAL (sin optimizar):")
    print(f"  Tarifa: {params.tarifa.value}")
    print(f"  Energía: {params.energia_mensual_kwh:,.0f} kWh/mes")
    print(f"  Demanda máxima: {params.demanda_maxima_kw:.1f} kW")
    if params.demanda_punta_kw > 0:
        print(f"  Demanda punta (abr-sep): {params.demanda_punta_kw:.1f} kW")
    print(f"  Factor potencia: {params.factor_potencia_actual:.2f}")

    anual = calc_actual.calcular_factura_anual()

    print(f"\n💰 DESGLOSE (mes con punta, abr-sep):")
    print(f"  Energía:           ${factura_actual.costo_energia_clp:>13,.0f} CLP")
    print(f"  Potencia:          ${factura_actual.costo_potencia_clp:>13,.0f} CLP")
    if factura_actual.costo_potencia_punta_clp > 0:
        print(f"  Demanda punta:     ${factura_actual.costo_potencia_punta_clp:>13,.0f} CLP")
    print(f"  Recargo factor*:   ${factura_actual.costo_recargo_factor_potencia_clp:>13,.0f} CLP ⚠️  ")
    print(f"  VAD:               ${factura_actual.costo_distribucion_clp:>13,.0f} CLP")
    print(f"  ─────────────────────────────────")
    print(f"  MES PUNTA (abr-sep):   ${anual['factura_mes_punta'].total_mes_clp:>13,.0f} CLP")
    print(f"  MES NORMAL (oct-mar):  ${anual['factura_mes_normal'].total_mes_clp:>13,.0f} CLP")
    print(f"  TOTAL AÑO (6+6 meses): ${anual['total_anual_clp']:>13,.0f} CLP")
    print(f"  Promedio mensual:      ${anual['promedio_mensual_clp']:>13,.0f} CLP")

    # 2. DINERO DESPERDICIADO POR FACTOR POTENCIA BAJO
    print(f"\n⚠️  DINERO DESPERDICIADO (por factor potencia bajo):")
    desperdicio_mensual = factura_actual.costo_recargo_factor_potencia_clp
    desperdicio_anual = desperdicio_mensual * 12

    print(f"  Recargo mensual: ${desperdicio_mensual:>13,.0f} CLP")
    print(f"  Recargo ANUAL:   ${desperdicio_anual:>13,.0f} CLP 💸")
    print(f"  → En 5 años:     ${desperdicio_anual * 5:>13,.0f} CLP")

    # 3. SIMULAR SOLUCIÓN
    sol = solucion_condensadores()
    sim = SimuladorEficiencia(params)
    proyeccion = sim.proyectar_solucion(sol)

    print(f"\n✅ SOLUCIÓN: {sol.nombre}")
    print(f"  CAPEX: ${sol.capex_hardware_clp:,.0f} (hardware) + ${sol.capex_instalacion_clp:,.0f} (labor)")

    param_despues, _, factura_despues = sim.aplicar_solucion(sol)

    print(f"\n  Factor potencia mejora: {params.factor_potencia_actual:.2f} → {param_despues.factor_potencia_actual:.2f}")
    print(f"  Recargo baja: {params.recargo_factor_potencia_pct:.1f}% → {param_despues.recargo_factor_potencia_pct:.1f}%")

    print(f"\n  Factura DESPUÉS: ${factura_despues.total_mes_clp:>13,.0f} CLP/mes")
    print(f"  Ahorro mensual (sin IVA*): ${proyeccion.ahorro_mensual_clp:>13,.0f} CLP")
    print(f"  Ahorro NETO de operación:  ${proyeccion.ahorro_neto_mensual_clp:>13,.0f} CLP")
    print(f"  Ahorro ANUAL (sin IVA):    ${proyeccion.ahorro_mensual_clp * 12:>13,.0f} CLP")
    print(f"  (*) IVA excluido: es crédito fiscal para la empresa")

    print(f"\n📈 VIABILIDAD (payback neto de opex):")
    if proyeccion.payback_anos == float("inf"):
        print(f"  Payback:         NO SE RECUPERA (ahorro neto ≤ 0) ❌")
    else:
        print(f"  Payback:         {proyeccion.payback_anos:.1f} años", end="")
        if proyeccion.payback_anos < 1.5:
            print(" ✅ EXCELENTE")
        elif proyeccion.payback_anos < 3:
            print(" ✅ VIABLE")
        elif proyeccion.payback_anos < 5:
            print(" ⚠️  BORDERLINE")
        else:
            print(" ❌ NO VIABLE")

    print(f"  ROI cliente 5y (neto):  {proyeccion.roi_pct:.1f}%")

    print(f"\n🎯 TU NEGOCIO:")
    print(f"  Inversión cliente:      ${proyeccion.capex_total_clp:,.0f} CLP")
    print(f"  Tu margen (hardware):   ${proyeccion.ingreso_tu_margen_hw_instalacion:,.0f} CLP")
    print(f"  Tu SaaS 5 años:         ${proyeccion.ingreso_tu_saas_5anos:,.0f} CLP")
    print(f"  Tu ingreso TOTAL:       ${proyeccion.ingreso_tu_total_5anos:,.0f} CLP")

    # Viabilidad para ti
    ratio = proyeccion.ingreso_tu_total_5anos / proyeccion.capex_total_clp
    print(f"  Ratio ingresos/capex:   {ratio:.1f}x", end="")
    if ratio > 1:
        print(" ✅ VIABLE")
    else:
        print(" ❌ REVISAR")


def mostrar_resumen():
    """Muestra tabla resumen de todos los casos"""
    print("\n" + "=" * 140)
    print("RESUMEN: TODOS LOS CASOS")
    print("=" * 140)

    sol = solucion_condensadores()

    print(f"\n{'Empresa':<35} {'Factor':<8} {'Factura/mes*':<15} {'Desperdicio/año':<18} {'Payback':<10} {'Viabilidad':<15}")
    print("-" * 140)

    for nombre_caso, params in CASOS.items():
        calc = CalculadoraFactura(params)
        anual = calc.calcular_factura_anual()

        sim = SimuladorEficiencia(params)
        proyeccion = sim.proyectar_solucion(sol)

        desperdicio_anual = anual["recargo_factor_anual_clp"]

        if proyeccion.payback_anos == float("inf"):
            payback_txt = "  nunca"
            viabilidad = "❌ No viable"
        else:
            payback_txt = f"{proyeccion.payback_anos:>6.1f}a"
            viabilidad = "✅ Excelente" if proyeccion.payback_anos < 1.5 else "✅ Viable" if proyeccion.payback_anos < 3 else "⚠️  Borderline" if proyeccion.payback_anos < 5 else "❌ No viable"

        print(
            f"{params.nombre_cliente:<35} {params.factor_potencia_actual:.2f}      "
            f"${anual['promedio_mensual_clp']:>13,.0f}  "
            f"${desperdicio_anual:>16,.0f}  "
            f"{payback_txt:>8}  "
            f"{viabilidad:<15}"
        )

    print("-" * 140)
    print("* 'Factura/mes' = promedio anual/12 (punta solo abr-sep)")
    print("* 'Desperdicio/año' = recargo por factor potencia bajo (base: costo de energía)")
    print("* Payback neto de costos de operación (SaaS + mantenimiento)\n")


def main():
    """Ejecuta demo automática"""
    mostrar_encabezado()

    # Mostrar cada caso
    for nombre_caso in CASOS.keys():
        analizar_caso(nombre_caso)

    # Resumen
    mostrar_resumen()

    print("\n" + "=" * 100)
    print("CONCLUSIONES")
    print("=" * 100)
    print("""
1. FACTOR POTENCIA es el COSTO OCULTO más importante
   - Afecta factura directamente (1% recargo por cada 0.01 bajo 0.93)
   - Fácil de corregir con condensadores
   - Payback (neto de opex): ~1-2.5 años cuando el factor es MUY bajo (<0.80)
   - Con recargos pequeños puede NO ser viable: el diagnóstico decide caso a caso

2. EL VERDADERO PROBLEMA: Nadie controla esto
   - Empresas no ven el "recargo factor" como línea independiente
   - Lo absorben como "costo normal" de electricidad
   - Pocos proveedores hablan de eficiencia

3. OPORTUNIDAD DE NEGOCIO
   - Condensadores = bajo CAPEX; ROI alto SOLO con factor muy bajo
   - El negocio empieza por el DIAGNOSTICO PAGADO (ver 09_PRICING_CANONICO.md)
   - Después upsell: BESS, solar, etc.

4. ADVERTENCIAS METODOLOGICAS (ver 10_ANALISIS_CRITICO.md)
   - Base del recargo (energía vs factura total) PENDIENTE de verificar
     con factura real (ver factura_electrica.py y 11_PLAN_VALIDACION.md)
   - Ahorros sin IVA (crédito fiscal); payback neto de SaaS + mantenimiento
   - Punta solo abril-septiembre y solo BT3/BT4

5. NEXT STEPS
   - Ejecutar 11_PLAN_VALIDACION.md (facturas reales, base del recargo)
   - Ajustar parámetros según feedback real
   - Entonces expandir a otras soluciones
    """)
    print("=" * 100 + "\n")


if __name__ == "__main__":
    main()
