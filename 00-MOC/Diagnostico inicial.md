# Diagnóstico inicial

Distribuilo en dos o tres sesiones. Intentá primero sin asistente ni solución; después podés consultar y registrar la ayuda. No es un examen de memoria: interesa detectar el siguiente ejercicio útil. La experiencia previa y las materias de tu carrera pueden acreditar partes si podés mostrar el trabajo y resolver una variante.

| Bloque | Tarea | Evidencia suficiente | Si no sale |
| --- | --- | --- | --- |
| Python | Laboratorio 01: leer CSV y validar filas | Pruebas aprobadas y explicar decisiones de error | Módulo 01 |
| Datos | Una pieza A pesa 10 g y tiene 3 fotos; B pesa 20 g y tiene 1 foto. Calcular media por pieza y por fila tras el join | 15 g por pieza y 12,5 g por fila; explicar ponderación accidental | Módulo 02 |
| Matemáticas | Para x=[1,2], y=[3,5], modelo wx+b y L=media((pred-y)^2), calcular gradiente en w=b=0 | dL/dw=-13 y dL/db=-8, con derivación y dimensiones correctas | Módulo 03 y laboratorio 02 |
| Probabilidad | Prevalencia 0,1, sensibilidad 0,9, falso positivo 0,2: calcular P(defecto dado alerta) | 0,09/(0,09+0,18)=1/3; no confundir con sensibilidad | Módulo 03, luego 04b |
| Búsqueda | Explicar cuándo BFS encuentra costo mínimo y resolver un mapa con obstáculos | Costos iguales; en costos distintos usar Dijkstra/A* con condiciones explícitas | Módulo 03b |
| ML | Diseñar split de varias fotos por pieza para probar piezas nunca vistas | Grupos de piezas disjuntos, transformaciones ajustadas solo con train | Módulo 04 y laboratorio 04 |
| Deep learning | Explicar por qué probar sobre 20 ejemplos ayuda a depurar entrenamiento | Distinguir capacidad de ajuste de capacidad de generalización; describir train/eval | Módulo 05 |
| IA local | Proponer comparación entre dos modelos en la misma máquina | Mismos datos, calentamiento separado, latencia y calidad, memoria y versiones | Módulo 11c |

## Decisión

Por bloque: **resuelto sin ayuda**, **resuelto con ayuda**, **no resuelto**. Guardá procedimiento, no solo respuesta. Las respuestas de la tabla permiten corregirte; una vez vistas, hacé la variante para que el diagnóstico siga teniendo valor.

Variantes: pesos 8 y 14 con dos y cuatro fotos; datos x=[-1,1], y=[-1,3] para el gradiente; prevalencia 0,2 y mismas tasas para Bayes. Resultados de control: media por pieza 11 y por foto 12; gradiente (-4,-2); posterior 0,5294118 aproximadamente.

Un bloque resuelto permite omitir la lectura introductoria, pero no todos los ejercicios ni los prerrequisitos de la ruta. El estado inicial del repo sigue sin acreditar: este diagnóstico lo completás vos.
