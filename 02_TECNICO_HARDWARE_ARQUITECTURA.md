# Zona 2: Análisis Técnico - Hardware + Arquitectura + Stack

## Objetivo
Definir la arquitectura técnica mínima viable, costos reales, y flujo de datos seguro.

---

## 1. Flujo de Datos

```
[Tablero Eléctrico]
        ↓
[Medidor: Eastron SDM630] (Modbus RTU)
        ↓
[Gateway: Teltonika RUT956] (4G)
        ↓
[Backend: Railway + Supabase] (Cloud)
   Python + FastAPI + Pydantic (tipado fuerte)
        ↓
[Dashboard: HTMX + Jinja2 + Tailwind] (Web)
   + JS de gráficos puntual (Plotly/uPlot) en paneles en tiempo real
        ↓
[Electricista + Pyme: Usan app]
```

---

## 2. Hardware: Costos (USD)

### Medidor Eastron SDM630
- Costo: $80-120
- Características: Modbus RTU, trifásico, precisión ±1%

### Gateway Teltonika RUT956
- Costo: $200-250
- Características: 4G/LTE, WiFi, Ethernet, RS485

### Total instalación
```
Medidor + Gateway = $405-600 USD (~$405k-600k CLP)
Instalación Labor = $200-400 USD (~$200k-400k CLP)
TOTAL = $605-1,000 USD (~$605k-1M CLP)
```

---

## 3. Stack Backend

### Railway (Hosting)
- API REST: $10-30 USD/mes
- Workers: $5-15 USD/mes

### Supabase (Database)
- PostgreSQL + TimescaleDB: $25-100 USD/mes
- Auth + Storage: Incluido

### Frontend
- HTMX + Jinja2 servido por el backend FastAPI: $0 USD/mes adicional
  (se sirve desde el mismo proceso backend; ver stack en `06_ROADMAP_TECNICO_MVP.md`)

**Total mensual**: $50-160 USD (~$50k-160k CLP/mes)

---

## 4. MVP Fases

**Fase 1 (8 semanas)**: Telemetría básica
**Fase 2 (8 semanas)**: Alertas + Análisis
**Fase 3 (8 semanas)**: EPC Integration

**Total: 6 meses full-time development**

---

**Estado**: ⏳ PENDING - Falta cotizaciones reales