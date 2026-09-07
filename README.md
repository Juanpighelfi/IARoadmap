# Mi roadmap de inteligencia artificial

Plan de estudio personal para **desarrollar software con IA, construir un SaaS y automatizar procesos de empresas y pymes**. Fundamentos, práctica independiente y un proyecto administrativo conductor. Meta inicial: diez horas semanales de formación y práctica aplicada, con bloques flexibles. Robótica, visión y entrenamiento avanzado quedan como especializaciones opcionales.

## Empezar

1. Abrí [Empezar aquí](00-MOC/Empezar%20aqui.md): primera sesión, diagnóstico y elección del siguiente paso.
2. Seguí [Mi ruta personal](02-Rutas/Mi%20ruta%20personal.md). No hace falta completar todas las especializaciones.
3. En programación, seguí el camino JavaScript/TypeScript del [módulo 01](01-Niveles/01%20-%20Computacion%20Python%20Git%20y%20entorno.md) y conectalo con [el código real del SaaS](03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md). Los laboratorios Python se conservan para ese lenguaje. No hace falta GPU ni API paga al inicio.
4. Registrá evidencia en [Estado actual](00-MOC/Estado%20actual.md). Una plantilla vacía no equivale a progreso realizado.

## Cómo está organizado

| Necesidad | Abrir |
| --- | --- |
| Saber qué hacer hoy | [Empezar aquí](00-MOC/Empezar%20aqui.md) |
| Ver dependencias y horas | [Catálogo de módulos](00-MOC/Catalogo%20de%20modulos.md) |
| Entender las ramas | [Mapa de estudio](00-MOC/Mapa%20de%20estudio.md) |
| Aprender con tu producto | [SaaS administrativo con IA](03-Proyectos/SaaS%20administrativo%20con%20IA.md) |
| Ubicar archivos y pruebas reales | [Estudiar con el SaaS real](03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md) |
| Organizar la semana | [Semana flexible](03-Proyectos/Semana%20flexible.md) |
| Empezar el primer trimestre | [Plan de 12 semanas](03-Proyectos/Plan%20de%2012%20semanas.md) |
| Organizar el año | [Plan de 12 meses](03-Proyectos/Plan%20de%2012%20meses.md) |
| Comprobar aprendizaje | [Autoevaluación y dominio](04-Recursos/Autoevaluacion%20y%20dominio.md) |
| Elegir material | [Guía de recursos](04-Recursos/Guia%20de%20recursos.md) |
| Navegar todo | [Índice del vault](00-MOC/Indice%20del%20vault.md) |

El orden real está en las rutas, no en el número del archivo. Los sufijos `b` y `c` conservan nombres y enlaces; no significan que un tema sea obligatorio u opcional. La evaluación empieza temprano. El fine-tuning, MCP y la publicación profesional entran cuando aportan a la ruta elegida.

## Usar con GitHub u Obsidian

Podés leer todo en GitHub. Para Obsidian, descargá o cloná este repositorio y abrí la carpeta como vault. Los enlaces Markdown relativos funcionan en ambos. El [Canvas](00-MOC/Mapa%20visual.canvas) muestra las ramas en Obsidian; el mapa Markdown ofrece una alternativa en GitHub.

El material curricular permanece separado de tu trabajo: guardá bitácoras, soluciones y resultados propios en `Mi-progreso/`, ignorado por Git. No subas fotografías, credenciales o datos personales por accidente. Si querés versionar un proyecto, usá un repositorio elegido para ese fin.

## Mantenimiento

Los comandos se ejecutan desde la raíz, con Python 3.11 o posterior:

```bash
python scripts/check_roadmap.py
python scripts/build_catalog.py --check
python -m unittest discover -s tests
python -m unittest discover -s 07-Laboratorios -p 'test_*.py'
python scripts/estimate.py --route personal --hours 10
```

`curriculum.json` es la fuente única de módulos, prerrequisitos, rutas y rangos de horas. Después de editarlo, ejecutá `python scripts/build_catalog.py`. Las horas estiman un ciclo de práctica y deben recalibrarse con tu experiencia; no acreditan aprendizaje.

Cambios en [CHANGELOG](CHANGELOG.md). Licencia [MIT](LICENSE).
