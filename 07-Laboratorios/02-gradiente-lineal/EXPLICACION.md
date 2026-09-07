# Explicación de referencia

## API y contrato

`mse` calcula la pérdida de `ŷ = w·x + b`. `gradients` devuelve `(∂MSE/∂w, ∂MSE/∂b)`. `fit` devuelve los parámetros finales y un historial de longitud `steps + 1`: pérdida inicial y pérdida real después de cada actualización.

## Cálculo paso a paso

Con `x=[1,2]`, `y=[3,5]` y `w=b=0`, los residuos son `[-3,-5]`. Entonces `dw=(2/2)(-3·1-5·2)=-13` y `db=(2/2)(-3-5)=-8`. Una actualización con tasa 0.1 produce `w=1.3`, `b=0.8`; el historial guarda la pérdida calculada con esos valores, no una estimación inventada.

## Decisiones y bordes

Ambos gradientes se calculan antes de modificar parámetros: mezclar un parámetro nuevo con otro viejo cambia el algoritmo. Se rechazan muestras vacías o longitudes distintas, tasa no positiva y cantidad de pasos inválida. Una tasa demasiado grande puede hacer crecer la pérdida; el algoritmo no promete convergencia universal.

## Errores y complejidad

Cada evaluación o gradiente cuesta O(n). `fit` cuesta O(n·steps) y el historial O(steps); los datos no se copian salvo la lista temporal de residuos.
