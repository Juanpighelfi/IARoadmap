# Proyecto opcional: inspección visual de piezas

Pertenece a la [especialización de IA local y robótica](../02-Rutas/IA%20local%20y%20robotica%20opcional.md). El proyecto conductor de la ruta personal es ahora el [SaaS administrativo](SaaS%20administrativo%20con%20IA.md).

## Pregunta inicial

¿Puedo detectar un defecto **visible en una fotografía** de una familia de piezas impresas y ejecutar la inspección localmente? Empezá con una sola familia y un defecto reconocible. No se pretende certificar resistencia mecánica, seguridad eléctrica ni calidad interna a partir de una foto.

## Alcance inicial

Una foto entra; el sistema devuelve clase, evidencia de evaluación y, cuando corresponde, “fuera de alcance/revisar”. La decisión final de aceptar una pieza sigue siendo tuya. No automatiza la impresora ni descarta piezas físicamente.

## Datos antes que modelo

Creá un manifiesto CSV con `image_path,piece_id,session_id,captured_at,material,lighting,label,split`. Guardá imágenes y manifiesto en `Mi-progreso/inspeccion/` o en el repositorio privado de tu proyecto. No subas datos personales ni fotos con información ajena.

Como piloto, intentá reunir 30–50 **piezas distintas** entre clases; es un punto de partida para aprender, no una muestra suficiente garantizada. Varias fotos de una pieza no equivalen a varias piezas independientes. Si hay pocas defectuosas, registrá el desbalance en lugar de fabricar un score convincente. Las imágenes sintéticas sirven para probar el pipeline, no para demostrar desempeño real.

1. Escribí una regla de etiquetado con ejemplos positivos, negativos y ambiguos.
2. Separá por pieza; reservá además una sesión posterior con iluminación distinta para prueba de cambio de dominio.
3. No compartas piezas entre train, validación y test. Si las sesiones se cruzan, explicá exactamente qué generalización estás midiendo.
4. Ajustá recortes, normalización y augmentations con train; aplicá transformaciones deterministas a evaluación.
5. No abras repetidamente test para elegir arquitectura o umbral. Si lo usaste para decidir, pasó a ser validación y necesitás otra muestra final.

## Entregas progresivas

| Módulo | Entrega |
| --- | --- |
| 01–02 | Lector/validador del manifiesto y reporte de conteos por pieza y segmento |
| 04 | Split comprobado, baseline simple, métrica y costos de falso positivo/negativo |
| 05–09b | Transfer learning pequeño y análisis visual de errores |
| 11c | Medición offline: captura/preprocesamiento/inferencia/salida; hardware y versiones |
| 10b | Taxonomía de fallos y un cambio comprobado contra baseline |
| 12c, opcional | Simulación que consulta la inspección; control separado del modelo visual |

## Comparación mínima

- Baseline constante (clase mayoritaria) y, si tiene sentido, regla de textura/color.
- Un modelo pequeño con pesos preentrenados, licencia verificada.
- Mismo conjunto de evaluación, misma definición de etiqueta y mismos segmentos.
- Precision/recall por clase, matriz de confusión y número de piezas, no solo accuracy.
- Latencia p50/p95, tamaño de modelo y memoria con método de medición declarado. Separar calentamiento y muestras repetidas.
- Intervalos por remuestreo a nivel de **pieza**, si la muestra permite interpretarlos; no remuestrear fotos correlacionadas como independientes.

Antes de entrenar, definí qué mejora sería útil y el presupuesto de latencia del uso previsto. Si todavía no conocés ese presupuesto, registrá mediciones exploratorias; no inventes un requisito de tiempo real.

## Prueba de transferencia

Capturá nuevas piezas en otra sesión, incluyendo un fondo nuevo y una imagen no válida. Investigá si el modelo depende del fondo. Ante una foto ilegible o ajena a la familia, debe aplicar el mecanismo de rechazo que definiste y evaluaste; un valor de confianza alto no prueba que esté dentro de distribución.

## Si el proyecto se traba

Sin imágenes: completá los laboratorios de datos/split y el plan de captura, pero no marques validada la visión. Sin GPU: entrená primero solo una cabeza pequeña o usá un dataset reducido; medí en CPU. Si faltan defectos: empezá por clasificar una característica visible fácil para aprender el pipeline y mantené separado ese resultado del objetivo de defectos.

## Cierre

README local con problema, datos, partición, baseline, resultados, fallas, costo de cómputo y comando de reproducción. Vale concluir que el modelo no aporta suficiente valor. Aplicá los [criterios de cierre del capstone](Capstone.md) sin exigir publicación ni usuarios externos.
