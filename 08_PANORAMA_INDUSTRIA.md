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

1. **Reforma de precios estabilizados de PMGD (2025–2026)**: incertidumbre regulatoria que
   golpea la economía de la solar distribuida. Refuerza nuestra decisión de **no liderar con
   solar** (payback 8–12 años) y priorizar factor de potencia (payback < 2 años), que no
   depende de estos vaivenes.
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

**Estado**: ✅ Contraste oferta/demanda documentado y fuentes de vigilancia registradas.
Pendiente: seguimiento de la reforma PMGD y condiciones de Net Billing vigentes.
