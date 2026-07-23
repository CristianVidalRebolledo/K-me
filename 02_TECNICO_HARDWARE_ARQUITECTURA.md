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
        ↓
[Dashboard: React/Next.js] (Web)
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
- Next.js: $0-20 USD/mes

**Total mensual**: $50-160 USD (~$50k-160k CLP/mes)

---

## 4. MVP Fases

**Fase 1 (8 semanas)**: Telemetría básica
**Fase 2 (8 semanas)**: Alertas + Análisis
**Fase 3 (8 semanas)**: EPC Integration

**Total: 6 meses full-time development**

---

**Estado**: ⏳ PENDING - Falta cotizaciones reales