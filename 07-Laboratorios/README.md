# Laboratorios de autoestudio

Para responder los ejercicios de cualquier módulo, abrí su [hoja lista para completar](../08-Ejercicios/README.md). Para 00, empezá por [comparar reglas y modelo](../08-Ejercicios/00.md). Las hojas son espacios de trabajo; los laboratorios siguientes aportan código y pruebas a los módulos que los usan.

Cinco prácticas reproducibles con Python 3.11 y biblioteca estándar. Copia cada `starter.py` a `Mi-progreso/labs/` (excluida por Git) y trabaja allí; consulta la referencia después de tu intento.

| Lab | Habilidad comprobada |
|---|---|
| [01 — Python/CSV](01-python-csv/README.md) | Parsear, normalizar y reportar datos inválidos de piezas 3D |
| [02 — Gradiente lineal](02-gradiente-lineal/README.md) | Derivar y comprobar descenso por gradiente |
| [03 — BFS/A*](03-busqueda-cuadricula/README.md) | Encontrar y reconstruir caminos mínimos |
| [04 — Partición sin fuga](04-particion-sin-fuga/README.md) | Separar fotos por pieza o tiempo sin fuga de grupos |
| [05 — Value iteration](05-value-iteration/README.md) | Aplicar Bellman a decisiones estocásticas con terminales |

## Qué corresponde a la nueva ruta personal

Para el SaaS TypeScript, empezá por el camino principal del [módulo 01](../01-Niveles/01%20-%20Computacion%20Python%20Git%20y%20entorno.md) y sus [archivos y pruebas reales](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md). El laboratorio Python 01 queda disponible si elegís ese lenguaje. Continuá con las [prácticas aplicadas al SaaS](Practicas%20SaaS.md) según el módulo. Estas prácticas tienen consignas y casos de aceptación, pero todavía no soluciones ni tests ejecutables incluidos: las pruebas se escriben en tu entorno de aprendizaje.

Los laboratorios 02–05 se conservan para matemáticas, búsqueda, ML y robótica opcionales. No hace falta completarlos todos antes de aprender web o automatización. Sus pruebas existentes pueden seguir ejecutándose para verificar este repositorio.

## Comandos desde la raíz

Referencias completas:

```bash
python -m unittest discover -s 07-Laboratorios -p 'test_*.py'
```

Tu implementación (ejemplo del lab 03):

```bash
LAB03_PATH=/ruta/privada/mi_solucion.py python -m unittest discover -s 07-Laboratorios -p 'test_lab03.py'
```

Usa `LAB01_PATH` … `LAB05_PATH` del mismo modo. La ruta debe implementar la API del `starter.py`. Los starters incompletos no se descubren ni rompen la comprobación por defecto.

## Alcance de la evaluación

Las pruebas varían entradas y cubren errores y bordes para desalentar respuestas fijadas a los datos de muestra. Comprueban comportamiento observable, pero no legibilidad, complejidad asintótica real, calidad de la explicación ni transferencia a datos propios. Las pruebas manuales y criterios de recuperación de cada lab cubren parte de esos límites. El lab 04 no entrena modelos ni presenta resultados de ML; con datos reales aún debes justificar muestreo, etiquetas y distribución.
