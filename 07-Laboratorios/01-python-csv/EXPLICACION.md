# Explicación de referencia

## API y contrato

`validate_rows(rows)` recibe cualquier iterable de diccionarios y devuelve dos listas: filas limpias y reportes de error. `read_and_validate(path)` abre un CSV UTF-8 con `newline=""` y delega en esa función. El número reportado empieza en 2 porque la fila 1 es la cabecera.

## Ejemplo paso a paso

Para `{"pieza_id": " P1 ", "material": "pla", "peso_g": "12.5", ...}`, se quitan espacios del ID, el material pasa a `PLA` y cada medida se convierte a `float`. Solo si no hay errores se agrega la fila limpia y se registra `P1` como aceptado. Así, una fila inválida no impide que una corrección posterior use el mismo ID.

## Decisiones y bordes

Se acumulan todos los errores de una fila para que el diagnóstico sea útil. `math.isfinite` rechaza `NaN` e infinitos, que `float` sí acepta. Cero y negativos tampoco describen medidas válidas. Una columna ausente se trata como valor no numérico. Las columnas pueden venir en cualquier orden porque se accede por nombre.

## Errores y complejidad

El contrato devuelve errores de datos; errores de apertura o CSV mal formado se propagan. Con `n` filas y cuatro campos numéricos fijos, el tiempo es O(n) y la memoria O(n) por las salidas y los IDs vistos.
