# Zona 9: Pricing canónico y economía unitaria

> **Esta es la ÚNICA tabla de precios válida del repositorio.** Reemplaza y prevalece
> sobre cualquier cifra de ingreso que aparezca en `00`, `03`, `04b` o `05` (esos
> documentos conservan sus números históricos como contexto, pero remiten aquí).
> Toda cifra de esta página es **[estimación]** salvo indicación contraria; se ajustará
> con las primeras ventas reales y las cotizaciones pendientes.
> Auditoría que originó esta unificación: `10_ANALISIS_CRITICO.md` §4.3.

---

## 1. Tabla canónica de precios (al cliente)

| Línea | Precio | Notas |
|---|---|---|
| **Diagnóstico energético** (30 días de telemetría + informe + simulación) | **$300.000–500.000 CLP** (una vez) | Primera línea que factura. Se puede descontar del proyecto si el cliente avanza. |
| **Instalación de telemetría permanente** | **Costo real + 30–40% de margen** | ⚠️ Pendiente cotización real de SDM630 + RUT956 + SIM + labor SEC (ver `02`). No fijar precio antes de conocer el costo — hoy el piso de precio histórico ($200k, `03`) quedaba BAJO el techo de costo (~$1M). |
| **SaaS de monitoreo — modelo HÍBRIDO (recomendado)** | **$30.000 CLP/mes base + 15% del ahorro verificado** | El modelo que `04b` §4 declara óptimo. Con ahorro típico de $120k/mes → ingreso $48k/mes/cliente. |
| **Proyecto condensadores** (hardware + instalación) | Costo + margen objetivo **30–40%** | El margen de 40% del simulador es supuesto; validar contra cotización. |
| **Gestión de subsidio** (Ponle Energía a tu Pyme u otro) | **3–5% del monto aprobado** | Unifica los valores contradictorios (3–5% en `04b`, 5–10% en `03`). Solo si hay convocatoria abierta. |
| **EPC (% del ahorro)** | **POSTERGADO** | No ofrecer hasta tener capital/financiamiento identificado. Ver `10` §3.4. |
| **CEE (certificados de eficiencia)** | **Valorar en $0** | Mercado no verificado como operativo + conflicto verificador/beneficiario. No incluir en ninguna proyección. |

**Costos variables por cliente/mes**: comisión electricista $5.000–10.000 (SaaS) +
SIM/datos 4G ~$10.000 [supuesto, ausente del presupuesto original].
**Costos fijos**: infraestructura cloud USD 50–160/mes (~$100k CLP punto medio).

---

## 2. Economía unitaria por cliente (reconstrucción auditada)

### One-off por cliente nuevo
| Componente | Rango |
|---|---|
| Diagnóstico | $300k–500k (precio canónico; histórico `04b` decía $500k–1.5M) |
| Comisiones financiamiento + gestión | $300k–800k (solo si hay convocatoria) |
| Margen hardware + instalación (condensadores) | $600k–1.6M |
| **Total one-off** | **~$1.2M–2.9M CLP por cliente que compra proyecto** |

### Recurrente por cliente/mes (modelo híbrido)
| Componente | Valor |
|---|---|
| Ingreso ($30k base + 15% × ahorro $120k) | +$48k |
| Comisión electricista | −$5k a −$10k |
| SIM/datos 4G [supuesto] | −$10k |
| **Margen de contribución** | **~$28k–33k/mes** |

### Punto de equilibrio EBITDA (costos fijos $2,1M/mes: infra $100k + sueldo fundador $2M [supuesto])
| Modelo | Clientes activos necesarios (solo recurrente) |
|---|---|
| Híbrido ($30k + 15%) | **~64–70** |
| SaaS puro ($40–50k) | ~70–84 |
| EPC 25% del ahorro | ~140 — inviable sin capital |
| Solo cubrir infra (sin sueldo) | 3–7 |

**Lectura correcta**: el EBITDA de los primeros 18–24 meses depende de los **one-offs**
(diagnósticos y proyectos), no del SaaS. Regla práctica: **4–5 diagnósticos/mes cubren
todos los costos fijos** sin un solo cliente SaaS. El SaaS construye el piso recurrente
que hace el negocio valioso a 3–5 años.

---

## 3. Metas coherentes con capacidad (fundador solo)

| Métrica | Plan histórico (`05`) | Meta corregida |
|---|---|---|
| Clientes año 1 | 20–25 | **8–15** (límite: horas de diagnóstico + desarrollo en paralelo) |
| Diagnósticos/mes sostenibles | — | 2–3 (en paralelo al MVP); 4–5 si se pausa desarrollo |
| Primera factura | no planificada | Diagnóstico pagado, **antes de la semana 8** del roadmap |

---

**Estado**: ✅ Pricing unificado (jul 2026). Revisar tras: (a) cotizaciones reales de
hardware/instalación, (b) primeras 3 ventas de diagnóstico, (c) resultado del plan de
validación (`11_PLAN_VALIDACION.md`).
