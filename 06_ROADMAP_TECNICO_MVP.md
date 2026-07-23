# Zona 6: Roadmap Técnico - MVP a Escala

## Objetivo
Plan de desarrollo realista con hitos y decisiones técnicas clave.

---

## 1. Fases de Desarrollo

### FASE 1: MVP - "Telemetría Básica" (8 semanas)
**Objetivo**: 1 cliente piloto con datos en dashboard

**Hitos**:
- Semana 1-2: Setup infraestructura (Railway + Supabase)
- Semana 3-4: Ingesta de datos
- Semana 5-6: Dashboard básico
- Semana 7-8: Testing + Piloto

### FASE 2: MVP+ - "Alertas + Análisis" (8 semanas)
**Objetivo**: 3-5 clientes en SaaS activo

**Hitos**:
- Semana 9-10: Alertas threshold-based
- Semana 11-12: Simulador de ahorros
- Semana 13-14: Multi-customer backend
- Semana 15-16: Electricista portal

### FASE 3: EPC Integration (8 semanas)
**Objetivo**: EPC model + Facturación automática

**Hitos**:
- Semana 17-18: Baseline + M&V
- Semana 19-20: Comisión automática
- Semana 21-22: CEE integration
- Semana 23-24: Testing + Hardening

**Total: 6 meses full-time development**

---

## 2. Tech Stack

```
FRONTEND:  Next.js + Tailwind CSS + Recharts
BACKEND:   Node.js + Express + TypeScript
DATABASE:  Supabase (PostgreSQL + TimescaleDB)
PAYMENT:   Stripe o Webpay
AUTH:      Supabase Auth
```

**Monthly infra**: $50-160 USD

---

## 3. Go/No-Go Decision (End of Phase 2)

### GO IF
- 5+ clientes pagando SaaS
- Churn < 10%
- NPS > 40
- 2-3 electricistas comprometidos

### NO-GO IF
- < 3 clientes
- Churn > 20%
- Data no confiable

---

**Estado**: ⏳ PENDING - Depende de tu ejecución