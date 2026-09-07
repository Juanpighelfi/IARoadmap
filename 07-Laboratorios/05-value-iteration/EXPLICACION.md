# Explicación de referencia

## API y convención

`value_iteration` devuelve valores y una política solo para estados no terminales. `terminals` es un conjunto y cada terminal mantiene `V=0`. La recompensa se cobra en la transición de entrada. Para una acción:

`Q(s,a) = Σ p(s'|s,a) · [r(s,a,s') + γV(s')]` y `V(s)=max_a Q(s,a)`.

## Ejemplo manual

Para `s`, terminal `t`, acción con `(0.5,t,4)` y `(0.5,s,-1)`, y `γ=0.5`, el punto fijo cumple `V(s)=0.5·4 + 0.5·(-1 + 0.5V(s)) = 1.5 + 0.25V(s)`. Por tanto `V(s)=2`. El terminal sigue en cero: la recompensa 4 no se almacena dos veces.

En el ejemplo completo, `intentar` desde `riesgo` tiene retorno inmediato esperado `0.8·10 + 0.2·(-5)=7`. `avanzar` paga -1 antes de llegar a ese estado. Los barridos son síncronos: cada estado usa exclusivamente los valores del barrido anterior.

## Validación, bordes y errores

Cada no terminal debe tener al menos una acción con resultados; un terminal no puede tener acciones. Estados destino deben existir, probabilidades finitas y no negativas deben sumar uno, y recompensas deben ser finitas. `gamma`, tolerancia e iteraciones también se validan. Si no converge dentro del presupuesto se lanza `RuntimeError`, evitando devolver una política presentada falsamente como convergente.

## Complejidad

Con K barridos y T resultados de transición totales, el tiempo es O(K·T). Valores y política usan O(S+A). Un `gamma` cercano a 1 suele requerir más barridos.
