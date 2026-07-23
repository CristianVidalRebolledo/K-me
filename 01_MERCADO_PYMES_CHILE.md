# Zona 1: Análisis de Mercado - Pymes Chile (Tarifas BT2/BT3)

## Objetivo
Entender el TAM (Total Addressable Market) real en Chile para servicios de eficiencia
energética dirigidos a Pymes en tarifa BT2/BT3.

> **Nota de método**: cada cifra está marcada como **[dato]** (con fuente citada) o
> **[estimación]** (derivada por nosotros a partir de datos). No se inventa precisión.
> Investigación actualizada a **julio 2026**. Fuentes al pie de cada sección.

---

## 1. Definición de Segmento (BT2/BT3)

| Parámetro | BT2 | BT3 |
|-----------|-----|-----|
| **Rango de potencia** | 10 kW - 50 kW | >50 kW (hasta ~250 kW) |
| **Clientes típicos** | Comercio pequeño, peluquería, farmacia, taller | Pequeña manufactura, supermercado, pyme industrial |
| **Uso predominante** | **Clientes comerciales** [dato CNE] | **Usuarios industriales** [dato CNE] |
| **Recargo Factor de Potencia** | Sí (cosϕ < 0.93) | Sí (cosϕ < 0.93) |
| **Control de Demanda Máxima** | Sí | Sí (crítico en horas punta) |
| **Distribuidor típico** | Enel, CGE, Engie | Enel, CGE, Engie |

Las tarifas de distribución a clientes finales las fija el Ministerio de Economía **cada
4 años**, sobre estudios de la CNE y las distribuidoras [dato CNE]. Esto implica que el
marco de precios es estable y predecible entre procesos tarifarios.

---

## 2. Tamaño del universo de empresas (TAM base)

### Número de empresas en Chile

- **~1.500.000** empresas registradas en el SII (universo amplio) **[dato]**.
- **732.924** empresas con ventas efectivas a sept-2024, según Banco Central **[dato]**.
  Esta es la base económicamente activa, más realista para prospección.
- Clasificación SII por ventas anuales: micro (<2.400 UF), pequeña (2.400–25.000 UF),
  mediana (25.000–100.000 UF), grande (≥100.000 UF) **[dato SII]**.

### Distribución geográfica (MiPymes)

- **Región Metropolitana: 51%** del total (~338.560 MiPymes) **[dato]**.
- **Valparaíso**: ~63.357 (única otra región sobre 50 mil) **[dato]**.
- Macrozona **sur + austral**: ~81.536; macrozona **norte**: ~39.679 **[dato]**.
- **Implicación GTM**: el piloto y los primeros clientes deben concentrarse en RM +
  Valparaíso (donde está >60% del mercado y el área de concesión de Enel) **[estimación]**.

### Distribución sectorial

- **Comercio al por mayor y menor**: sector con más empresas (>60.000) **[dato]**.
- Alta relevancia para nosotros: comercio con refrigeración (retail alimentos), talleres
  y pequeña manufactura son los de **peor factor de potencia** por carga inductiva.

**Fuentes sección 2**:
- SII — Estadísticas de empresas: https://www.sii.cl/sobre_el_sii/estadisticas_de_empresas.html
- SII — Infografía a las Pymes: https://www.sii.cl/sobre_el_sii/empresas/Infografia_a_las_pymes_SII.pdf
- CNN Chile / Unholster — Radiografía MiPymes: https://data.cnnchile.com/mercado-laboral/radiografia-y-analisis-completo-a-las-mipymes-de-chile/
- CNE — Opciones tarifarias a usuarios finales: https://www.cne.cl/en/tarificacion/electrica/valor-agregado-de-distribucion/opciones-tarifarias-a-usuarios-finales/

---

## 3. Peso de la energía en la PYME (el dolor)

- La energía eléctrica representa **>10% de los ingresos anuales** de la PYME
  (estudio Accenture citado en prensa) **[dato]**.
- El **cargo por energia** es el **75%–85%** de la factura eléctrica total **[dato]**.
- Solo entre **10% y 17%** de las PYMES ha ejecutado acciones de eficiencia energética
  con impacto en ahorro (1ª Encuesta Nacional de EE en Empresas, 2018) **[dato]**.
  → El 83%–90% del mercado **no ha hecho nada**: espacio enorme y sin explotar.

### Consumo eléctrico típico por tipo de negocio [dato]

| Negocio | Consumo anual |
|---------|---------------|
| Oficina pequeña | 5.000 – 20.000 kWh |
| Tienda minorista | 10.000 – 50.000 kWh |
| Restaurante | 20.000 – 100.000 kWh |
| E-commerce / online | 1.000 – 10.000 kWh |

### Contexto crítico: el "tarifazo" eléctrico 2024

- El precio del kWh subió de **$125 a $179 CLP → +43,2%** (2024) **[dato]**.
- Ejemplo concreto: una fábrica pequeña de **50.000 kWh/año** pasó de **$6,25M a
  $8,95M anuales**, un alza de **~$225.000 CLP/mes** **[dato]**.
- **Implicación comercial**: el alza convirtió la eficiencia energética de "nice to have"
  a urgencia de caja. El timing de entrada al mercado es favorable **[estimación]**.

**Fuentes sección 3**:
- trendTIC — "Tarifazo eléctrico y las pymes": https://www.trendtic.cl/2024/07/tarifazo-electrico-cuanto-afecta-a-las-pymes-y-cuales-son-las-medidas-para-mitigarlo/
- Ministerio de Energía — 1ª Encuesta Nacional de EE en Empresas (2018), vía Gestiona Energía MiPyMEs: https://mipymes.gestionaenergia.cl/

---

## 4. Facturación eléctrica y recargo por factor de potencia

### Facturación eléctrica típica

- **Comercio pequeño (BT2)**: $300k – $800k CLP/mes **[estimación, coherente con consumos citados]**.
- **Pequeña manufactura (BT3)**: $1M – $5M CLP/mes **[estimación]**.

### Recargo por factor de potencia (marco legal y real)

- **Regla legal**: recargo de **1% sobre la facturación de energía por cada 0,01** que el
  factor de potencia esté bajo **0,93** **[dato]**.
  - Ejemplo: FP 0,86 → recargo del **7%** (0,93 − 0,86 = 0,07). *(Nota: una fuente ilustró
    mal el cálculo con 0,85; el método correcto es (0,93 − FP)×100.)*
- **Impacto real**: en la práctica una empresa puede estar pagando **entre 15% y 35%
  adicional** en su cuenta sin aumentar producción ni consumo activo **[dato]**.
  → Rango mayor al 5–15% que asumíamos antes; refuerza el tamaño del dolor.
- Se aplica principalmente a suministros **comerciales e industriales** (nuestro segmento) **[dato]**.
- **Solución estándar**: bancos de condensadores para compensar energía reactiva y
  subir el FP sobre 0,93 **[dato]**.

**Fuentes sección 4**:
- NormaEléctrica — "Factor de potencia: el costo oculto": https://www.normaelectrica.cl/blog/factor-de-potencia-costo-oculto-cuenta-electrica
- Círculo Electricidad Chile — Multas por factor de potencia: http://circuloelectricidad.blogspot.com/2015/01/multas-por-factor-de-potencia.html

---

## 5. Tamaño del mercado de eficiencia energética y ESCO

- **Potencial del mercado de EE**: del orden de **USD 100 millones**, según estudio del
  Ministerio de Energía con ~300 auditorías **[dato]**.
- **Mercado ESCO actual**: mueve **~USD 15 millones/año** y se estima en solo el **10% de
  su potencial de crecimiento** **[dato]**. → Mercado incipiente, con espacio de 10x.
- **ANESCO Chile** agrupa **~34 empresas**; sus miembros ejecutaron el **90% de los
  proyectos ESCO** desde 2014 **[dato]**.
- En los socios ANESCO, la venta de **implementación y construcción** supera los
  **USD 114 millones = 78%** de sus ventas totales **[dato]**. → El grueso del ingreso del
  sector está en ejecutar proyectos (hardware + instalación), no en consultoría.
- **Sectores más beneficiados por ESCO (solar FV)**: agroindustria (1º),
  educación y salud (2º), **retail (3º)** **[dato]**.
- **Impacto país proyectado por la Ley de EE al 2030**: −10% intensidad energética,
  **US$15.200 millones** de ahorro acumulado, −28,6 MtCO2 **[dato]**.

**Fuentes sección 5**:
- Ministerio de Energía — Estudio de Mercado de Eficiencia Energética (2019): https://energia.gob.cl/sites/default/files/documentos/estudio_de_mercado_de_eficiencia_energetica_en_chile.pdf
- Autogeneración (Min. Energía) — "La irrupción del modelo ESCO": https://autoconsumo.minenergia.cl/?p=2587
- ANESCO Chile: https://www.anesco.cl/que-es-eficiencia-energetica/
- Ministerio de Energía — Ley y Plan de Eficiencia Energética: https://energia.gob.cl/ley-y-plan-de-eficiencia-energetica

---

## 6. Barreras de adopción (por qué no invierten aún)

Según el propio Ministerio de Energía, las PYMES **no invierten aunque el retorno sea
atractivo**, por **[dato]**:

1. **Falta de conocimiento** de las altas tasas de retorno.
2. **Percepción de riesgo** ante tecnologías nuevas.
3. **Sesgos de comportamiento** (postergan hasta enfrentar una factura elevada).

**Implicación para nuestro modelo**: estas tres barreras se atacan directamente con
(a) diagnóstico con datos reales que muestra el ahorro, (b) modelo **ESCO/EPC** que
traslada el riesgo de inversión a nosotros, y (c) el "gancho" del tarifazo como disparador.
Ver `04b_SERVICIO_INTEGRADO_ESCO.md` y `03_SUBSIDIOS_FINANCIAMIENTO.md`.

**Fuente**: Ministerio de Energía / AgenciaSE — Gestiona Energía MiPyMEs: https://mipymes.gestionaenergia.cl/

---

## 7. Estimación de mercado (TAM / SAM / SOM)

> Ejercicio **[estimación]** construido sobre los datos anteriores. Rango conservador;
> validar con datos de distribuidoras.

- **TAM (mercado total EE Chile)**: ~USD 100M de potencial de EE **[dato base]**; el
  mercado ESCO hoy es ~USD 15M/año con proyección a ~10x **[dato base]**.
- **SAM (PYMES BT2/BT3 con dolor de FP/demanda)**: subconjunto de las ~732 mil empresas
  activas que son comerciales/industriales con carga inductiva y factura >$500k/mes.
  Orden de magnitud: **decenas de miles de empresas** concentradas en RM + Valparaíso
  **[estimación]**.
- **SOM (alcanzable en 24–36 meses vía canal de electricistas)**: **~50–200 clientes**,
  coherente con el objetivo Go/No-Go de `06_ROADMAP_TECNICO_MVP.md` (5+ clientes al fin
  de Fase 2) **[estimación]**.

**Ancla de validación**: el programa público "Ponle Energía a tu Pyme" espera beneficiar
a **~500 empresas** por convocatoria con cofinanciamiento **[dato]** — señal del volumen
que el propio Estado considera abordable por ciclo. Ver `03_SUBSIDIOS_FINANCIAMIENTO.md`.

---

## 8. Ciclo de Decisión

- Descubrimiento: 0-2 meses
- Evaluación: 1-3 meses
- Decisión + compra: 1-2 meses
- **Ciclo total**: 3-6 meses **[estimación; validar con pilotos]**

Acelerador clave: la barrera #3 (postergación) implica que el ciclo se **acorta
drásticamente tras un evento gatillante** (factura alta, tarifazo, falla). Conviene
prospectar justo después de esos eventos **[estimación]**.

---

## 9. Preguntas aún abiertas (para validar con fuente primaria)

- [ ] Número exacto de clientes BT2 vs BT3 por distribuidora (pedir a CNE/Enel/CGE).
- [ ] % real de PYMES BT2/BT3 con FP < 0,93 (dato de distribuidora, no público).
- [ ] Ahorro promedio verificado en las ~300 auditorías del Ministerio.
- [ ] Ticket promedio y payback real de proyectos ESCO PYME (no solo agroindustria/solar).
- [ ] Tasa de conversión real del canal electricistas (medir en piloto).

---

**Estado**: ✅ Investigación de mercado levantada con fuentes (jul 2026). Pendiente:
datos primarios de distribuidoras (sección 9) para afinar SAM/SOM.
