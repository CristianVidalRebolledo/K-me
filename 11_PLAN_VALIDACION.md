# Zona 11: Plan de validación 30–60–90 días

> **Inicio**: 28 de julio de 2026. Este plan cierra las cuatro incógnitas existenciales
> de `10_ANALISIS_CRITICO.md` §3 **antes de escribir más producto**. Cada ítem tiene
> criterio de éxito medible y fecha. Si una validación falla, la decisión asociada se
> toma de inmediato (pivotar, buscar canal alternativo, postergar línea de negocio).

---

## Fase 1 — 30 días (al 28 de agosto de 2026)

### 1.1 Facturas reales: el dato existencial 🔴 PRIORIDAD MÁXIMA
- **Qué**: conseguir **20–30 facturas eléctricas reales BT2/BT3** (electricistas
  conocidos, contadores, gremios locales; pagar si hace falta).
- **Medir**: (a) % con recargo por factor de potencia, (b) magnitud del recargo,
  (c) **sobre qué base lo cobra cada distribuidora** (¿% sobre energía o sobre total?),
  (d) desviación factura real vs simulador (meta: <5%).
- **Criterio de éxito**: ≥20 facturas analizadas y la base del recargo confirmada contra
  al menos 2 distribuidoras (Enel + CGE). Actualizar `RECARGO_SOBRE_FACTURA_TOTAL` en
  `factura_electrica.py` y re-generar todas las tablas.
- **Decisión si falla**: si <20% de las facturas muestra recargo material (>3% de la
  cuenta), **pivotar el producto líder** (de condensadores a demanda punta / telemetría
  pura) antes de gastar en el MVP.

### 1.2 Verificación regulatoria de la base del recargo
- **Qué**: localizar en el decreto tarifario CNE vigente (o pliego de la distribuidora)
  la definición exacta del cobro por factor de potencia.
- **Criterio de éxito**: cita textual del decreto archivada en `FUENTES_Y_DESPERDICIO.md`.

### 1.3 Hitos administrativos para poder facturar
- [ ] Inicio de actividades ante SII (o confirmación de la sociedad a usar).
- [ ] Facturación electrónica operativa.
- [ ] Contrato tipo de **diagnóstico energético** (1–2 páginas, revisado por abogado).
- [ ] Registro en el **Registro Energético de AgenciaSE** (declarar modelo ESCO).
- **Criterio de éxito**: capacidad legal de emitir la primera factura de diagnóstico.

---

## Fase 2 — 60 días (al 28 de septiembre de 2026)

### 2.1 Canal: electricistas con nombre y apellido
- **Qué**: firmar acuerdo simple con **2 electricistas reales** (comisiones según
  `09_PRICING_CANONICO.md`, no-competencia acotada, propiedad del cliente/data,
  responsabilidad **SEC/TE1** del instalador).
- **Criterio de éxito**: 2 acuerdos firmados y ≥5 leads calificados aportados por el canal.
- **Decisión si falla**: declarar el canal muerto y activar plan B (contadores, gremios
  de barrio industrial, corredores de seguros PYME).

### 2.2 Primeras ventas de diagnóstico (la primera línea de EBITDA)
- **Qué**: vender **3 diagnósticos pagados** ($300–500k c/u) usando el SDM630 temporal +
  los simuladores existentes. No requiere SaaS ni backend.
- **Medir**: CAC real (horas + gastos por venta), tasa de conversión lead→diagnóstico,
  horas reales por diagnóstico (vs las 40–60 estimadas).
- **Criterio de éxito**: 3 ventas y desviación simulador vs factura real <5% en esos
  clientes.

### 2.3 Cotizaciones reales (cerrar el "PENDING" de `02`)
- **Qué**: cotizar SDM630, RUT956, SIM/plan de datos, banco de condensadores típico
  (25–50 kVAr) e instalación con electricista autorizado SEC.
- **Criterio de éxito**: `02_TECNICO_HARDWARE_ARQUITECTURA.md` actualizado con costos
  reales y el precio de instalación fijado en costo + 30–40% en `09_PRICING_CANONICO.md`.

---

## Fase 3 — 90 días (al 28 de octubre de 2026)

### 3.1 SAM bottom-up en pesos
- **Qué**: con los datos de 1.1 + solicitud de transparencia a CNE/SEC (nº de clientes
  BT2/BT3 por distribuidora), construir: clientes BT2/BT3 × % con FP<0.93 × ingreso
  anual híbrido.
- **Criterio de éxito**: SAM expresado en CLP/año en `01_MERCADO_PYMES_CHILE.md` §7,
  reemplazando "decenas de miles de empresas". **Aunque dé chico, se publica** — si da
  negocio de nicho, se ajusta ambición o pricing, no se esconde.

### 3.2 Análisis de competencia descendente
- **Qué**: documentar en `08_PANORAMA_INDUSTRIA.md` qué ofrecen hoy Enel X / CGE y las
  ESCOs de ANESCO al segmento PYME, y cuál es nuestra defensa concreta (velocidad, foco,
  canal, costo).

### 3.3 Escenarios de estrés (subsidio y regulación)
- **Qué**: proyección a 24 meses en 3 escenarios: (a) Ponle Energía con presupuesto
  nivel 2022 (−85%), (b) sin subsidio, (c) CNE cambia la regla del 0.93 (cobro por kVArh).
- **Criterio de éxito**: el negocio cierra al menos en (a) y (b) con la secuencia
  diagnóstico → instalación → SaaS. Si solo cierra en el escenario optimista, replantear.

### 3.4 Decisión Go/No-Go de producto (reemplaza el de la semana 16 del roadmap)
- **GO** si: base del recargo confirmada, ≥3 diagnósticos vendidos, ≥1 proyecto de
  condensadores cerrado, 2 electricistas activos.
- **NO-GO / pivote** si: penetración FP <20%, 0 diagnósticos vendidos en 60 días, o
  canal sin reemplazo viable.

---

## Registro de resultados

| Validación | Fecha cierre | Resultado | Decisión |
|---|---|---|---|
| 1.1 Facturas reales | | | |
| 1.2 Base del recargo (CNE) | | | |
| 1.3 Hitos administrativos | | | |
| 2.1 Canal firmado | | | |
| 2.2 Tres diagnósticos | | | |
| 2.3 Cotizaciones | | | |
| 3.1 SAM en pesos | | | |
| 3.4 Go/No-Go | | | |

---

**Estado**: ⏳ EN EJECUCIÓN desde 28-jul-2026. Actualizar la tabla de registro al cerrar
cada validación; reflejar conclusiones en `10_ANALISIS_CRITICO.md`.
