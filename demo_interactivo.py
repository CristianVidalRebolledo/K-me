#!/usr/bin/env python3
"""
DEMO INTERACTIVA - Simulador de Costos Eléctricos y Eficiencia Energética
Mercado Eléctrico Chileno

Ejecuta: python3 demo_interactivo.py
"""

import sys
from parametros import (
    Parametros,
    TarifaType,
    PARAMETROS_TIPICOS,
    validar_parametros,
    imprimir_documentacion_parametros,
)
from factura_electrica import CalculadoraFactura, comparar_facturas
from simulador_eficiencia import (
    Solucion,
    SolucionType,
    SimuladorEficiencia,
)


# ============ SOLUCIONES PREDEFINIDAS ============


def definir_soluciones():
    """Define soluciones de eficiencia disponibles"""
    return {
        "condensadores": Solucion(
            tipo=SolucionType.CONDENSADORES,
            nombre="Condensadores (Corrección Factor Potencia)",
            capex_hardware_clp=2_500_000,
            capex_instalacion_clp=600_000,
            mejora_factor_potencia=0.93,  # Lleva a 0.93
            reduccion_demanda_punta_pct=0,  # No reduce demanda
            reduccion_energia_pct=0,  # No reduce energía
            costo_saas_mensual_clp=25_000,  # Monitoreo
            costo_mantenimiento_anual_clp=50_000,
        ),
        "bess": Solucion(
            tipo=SolucionType.BESS,
            nombre="BESS (Peak Shaving - Reducción Demanda Punta)",
            capex_hardware_clp=8_000_000,
            capex_instalacion_clp=1_500_000,
            mejora_factor_potencia=0.95,  # También mejora factor
            reduccion_demanda_punta_pct=40,  # Reduce 40% de punta
            reduccion_energia_pct=5,  # Ahorrar 5% total
            costo_saas_mensual_clp=50_000,  # Monitoreo + control
            costo_mantenimiento_anual_clp=150_000,
        ),
        "bess_solar": Solucion(
            tipo=SolucionType.BESS_SOLAR,
            nombre="BESS + Solar (Generación + Almacenamiento)",
            capex_hardware_clp=18_000_000,
            capex_instalacion_clp=3_500_000,
            mejora_factor_potencia=0.96,
            reduccion_demanda_punta_pct=50,  # Reduce 50% de punta (solar en punta)
            reduccion_energia_pct=30,  # Solar genera 30% del consumo
            costo_saas_mensual_clp=80_000,  # Monitoreo + control avanzado
            costo_mantenimiento_anual_clp=250_000,
        ),
    }


# ============ FUNCIONES DE MENÚ ============


def menu_principal():
    """Menú principal"""
    print("\n" + "=" * 80)
    print("SIMULADOR DE COSTOS ELÉCTRICOS - EFICIENCIA ENERGÉTICA CHILE")
    print("=" * 80)
    print("""
1. Ver factura eléctrica actual (ingresar parámetros)
2. Simular soluciones de eficiencia
3. Ver ejemplos predefinidos (tienda, call center, manufactura)
4. Ver documentación de parámetros
5. Salir
    """)
    return input("Elige opción (1-5): ").strip()


def opcion_1_factura_actual():
    """Opción 1: Calcular factura actual con parámetros ingresados"""
    print("\n" + "=" * 80)
    print("INGRESAR PARÁMETROS DEL CLIENTE")
    print("=" * 80)

    nombre = input("\nNombre/descripción del cliente: ")

    print("\nOpciones tarifarias: BT1, BT2, BT3, BT4")
    print("  BT2: Pequeños comercios (tiendas, call centers)")
    print("  BT3: Pequeña manufactura")
    print("  BT4: Industria")
    tarifa_str = input("Tarifa (BT1/BT2/BT3/BT4): ").strip().upper()
    try:
        tarifa = TarifaType[tarifa_str]
    except KeyError:
        print("❌ Tarifa no válida")
        return

    energia = float(input("Energía mensual (kWh): "))
    demanda_max = float(input("Demanda máxima (kW): "))
    demanda_punta = float(input("Demanda punta (kW) [0 si no aplica]: "))

    print("\nFactor de potencia: Entre 0 y 1 (típicamente 0.75-0.95)")
    print("  <0.93 genera recargos")
    factor_potencia = float(input("Factor potencia actual: "))

    # Calcular recargo automáticamente
    recargo = max(0, (0.93 - factor_potencia) * 100)

    # Precios
    print("\nPrecios según distribuidor (valores 2026 aproximados):")
    print("  BT2: $180-200/kWh, $12,000-15,000/kW")
    print("  BT3: $180-195/kWh, $12,000-14,000/kW")
    precio_energia = float(
        input("Precio energía (CLP/kWh) [195 por defecto]: ") or "195"
    )
    precio_potencia = float(
        input("Precio potencia (CLP/kW/mes) [14000 por defecto]: ") or "14000"
    )
    precio_potencia_punta = float(
        input("Precio potencia punta (CLP/kW/mes) [17500 por defecto]: ") or "17500"
    )

    # Crear parámetros
    params = Parametros(
        nombre_cliente=nombre,
        tarifa=tarifa,
        energia_mensual_kwh=energia,
        demanda_maxima_kw=demanda_max,
        demanda_punta_kw=demanda_punta,
        factor_potencia_actual=factor_potencia,
        recargo_factor_potencia_pct=recargo,
        precio_energia_clp_per_kwh=precio_energia,
        precio_potencia_clp_per_kw=precio_potencia,
        precio_potencia_punta_clp_per_kw=precio_potencia_punta,
    )

    # Validar
    problemas = validar_parametros(params)
    if problemas:
        print("\n❌ PROBLEMAS ENCONTRADOS:")
        for p in problemas:
            print(f"  - {p}")
        return

    # Calcular y mostrar
    calc = CalculadoraFactura(params)
    print(calc.imprimir_factura())


def opcion_2_simular_soluciones():
    """Opción 2: Simular soluciones sobre parámetros ingresados"""
    print("\n" + "=" * 80)
    print("SIMULAR SOLUCIONES DE EFICIENCIA")
    print("=" * 80)

    # Primero obtener cliente
    print("\n¿Usas cliente predefinido o ingresas uno custom?")
    print("1. Tienda de congelados (BT2)")
    print("2. Call center (BT2)")
    print("3. Manufactura pequeña (BT3)")
    print("4. Ingresar cliente custom")

    opcion_cliente = input("Elige (1-4): ").strip()

    if opcion_cliente in ["1", "2", "3"]:
        keys = ["tienda_congelados", "call_center", "manufactura"]
        params = PARAMETROS_TIPICOS[keys[int(opcion_cliente) - 1]]
    elif opcion_cliente == "4":
        # Mismo flow que opción 1
        nombre = input("\nNombre cliente: ")
        tarifa_str = input("Tarifa (BT2/BT3): ").strip().upper()
        tarifa = TarifaType[tarifa_str]
        energia = float(input("Energía (kWh): "))
        demanda_max = float(input("Demanda máxima (kW): "))
        demanda_punta = float(input("Demanda punta (kW) [0]: "))
        factor = float(input("Factor potencia: "))

        params = Parametros(
            nombre_cliente=nombre,
            tarifa=tarifa,
            energia_mensual_kwh=energia,
            demanda_maxima_kw=demanda_max,
            demanda_punta_kw=demanda_punta,
            factor_potencia_actual=factor,
            recargo_factor_potencia_pct=max(0, (0.93 - factor) * 100),
            precio_energia_clp_per_kwh=195,
            precio_potencia_clp_per_kw=14000,
            precio_potencia_punta_clp_per_kw=17500,
        )
    else:
        print("❌ Opción no válida")
        return

    # Mostrar factura actual
    calc_actual = CalculadoraFactura(params)
    print(calc_actual.imprimir_factura())

    # Seleccionar soluciones
    soluciones_dict = definir_soluciones()
    print("\nSoluciones disponibles:")
    for i, (key, sol) in enumerate(soluciones_dict.items(), 1):
        print(f"  {i}. {sol.nombre}")

    print("\nElige soluciones para simular (ej: 1,2 o solo 1):")
    seleccion = input("Soluciones [1 por defecto]: ").strip() or "1"

    indices = [int(x.strip()) - 1 for x in seleccion.split(",")]
    soluciones_sel = [list(soluciones_dict.values())[i] for i in indices]

    # Simular
    sim = SimuladorEficiencia(params)
    print(sim.comparar_soluciones(soluciones_sel))

    for sol in soluciones_sel:
        proyeccion = sim.proyectar_solucion(sol)
        print(sim.imprimir_proyeccion(proyeccion))


def opcion_3_ejemplos_predefinidos():
    """Opción 3: Ver ejemplos precargados"""
    print("\n" + "=" * 80)
    print("EJEMPLOS PREDEFINIDOS - CASOS REALES CHILENOS")
    print("=" * 80)

    print("\nCalculando facturas actuales...")
    params_lista = list(PARAMETROS_TIPICOS.values())

    # Mostrar facturas actuales
    for params in params_lista:
        calc = CalculadoraFactura(params)
        print(calc.imprimir_factura())

    print(comparar_facturas(params_lista))

    # Opción de simular soluciones en uno
    print("\n¿Simular soluciones en alguno de estos clientes?")
    for i, params in enumerate(params_lista, 1):
        print(f"  {i}. {params.nombre_cliente}")
    print("  0. No simular")

    opcion = input("\nElige (0-3): ").strip()
    if opcion == "0":
        return

    try:
        cliente_idx = int(opcion) - 1
        params = params_lista[cliente_idx]
    except (ValueError, IndexError):
        print("❌ Opción no válida")
        return

    # Simular soluciones
    soluciones = list(definir_soluciones().values())
    sim = SimuladorEficiencia(params)

    print(sim.comparar_soluciones(soluciones))

    print("\n¿Ver detalles de alguna solución?")
    for i, sol in enumerate(soluciones, 1):
        print(f"  {i}. {sol.nombre}")
    print("  0. No")

    opcion_sol = input("Elige (0-3): ").strip()
    if opcion_sol != "0":
        try:
            sol_idx = int(opcion_sol) - 1
            proyeccion = sim.proyectar_solucion(soluciones[sol_idx])
            print(sim.imprimir_proyeccion(proyeccion))
        except (ValueError, IndexError):
            print("❌ Opción no válida")


def opcion_4_documentacion():
    """Opción 4: Ver documentación de parámetros"""
    imprimir_documentacion_parametros()


def main():
    """Programa principal"""
    while True:
        opcion = menu_principal()

        if opcion == "1":
            opcion_1_factura_actual()
        elif opcion == "2":
            opcion_2_simular_soluciones()
        elif opcion == "3":
            opcion_3_ejemplos_predefinidos()
        elif opcion == "4":
            opcion_4_documentacion()
        elif opcion == "5":
            print("\n👋 Hasta luego!\n")
            sys.exit(0)
        else:
            print("\n❌ Opción no válida")

        input("\n[Presiona Enter para continuar...]")


if __name__ == "__main__":
    main()
