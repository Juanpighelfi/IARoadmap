---
tags:
  - recursos
  - metodo
  - repaso
---

# Repaso espaciado

Un plan de 12 meses tiene un problema aritmetico: cuando llegues al nivel 09, el nivel
03 lo viste hace ocho meses y una sola vez. Sin repaso, para el capstone vas a estar
releyendo cosas que ya "sabias". Veinte minutos por semana lo evitan.

## Regla

- Las tarjetas salen de la seccion "que no entendi" de tu bitacora semanal, no de
  copiar definiciones de un libro.
- Una tarjeta por concepto. Si la respuesta ocupa un parrafo, son varias tarjetas.
- Preferi tarjetas que piden explicar o decidir, no recitar. "Que hace un optimizador"
  es debil; "por que Adam converge mas rapido que SGD en la practica" es util.
- 15-20 min, 3 veces por semana. Mas que eso compite con construir, que rinde mas.

## Herramientas

- Anki, si queres el algoritmo serio y sincronizacion entre dispositivos:
  <https://apps.ankiweb.net/>
- Plugin Spaced Repetition de Obsidian, si preferis no salir del vault:
  <https://www.stephenmwangi.com/obsidian-spaced-repetition/>

Con el plugin, las tarjetas viven dentro de cualquier nota del vault y se agrupan por
tag. Una tarjeta de una linea usa `::`:

```text
#flashcards/rag

Que mide groundedness en un pipeline RAG?::El grado en que la respuesta esta apoyada
por los documentos recuperados y no inventada por el modelo.
```

Y una de varias lineas usa `?` como separador:

```text
#flashcards/rag

Que problema resuelve el reranking en un pipeline RAG?
?
El retriever optimiza recall barato sobre muchos documentos. El reranker reordena
un grupo chico de candidatos con un modelo mas caro y preciso, y sube la precision
del contexto que ve el generador.
```

La ventaja de este formato: la tarjeta vive junto a la nota del nivel donde aprendiste
el concepto, no en un archivo aparte que se desincroniza.

## Mazo base sugerido

Unas 100 tarjetas alcanzan para cubrir lo que se olvida. Distribucion orientativa:

| Area | Tarjetas | Ejemplos de pregunta |
| --- | --- | --- |
| Matematicas y estadistica | 20 | Que mide la KL divergence. Por que la varianza sube al bajar el sesgo. Que es leakage y como se detecta. |
| ML clasico | 15 | Cuando PR-AUC dice mas que ROC-AUC. Que significa que un modelo este mal calibrado. Que hace realmente un gradient boosting. |
| Deep learning | 15 | Que calcula autograd. Por que sirve la normalizacion. Que rompe un learning rate alto. |
| LLMs y contexto | 15 | Que cambia temperature y que cambia top-p. Por que un contexto mas largo puede empeorar la respuesta. Que es prompt caching y cuando aplica. |
| RAG | 10 | Que mide groundedness. Por que chunking por secciones gana a chunking fijo. Que falla primero cuando el RAG responde de mas. |
| Agentes y herramientas | 10 | Diferencia entre workflow determinista y agent loop. Que hace idempotente a una herramienta. Que es prompt injection indirecta. |
| Evals y seguridad | 10 | Cuando LLM-as-judge es aceptable. Que es una regresion de prompt. Que va en un risk register. |
| Produccion y costos | 5 | Que es drift y como se detecta. Que compone el costo por request. Que es un canary release. |

## Cuando borrar una tarjeta

Cuando la respondes bien tres veces seguidas sin pensar y ademas la usaste en un
proyecto. El mazo no deberia crecer para siempre: es un colchon contra el olvido,
no un segundo glosario. El glosario ya existe en [[04-Recursos/Glosario esencial]].
