# Proyecto sectorial: Viñas y bodegas (vitivinícola)

> Dossier de sector candidato. Cruza con `../07_MODELO_ESI_BID.md` (datos primarios del
> sector), `../09_PRICING_CANONICO.md` (precios), `../02_TECNICO_HARDWARE_ARQUITECTURA.md`
> (stack de telemetría) y `../12_SECTORES_PRODUCTIVOS.md` (marco general).
> Cifras marcadas **[dato]** (con fuente) o **[estimación]**. Julio 2026.

---

## 1. Resumen ejecutivo

La bodega (vinificación) es un cliente casi ideal para nuestro servicio: **la
refrigeración es ~45% de su consumo eléctrico** **[dato BID]** y aparece en **tres etapas
distintas** del proceso (fermentación, estabilización por frío, guarda). Eso significa
carga inductiva pesada (compresores) → **factor de potencia bajo** (nuestro producto
ancla) + un pico de demanda estacional en vendimia. Además el orujo, su principal residuo
sólido, **sí es sustrato viable de biogás** (a diferencia del aserrín) y tiene rutas de
valorización con valor real — una conversación de segunda etapa.

**Entrada al cliente**: diagnóstico energético pagado (medición en el empalme + análisis de
factura). **Escalamiento**: corrección de factor de potencia → gestión del frío (peak
shaving) → SaaS de monitoreo → solar de autoconsumo. **Muy segunda etapa**: valorización
del orujo.

---

## 2. Por qué el sector vitivinícola

- **Priorizado por el BID** entre los 4 subsectores de mayor oportunidad para el Modelo
  ESI en Chile (puntaje 73%) **[dato BID, IDB-TN-2038]**.
- **Universo**: ~14.413 empresas vitivinícolas; de ellas ~**401 son bodegas (vinícolas)**,
  que son las intensivas en energía; ~240 son pequeñas/medianas **[dato BID]**.
- **Concentración geográfica** (facilita rutas y prospección): **Biobío ~6.433**, **Maule
  ~5.396**, **O'Higgins ~1.534** propiedades vitícolas **[dato BID]**. Publican teléfono
  en Google Maps por rubro ("viña", "bodega", "vineyard").
- **Costo energético de una bodega** (referencia) **[dato BID]**:
  - Grande: ~USD 12.372/mes (USD 8.414 eléctrica + 3.958 térmica)
  - Mediana: ~USD 2.963/mes
  - Pequeña: ~USD 1.362/mes
- **Reparto del consumo eléctrico de una bodega** **[dato BID]**: refrigeración **45%**,
  calentamiento 21%, equipamiento vinífero 16%, aire comprimido 8%, bombeo/iluminación ~5%
  c/u.

---

## 3. El proceso y dónde duele la energía (respuesta técnica)

**Sí, la temperatura es central — y el problema es sobre todo de FRÍO, no de calor.**
La fermentación es **exotérmica**: la levadura convierte azúcar en alcohol + CO₂ + **calor**.
El mosto se calienta solo, y si no se controla, la temperatura se dispara, la levadura
muere o genera sabores defectuosos. Por eso la bodega **enfría**, no calienta, en la etapa
clave. El frío aparece en tres momentos:

| Etapa | Qué pasa | Carga energética |
|---|---|---|
| **Fermentación** | Blanco: se fermenta **frío** (12–18 °C) para conservar aromas → refrigeración intensa. Tinto: más cálido (25–30 °C) pero hay que **enfriar** para no pasarse. | Pico de frío en **vendimia** (feb–abr): demanda alta y estacional |
| **Estabilización tartárica por frío** | Se baja el vino a ~**−4 °C** por días/semanas para precipitar tartratos (cristales). | **Gran carga de frío**, muy intensiva en energía |
| **Guarda / conservación** | Mantener cubas y sala de barricas a temperatura estable. | Frío continuo, todo el año |

Sobre tu duda de "frenar la fermentación con químicos o con frío": **ambas cosas existen
y se combinan**. Para detener la fermentación (p. ej. para dejar azúcar residual en vinos
dulces) se **baja la temperatura** (la levadura entra en dormancia) y se ajusta **SO₂**
(anhídrido sulfuroso) + trasiego/filtración. El frío es la palanca energética; el químico
es complementario.

**Implicación**: la refrigeración es simultáneamente (a) el mayor consumo, (b) la mayor
fuente de factor de potencia bajo (compresores), y (c) lo que crea el **pico de demanda de
vendimia**. Es el corazón del proyecto.

---

## 4. Qué ofrecer (secuencia de producto)

Ordenado por payback/CAPEX, alineado con `../09_PRICING_CANONICO.md`:

1. **Diagnóstico energético pagado** ($300–500k CLP). Medir 30 días en el empalme +
   analizar 12 facturas. Entrega: dónde se va la energía, factor de potencia real, pico de
   vendimia, y el ranking de oportunidades. **Es la primera venta y no depende de nada más.**
2. **Corrección de factor de potencia** (banco de condensadores). Los compresores de frío
   y bombas dan cosϕ bajo → recargo. Payback corto (ver casos BT3 del simulador). **Producto
   ancla.**
3. **Gestión del frío / peak shaving** (thermal storage o control de demanda). Pre-enfriar
   o desplazar carga fuera de la ventana punta (18–22h, abr–sep) y aplanar el pico de
   vendimia. CAPEX mayor → evaluar caso a caso con el diagnóstico.
4. **SaaS de monitoreo** (modelo híbrido $30k + 15% del ahorro). Dashboard del frío en
   tiempo real, alertas de desviación, M&V.
5. **Solar de autoconsumo (Net Billing)** como upsell. Payback largo (8–12 años,
   `../07_MODELO_ESI_BID.md`); no liderar con esto.
6. **[Segunda etapa, gran cuenta] Valorización del orujo** (ver §6).

---

## 5. Dónde conectar la telemetría

**Punto principal: el tablero general, aguas abajo del EMPALME.** Ahí se mide la "verdad de
facturación" (lo mismo que ve la distribuidora):

```
[Red distribuidora]
      │
   [EMPALME + medidor de la distribuidora]   ← referencia de la factura
      │
[Tablero general (TGD)]  ←──── AQUÍ instalamos el medidor Eastron SDM630
      │                        · Voltaje: tomas directas de las 3 fases
      │                        · Corriente: 3 transformadores de corriente (TC / CT)
      │                          abrazando los conductores principales
      │                        · Mide: V, I, P, Q, cosϕ, kWh, demanda máx, THD
      │                        · Salida Modbus RTU (RS-485) → gateway Teltonika RUT956 → nube
      │
      ├─→ [CCM / tablero de REFRIGERACIÓN]  ←──── (recomendado) 2º medidor aquí
      │        compresores, condensadores, torres          para aislar el 45% del consumo
      │
      ├─→ [Bombas / equipamiento vinífero]
      └─→ [Iluminación, oficinas, servicios]
```

Detalle técnico:
- El **SDM630 no corta corriente**: mide por **transformadores de corriente (TC)** que se
  abrazan alrededor de los cables principales, sin interrumpir el suministro. Instalación
  rápida y de bajo riesgo (la hace el electricista autorizado **SEC**, con declaración
  **TE1** si se interviene el tablero — ver `../11_PLAN_VALIDACION.md`).
- **Dónde va físicamente**: dentro del **tablero general de distribución (TGD)**, junto a
  las protecciones principales, después del empalme/medidor de la distribuidora.
- **Sub-medición del frío (muy recomendada)**: un segundo SDM630 en el **centro de control
  de motores (CCM) de refrigeración** aísla el 45% del consumo. Es lo que permite
  optimizar de verdad (y facturar el ahorro con M&V creíble), no solo ver el total.
- **Conectividad**: el RUT956 usa 4G (SIM con plan de datos — costo variable por sitio, ver
  `../09_PRICING_CANONICO.md`). En bodegas rurales sin buena señal, evaluar antena externa.
- **Qué medir primero (diagnóstico de 30 días)**: factor de potencia real, curva de carga
  (para ver el pico de vendimia y la ventana punta), y consumo del frío vs. total.

---

## 6. Residuos: orujo (hollejo) y borra

A diferencia del aserrín, **el orujo SÍ es buen sustrato de biogás** (húmedo, con azúcares
fermentables y buena relación C/N al co-digerir) **[dato]**. Rutas de valorización, de
menor a mayor complejidad:

| Residuo | Rutas de valorización | Nota |
|---|---|---|
| **Orujo / hollejo** (piel, pepita, pulpa) | Destilación (alcohol/pisco), **aceite de pepita de uva**, **polifenoles/antioxidantes** (cosmética, alimentos), **biogás** (digestión anaerobia), compost/biofertilizante, alimento animal | Ruta de alto valor: polifenoles y aceite; ruta energética: biogás |
| **Borra / lías** (sedimento de fermentación) | Recuperación de vino, **ácido tartárico**, biomasa | El ácido tartárico tiene mercado enológico y farmacéutico |
| **Escobajo** (raspón) | Compost, biomasa | Bajo valor |

**Encaje con nuestro negocio (honesto)**: el biogás del orujo es un **proyecto de segunda
etapa y de gran cuenta** — requiere volumen constante, biodigestor y capital. NO es el
gancho. Nuestra entrada es la eficiencia eléctrica del frío. La valorización del orujo se
menciona en el diagnóstico como "oportunidad futura / alianza", posicionándonos como quien
entiende todo el ciclo, sin comprometer un proyecto que no operamos.

**Fuentes**: valorización de orujo y biogás (Energías Renovables; U. de Concepción; U.
Nac. de Cuyo — digestión anaerobia de orujo en bodegas de Mendoza); nota "El orujo de uva:
un residuo vitivinícola prometedor" (reporteagricola.cl, 2025).

---

## 7. Economía del proyecto (orden de magnitud)

Basado en `../09_PRICING_CANONICO.md` y los costos de bodega del BID **[estimación]**:

- **Bodega mediana** (~USD 2.963/mes ≈ ~$2,8M CLP/mes de energía): un factor de potencia
  típico de compresores (0.80–0.85) puede implicar un recargo relevante sobre el costo de
  energía → el diagnóstico lo cuantifica exacto.
- **Ingreso por cliente (one-off)**: diagnóstico $300–500k + margen de instalación de
  condensadores $600k–1.6M = **~$1–2M CLP** por bodega que avanza.
- **Recurrente**: SaaS híbrido $30k + 15% del ahorro (~$48k/mes con ahorro típico).
- **Estacionalidad a considerar**: el pico de vendimia (feb–abr) concentra el consumo; el
  diagnóstico debe cubrir o modelar ese periodo, no un mes cualquiera.

---

## 8. Lista de candidatos (a poblar)

Construir el padrón cruzando **Google Maps por rubro** ("viña", "bodega") con las comunas
vitícolas de **Maule, Ñuble, Biobío, O'Higgins y Valparaíso** (Casablanca, Colchagua,
Curicó, Maule, Itata, etc.). Priorizar **bodegas** (vinifican) sobre viñas que solo
cultivan, porque las primeras tienen el frío.

| # | Nombre | Comuna / Valle | Teléfono | ¿Vinifica? | Factura estimada | Contactado | Notas |
|---|--------|----------------|----------|------------|------------------|------------|-------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

> Meta fase de validación: 20–30 bodegas identificadas, 3 diagnósticos vendidos
> (ver `../11_PLAN_VALIDACION.md`). Priorizar medianas (mejor ratio dolor/complejidad).

---

## 9. Plan de contacto y validación específico del sector

1. **Poblar la tabla §8** con 20–30 bodegas de un valle acotado (empezar por uno: p. ej.
   Maule o Itata, alta densidad).
2. **Guion de contacto**: entrar por el dolor de vendimia y el recargo mal entendido —
   *"¿sabía que sus equipos de frío probablemente le están cargando una multa en la cuenta
   de la luz que casi nadie revisa ni sabe cómo eliminar?"* (registro **usted**, igual que
   el guion completo de §11).
3. **Oferta de entrada**: diagnóstico pagado con medición real de 30 días (idealmente
   cubriendo vendimia).
4. **Verificaciones del sector** (además de las de `../11_PLAN_VALIDACION.md`):
   - [ ] Confirmar factor de potencia real de 3–5 bodegas (dato del diagnóstico).
   - [ ] Confirmar tarifa (¿BT3? ¿AT si son grandes?) y si miden demanda punta.
   - [ ] Estimar el pico de vendimia vs. base para dimensionar el aplanamiento del pico
         de demanda (peak shaving).
   - [ ] Mapear quién compra orujo hoy en la zona (destilerías, extractores) para la
         conversación de residuos.

---

## 10. Programas públicos aplicables (para el pitch)

Detalle y fuentes en `../03_SUBSIDIOS_FINANCIAMIENTO.md` §0-bis. Resumen para el vendedor.
Siglas: **EE** = eficiencia energética; **ERNC** = energías renovables (solar, eólica, etc.);
**FV** = fotovoltaica (paneles solares); **I+D** = investigación y desarrollo.

| Programa | Qué financia | Encaje con el cliente |
|---|---|---|
| **CNR – Ley de Riego 18.450** ⭐ | Hasta 90% de obras de riego/drenaje; **permite incluir energía solar para el riego** (bombeo solar / paneles) | Aplica al **campo con riego**, NO al frío de la bodega. Solo si el mismo dueño tiene riego propio. Concursable, ventanas anuales |
| **FIA – Innovación de Interés Privado** ⭐ | Innovación agroalimentaria (hasta $50M / 80% en validación) | Financia el **piloto** de telemetría + optimización de frío |
| **CORFO** (PDT, PROFO, Crece, Ley I+D con crédito tributario 35%) | Transferencia tecnológica, fomento, crédito por I+D | Llevar telemetría a un valle de viñas (grupo); I+D si hay producto propio |
| **Ponle Energía a tu Pyme** | EE + ERNC (50–80%) | ⚠️ Sin convocatoria vigente desde 2022 — no comprometer |

**Aclaración importante (viña vs bodega)**: el dolor que atacamos es el **frío de la bodega**
(eléctrico). Para eso **no aplica la Ley de Riego** (que es para el riego del campo) ni la
solar de la bodega califica como riego. La solar de la bodega va por **Net Billing**
(`../08_PANORAMA_INDUSTRIA.md`). CNR solo entra si el cliente además tiene riego propio y
quiere solar **para el bombeo de riego**. No ofrecer Ley de Riego para condensadores/frío.

**Regla**: los subsidios son **aceleradores**, no la base de la venta. El diagnóstico +
corrección de factor de potencia cierra con la economía propia del cliente; el subsidio
agranda el proyecto (solar, riego) y es un gancho de conversación ("le gestiono la
postulación"). La bodega postula como titular; nosotros gestionamos la postulación y
cobramos una comisión de **3–5% sobre el monto aprobado del subsidio** (ver
`../09_PRICING_CANONICO.md`).

⚠️ **Timing**: varias convocatorias 2026 ya cerraron (jun–jul). Planificar para el **ciclo
2027** y verificar bases al abrirse cada llamado.

---

## 11. Diálogo de ventas (guion para el vendedor)

> Guion base, adaptable. Registro: **usted** (formal, como corresponde a un primer
> contacto con un dueño de bodega). Objetivo de la primera conversación: **vender el
> diagnóstico pagado**, no la solución. **Regla de oro**: no prometer cifras de ahorro
> hasta tener la factura real medida (ver `../10_ANALISIS_CRITICO.md`). Traducir todo
> tecnicismo a lenguaje simple; el término técnico se introduce solo después, con interés
> ya ganado.

### Apertura (gancho: la multa oculta del frío + el pico de vendimia)

> "Hola [nombre], hablo de [empresa]. Trabajamos con bodegas ayudándolas a bajar la cuenta
> de luz, sobre todo la del frío. Una pregunta rápida: **¿sabía que sus equipos de frío
> probablemente le están cargando una multa en la cuenta de la luz que casi nadie revisa
> ni sabe cómo eliminar?** A la mayoría de las bodegas les pasa. ¿Le parece si le hago una
> pregunta y vemos si tiene sentido conversar?"

- *Nota para el vendedor*: esa "multa" es el **recargo por factor de potencia** (bajo cosϕ).
  No use el término técnico en la primera frase; introdúzcalo recién si el dueño pregunta
  "¿qué multa?".

Gancho alternativo (estacional): *"¿Cómo se le dispara la cuenta en vendimia, cuando todo
el frío trabaja al máximo?"*

### Descubrimiento (calificar — 4 preguntas)

1. "¿Vinifican acá o solo cultivan?" → *(nos interesa quien vinifica: tiene el frío)*
2. "¿La cuenta de luz en vendimia les llega más cerca de 1, 3 o 5 millones?" → *(tamaño,
   en rango, sin pedir la cifra exacta a un desconocido)*
3. "¿Ha notado en la factura algún cargo que no sabe bien de dónde sale? No se preocupe si
   no lo tiene claro —eso es justo lo que medimos." → *(dolor, sin exigir el dato técnico)*
4. "¿Quién les ve hoy el tema eléctrico?" → *(canal / competencia)*

Si vinifica + factura relevante + no controla el tema eléctrico → **es candidato**.

### Propuesta de valor (el diagnóstico)

> "Le propongo algo concreto: instalamos un medidor en su tablero —**sin cortar nada, sin
> obra**— que queda **midiendo 30 días** para ver bien la vendimia. Con eso le entregamos
> un informe que le dice, **con los números de su bodega**, en qué se le va la energía,
> **el rango real de lo que le cuesta ese cargo del frío**, y cuánto podría recuperar. Eso
> cuesta **entre $300 y $500 mil** (según el tamaño de la bodega) y, si avanza con una
> solución, se lo descuento del proyecto."

- *Nota para el vendedor*: decimos **"el rango real"**, no "exactamente" — la base fina del
  cálculo se confirma con la factura real (ver `../10_ANALISIS_CRITICO.md`). El monitoreo
  del ahorro que ofrecemos después se llama medición y verificación (M&V).

### Manejo de objeciones

| Objeción | Respuesta |
|---|---|
| *"Ya tengo electricista"* | "Perfecto, coordinamos con su eléctrico. La instalación del medidor la hace **nuestro técnico autorizado** (es un equipo específico), y lo que aportamos es el análisis y el monitoreo que un eléctrico normalmente no hace: medir cuánto le cuesta ese cargo y cuantificar el ahorro." |
| *"No es buen momento, estamos en vendimia"* | "Justamente vendimia es **el mejor momento para medir**, porque es cuando el frío trabaja al máximo y se ve el problema real. Instalar el medidor toma una hora y no interrumpe nada." |
| *"¿Y cómo sé que voy a ahorrar?"* | "No le prometo un número hasta medir. Por eso es un **diagnóstico**: si los datos no muestran un ahorro que valga la pena, se lo digo y no le vendo nada. Solo avanzamos si **la inversión se paga rápido con el ahorro**." |
| *"¿Está caro? ¿Hay subsidio?"* | "El diagnóstico se descuenta si avanza. Y para la inversión mayor hay programas del agro (FIA, y la Ley de Riego si tiene riego propio) que pueden cofinanciar; **yo le gestiono la postulación**." |
| *"Mándeme info por correo"* | "Se la mando, pero lo que de verdad sirve es la medición de su bodega. ¿Le parece si agendamos la visita del medidor para [fecha] y de paso ve el informe?" |

### Cierre

> "Entonces quedamos así: [fecha] pasa nuestro técnico e **instala el medidor en una hora,
> sin cortar nada**; **queda midiendo 30 días** —cubriendo la vendimia— y **unas 2 semanas
> después de retirarlo** le entrego el informe con los números. En total, alrededor de 6
> semanas. ¿Le queda bien [día]?"

### Segunda conversación (tras el informe / expansión)

- Presentar el ahorro **con sus datos** → proponer condensadores (se pagan rápido).
- Explicar que **el frío trabajando en horario de punta** (18–22h, abr–sep) encarece la
  cuenta y que ese consumo se puede desplazar; proponerlo como fase siguiente. La solar,
  si tiene riego, puede ir cofinanciada con la Ley de Riego (solo para el bombeo de riego);
  la solar de la bodega va por Net Billing.
- Dejar sembrados los residuos (§6): *"su orujo hoy probablemente lo regala, y de ahí se
  sacan productos con valor —aceite y antioxidantes—; y de la borra, ácido para la
  industria. Cuando quiera se lo mostramos con números."*

---

**Estado**: ✅ Dossier del sector vitivinícola listo (jul 2026), con programas públicos y
diálogo de ventas. Pendiente: poblar la lista de candidatos (§8) y ejecutar los 3 primeros
diagnósticos.
