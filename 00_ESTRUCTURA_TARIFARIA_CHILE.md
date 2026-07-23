# Zona 0: Estructura Tarifaria Chile - Dónde Está el Dinero Real

## Objetivo
Mapear exactamente de dónde salen los costos eléctricos en Chile para Pymes. Aquí es donde tu servicio genera valor.

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

EJEMPLO CLIENTE BT2 ($600k/mes factura):
├─ Cargo fijo: $15k CLP
├─ Energía consumida (800 kWh × $550 $/kWh): $440k CLP
├─ Potencia contratada (20 kW × $2,000 $/kW): $40k CLP
├─ Recargo factor de potencia (10%): $60k CLP
└─ TOTAL: $555k CLP

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
├─ Demanda en horas punta: $/kW × demanda máxima EN horas punta (18-23h)
└─ Factor de potencia: Recargo % si cosϕ < 0.93

EJEMPLO CLIENTE BT3 ($1.5M/mes factura):
├─ Cargo fijo: $25k CLP
├─ Energía consumida (2,500 kWh × $550 $/kWh): $1.375M CLP
├─ Demanda máxima (50 kW × $3,000 $/kW): $150k CLP
├─ Demanda horas punta (45 kW × $5,000 $/kW): $225k CLP
├─ Recargo factor de potencia (12%): $180k CLP
└─ TOTAL: $1.955M CLP

⚠️ PROBLEMA: Demanda punta cuesta casi 2x la demanda off-peak
💡 OPORTUNIDAD: Reducir demanda EN HORAS PUNTA = Ahorro máximo
```

---

## 2. Horas Punta en Chile (Factor Clave)

```
DEFINICIÓN OFICIAL:
├─ Horario: 18:00 - 23:00 horas
├─ Período: 1 Abril - 30 Septiembre (invierno)
└─ Vigencia: Afecta cargo de demanda durante TODO el año

IMPACTO EN FACTURA:
├─ Si demanda máxima en punta: Pago $/kW punta FULL por 12 meses
├─ Si no hay demanda en punta: Pago más bajo (off-peak)
└─ DIFERENCIA TÍPICA: 50-80% más caro en punta

FÓRMULA DE CÁLCULO:
El cargo de demanda del mes es el MAYOR entre:
├─ Demanda máxima registrada en el mes actual
└─ Promedio de 2 mayores demandas en últimos 12 meses EN HORAS PUNTA

EJEMPLO REAL:
├─ Cliente tiene máximo de 60 kW en febrero (off-peak)
├─ Cliente tiene máximo de 50 kW en junio ENTRE 18-23h (punta)
├─ Paga como si consumiera 60 kW... pero al precio de punta
│  (porque el promedio de 2 mayores demandas en punta incluye esos 50 kW)
└─ RESULTADO: Paga mucho más por máxima registrada, aunque sea lower
```

---

## 3. Dónde Está El Dinero (Análisis de Oportunidades)

### Ranking de Impacto en Factura (% del total)

```
CLIENTE BT3 TÍPICO: $1.5M CLP/mes

1️⃣ ENERGÍA: 70% (~$1.05M CLP)
   ├─ Costo fijo por kWh consumido
   ├─ Difícil de reducir sin cambiar proceso
   └─ Oportunidad: Autogeneración (solar/eólica)

2️⃣ DEMANDA EN HORAS PUNTA: 15% (~$225k CLP)
   ├─ ⭐⭐⭐ MAYOR OPORTUNIDAD ⭐⭐⭐
   ├─ Costo ~2x la demanda off-peak
   ├─ Fija el cargo por 12 meses
   ├─ REDUCIBLE con: BESS, Demand Response, Thermal Storage
   └─ Ahorro potencial: $100-150k CLP/mes

3️⃣ FACTOR DE POTENCIA: 10-15% (~$180k CLP)
   ├─ Recargo por cosϕ < 0.93
   ├─ REDUCIBLE con: Banco de condensadores (~$2M inversión)
   ├─ Payback: 12-18 meses
   └─ Ahorro potencial: $150-180k CLP/mes permanente

4️⃣ DEMANDA OFF-PEAK: 5% (~$150k CLP)
   ├─ Menos crítico
   └─ Reducible solo si cambias perfil operacional

TOTAL OPORTUNIDAD DE AHORRO: $250-330k CLP/mes (~30% de factura)
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
├─ Modelo EPC + FFEE soluciona el problema
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
│  └─ Financiamiento: FFEE cubre 50%, cliente 50%, tú SaaS

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

FINANCIAMIENTO:
├─ FFEE cubre: 50% = $3.75M CLP (estado paga)
├─ Cliente paga: 50% = $3.75M CLP
└─ Modelo: BancoEstado línea energía @ 4.5% = $250k CLP/mes × 15 años

TUS INGRESOS (Escenario Completo):
├─ Instalación + engineering: $1M CLP (margen sobre costo)
├─ Comisión FFEE (5% de $3.75M): $187.5k CLP
├─ SaaS 60 meses @ $50k/mes: $3M CLP
├─ Comisión EPC (25% de $120k × 60 meses): $1.8M CLP
│  (Solo si modelo EPC, sino cliente paga SaaS)
├─ Margen hardware + instalación: $200k-500k CLP
└─ TOTAL INGRESOS: $6.2M - $6.7M CLP EN 5 AÑOS

CLIENTE AHORRA:
├─ Inversión: $3.75M CLP (50%, el resto es subsidio)
├─ Ahorro mensual: $120k CLP
├─ Payback (su 50%): 31 meses
└─ NETO año 5: $3.75M inversión + $5.4M ahorros = +$1.65M profit
```

### CASO 2: Cliente BT3 con Problema de Factor de Potencia

```
CLIENTE ACTUAL:
├─ Factura: $1.5M CLP/mes
├─ Factor potencia: 0.82
├─ Recargo: $180k CLP/mes
├─ Ahorro potencial: $180k CLP/mes FIJO (12% factura)

SOLUCIÓN: Banco de Condensadores 75 kVAR
├─ Costo: $2.2M CLP
├─ Instalación: $600k CLP
├─ TOTAL: $2.8M CLP

FINANCIAMIENTO:
├─ BancoEstado línea energía: 100% @ 4.5%
└─ Cuota mensual: $150k CLP × 18 meses (payback)

TUS INGRESOS:
├─ Margen hardware + instalación: $400k-600k CLP
├─ Comisión FFEE (si postula - opcional): $100k-150k CLP
├─ SaaS 36 meses @ $30k/mes: $1.08M CLP
├─ Margen comisión BancoEstado (1-2%): $28k-56k CLP
└─ TOTAL INGRESOS: $1.6M - $2M CLP EN 3 AÑOS

CLIENTE AHORRA:
├─ Inversión: $2.8M CLP
├─ Ahorro mensual: $180k CLP
├─ Payback: 15.5 meses
└─ NETO año 3: +$3.6M CLP profit (después payback)
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

### Eficiencia Energética (FFEE)
```
Agencia Sostenibilidad y Clima:
├─ Financia 40-50% de proyectos de eficiencia
├─ Requiere: Diagnosis energética (ISO 50002)
├─ Límite: Hasta $500k USD por proyecto
├─ Ciclo: 6-12 meses
├─ OPORTUNIDAD: Gestor de proyectos entre cliente + FFEE
└─ COMISIÓN: 3-5% del monto aprobado (negociable)
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
