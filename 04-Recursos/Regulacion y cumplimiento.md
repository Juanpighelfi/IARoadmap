---
tags:
  - recursos
  - regulacion
  - gobernanza
  - privacidad
actualizado: 2026-09-01
---

# Regulacion y cumplimiento

Complementa [[01-Niveles/10 - Evaluacion seguridad gobernanza]]. Los marcos tecnicos
que ya estan ahi (NIST AI RMF, OWASP) dicen como construir bien. Esta nota cubre lo que
ademas es obligatorio segun donde operes y con que datos.

No es asesoramiento legal. Es el mapa minimo para saber que preguntar y cuando conviene
consultar a alguien que si sepa.

## Aviso de vigencia

Las fechas de abajo cambiaron mas de una vez desde 2024, incluyendo un aplazamiento de
las obligaciones de alto riesgo. Verifica siempre contra la fuente oficial antes de
tomar una decision: <https://artificialintelligence-act.eu/> y
<https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>.

## EU AI Act

Aplica si ofreces un sistema de IA en la Union Europea o si su salida se usa alli,
aunque tu empresa este fuera. Clasifica por riesgo, no por tecnologia.

### Categorias

- **Prohibido**: puntuacion social, manipulacion que causa dano, categorizacion
  biometrica por atributos sensibles, reconocimiento de emociones en trabajo y
  educacion, entre otros.
- **Alto riesgo**: empleo, educacion, credito, servicios esenciales, y sistemas usados
  como componente de seguridad de productos regulados. Exige gestion de riesgos,
  gobernanza de datos, documentacion tecnica, registro de eventos, supervision humana,
  precision y robustez.
- **Riesgo limitado**: obligaciones de transparencia. Avisar que se interactua con una
  IA, y marcar contenido sintetico.
- **Riesgo minimo**: sin obligaciones especificas.
- **Modelos de proposito general (GPAI)**: obligaciones propias para quien los provee,
  con requisitos extra para modelos con riesgo sistemico.

### Fechas de aplicacion

| Fecha | Que aplica |
| --- | --- |
| 2024-08-01 | Entrada en vigor |
| 2025-02-02 | Definiciones, alfabetizacion en IA y practicas prohibidas |
| 2025-08-02 | Obligaciones de proveedores de GPAI, autoridades nacionales, sanciones |
| 2026-08-02 | Grueso del reglamento y comienzo de la aplicacion efectiva, incluida transparencia |
| 2026-12-02 | Nuevas prohibiciones sobre deepfakes no consentidos y material de abuso infantil |
| 2027-08-02 | Sandboxes regulatorios operativos en los estados miembro |
| 2027-12-02 | Sistemas de alto riesgo del Anexo III |
| 2028-08-02 | Alto riesgo embebido en productos regulados del Anexo I |

### Que significa en la practica para un builder

Aunque tu app sea de riesgo limitado, tres cosas dejan de ser opcionales: avisar que
hay IA, marcar lo generado, y poder demostrar que documentaste como funciona. Todo eso
ya te lo da el material de [[01-Niveles/10 - Evaluacion seguridad gobernanza]] y
[[01-Niveles/10b - Error analysis y evals desde trazas]] si lo hiciste bien.

## Datos personales

- **GDPR** en Europa. Base legal para tratar los datos, minimizacion, limitacion de
  plazo, derechos de acceso, rectificacion y borrado, decisiones automatizadas con
  efecto significativo, transferencias internacionales, y evaluacion de impacto (DPIA)
  cuando el tratamiento es de riesgo alto.
- **Datos de categoria especial** (salud, biometricos, entre otros): prohibidos por
  defecto salvo excepcion explicita. Si tu producto los toca, esto no es un detalle de
  implementacion, es el eje del diseno.
- **America Latina**: cada pais tiene su regimen. Argentina, Ley 25.326 y su proceso de
  actualizacion; Brasil, LGPD; Mexico, LFPDPPP. Verifica el estado vigente, varios
  estan en revision.
- **Estados Unidos**: sectorial. HIPAA para informacion de salud tratada por entidades
  cubiertas y sus asociados, mas leyes estatales tipo CCPA/CPRA.

### Preguntas que hay que poder responder de tu propio sistema

1. Que dato personal entra al prompt, y hace falta que entre.
2. Que guarda el proveedor del modelo, por cuanto tiempo, y lo usa para entrenar.
3. Donde se procesan y almacenan los datos, en que pais.
4. Que queda en los logs y las trazas, quien puede verlos, cuando se borran.
5. Como se borra a una persona del sistema completo, incluidos indices vectoriales y
   datasets de evaluacion.
6. Que pasa si el modelo genera una salida perjudicial: quien responde y como se detecta.

La numero 5 es la que rompe la mayoria de las arquitecturas RAG que se construyeron sin
pensarla. Ver [[01-Niveles/07 - RAG busqueda embeddings]].

## Dominios sensibles

Si trabajas en salud, finanzas, legal, educacion o empleo, tres reglas adicionales:

- **Supervision humana real**, no un boton de confirmar que nadie mira. La revision
  humana solo cuenta si quien revisa tiene tiempo, contexto y poder de decir que no.
- **Umbral de eval mas alto**, con segmentos. Un promedio bueno puede esconder un
  desempeno malo en el grupo que mas riesgo corre.
- **Limite explicito de alcance**, escrito y visible: que el sistema no hace, y que
  decision nunca toma solo.

## Propiedad intelectual

- Licencias de los modelos abiertos: varias no son licencias libres y restringen el uso
  comercial o la destilacion.
- Licencia y procedencia de los datos de entrenamiento y de los datos sinteticos.
  Conecta con [[01-Niveles/05b - Post-training aplicado]].
- Titularidad de lo generado y su tratamiento en tu producto.

## Recursos

- Texto y explorador del EU AI Act: <https://artificialintelligence-act.eu/>
- Comision Europea, marco regulatorio de IA:
  <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>
- Texto del GDPR: <https://gdpr-info.eu/>
- NIST AI Risk Management Framework: <https://airc.nist.gov/airmf-resources/>
- ISO/IEC 42001, sistema de gestion de IA:
  <https://www.iso.org/standard/42001>
- OWASP Top 10 for LLM Applications:
  <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
