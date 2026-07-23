# Zona 8: Panorama de industria y vigilancia (oferta vs. demanda)

## Objetivo
Ubicar nuestro proyecto dentro del ecosistema eléctrico chileno, distinguir **en qué capa
jugamos** (demanda / detrás del medidor) frente a la capa de **oferta / gran escala**, y
registrar las fuentes de vigilancia regulatoria y tecnológica que debemos monitorear.

> **Contexto**: el fundador seguía originalmente los webinars de **ATA Insights / RENMAD**
> (fuentes técnicamente confiables). Al contrastarlas con nuestro trabajo se confirmó que
> operan en **otra capa de la cadena de valor**, lo que valida que nuestro nicho está
> menos saturado y bien delimitado. Este documento deja registrado ese contraste.

---

## 1. Dónde jugamos nosotros vs. dónde juega RENMAD/ATA

| Dimensión | RENMAD / ATA Insights (y ACERA) | Nuestro proyecto |
|-----------|--------------------------------|------------------|
| Capa de la cadena | **Oferta**: generación, red, mercado mayorista (SEN) | **Demanda**: detrás del medidor, cliente final |
| Escala | MW–GW (utility-scale); PMGD ≤ 9 MW | kW (BT2/BT3, ~10–250 kW) |
| Cliente / audiencia | Desarrolladores, IPP, utilities, inversionistas | **PYME** (comercio, manufactura) |
| Palanca de valor | Arbitraje de energía, inyección a red, PPA | **Factor de potencia, demanda punta, eficiencia** |
| Modelo de negocio | Project finance, PPA, mercado spot | **ESCO / EPC, SaaS, ISO 50001** |
| Regulación relevante | Precio nudo, PMGD, valorización de storage | **Tarifas de distribución (VAD), recargo cosϕ, Net Billing** |
| Tecnología estrella | BESS grid-scale, H₂ verde, PV/CSP utility | Condensadores, BESS peak-shaving, telemetría |

**Conclusión**: no competimos ni duplicamos su contenido. La eficiencia detrás del medidor
para PYME vía ESCO es justamente lo que estos eventos **no** tratan a fondo (su mundo es la
generación). Nuestra fuente primaria más pertinente sigue siendo el estudio BID
(`07_MODELO_ESI_BID.md`), no la agenda de estos congresos.

---

## 2. Distinción regulatoria clave: Net Billing vs. PMGD

Error común (que corregimos en `00_ESTRUCTURA_TARIFARIA_CHILE.md`): usar "generación
distribuida" de forma laxa. En Chile hay **dos regímenes formales y distintos**:

- **Net Billing / autoconsumo — Ley 21.118 (2018, modifica Ley 20.571)**
  - Hasta **300 kW**, detrás del medidor del cliente.
  - El cliente autoconsume y **inyecta excedentes** a la distribuidora (valorizados a
    precio menor que el de compra).
  - **ESTE es nuestro régimen** cuando una PYME instala paneles ("solar upsell").

- **PMGD (Pequeños Medios de Generación Distribuida)**
  - Hasta **9 MW**, se conecta a la red de distribución para **inyectar** energía.
  - Régimen de **desarrolladores/inversionistas**, no de clientes finales PYME.
  - Precio estabilizado, **en reforma 2025–2026** (afecta economía de la solar distribuida).
  - Es el mundo de RENMAD/ACERA. Lo registramos solo para **no confundirlo** con Net Billing.

---

## 3. Temas a vigilar (donde nuestra investigación es más débil)

1. **Fin del precio estabilizado de PMGD (2025–2026) → exposición a vertimiento**: la
   Contraloría validó (jun 2026) la reforma del reglamento PMGD que **reemplaza el precio
   estabilizado por un "precio básico de energía"**. Consecuencia clave: los proyectos de
   **inyección directa** dejan de tener un precio garantizado y quedan **expuestos al mercado
   spot y al vertimiento (curtailment)** — cuando hay sobreoferta renovable, su energía se
   corta o se paga a precio cercano a cero. Contexto de magnitud: solo en 2025 las
   compensaciones del precio estabilizado sumaron **~USD 250 millones** (≈ 2 años del
   subsidio eléctrico), lo que motivó la reforma.
   - **Implicación para nosotros (refuerza la tesis)**: el negocio de *inyectar* (PMGD) se
     vuelve más riesgoso, mientras que el de *autoconsumir/no comprar* (nuestro foco:
     factor de potencia, demanda, eficiencia detrás del medidor) **no sufre vertimiento** —
     el valor del kWh ahorrado es el precio de compra evitado, no el precio de inyección.
     Es decir: el viento regulatorio empuja el valor **desde la inyección hacia el
     autoconsumo y la eficiencia**, justo donde jugamos.
   - **Matiz para el "solar upsell"**: una PYME con solar bajo **Net Billing** (autoconsumo)
     está mucho menos expuesta que un PMGD, porque su valor principal es reducir la compra,
     no vender excedentes. Pero los excedentes que sí inyecta valen menos en este escenario
     → un argumento más para **dimensionar la solar al autoconsumo**, no a la inyección.
2. **Net Billing (Ley 21.118)**: condiciones de valorización de excedentes y eventuales
   cambios de límite/precio — relevante para el caso solar de la PYME.
3. **Almacenamiento (BESS)**: reglas de valorización y agregación. Conecta con nuestro
   peak-shaving detrás del medidor y con la idea futura de agregación.
4. **VPP (Virtual Power Plants) / centrales eléctricas virtuales**: tema emergente en Chile
   (mejoran calidad de energía en redes con alta penetración FV). Es el **puente natural**
   entre la capa de oferta y nuestra visión de **demand response agregado** (`04b`): agregar
   muchas PYMES con BESS = una VPP. Buen ángulo de pitch a futuro.

---

## 4. Fuentes de vigilancia (monitorear, no citar como dato duro)

| Fuente | Tipo | Uso para nosotros |
|--------|------|-------------------|
| **ATA Insights** (my.atainsights.com) | Webinars/investigación de mercado | Vigilancia tecnológica (BESS, H₂, storage) |
| **RENMAD** (renmad.com) | Congresos presenciales | Vigilancia regulatoria y de mercado; RENMAD Chile (Santiago, jul) |
| **ACERA A.G.** (acera.cl) | Gremio renovables + almacenamiento | Postura de industria, regulación de storage/PMGD |
| **pv-magazine Latinoamérica** | Prensa especializada | Noticias FV, Net Billing, VPP en Chile |
| **CNE / Ministerio de Energía** | Regulador | Fuente primaria de tarifas y normativa |

> Estas fuentes son excelentes para **vigilancia** (tendencias, regulación, tecnología),
> pero su foco es la **oferta/gran escala**. Para datos de nuestro caso (PYME, eficiencia,
> ESCO) priorizar siempre CNE, distribuidoras y el estudio BID (`07_MODELO_ESI_BID.md`).

---

**Fuentes sobre la reforma PMGD / fin del precio estabilizado**:
- Contraloría valida reforma del reglamento PMGD (jun 2026): https://www.reporteminero.cl/noticia/noticias/2026/06/contraloria-valida-reforma-reglamento-pmgd-precios-estabilizados
- "¿Fin al precio estabilizado?" (Energía Estratégica): https://www.energiaestrategica.com/fin-al-precio-estabilizado-gobierno-chileno-abre-consulta-para-modificar-el-reglamento-pmgd-y-permitir-participacion-bess/
- Análisis del precio estabilizado PMGD/PMG (Consejo Minero, 2025): https://consejominero.cl/wp-content/uploads/2025/12/20250707-energiE-PPU_Analisis-del-Precio-Estabilizado-de-los-PMGD-y-PMG_Informe-Definitivo-2.pdf

---

**Estado**: ✅ Contraste oferta/demanda documentado, fuentes de vigilancia registradas y
fin del precio estabilizado PMGD (→ vertimiento) incorporado. Pendiente: seguir la
implementación del "precio básico de energía" y condiciones de Net Billing vigentes.
