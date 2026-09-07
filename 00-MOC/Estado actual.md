# Estado actual

Esta página explica el seguimiento. **No contiene horas ni módulos aprobados por vos.** El ejemplo de bitácora es material didáctico y queda fuera de los cálculos.

## Preparar tu registro

Creá `Mi-progreso/` en la raíz del vault y copiá allí la [plantilla de progreso](../05-Plantillas/Plantilla%20de%20progreso.md). Copiá también las plantillas que uses para sesiones, bitácoras y proyectos. La carpeta está ignorada por Git para separar tus datos del currículo; el contenido local necesita tu propio respaldo si querés conservarlo entre dispositivos.

Registrá el estado y el dominio por separado:

| Campo | Valores |
| --- | --- |
| Estado | pendiente, en curso, pausado, cerrado, omitido |
| Dominio | sin evaluar, explorado, practicado, dominado, retenido |
| Evidencia | archivo/commit, prueba, explicación y variante |
| Omisión | motivo y prueba que acredita la habilidad |
| Repaso | fechas previstas y resultado real |

Cerrar un módulo no implica que quede retenido para siempre. Si el repaso falla, corregí el dominio y programá un ejercicio breve; mantené la evidencia histórica.

## Revisión cada cuatro semanas

1. Horas reales y qué parte se fue en entorno, lectura, práctica, corrección y repaso.
2. Qué podés resolver ahora sin ayuda que antes no podías.
3. Qué error se repite y cuál es el siguiente ejercicio que lo ataca.
4. Qué tema podés posponer para reducir carga sin romper prerrequisitos.

No se exige probar el curso con otras personas, publicar resultados o sostener una cadencia de papers durante todos los módulos.

## Dataview opcional

Si usás el plugin, esta consulta lee únicamente tus registros personales; los ejemplos quedan excluidos incluso si los copiaste sin modificarlos:

```dataview
TABLE semana AS "Semana", horas AS "Horas"
FROM "Mi-progreso"
WHERE tipo = "bitacora" AND !ejemplo
SORT semana DESC
```

Sin Dataview, la plantilla Markdown alcanza. No hace falta mantener otra tabla de estado dentro de cada módulo.
