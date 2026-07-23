# Zona 7: Modelo ESI y mercado potencial PYME — Fuente primaria BID

## Objetivo
Consolidar los datos y el marco del **Modelo ESI (Energy Savings Insurance / Seguro de
Ahorro de Energía)** del BID, la fuente **primaria más completa** que tenemos sobre el
mercado de eficiencia energética en PYMES chilenas y su financiamiento.

> **Fuente**: Chaparro, R.; Netto, M.; Mansilla, P.; Magallón, D. (2020).
> *"Seguro de ahorro de energía: Avances y oportunidades para el financiamiento de
> proyectos de eficiencia energética y generación distribuida en pequeñas y medianas
> empresas en Chile."* Banco Interamericano de Desarrollo, **Nota Técnica IDB-TN-2038**,
> diciembre 2020. PDF de respaldo en `fuentes_pdf/Seguro-de-ahorro-de-energia-Avance.pdf`
> (**no leer con LLM** — datos ya extraídos aquí; ver CLAUDE.md).
>
> Todas las cifras de este documento son **[dato primario BID]** salvo indicación contraria.

---

## 1. Qué es el Modelo ESI

Conjunto de instrumentos financieros y no financieros del BID (replicado con BancoEstado
en Chile) para **mitigar el riesgo de proyectos de eficiencia energética y generación
distribuida** y generar confianza en el inversionista PYME. Se apoya en cuatro elementos:

1. **Contrato estándar**: fija responsabilidades proveedor-cliente y un **Ahorro o
   Generación Mínimo Garantizado (AGMG)**, precios de referencia de energía, periodicidad
   de mediciones y duración (típicamente anual, hasta 5 años).
2. **Seguro**: el proveedor compra y paga una póliza en beneficio del cliente; si el
   proyecto no alcanza el AGMG y el proveedor no compensa, la **aseguradora cubre el
   siniestro**. Costo estimado en Chile: **0,5%–1% del valor asegurado**.
3. **Validación**: una entidad técnica independiente valida el potencial de ahorro y
   verifica la instalación (árbitro vinculante). Las líneas base se establecen con
   **protocolos ISO 50001**. Costo: **~USD 1.500/proyecto**.
4. **Financiamiento**: crédito bancario (BancoEstado) cuyo repago se respalda en el flujo
   de ahorro garantizado.

**Actores en Chile** (a 2020):
- **Banco / financiador**: BancoEstado (líder local, ~400 ejecutivos de negocios).
- **Validador**: Agencia de Sostenibilidad Energética (ASE / AgenciaSE).
- **Aseguradoras**: **CESCE y SURA** (pólizas finalizadas); **HDI** también manifestó interés.
- **Promotor**: BID (con apoyo del gobierno de Dinamarca, Coop. Técnica RG-X1258).

El Modelo ESI se originó en **Colombia** (>50 proyectos garantizados a jun-2020) y se
replica en **Brasil, Chile, El Salvador y Perú**; en desarrollo en Argentina, México,
Nicaragua, Paraguay, y también España, Italia y Portugal (UE).

**Relevancia para nosotros**: el Modelo ESI es esencialmente el andamiaje contractual/
financiero del modelo **ESCO/EPC** que proponemos en `04b_SERVICIO_INTEGRADO_ESCO.md`.
Valida que el mecanismo de "cliente no paga si no ahorra" ya existe institucionalmente en
Chile y que el rol de **validador con ISO 50001** es parte del estándar.

---

## 2. Universo de empresas (dato primario)

- En Chile hay **poco menos de 1.000.000 de empresas**; **220.000** están categorizadas
  por el Ministerio de Economía como **grandes + PYME**. La PYME es el **23,5%** del
  universo; la microempresa el **75,2%**.
- Clasificación por **Estatuto PYME (Ley 20.416)**:

| Categoría | Ventas (UF/año) | Empleados |
|-----------|-----------------|-----------|
| Microempresa | 0 – 2.400 | 0–9 |
| Pequeña | 2.400 – 25.000 | 10–49 |
| Mediana | 25.000 – 100.000 | 50–199 |
| Grande | ≥ 100.000 | 200+ |

**Precio de la energía (ancla del dolor)**: para las PYMES objetivo, ~**USD 0,158/kWh**
(15,80 ¢USD, marzo 2019). Chile tiene de **las tarifas eléctricas más altas de
Sudamérica** (comparable a Uruguay USD 0,23; muy por encima de Paraguay USD 0,028). Esto
hace que los proyectos de EE tengan **payback corto** en Chile.

---

## 3. Barreras (confirmadas por fuente primaria)

**Del lado del cliente**:
- Los proyectos de EE **compiten por recursos** con inversiones del giro principal, que el
  dueño entiende mejor (mejor valoración riesgo-retorno percibida).
- **Alta sensibilidad al precio del equipo (CAPEX)**, ignorando que el OPEX de largo plazo
  es mucho mayor → eligen tecnología "barata" e ineficiente.
- **Incertidumbre sobre el desempeño/ahorro**: sin garantías, el riesgo percibido es alto;
  los paybacks de 3–7 años hacen el periodo de riesgo largo.

**Del lado del proveedor**:
- La mayoría **solo vende e instala equipos** (el vínculo termina con la entrega); **no
  garantiza** ahorro. Las ESCO son la excepción.
- Muchos son distribuidores de fabricantes con gama amplia (eficiente y no); su oferta no
  se dirige específicamente a alta eficiencia sino a lo que pide el mercado.

→ Estas barreras son **exactamente** las que ataca nuestro modelo ESCO + telemetría +
garantía de desempeño.

---

## 4. Sectores priorizados y tamaño (dato primario)

El estudio evaluó 17 subsectores comercial/industrial con matriz multicriterio (tamaño de
mercado, intensidad energética, crecimiento, políticas/gremios). **Top 4 priorizados**:

| Sector | Puntaje | Nº empresas (pequeña→grande) |
|--------|---------|------------------------------|
| Hotelero | 79% | 1.596 |
| Agroindustrial (procesamiento alimentos) | 79% | 21.259 |
| Vitivinícola | 73% | 4.605 |
| Pesquero | 73% | 3.510 |
| **Total 4 subsectores** | — | **30.970** (22.110 peq. / 6.648 med. / 2.212 grandes) |

Estos sectores crecen **~4%/año** (Cuentas Nacionales BCCh 2018). Nota: el estudio prioriza
por sector productivo, no por tarifa BT2/BT3; nuestro foco (factor de potencia y demanda)
es transversal y complementario. Los sectores con **cámaras de refrigeración 24/7**
(agroindustria, retail alimentos) son los de mayor consumo y peor factor de potencia.

**Costo de energía de una bodega vitivinícola** (referencia de intensidad):
grande USD ~12.372/mes (8.414 eléctrica + 3.958 térmica); mediana ~USD 2.963/mes; pequeña
~USD 1.362/mes. Reparto eléctrico: refrigeración 45%, calentamiento 21%, equipo vinífero
16%, aire comprimido 8%.

---

## 5. Tecnologías: ahorro, inversión y retorno (dato primario)

### Ahorro potencial por tecnología (equipo eficiente vs. ineficiente)

| Tecnología | Ahorro en consumo |
|-----------|-------------------|
| Aire acondicionado | 22% |
| Motores eléctricos | 6% |
| Cámaras de refrigeración | 20% |
| Caldera | 6% |
| Calentador solar térmico | 50% |
| Sistema solar fotovoltaico | 100% (energía de red reemplazada) |

### Inversión promedio por proyecto: **USD 30.000 – 500.000** (casos reales USD 80k–230k)

| Tecnología | Proyectos pequeños | Proyectos grandes |
|-----------|--------------------|-------------------|
| Aire acondicionado | USD 1.500/ton refrig. | USD 1.200/ton |
| Motores | USD 150/HP | USD 120/HP |
| Calderas | USD 1.200/BHP | USD 1.000/BHP |
| Cámaras refrigerantes | USD 2.800/ton | USD 2.500/ton |
| Solar térmico | USD 700/m² | USD 550/m² |
| Solar fotovoltaico | USD 1.500/kWp | USD 1.100/kWp |

### Rentabilidad (TIR) y payback por tecnología

| Tecnología | TIR sin financ. | TIR con 80% financ. | Payback sin financ. | Payback con financ. |
|-----------|-----------------|---------------------|---------------------|---------------------|
| Aire acondicionado | 19,91% | 36,31% | 4,6 años | 4,0 años |
| Motores | 20,62% | 38,93% | 4,9 | 4,1 |
| Calderas | 26,23% | 42,68% | 4,1 | 3,4 |
| Refrigeración industrial | 18,73% | 22,62% | 6,1 | 5,4 |
| Solar FV | 6,87% | 12,55% | 8,5 | 7,6 |

Supuestos: tasa descuento 10%, inflación energía 4%, impuesto renta 25%, depreciación 5
años, financiamiento 80% a 5 años. **El financiamiento mejora fuertemente la TIR** →
argumento central para el modelo ESCO/EPC. Los **costos transaccionales** (validación
USD 1.500 + prima seguro 1,5%) son **relevantes en proyectos < USD 30.000** y **marginales
en > USD 100.000** → conviene apuntar a tickets medianos/grandes.

### Casos de estudio reales (Chile, sector agroindustrial)

| Empresa | Tecnología | Inversión | Ahorro energía | Ahorro $ | Payback |
|---------|-----------|-----------|----------------|----------|---------|
| Bayas del Sur S.A. | Caldera 3 ton/vapor | USD 230.100 | 665.000 kWh/año | USD 39.000/año | < 6 años |
| Faenadora Ariztía El Paico | 3 motores (600/522/336 kW) | USD 80.279 | 43.319 kWh/año | USD 46.223/año | **< 2 años** |
| Agrícola El Retorno | Solar FV 63 kW | USD 134.328 | 107.600 kWh/año | USD 11.768/año | 12 años |

---

## 6. Tamaño del mercado ESI/EE (dato primario)

- **Mercado efectivo** (los 4 subsectores priorizados): **~533 proyectos/año**, con
  inversión **~USD 45 millones/año** y necesidad de financiamiento **~USD 36 millones/año**
  (asumiendo 80% financiado).
- **Mercado potencial** (las 30.970 empresas): inversión de **~USD 3.000 millones**.
- **Metodología del "efectivo"**: solo 3–4% de las empresas tiene necesidad de inversión en
  EE en un año dado; y solo 50–60% de las PYME accede a crédito → filtra de 30.970 a
  1.049 empresas con necesidad y **533 con potencial de crédito**.
- **Impacto ambiental** del mercado efectivo: **~50.000 tCO₂/año** y **~75 GWh/año** de
  ahorro.
- **Proyección BancoEstado a 5 años**: 1.599 proyectos acumulados, **USD 135,1M** de
  inversión, **USD 108,1M** de financiamiento; demanda estimada de financiamiento de
  **~USD 200 millones** en el periodo.
- **Mercado de garantías de cumplimiento** en Chile: ~USD 20 millones (2018).

> **Nota de conciliación con `01_MERCADO_PYMES_CHILE.md`**: el mercado ESCO "actual" de
> ~USD 15M/año (fuente ANESCO) y este "mercado efectivo" de ~USD 45M/año no son
> contradictorios: el primero es lo que hoy se ejecuta; el segundo es la demanda anual
> potencial financiable en 4 sectores. Ambos apuntan a un mercado incipiente con espacio
> de varios múltiplos.

---

## 7. Precedente público directo: Programa CAPE (sector público)

En 2017–2018 el Ministerio de Energía impulsó EE en el **sector público** con un modelo
que ya incluía diagnósticos, contratos de ahorro, validación por la ASE y garantías de
ahorro (**Programa CAPE**):

- **39 hospitales**, **9 empresas implementadoras**, inversión de **~$9.000 millones CLP
  (~USD 14 millones)**.
- Solo **3 de los 39** proyectos presentaron problemas de ahorro.
- En 2019 se extendió a **100 edificios más** bajo **modelo ESCO**.

→ Evidencia local de que el modelo de garantía de ahorro **funciona en Chile** y de que el
Estado ya lo escala. Referencia útil para el pitch a inversionistas y clientes.

---

## 8. Oferta de financiamiento (dato primario, complementa Zona 3)

**Línea verde de BancoEstado** (dirigida a PYME y ESCO):
- Plazo **hasta 12 años**.
- Financia **hasta 80% del valor neto** del proyecto.
- En **pesos o UF**; calendario de pagos acorde al ciclo del negocio.
- **Garantías estatales o reales**.
- Opera con ficha de factibilidad técnica validada por la **ASE** (www.acee.cl / agenciase).

Ver también `03_SUBSIDIOS_FINANCIAMIENTO.md` (programa "Ponle Energía a tu Pyme",
Registro Energético/ESCO) y `04b_SERVICIO_INTEGRADO_ESCO.md` (modelo EPC/SaaS).

---

## 9. Implicaciones estratégicas para nosotros

1. **El andamiaje ya existe**: BancoEstado (crédito 12 años/80%), ASE (validador ISO 50001),
   CESCE/SURA (seguro). No hay que inventar el ecosistema, hay que **operarlo mejor**.
2. **Ticket objetivo**: proyectos **> USD 30.000–100.000** para diluir costos
   transaccionales; motores y calderas dan el mejor payback (< 4 años con financiamiento).
3. **Nuestra cuña diferencial**: el estudio BID cubre reemplazo de equipos y solar, pero
   **no** explota factor de potencia + demanda punta + telemetría continua, que es
   nuestro foco de menor CAPEX y payback más corto (ver casos en `demo_automatica.py`).
4. **Sectores calientes**: agroindustria y retail con **refrigeración 24/7** — alto consumo,
   peor factor de potencia, y ya priorizados por la banca.
5. **Payback solar es largo (8–12 años)**: no liderar con solar; liderar con condensadores/
   eficiencia (payback < 2 años) y usar solar como upsell posterior.

---

**Estado**: ✅ Fuente primaria BID incorporada (IDB-TN-2038, 2020). Datos de mercado,
tecnologías, TIR/payback, actores y financiamiento consolidados.
