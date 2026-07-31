# Zona 12: Sectores productivos objetivo y estrategia de prospección

## Objetivo
Definir a QUÉ sectores llegar con un producto/servicio bien estructurado, priorizando por
la intersección de tres filtros prácticos: (1) **contactabilidad** (publican teléfono en
Google Maps por rubro), (2) **intensidad energética** (dolor real: frío 24/7, calor de
proceso, motores → factor de potencia bajo), y (3) **encaje con nuestra oferta**
(diagnóstico → factor de potencia / demanda / eficiencia térmica → SaaS).

> **Método**: cifras marcadas **[dato]** (con fuente) o **[estimación]**. Investigación
> jul 2026. La estrategia de contacto uno-a-uno vía Google Maps por rubro es del fundador;
> este documento se enfoca en **qué ofrecer** a cada sector, no en cómo contactarlos.

---

## 1. Marco de priorización

Un sector es buen objetivo si cumple los tres filtros:

| Filtro | Por qué importa |
|---|---|
| **Contactable en mapas** | Publica teléfono/dirección por rubro → prospección barata sin canal |
| **Intensivo en energía** | Frío 24/7, calor de proceso o muchos motores → dolor visible y factura alta |
| **Encaje con la oferta** | Factor de potencia bajo (motores), demanda punta, o carga térmica desplazable |

Bonus: **residuo o autogeneración** aprovechable (aserrín, orujo, guano) = segunda
conversación de mayor ticket, pero **no** es el gancho inicial.

---

## 2. Sectores priorizados

### 2.1 Aserraderos e industria secundaria de la madera ⭐ (foco del fundador)

- **Dónde**: Maule, Ñuble, Biobío y La Araucanía son las 4 regiones productoras de madera
  aserrada **[dato INFOR]**. Gremios: **PYMEMAD** y **CORMA**.
- **Dolor energético doble**:
  - **Eléctrico**: motores de sierra y canteadoras → **factor de potencia bajo** (nuestro
    producto ancla) + demanda punta. Muchos usan **generadores** (diésel) → costo de
    combustible alto y oportunidad de optimización.
  - **Térmico**: el **secado de la madera** (cámaras de secado) es el gran consumo de
    calor; hoy muchos usan diésel/gas.
- **La oferta correcta (gestión de energía, NO biogás)**:
  1. Diagnóstico eléctrico → corrección de factor de potencia (payback corto).
  2. **Caldera de biomasa que quema su propio aserrín/despunte** para el secado →
     sustituye diésel/gas, ahorro directo y trazable. Hay **>70 proveedores** de
     calderas/quemadores de biomasa en Chile **[dato]**.
  3. Densificación del excedente (pellet/briqueta) como línea de ingreso adicional;
     precios de pellet varían por región (Maule barato ↔ Aysén caro) **[dato]** → arbitraje.
- **⚠️ Realidad técnica del aserrín (ver §3)**: NO es sustrato viable para biometano por
  digestión anaerobia (lignina). NO liderar con proyectos de biogás.
- **Fuentes**: INFOR (bibliotecadigital.infor.cl), "Análisis de costos de producción de
  madera aserrada en pymes" (SIMEF/Minagri), Ministerio de Energía (índice de precios de
  calefactores/calderas de biomasa), autoconsumo.minenergia.cl (caldera de biomasa).

### 2.2 Viñas y bodegas (vitivinícola)

- **Dónde**: Biobío (~6.433 propiedades vitícolas), Maule (~5.396), O'Higgins (~1.534)
  **[dato primario BID, ver `07_MODELO_ESI_BID.md`]**. Publican teléfono en mapas.
- **Dolor**: la **bodega** (vinificación) es intensiva; ~54% del consumo es eléctrico,
  principalmente **refrigeración** (45%), climatización y bombeo **[dato BID]**. Costo de
  energía de una bodega: grande ~USD 12.372/mes, mediana ~USD 2.963, pequeña ~USD 1.362
  **[dato BID]**.
- **Oferta**: factor de potencia (bombas/compresores), peak shaving en frío (pre-enfriar
  fuera de punta), y solar de autoconsumo como upsell. Sector **priorizado por el BID**.
- **Residuo**: el **orujo** (bagazo de uva) SÍ es buen sustrato de biogás (a diferencia
  del aserrín) — conversación de segunda etapa, no el gancho.

### 2.3 Packing frutícola y frigoríficos ⭐

- **Dónde**: O'Higgins y Maule concentran las cámaras de frío (O'Higgins ~26% de las
  cámaras frutícolas RM/centro **[dato 2013, verificar vigencia]**). Muchos publican
  contacto.
- **Dolor**: **refrigeración 24/7** = el mejor caso para factor de potencia (compresores
  = carga inductiva pura) + demanda punta + peak shaving con almacenamiento térmico
  (pre-enfriar cámaras). Es el sector con dolor más alineado con TODA nuestra oferta.
- **Oferta**: diagnóstico → condensadores → gestión de demanda punta (thermal storage de
  frío) → monitoreo. Ticket alto y payback corto.

### 2.4 Planteles y agroindustria animal (avícola, lechero, porcino, faenadoras)

- **Dolor**: refrigeración, bombeo, ventilación, motores → factor de potencia bajo.
  Faenadoras y lecheras tienen frío intensivo.
- **Residuo**: el **guano/purín** SÍ es sustrato de biogás (buen C/N con co-digestión) —
  proyectos de biodigestor reales en el sector, pero de mayor complejidad/capital.
- **Oferta inicial**: la misma cuña eléctrica (factor de potencia + demanda); biogás solo
  como conversación de gran cuenta.

### 2.5 Sectores urbanos de contacto fácil (validación rápida del producto ancla)

Para **probar el producto de factor de potencia** sin viajar al sur, con alta densidad en
RM + Valparaíso (>60% del mercado, ver `01_MERCADO_PYMES_CHILE.md`):

- **Lavanderías industriales**: motores de lavado/centrífugas + calor → factor bajo
  (caso ya simulado: payback ~1.9 años).
- **Panaderías con horno**: calor + motores (caso simulado: payback ~2.7 años).
- **Talleres mecánicos / metalmecánica**: motores, soldadoras → factor MUY bajo (caso
  simulado: payback ~1.1 años, el mejor).
- **Frigoríficos urbanos / distribución de alimentos**: refrigeración 24/7.

---

## 3. Nota técnica: por qué el aserrín NO sirve para biometano

Registro para no volver a evaluar proyectos de biogás con aserrín:

- **Digestión anaerobia (biogás/biometano)**: el aserrín es **lignocelulósico**; la
  **lignina blinda la celulosa** y los microorganismos no acceden a ella sin pretratamiento
  severo (rara vez rentable a escala pyme). El proceso lo hacen bacterias
  hidrolíticas/acidogénicas y, en el paso final, **arqueas metanogénicas**. La relación
  **C/N desfavorable** de la madera (~200-500:1 vs. óptimo ~20-30:1) es un problema
  secundario; mezclar con guano mejora el C/N pero **la lignina sigue limitando**.
  → **No viable como proyecto pyme.**
- **Gasificación**: el aserrín SÍ se puede gasificar (estudios chilenos con aserrín de
  pino), pero produce **syngas (CO + H₂), no CH₄ directo**; el metano requeriría un paso
  extra de metanación. Además el aserrín, por fino y poco denso, funciona mal en
  gasificadores de lecho fijo pequeños (prefieren astillas) → habría que densificar.
- **Ruta madura y bancable**: **densificación (pellet/briqueta) + combustión en caldera
  de biomasa** para el secado. Esta es la que encaja con nuestra tesis de gestión de
  energía.

**Regla**: al aserradero se le vende **eficiencia energética** (calor de su propio residuo
+ corrección eléctrica), no un proyecto de biogás.

**Fuentes**: "Gasificación de aserrín de pino" (RECyT-UNaM), "Valorización de pellets
combustibles usando aserrín" (TECNOCIENCIA), guías de digestión anaerobia (sustratos
lignocelulósicos requieren pretratamiento).

---

## 4. Matriz resumen

| Sector | Contacto en mapas | Dolor energético | Nuestra cuña inicial | Residuo→energía | Prioridad |
|---|---|---|---|---|---|
| Aserraderos | Alta | Motores + secado (térmico) | Factor potencia + caldera biomasa | Pellet (NO biogás) | ⭐⭐⭐ |
| Packing / frigoríficos | Media-alta | Frío 24/7 + punta | Factor + peak shaving frío | — | ⭐⭐⭐ |
| Viñas / bodegas | Alta | Frío + bombeo | Factor potencia + solar | Orujo (biogás sí) | ⭐⭐ |
| Planteles / faenadoras | Media | Frío + motores | Factor potencia | Guano (biogás sí) | ⭐⭐ |
| Lavanderías / panaderías / talleres (urbano) | Alta | Motores + calor | Factor potencia | — | ⭐⭐ (piloto) |

---

## 5. Preguntas abiertas (validar)

- [ ] Nº de aserraderos pyme por región (pedir a INFOR/PYMEMAD; hay padrón gremial).
- [ ] Costo energético medio de un aserradero pyme y % en secado vs. eléctrico.
- [ ] Vigencia del dato de cámaras frigoríficas (el disponible es de 2013).
- [ ] ¿El diagnóstico térmico (caldera de biomasa) requiere competencia que aún no tenemos?
      Definir si es upsell propio o alianza con proveedor de calderas.

---

**Estado**: ✅ Marco de sectores levantado (jul 2026). Aserraderos, packing/frío y
vitivinícola como focos; corregida la ruta técnica del aserrín (eficiencia, no biogás).
Cruza con `01` (mercado), `07` (subsectores BID) y `09` (pricing).
