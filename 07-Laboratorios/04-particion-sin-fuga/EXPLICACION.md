# Explicación de referencia

## API y contrato

`group_split` devuelve listas de las mismas filas recibidas, sin copiar, inventar ni omitir registros, y coloca todas las fotos de cada `pieza_id` en un solo lado. `time_split` usa un corte ISO inclusivo para test. `detect_group_leakage` responde si algún grupo cruza conjuntos.

## Ejemplo paso a paso

Si A tiene cinco fotos y B, C y D tienen una, con ratio 0.5 se seleccionan dos de los cuatro IDs para test después de barajar los IDs con una semilla local. El porcentaje de fotos puede no ser 50%: el objetivo solicitado es aproximar el porcentaje de grupos y proteger su independencia.

## Decisiones y bordes

Se ordenan los IDs antes de barajarlos para que la semilla sea reproducible. El número de grupos de test es `round(grupos·ratio)`, acotado para dejar al menos un grupo en cada lado. Se requieren dos grupos. La fecha se convierte con `date.fromisoformat`, de modo que fechas inválidas fallen en vez de ordenarse silenciosamente.

## Errores y complejidad

Una fuga puede existir aunque las fotos tengan IDs distintos; por eso se comparan piezas. Crear grupos y particionar cuesta O(n + g log g), donde g es el número de piezas. Las salidas usan O(n) referencias. Este laboratorio no mide ni afirma calidad de un modelo.
