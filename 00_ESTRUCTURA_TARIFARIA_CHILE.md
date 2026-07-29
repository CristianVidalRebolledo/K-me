# Zona 0: Estructura Tarifaria Chile - Dónde Está el Dinero Real

## Objetivo
Mapear exactamente de dónde salen los costos eléctricos en Chile para Pymes. Aquí es donde tu servicio genera valor.

> **Nota (corregido jul 2026)**: los ejemplos numéricos de este documento usan los
> precios canónicos del simulador (`parametros.py` / `FUENTES_Y_DESPERDICIO.md`
> §Metodología: energía $190-195/kWh, potencia $13.500-14.500/kW/mes, punta
> $17.500-18.000/kW/mes). Versiones anteriores usaban precios ilustrativos ~3x mayores
> sin fuente. El recargo por factor de potencia se calcula aquí sobre el **costo de
> energía** (base pendiente de verificar; ver `10_ANALISIS_CRITICO.md` §3.2).

---

## 1. Tarifarios BT2 vs BT3 (Diferencia Crítica)

### BT2 (Tarifa de Energía y Potencia Contratada)
**Clientes típicos**: Comercio pequeño, oficinas, peluquería, farmacia

```
COMPONENTES DE COBRO:
├─ Cargo fijo mensual: ~$10k-20k CLP/mes
├─ Energía (kWh): $/kWh × consumo total
├─ Potencia contratada: $/kW × potencia contratada (fija)
└─ Factor de potencia: Recargo % si cosϕ < 0.93

EJEMPLO CLIENTE BT2 (comercio con refrigeración, precios canónicos):
├─ Cargo fijo: $15.0k CLP
├─ Energía consumida (3,000 kWh × $195/kWh): $585.0k CLP
├─ Potencia contratada (30 kW × $14,500/kW): $435.0k CLP
├─ VAD distribución (3,000 kWh × $30/kWh): $90.0k CLP
├─ Recargo factor de potencia (10% sobre energía): $58.5k CLP
└─ TOTAL (neto, sin IVA): ~$1,183.5k CLP

⚠️ PROBLEMA: Paga potencia fija aunque consuma poco en punta
💡 OPORTUNIDAD: Reducir potencia contratada si se optimiza demanda
```

### BT3 (Tarifa de Energía y Demanda Máxima)
**Clientes típicos**: Pequeña manufactura, supermercado, taller

```
COMPONENTES DE COBRO:
├─ Cargo fijo mensual: ~$20k-30k CLP/mes
├─ Energía (kWh): $/kWh × consumo total
├─ Demanda máxima (kW): $/kW × demanda máxima registrada en mes
├─ Demanda en horas punta: $/kW × demanda máxima EN horas punta (18-22h, abr-sep)
└─ Factor de potencia: Recargo % si cosϕ < 0.93

EJEMPLO CLIENTE BT3 (caso taller mecánica del simulador, mes con punta):
├─ Cargo fijo: $25k CLP
├─ Energía consumida (8,000 kWh × $190/kWh): $1,520k CLP
├─ Demanda máxima (85 kW × $13,500/kW): $1,148k CLP
├─ Demanda horas punta (70 kW × $17,500/kW, solo abr-sep): $1,225k CLP
├─ VAD distribución (8,000 kWh × $25/kWh): $200k CLP
├─ Recargo factor de potencia (17% sobre energía): $258k CLP
└─ TOTAL mes punta (neto, sin IVA): ~$4,376k CLP
   (meses oct-mar, sin punta: ~$3,151k CLP)

⚠️ PROBLEMA: en un mes punta, la demanda concentra ~54% de la factura
💡 OPORTUNIDAD: Reducir demanda EN HORAS PUNTA = Ahorro máximo
```

---

## 2. Horas Punta en Chile (Factor Clave)

```
DEFINICIÓN OFICIAL:
├─ Horario: 18:00 - 22:00 horas
├─ Período: 1 Abril - 30 Septiembre (invierno, 6 meses)
└─ El cargo de punta se factura SOLO en esos meses (así lo modela el simulador)

IMPACTO EN FACTURA:
├─ Es un cargo ADICIONAL al de demanda máxima, durante abr-sep
├─ Precio punta vs potencia normal: ~25-30% más caro por kW
│  ($17,500-18,000 vs $13,500-14,500 según precios canónicos)
└─ En un mes punta puede ser ~28% de la factura de un BT3 industrial

FÓRMULA DE CÁLCULO (según pliego de la distribuidora):
El cargo de demanda del mes puede tomar el MAYOR entre:
├─ Demanda máxima registrada en el mes actual
└─ Promedio de 2 mayores demandas en últimos 12 meses EN HORAS PUNTA
(⚠️ Verificar la fórmula exacta en el pliego tarifario de cada distribuidora;
el simulador usa el modelo simple demanda × precio)

EJEMPLO REAL:
├─ Cliente tiene máximo de 60 kW en febrero (off-peak)
├─ Cliente tiene máximo de 50 kW en junio ENTRE 18-22h (punta)
├─ Puede pagar como si consumiera 60 kW... pero al precio de punta
│  (porque el promedio de 2 mayores demandas en punta incluye esos 50 kW)
└─ RESULTADO: Paga mucho más por máxima registrada, aunque sea menor
```

---

## 3. Dónde Está El Dinero (Análisis de Oportunidades)

### Ranking de Impacto en Factura (% del total)

```
CLIENTE BT3 INDUSTRIAL (caso taller del simulador, mes punta, neto ~$4.38M):

1️⃣ ENERGÍA: ~35% ($1,520k CLP)
   ├─ Costo por kWh consumido
   ├─ Difícil de reducir sin cambiar proceso
   └─ Oportunidad: Autoconsumo solar (Net Billing) — payback largo, upsell

2️⃣ DEMANDA MÁXIMA: ~26% ($1,148k CLP)
   ├─ Se paga los 12 meses
   └─ Reducible solo con cambio de perfil operacional

3️⃣ DEMANDA EN HORAS PUNTA: ~28% en mes punta ($1,225k CLP, solo abr-sep)
   ├─ ⭐ Oportunidad estacional relevante
   ├─ Precio ~25-30% mayor que la potencia normal
   ├─ REDUCIBLE con: BESS, Demand Response, Thermal Storage
   └─ CAPEX alto (BESS): evaluar caso a caso con diagnóstico

4️⃣ FACTOR DE POTENCIA: ~6% ($258k CLP, todo el año)
   ├─ ⭐⭐⭐ MEJOR RATIO AHORRO/CAPEX ⭐⭐⭐
   ├─ Recargo por cosϕ < 0.93 (aquí 0.76 → 17% sobre energía)
   ├─ REDUCIBLE con: Banco de condensadores (~$3.1M inversión)
   └─ Payback neto: ~1.1 años en este caso (ver demo_automatica.py)

5️⃣ VAD: ~5% ($200k CLP) — regulado, no reducible

NOTA: en meses sin punta (oct-mar) la factura baja a ~$3.15M y el recargo por
factor de potencia sigue presente — por eso es el ahorro más ESTABLE del año.
```

---

## 4. El Perverso Incentivo de Distribuidoras

### El Problema Regulatorio

```
MODELO ACTUAL:
├─ Enel, CGE, etc. = Empresas de distribución
├─ Ingresos = Basados en KWh vendidos + demanda
└─ INCENTIVO: Más consumo = Más ingresos

CONSECUENCIA:
├─ Distribuidoras NO tienen incentivo de promover eficiencia
├─ De hecho, perderían dinero si clientes reducen demanda
├─ El cliente debe buscar solución externa (tú)

OPORTUNIDAD REGULATORIA:
├─ Gobierno busca incentivar demand response
├─ Necesita terceros (tipo ESCO) que hagan el trabajo
├─ Modelo EPC + subsidio ("Ponle Energía a tu Pyme") soluciona el problema
└─ Tú = Intermediario entre cliente y dinero público/ahorros
```

---

## 5. Servicios Integrados: El Modelo ESCO Real

### Lo que Ofrecerás (Visión Completa)

```
ETAPA 1: DIAGNÓSTICO (Incluido o mínimo fee)
├─ Telemetría 30 días: Identificar patrones
├─ Análisis de factura: Desglosar dónde va el dinero
├─ Simulación de ahorros: "Podrías ahorrar $X"
└─ Reporte: Presentar al cliente

ETAPA 2: SOLUCIONES ESPECÍFICAS (Hardware + Consultoría)

┌─ Si DEMANDA PUNTA es problema (#2 oportunidad):
│  ├─ Solución: BESS (Battery Energy Storage System) = Peak Shaving
│  ├─ Cómo: Batería carga en valle, descarga en punta
│  ├─ Ahorro: Reducir demanda punta 30-50% = $100-150k CLP/mes
│  ├─ Inversión: $5M-15M CLP (depende kWh)
│  ├─ Payback: 3-5 años
│  ├─ Regulación: RGR N°06/2024 permite BESS + GD
│  └─ Financiamiento: "Ponle Energía" 50-80% según tamaño (ver 03), tú SaaS

├─ Si FACTOR DE POTENCIA es problema (#3 oportunidad):
│  ├─ Solución: Banco de condensadores (Var correction)
│  ├─ Ahorro: Eliminar recargo = $150-180k CLP/mes fijo
│  ├─ Inversión: $1.5M-3M CLP (one-time)
│  ├─ Payback: 12-18 meses
│  └─ Financiamiento: BancoEstado línea energía

├─ Si DEMANDA TÉRMICA es problema (máquinas de arranque fuerte):
│  ├─ Solución: Thermal Energy Storage + Secuenciador
│  ├─ Cómo: Precalienta/enfría en valle, descarga en punta
│  ├─ Ahorro: Reducir demanda punta + energía = $80-150k CLP/mes
│  ├─ Inversión: $2M-8M CLP
│  └─ Payback: 2-4 años

└─ Si hay ESPACIO + RADIACIÓN SOLAR:
   ├─ Solución: Autoconsumo solar fotovoltaico (Net Billing)
   ├─ Cómo: Reduce energía comprada en punta (generación máxima ≠ punta)
   ├─ Ahorro: Reducir energía 20-40% = $200-400k CLP/mes
   ├─ Inversión: $8M-20M CLP
   ├─ Payback: 8-12 años (ver caso solar en 07_MODELO_ESI_BID.md)
   ├─ EXTRA: Inyectar excedentes bajo Net Billing (no confundir con PMGD)
   └─ Regulación: Net Billing / autoconsumo, Ley 21.118 (hasta 300 kW)

ETAPA 3: MONITOREO + OPTIMIZACIÓN (SaaS Recurrente)
├─ Dashboard de demanda real-time
├─ Alertas automáticas si demanda sube > umbral
├─ Recomendaciones: "Desconecta carga X en punta"
├─ Demand response automático (si BESS + Thermal)
├─ Seguimiento de ahorros (M&V para CEE)
├─ Reportes mensuales
└─ SaaS: $40k-80k CLP/mes (según cliente)

ETAPA 4: MONETIZACIÓN DE AHORROS (EPC + CEE)
├─ Modelo EPC: Tú cobras 20-30% del ahorro verificado
├─ Certificados de Eficiencia (CEE): Vender al mercado
├─ Comisión: 20-30% de CEE vendidos
└─ Ingresos recurrentes 5-7 años
```

---

## 6. Estructura de Ingresos por Solución

### CASO 1: Cliente BT3 con Problema de Demanda Punta

```
CLIENTE ACTUAL:
├─ Factura: $1.5M CLP/mes
├─ Demanda punta: 45 kW
├─ Ahorro potencial: $120k CLP/mes (8% de factura)

SOLUCIÓN: BESS 100 kWh
├─ Costo hardware: $6M CLP
├─ Costo instalación: $1.5M CLP
├─ TOTAL PROYECTO: $7.5M CLP

FINANCIAMIENTO (actualizado: programa ancla "Ponle Energía a tu Pyme"):
├─ Cofinanciamiento estatal: 50-80% según tamaño de empresa (ver 03)
├─ Cliente paga el resto
└─ Alternativa: BancoEstado Línea Verde (hasta 80%, hasta 12 años; ver 07 §8)

TUS INGRESOS (⚠️ cifras históricas ilustrativas — el pricing vigente y único
válido está en 09_PRICING_CANONICO.md):
├─ Instalación + engineering: margen sobre costo
├─ Comisión gestión de subsidio: 3-5% del monto aprobado
├─ SaaS híbrido: $30k/mes base + 15% del ahorro verificado
└─ EPC: POSTERGADO hasta tener capital (ver 10_ANALISIS_CRITICO.md §3.4)

CLIENTE AHORRA:
├─ Inversión: $3.75M CLP (50%, el resto es subsidio)
├─ Ahorro mensual: $120k CLP
├─ Payback (su 50%): 31 meses
└─ NETO año 5: $3.75M inversión + $5.4M ahorros = +$1.65M profit
```

### CASO 2: Cliente BT3 con Problema de Factor de Potencia

```
CLIENTE ACTUAL (caso panadería del simulador):
├─ Factura promedio: ~$3.25M CLP/mes
├─ Factor potencia: 0.81
├─ Recargo: $125.4k CLP/mes (12% sobre costo de energía de $1,045k)
├─ Ahorro potencial: $125.4k CLP/mes, todo el año

SOLUCIÓN: Banco de Condensadores
├─ Hardware: $2.5M CLP
├─ Instalación: $600k CLP
├─ TOTAL: $3.1M CLP

FINANCIAMIENTO:
├─ Cofinanciamiento "Ponle Energía a tu Pyme" (si hay convocatoria): 50-80%
└─ Alternativa: BancoEstado Línea Verde

RESULTADO CLIENTE (salida real de demo_automatica.py):
├─ Ahorro neto de operación: $96.2k CLP/mes
├─ Payback neto: 2.7 años ✅ VIABLE
└─ ROI 5 años (neto): 86.3%

TUS INGRESOS: ver pricing canónico en 09_PRICING_CANONICO.md
```

---

## 7. Regulaciones Clave para tu Modelo

### Autoconsumo / Net Billing — el régimen que aplica a la PYME
```
LEY 21.118 (2018, modifica Ley 20.571):
├─ "Net Billing": autoconsumo con inyección de excedentes a la distribuidora
├─ Límite: hasta 300 kW por instalación
├─ Precio de excedentes: valorizados por la distribuidora (menor al de compra)
├─ Aplicable a: Solar FV, eólica, etc. detrás del medidor del cliente
├─ ESTE es el régimen para una PYME con paneles (NUESTRO caso de "solar upsell")
└─ OPORTUNIDAD: reduce factura + inyecta excedentes; payback largo (8-12 años)
```

### Generación Distribuida (PMGD) — NO es nuestro segmento
```
PMGD (Pequeños Medios de Generación Distribuida):
├─ Límite: hasta 9 MW; se conecta a la red de distribución para INYECTAR
├─ Régimen de DESARROLLADORES/inversionistas, no de clientes finales PYME
├─ Precio: régimen de precio estabilizado (en reforma regulatoria 2025-2026)
├─ Es el mundo de los congresos tipo RENMAD/ACERA (ver 08_PANORAMA_INDUSTRIA.md)
└─ Se documenta solo para NO confundirlo con Net Billing (lo de arriba)
```

### Almacenamiento de Energía (BESS)
```
RGR N°06/2024 (SEC - Reciente):
├─ Reglamenta instalación de baterías
├─ Especifica requisitos de seguridad
├─ Habilita BESS como activo de red
├─ Permite agregación (muchas baterías pequeñas = recurso grande)
├─ SANDBOX REGULATORIO: Pilotos de nuevas tecnologías
└─ OPORTUNIDAD: Tu solución puede ser "piloto regulatorio"
```

### Medición y Verificación (M&V)
```
ISO 50006 + Protocolo CEE (Chile):
├─ Necesario para generar Certificados de Eficiencia
├─ Define cómo calcular "ahorro verificado"
├─ Requiere: Baseline + metodología estandarizada
├─ OPORTUNIDAD: Tu dashboard + SaaS hace M&V automático
└─ VALOR: CEE se venden a distribuidoras (dinero adicional)
```

### Eficiencia Energética — programa ancla verificado
```
"Ponle Energía a tu Pyme" (Ministerio de Energía + AgenciaSE; ver 03):
├─ Cofinancia: micro 80% ($4.5M), pequeña 70% ($8.5M), mediana 50% ($15M)
├─ Financia: eficiencia energética y ER para autoconsumo
├─ Fondo concursable, convocatorias anuales (verificar bases vigentes)
├─ OPORTUNIDAD: Gestor de proyectos entre cliente + subsidio
└─ COMISIÓN: 3-5% del monto aprobado [estimación] (ver 09_PRICING_CANONICO.md)
```

---

## 8. Próximos Pasos Inmediatos

1. **Cotiza BESS real**: Proveedores locales, precio por kWh
2. **Cotiza condensadores**: Precios de bancos 50-100 kVAR
3. **Contacta Agencia Sostenibilidad**: ¿Qué necesitas para ser verificador?
4. **Entrevista 5 Pymes BT3**: Mide su demanda punta real, factor potencia, cargas térmicas
5. **Mapea competencia**: ¿Quién vende BESS + servicios en Chile hoy?

---

**Estado**: ✅ MAPPING COMPLETO - Listo para validación real
