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

### Stack elegido (decisión preliminar, jul 2026)

```
FRONTEND:  HTMX + Jinja2 + Tailwind CSS
           + librería JS de gráficos puntual (Plotly / uPlot / Chart.js)
             solo en los paneles de visualización en tiempo real
BACKEND:   Python + FastAPI + Pydantic (tipado fuerte, verificado con pyright/mypy)
DATABASE:  Supabase (PostgreSQL + TimescaleDB)
PAYMENT:   Stripe o Webpay
AUTH:      Supabase Auth
```

**Monthly infra**: $50-160 USD

### Por qué este stack (y no Node + Next.js + React)

1. **Reutiliza la lógica de dominio existente.** Los simuladores ya están en
   Python (`factura_electrica.py`, `simulador_eficiencia.py`, `parametros.py`).
   Un backend Node/TS obligaría a reescribirlos o a mantener dos runtimes; con
   FastAPI se reutilizan tal cual. Evita desincronizar el código con el discurso
   del negocio (regla del `CLAUDE.md`).

2. **Tipado fuerte sin salir de Python.** FastAPI + Pydantic + pyright/mypy dan el
   mismo rigor de tipos que se buscaba en TypeScript, en el lenguaje del dev.

3. **HTMX baja la carga de mantención para un dev solo.** Render en servidor con
   Jinja2 + HTMX: sin estado de cliente, sin build pipeline JS, sin duplicar el
   contrato de API. HTMX actualiza un `div` sin recargar la página. Para tablas,
   formularios, alertas y navegación (el ~80% de la app) es más simple y mantenible
   que un SPA React.

4. **Matiz sobre gráficos.** Las visualizaciones de telemetría en tiempo real
   (V, I, P, cosϕ, demanda) son inherentemente de cliente. Se usa una librería JS
   ligera SOLO en esos paneles; el resto sigue en HTMX. No se necesita React.

### Dónde vive la eficiencia (dos ejes distintos)

- **Eficiencia de render / mantenibilidad** → HTMX + Python (punto anterior).
- **Eficiencia de consulta de datos** → NO se resuelve en el frontend. La telemetría
  es serie de tiempo de alto volumen: se **pre-agrega** en la base, no al renderizar.
  Patrón: cada vista consulta una tabla ya calculada ("gold"), alimentada por un
  proceso independiente. TimescaleDB implementa esto con **continuous aggregates**
  (tablas de rollup que se refrescan solas) — es la feature que materializa esa idea.

  Regla de separación:
  - **En la DB (SQL / Timescale)**: agregaciones pesadas de telemetría (promedios
    horarios, demanda máxima, cosϕ por ventana).
  - **En Python tipado**: lógica de negocio (factura CNE, recargo factor de potencia,
    ROI, M&V ISO 50006). Cambia seguido, necesita tests y ya existe — no bajarla a
    funciones PL/pgSQL.

  ⚠️ **Timing**: en Fase 1 (1–5 pilotos) basta con vistas materializadas simples.
  Subir a continuous aggregates / capas medallion completas cuando el volumen lo
  justifique — no antes, para no sobre-ingeniar el MVP.

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