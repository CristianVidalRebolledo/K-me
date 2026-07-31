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
2. **Guion de contacto**: entrar por el dolor de vendimia y el recargo invisible —
   *"¿sabías que tus compresores de frío probablemente te están sumando un recargo por
   factor de potencia que no aparece como línea en la factura?"*
3. **Oferta de entrada**: diagnóstico pagado con medición real de 30 días (idealmente
   cubriendo vendimia).
4. **Verificaciones del sector** (además de las de `../11_PLAN_VALIDACION.md`):
   - [ ] Confirmar factor de potencia real de 3–5 bodegas (dato del diagnóstico).
   - [ ] Confirmar tarifa (¿BT3? ¿AT si son grandes?) y si miden demanda punta.
   - [ ] Estimar el pico de vendimia vs. base para dimensionar peak shaving.
   - [ ] Mapear quién compra orujo hoy en la zona (destilerías, extractores) para la
         conversación de residuos.

---

## 10. Programas públicos aplicables (para el pitch)

Detalle y fuentes en `../03_SUBSIDIOS_FINANCIAMIENTO.md` §0-bis. Resumen para el vendedor:

| Programa | Qué financia | Encaje con la bodega |
|---|---|---|
| **CNR – Ley de Riego 18.450** ⭐ | Hasta 90% de riego/drenaje, **permite ERNC** (bombeo solar, FV) | Viña con riego → financia la solar; concursable, ventanas anuales |
| **FIA – Innovación de Interés Privado** ⭐ | Innovación agroalimentaria (hasta $50M/80% en validación) | Financia el **piloto** de telemetría + optimización de frío |
| **CORFO** (PDT, PROFO, Crece, Ley I+D 35%) | Transferencia tecnológica, fomento, crédito tributario I+D | Llevar telemetría a un valle de viñas (grupo); I+D si hay producto propio |
| **Ponle Energía a tu Pyme** | EE + ERNC (50–80%) | ⚠️ Sin convocatoria vigente desde 2022 — no comprometer |

**Regla**: son **aceleradores**, no la base de la venta. El diagnóstico + factor de potencia
cierra con la economía del cliente; el subsidio agranda el proyecto (solar, riego) y es un
gancho ("te gestiono la postulación"). Postula la bodega; nosotros asesoramos (comisión 3–5%).

⚠️ **Timing**: varias convocatorias 2026 ya cerraron (jun–jul). Planificar para el **ciclo
2027** y verificar bases al abrirse cada llamado.

---

## 11. Diálogo de ventas (guion para el vendedor)

> Guion base, adaptable. Objetivo de la primera conversación: **vender el diagnóstico
> pagado**, no la solución. No prometer ahorros en cifras hasta tener la factura real.

### Apertura (gancho: el recargo invisible + el pico de vendimia)

> "Hola [nombre], hablo de [empresa]. Trabajamos con bodegas ayudándolas a bajar la cuenta
> de luz, sobre todo la del frío. Una pregunta rápida: **¿sabía que sus compresores de
> refrigeración probablemente le están sumando un recargo por factor de potencia que ni
> siquiera aparece como línea separada en la factura?** A la mayoría de las bodegas les
> pasa y no lo ven. ¿Le hace sentido que conversemos 5 minutos?"

Gancho alternativo (estacional): *"¿Cómo se le dispara la cuenta en vendimia cuando todo el
frío trabaja al máximo?"*

### Descubrimiento (calificar — 4 preguntas)

1. "¿Vinifican acá o solo cultivan?" → *(nos interesa quien vinifica: tiene el frío)*
2. "¿Cuánto les llega la cuenta de luz en un mes de vendimia, más o menos?" → *(tamaño)*
3. "¿Saben qué factor de potencia les marca la factura? ¿0.9-algo?" → *(dolor)*
4. "¿Quién les ve hoy el tema eléctrico?" → *(canal / competencia)*

Si vinifica + factura relevante + factor bajo/desconocido → **es candidato**.

### Propuesta de valor (el diagnóstico)

> "Le propongo algo concreto: instalamos un medidor por 30 días en su tablero —**sin cortar
> nada, sin obra**, lo pone un eléctrico autorizado— y le entregamos un informe que le dice
> exactamente **en qué se va la energía, cuánto le cuesta el recargo del frío, y cuánto
> podría recuperar**. Con números de su bodega, no de un folleto. Eso cuesta [monto] y si
> avanza con una solución, se lo descuento del proyecto."

### Manejo de objeciones

| Objeción | Respuesta |
|---|---|
| *"Ya tengo electricista"* | "Perfecto, trabajamos **con** su eléctrico —él instala. Nosotros ponemos el análisis y el monitoreo que un eléctrico normalmente no hace: medir el factor de potencia y cuantificar el ahorro." |
| *"No es buen momento, estamos en vendimia"* | "Justamente vendimia es **el mejor momento para medir**, porque es cuando el frío trabaja al máximo y se ve el problema real. La instalación toma una hora y no interrumpe nada." |
| *"¿Y cómo sé que voy a ahorrar?"* | "No le prometo un número hasta medir. Por eso es un **diagnóstico**: si los datos no muestran ahorro que valga la pena, se lo digo y no le vendo nada. Solo avanzamos si el payback es corto." |
| *"Está caro / hay subsidio?"* | "El diagnóstico se descuenta si avanza. Y sí: hay programas (Ley de Riego, FIA) que pueden cofinanciar la inversión mayor; **yo le gestiono la postulación**." |
| *"Mándame info por correo"* | "Se la mando, pero lo que de verdad sirve es la medición de su bodega. ¿Le parece si agendamos la visita del medidor para [fecha] y de paso ve el informe?" |

### Cierre

> "Entonces quedamos así: [fecha] pasa el técnico, instala el medidor —una hora, sin
> cortar—, y en [X] semanas le tengo el informe con los números. ¿Le queda bien [día]?"

### Segunda conversación (tras el informe / expansión)

- Presentar el ahorro **con sus datos** → proponer condensadores (payback corto).
- Mencionar el **frío en punta** y la **solar con Ley de Riego** como fase siguiente.
- Dejar sembrado el **orujo/borra**: *"su orujo hoy probablemente lo regala; tiene aceite
  de pepita, polifenoles y ácido tartárico recuperables — cuando quiera lo vemos"* (§6).

---

**Estado**: ✅ Dossier del sector vitivinícola listo (jul 2026), con programas públicos y
diálogo de ventas. Pendiente: poblar la lista de candidatos (§8) y ejecutar los 3 primeros
diagnósticos.
