# Directorio `candidatos/`

Dossiers de **proyectos por sector productivo candidato**: cada archivo es una propuesta
completa y accionable para llegar a un sector con un producto/servicio bien estructurado
(diagnóstico → eficiencia eléctrica → gestión de demanda/frío → SaaS → upsell).

Cada dossier reúne, para su sector: por qué es buen objetivo, el proceso productivo y
dónde duele la energía, qué ofrecer, dónde conectar la telemetría, la economía, la lista
de candidatos reales y el plan de contacto.

| Archivo | Sector | Estado |
|---------|--------|--------|
| `vitivinicola.md` | Viñas y bodegas | Primer dossier completo (jul 2026) |

**Marco general y priorización de sectores**: `../12_SECTORES_PRODUCTIVOS.md`.

**PDF**: se generan por código con el conversor del repo, p. ej.:

```bash
python3 md_a_pdf.py candidatos/vitivinicola.md --salida candidatos
```
