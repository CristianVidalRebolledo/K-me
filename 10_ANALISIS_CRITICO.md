# Zona 10: Análisis crítico del proyecto (auditoría interna)

> **Fecha**: 28 de julio de 2026.
> **Método**: revisión multi-agente exhaustiva — 4 lectores por dimensión (tesis de
> mercado, modelo de negocio, código, roadmap) + 3 críticos cruzados (consistencia
> numérica, abogado del diablo, economía unitaria). Se ejecutó `demo_automatica.py` y se
> verificó la aritmética a mano. **29 discrepancias confirmadas con archivo:línea.**
> **Propósito**: registro honesto del estado real del proyecto para leerse antes de
> cualquier pitch, decisión de inversión de tiempo, o conversación con terceros.

---

## 1. Veredicto ejecutivo

**El repositorio es un buen mapa de investigación; todavía no es un negocio.** La tesis
direccional (desperdicio por factor de potencia y demanda punta en PYMES BT2/BT3,
capturable vía modelo ESCO con subsidio) es plausible y está mejor documentada que el
promedio. Pero el proyecto se sostenía sobre **cuatro incógnitas existenciales** sin plan
de cierre, y las tres capas del repo (investigación, material de venta, simulador) se
contradecían entre sí.

Parte de los problemas mecánicos se corrigieron en el commit que acompaña este documento
(ver §6). Las incógnitas existenciales **solo se cierran en terreno** — ver
`11_PLAN_VALIDACION.md`.

---

## 2. Lo que está sólido (fortalezas verificadas)

1. **Regla regulatoria central correcta y consistente**: recargo = 1% por cada 0.01 bajo
   cosϕ 0.93, implementada bien en el código (fórmula verificada a mano, clamp a cero
   incluido).
2. **Disciplina de trazabilidad [dato]/[estimación]** cumplida con rigor en `01` y `07`.
3. **Doble ancla de mercado**: Min. Energía (~USD 100M potencial EE) + BID IDB-TN-2038
   (~USD 45M/año efectivo, ~USD 3.000M potencial), con nota de conciliación.
4. **Validación institucional del modelo ESCO por dos vías independientes**: programa
   CAPE (39 hospitales, solo 3 con problemas de ahorro) y andamiaje financiero operativo
   (BancoEstado 12 años/80%, ASE validador, CESCE/SURA aseguradoras).
5. **Posicionamiento delimitado** (`08`): capa demanda vs oferta; Net Billing vs PMGD; el
   fin del precio estabilizado PMGD empuja el valor hacia el autoconsumo/eficiencia.
6. **Honestidad intelectual**: preguntas abiertas declaradas (`01` §9), advertencias de
   precisión del simulador, la demo no esconde casos malos (call center sale NO VIABLE).
7. **Barreras de adopción trianguladas** entre Min. Energía y BID, y el modelo ESCO
   propuesto ataca exactamente esas barreras.
8. **Stack técnico bien decidido** para un dev Python solo (FastAPI+Pydantic, HTMX,
   reutiliza los simuladores existentes).

---

## 3. Las cuatro incógnitas existenciales (no se arreglan editando archivos)

### 3.1 ¿Qué % de PYMES BT2/BT3 tiene FP < 0.93? — NADIE LO SABE
Todo el producto líder (condensadores, payback corto) depende de esta penetración, que no
está medida. Los 6 casos son simulados; no hay **ninguna factura real** en el repo (pese a
que `FUENTES` afirmaba "verificado en múltiples facturas" — afirmación retirada). Si la
penetración real es baja, el SAM colapsa. **Agravante competitivo**: las distribuidoras ya
tienen este dato con nombre y RUT — ellas cobran el recargo.

### 3.2 ¿Sobre qué base se cobra el recargo? — DIFERENCIA DE ~2.4x
El repo aplicaba el recargo sobre tres bases distintas: solo energía (código), factura
total (`parametros.py`, ejemplos de `00`). La diferencia es ~2.4x en el valor del producto.
**Estado actual**: el código quedó unificado en la base **energía** (criterio conservador)
con flag `RECARGO_SOBRE_FACTURA_TOTAL` documentado en `factura_electrica.py`, hasta
verificar contra el decreto tarifario CNE y facturas reales.

### 3.3 ¿El canal de electricistas convierte? — HIPOTÉTICO Y DESINTERMEDIABLE
Estado declarado "PENDING": sin nombres, sin contrato de canal, sin piloto. Riesgo
estructural: el condensador es un commodity que el electricista puede instalar solo,
quedándose el 100% del margen. El único "pegamento" es el M&V continuo + acceso a
subsidio + garantía — que aún no existen como producto. Todo el SOM cuelga de este canal
sin plan B.

### 3.4 ¿Quién pone el capital del EPC? — NO CUANTIFICADO
"Cliente no gasta nada si no ahorra" exige que alguien financie el CAPEX. La Línea Verde
BancoEstado exige garantías estatales o reales que un fundador solo no tiene; el capital
propio requerido no está cuantificado en ningún archivo. Con margen recurrente EPC de
~$15k/mes/cliente, el equilibrio exige ~140 clientes: **inviable sin capital externo**.
Además: el CEE debe valorarse en **$0** hasta verificar que el mercado de certificados
opera (y existe conflicto de interés: no se puede ser "verificador independiente" del
ahorro del que se cobra 25%).

---

## 4. Problemas mecánicos detectados (y su estado)

### 4.1 Simulador (bugs metodológicos que inflaban el pitch) — CORREGIDOS
| Problema | Efecto | Estado |
|---|---|---|
| Demanda punta cobrada 12 meses (real: abr–sep, 6 meses) | Sobreestimaba factura anual; duplicaba ahorro de peak shaving | ✅ Corregido: año = 6 meses punta + 6 normales |
| Punta cobrada a tarifas BT2 (que no la miden) | +28% de factura inexistente en caso tienda | ✅ Corregido: punta solo BT3/BT4 |
| Payback = capex / ahorro **bruto** (ignoraba SaaS + mantenimiento) | Tienda: mostraba 3.2 años; real ~5.0. Call center: flujo negativo mostrado como "payback 13.3 años" | ✅ Corregido: payback sobre ahorro neto de opex |
| ROI incluía devolución del capital (break-even se imprimía "100%") | Cliente leería "duplico mi plata" donde hay empate | ✅ Corregido: ROI = beneficio neto / capex |
| Ahorro contaba IVA (crédito fiscal para una empresa) | Ahorro ~19% sobreestimado | ✅ Corregido: ahorro sobre subtotal sin IVA |
| `aplicar_solucion` podía EMPEORAR un FP > 0.93 | Caso borde | ✅ Corregido con `max()` |
| "TIR aproximado" no era TIR (código muerto engañoso) | — | ✅ Reemplazado por retorno anual simple documentado |
| Mensaje umbral payback inconsistente (<100 vs ">10 años") | — | ✅ Corregido |
| "4 meses (abril-septiembre)" en parametros.py | Son 6 | ✅ Corregido |

### 4.2 Material de venta desincronizado — CORREGIDO
- **Ningún payback de la tabla del README coincidía con la demo** (tienda 0.9 vs 3.2;
  call center 2.5 vs 13.3). El caso estrella del taller usaba números de la manufactura.
- La tabla "Casos reales que simulamos" de `FUENTES` tampoco salía del simulador.
- **Estado**: tablas regeneradas desde la salida real de la demo corregida (los números
  nuevos son menos espectaculares y más defendibles).

### 4.3 Inconsistencias de documentación — CORREGIDAS
- `00`: precios ilustrativos ~3x los investigados ($550/kWh vs $195), errores aritméticos,
  horario punta 18–23h (es 18–22h), referencias FFEE obsoletas → corregido/anotado.
- Pricing caótico: 6 precios de SaaS, ingreso por cliente a 5 años con diferencias de
  3–6x entre `03`, `04b` y `00`, 3 valores de comisión FFEE → unificado en
  `09_PRICING_CANONICO.md` (los docs antiguos remiten allí).
- `04b`/`00` anclados a "FFEE 50%" cuando el programa ancla es Ponle Energía (50–80%) →
  sincronizado.
- Edelmag región XIV → XII; prima seguro ESI en `07` (0,5–1% vs 1,5%) → aclarado (el BID
  usó 1,5% como supuesto conservador de su análisis).
- Conciliaciones agregadas en `01`: universo 1,5M (SII 2026) vs ~1M (BID 2020); USD 100M
  (Min. Energía) vs USD 3.000M (potencial BID).
- Claim "15–35% adicional" re-etiquetado como estimación de tercero (fuente blog), no [dato].

### 4.4 Riesgos señalados por el abogado del diablo — ABIERTOS (por diseño)
- **Riesgo regulatorio**: si CNE migra a cobro de reactivos por kVArh medido (tendencia
  con medidores inteligentes) o cambia el umbral 0.93, el producto líder cambia por
  decreto. No hay análisis de sensibilidad regulatoria.
- **Competencia descendente**: Enel X/CGE y las ~34 ESCOs de ANESCO pueden bajar al
  segmento con ventaja de datos y balance. `08` no las analiza como competidor directo.
- **Dependencia de subsidios**: el presupuesto de Ponle Energía cayó ~85% entre 2021
  ($3.781M) y 2022 ($588M) — dato presente en `03` sin análisis de escenario.
- **Evidencia envejecida**: encuesta EE 2018, BID 2020 con precios 2019 — en un mercado
  que vivió un tarifazo de +43% (que, en todo caso, mejora los paybacks).
- **SEC/TE1**: intervenir tableros exige instalador autorizado y declaración TE1; el repo
  no lo mencionaba (ahora está en `11_PLAN_VALIDACION.md`).

---

## 5. Economía y camino al EBITDA (síntesis del crítico financiero)

Reconstrucción con cifras del propio repo (detalle en `09_PRICING_CANONICO.md`):

| Concepto | Valor |
|---|---|
| One-off por cliente nuevo (diagnóstico + comisiones + márgenes) | $1.4M–3.9M CLP |
| Margen recurrente/cliente/mes (híbrido, neto de comisiones + SIM) | ~$33k CLP |
| Costos fijos (infra ~$100k + sueldo fundador $2M **[supuesto]**) | ~$2.1M/mes |
| Equilibrio EBITDA solo con recurrente — híbrido | ~64–70 clientes |
| Equilibrio EBITDA solo con recurrente — EPC 25% | ~140 clientes |
| Equilibrio cubriendo solo infra (sin sueldo) | 3–7 clientes |

**Conclusiones duras**:
1. La meta de 20–25 clientes/año 1 del plan de canal generaría ~$600–825k/mes recurrente:
   cubre infraestructura pero solo 30–40% del sueldo del fundador.
2. La misma meta es **físicamente imposible**: 20–25 diagnósticos × 40–60 h = 800–1.500
   horas, en paralelo a 6 meses full-time de desarrollo. Meta realista: **8–15 clientes**.
3. **El EBITDA del año 1–2 viene de los one-offs, no del SaaS.** La línea que factura
   primero es el **diagnóstico energético pagado** ($300–500k): vendible hoy con el
   SDM630 temporal + los simuladores existentes. 4–5 diagnósticos/mes cubren todos los
   costos fijos sin un solo cliente SaaS.
4. Cada diagnóstico ES el generador de oportunidades (la visión "entorno de
   oportunidades"): de él nacen los proyectos de condensadores → instalación con margen →
   SaaS → (mucho después) EPC.
5. **Postergar EPC y valorar CEE en $0** hasta tener capital identificado y mercado
   verificado, respectivamente.

**Secuencia de facturación recomendada**:
1º Diagnóstico pagado → 2º margen instalación condensadores → 3º SaaS/híbrido →
4º comisiones de subsidio (dependen de convocatoria) → 5º EPC/CEE (postergados).

**Bloqueador administrativo** (ausente del roadmap): inicio de actividades SII,
facturación electrónica, contrato tipo de diagnóstico, registro AgenciaSE, SEC/TE1,
pasarela de pago. Sin esto no se factura el primer peso. → hitos con fecha en
`11_PLAN_VALIDACION.md`.

---

## 6. Qué se corrigió en este commit y qué sigue abierto

**Corregido (mecánico)**: simulador (punta 6 meses + filtro tarifa, payback neto, ROI
neto, ahorro sin IVA, fp con max, retorno anual, mensajes), tablas de README y FUENTES
regeneradas desde la demo, precios y aritmética de `00`, sincronización Ponle Energía en
`00`/`04b`, pricing canónico (`09`), conciliaciones y re-etiquetados en `01`/`07`/`FUENTES`,
Edelmag XII.

**Abierto (requiere terreno, no edición)**: las 4 incógnitas existenciales de §3 — ver
plan con fechas en `11_PLAN_VALIDACION.md`.

---

**Estado**: ✅ Auditoría registrada. Este documento debe releerse antes de cualquier pitch
y actualizarse cuando se cierren las validaciones de `11_PLAN_VALIDACION.md`.
