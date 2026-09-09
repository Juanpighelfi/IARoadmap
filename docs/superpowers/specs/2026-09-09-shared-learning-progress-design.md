# Diseño: progreso de aprendizaje compartido entre Pi y ChatGPT

Fecha: 2026-09-09

## Objetivo

Usar el repositorio privado `IARoadmap` como fuente de verdad del progreso de aprendizaje, de modo que:

- Pi pueda leer y actualizar el progreso desde la copia local del repo.
- ChatGPT pueda leer y actualizar los mismos archivos mediante GitHub.
- El sistema de enseñanza de `amosblomqvist/learn` pueda convivir sin ser modificado ni reemplazado.
- El registro siga siendo pequeño, útil y legible en Obsidian.

## Decisiones de arquitectura

### 1. GitHub será la fuente de verdad

`Mi-progreso/` dejará de estar ignorado por Git. El contenido de esa carpeta se versionará en el repositorio privado.

Esto permite este flujo:

```text
Pi local -> edita Mi-progreso -> commit/push -> GitHub
                                             ^
                                             |
                                      ChatGPT lee/edita
```

Pi debe hacer `git pull --rebase` antes de iniciar una sesión si hubo cambios remotos y `git push` al terminar si modificó el progreso.

### 2. Separar "próximo paso" de "mapa de conocimientos"

Se conservará `Mi seguimiento.md` como registro corto de sesión:

- Estoy estudiando
- Hice
- Me costó
- Cómo sigo

Se agregará `Mi-progreso/Conocimientos.md` para guardar el estado persistente por concepto. Esto evita volver complejo el seguimiento diario.

Cada concepto tendrá únicamente:

- área
- concepto
- estado
- evidencia
- última comprobación

Estados permitidos:

- `pendiente`: todavía no se comprobó.
- `en aprendizaje`: hay comprensión parcial o errores relevantes.
- `demostrado`: el usuario resolvió una comprobación sin depender de copiar la respuesta.

El estado no representa una calificación ni garantiza dominio permanente; es una señal operativa para elegir el próximo ejercicio.

### 3. Pi recibirá instrucciones a nivel proyecto

Se añadirá `AGENTS.md` en la raíz. Pi carga `AGENTS.md` como contexto del proyecto.

Las instrucciones exigirán que, cuando la sesión sea de aprendizaje:

1. lea `Mi-progreso/Mi seguimiento.md` y `Mi-progreso/Conocimientos.md` antes de enseñar;
2. use la evidencia existente para evitar repetir diagnóstico ya resuelto;
3. actualice solo conceptos realmente comprobados;
4. agregue una entrada breve en `Mi seguimiento.md` al terminar una sesión sustantiva;
5. no marque `demostrado` por mera exposición o por haber leído una explicación;
6. no sobrescriba respuestas de ejercicios del usuario.

### 4. Skill de progreso independiente de `.pi`

Se añadirá `.agents/skills/roadmap-progress/SKILL.md`.

Pi descubre skills de proyecto bajo `.agents/skills/`. De esta forma el usuario puede mantener `amosblomqvist/learn` dentro de `.pi/` sin mezclar ambos sistemas.

La skill `roadmap-progress` se centrará solo en persistencia del progreso. No duplicará la metodología de `teach`.

Responsabilidades:

- cargar el estado antes de `/teach` o sesiones de estudio;
- registrar evidencia después de quizzes, ejercicios o explicaciones del usuario;
- actualizar el próximo paso;
- mantener cambios mínimos y trazables.

### 5. Convención para ChatGPT

El repo contendrá `Mi-progreso/README.md` con el contrato de actualización para cualquier asistente externo.

Cuando ChatGPT trabaje con el roadmap debe:

1. leer primero `Mi seguimiento.md` y `Conocimientos.md` si la petición depende del progreso;
2. basar cambios de estado en evidencia visible en la conversación o ya registrada;
3. modificar los archivos mediante GitHub;
4. registrar el origen como `ChatGPT` o `Pi` solo en la entrada de sesión si aporta trazabilidad; no mantener dos historiales separados.

## Archivos a modificar o crear

- `.gitignore`: eliminar `Mi-progreso/` de exclusiones.
- `AGENTS.md`: instrucciones persistentes para Pi en este proyecto.
- `.agents/skills/roadmap-progress/SKILL.md`: skill de sincronización de progreso.
- `Mi-progreso/Mi seguimiento.md`: seguimiento mínimo inicial.
- `Mi-progreso/Conocimientos.md`: mapa persistente de conceptos.
- `Mi-progreso/README.md`: contrato de uso para Pi, ChatGPT y edición manual.
- `00-MOC/Estado actual.md`: actualizar instrucciones antiguas que dicen que `Mi-progreso/` no se sincroniza.
- `05-Plantillas/Plantilla de progreso.md`: mantenerla alineada con el nuevo sistema.

## Estado inicial de JavaScript

Como la sesión actual comenzó con JavaScript pero el diagnóstico todavía no fue respondido, los conceptos iniciales se crearán como `pendiente`:

- variables
- tipos
- condicionales
- bucles
- funciones
- arrays
- objetos

No se inferirá dominio a partir de haber pedido una explicación.

## Conflictos y sincronización

No se implementará automatización compleja ni backend adicional.

Regla operativa:

- antes de estudiar con Pi: `git pull --rebase`;
- después de una sesión que cambie el progreso: commit y push;
- ChatGPT editará directamente la versión remota;
- si Pi tiene cambios locales sin publicar, Git puede requerir resolver un conflicto antes del siguiente push.

Los archivos se diseñarán para minimizar conflictos: `Mi seguimiento.md` será append-oriented y `Conocimientos.md` tendrá una fila por concepto.

## Privacidad

No guardar:

- credenciales;
- secretos;
- datos de pacientes;
- información personal sensible innecesaria.

El repositorio es privado, pero el seguimiento debe contener únicamente información útil para el aprendizaje.

## Criterios de aceptación

El cambio se considera correcto cuando:

1. `Mi-progreso/` está versionado.
2. Pi puede descubrir `roadmap-progress` sin interferir con las skills de `.pi/`.
3. una nueva sesión de Pi recibe instrucciones explícitas para leer y actualizar el progreso.
4. ChatGPT puede leer y modificar los mismos archivos mediante GitHub.
5. JavaScript aparece con los siete conceptos iniciales en estado `pendiente`.
6. la documentación ya no afirma que `Mi-progreso/` está excluido de Git.
7. no se añade ninguna dependencia, servicio externo ni formato difícil de editar a mano.
