# Mi seguimiento: cómo usarlo

Un solo lugar para saber dónde estás y retomar sin pensar todo de nuevo. Las respuestas se resuelven en la [hoja ya preparada de cada módulo](../08-Ejercicios/README.md); el seguimiento guarda solo el estado necesario para continuar.

## Ya está preparado

La carpeta `Mi-progreso/` forma parte del repositorio privado y es la fuente de verdad compartida entre tu copia local, Pi y ChatGPT.

Usá estos dos archivos:

- `Mi-progreso/Mi seguimiento.md`: tema actual y próximo paso.
- `Mi-progreso/Conocimientos.md`: estado y evidencia por concepto.

No hace falta crear otra ficha por sesión, semana o módulo.

## Antes de estudiar con Pi

Desde la raíz del repo, actualizá la copia local:

```bash
git pull --rebase
```

Pi tiene instrucciones de leer el seguimiento y los conocimientos antes de enseñar. Si encuentra cambios locales sin confirmar, no debe descartarlos ni hacer pull automáticamente.

## Al terminar de estudiar: dos minutos

Agregá una fecha y completá tres líneas en `Mi-progreso/Mi seguimiento.md`:

- **Hice:** el ejercicio o tema que trabajaste; una frase alcanza.
- **Me costó:** la duda o el bloqueo principal. Si no hubo, poné «nada en particular».
- **Cómo sigo:** una acción pequeña para la próxima vez, como «probar una duración de turno inválida».

La próxima sesión empieza leyendo el último «Cómo sigo». Actualizá «Estoy estudiando» solo cuando cambies de tema.

Pi puede hacer esta actualización al finalizar una sesión. Si cambió el progreso, sincronizá:

```bash
git add Mi-progreso
git commit -m "progress: update learning state"
git push
```

Si no hubo cambios, no hace falta crear un commit.

Cuando estudies con ChatGPT, puede leer y editar esos mismos archivos directamente en GitHub.

## Estado por concepto

`Mi-progreso/Conocimientos.md` usa solo tres estados:

- `pendiente`: todavía no se comprobó suficientemente.
- `en aprendizaje`: hay comprensión parcial o errores relevantes.
- `demostrado`: resolviste una comprobación significativa sin depender de copiar la solución.

Leer una explicación o decir «entiendo» no alcanza para marcar `demostrado`; tiene que existir evidencia observable.

## Qué no hace falta completar

Sin puntajes, horas por actividad, archivos semanales ni calendarios de repaso obligatorios. Si faltaste unos días, continuá desde el último «Cómo sigo».

Las respuestas se escriben en la [hoja del ejercicio](../08-Ejercicios/README.md). El código y sus pruebas quedan en sus propios archivos. Podés nombrarlos en «Hice» sin copiar sus resultados. Para decidir si avanzar, usá [esta comprobación breve](../04-Recursos/Autoevaluacion%20y%20dominio.md).

No guardes datos de pacientes, credenciales, secretos ni información personal sensible innecesaria en `Mi-progreso/`. Aunque el repositorio sea privado, el seguimiento debe seguir siendo mínimo.
