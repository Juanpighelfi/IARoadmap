---
id: "04"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 04 - Machine learning clasico

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://scikit-learn.org/stable/user_guide.html>

Qué estudiar: Supervised learning: linear models y árboles; model selection: cross-validation y metrics; preprocessing y pipelines. Leer también Common pitfalls antes del primer experimento.

### Diagnóstico breve

Ante varias fotos de cada pieza, proponé un split para evaluar piezas nuevas. Explicá dónde se ajusta un scaler y por qué accuracy puede engañar. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Resolvé el laboratorio 04 de separación por grupo/tiempo. Luego usá load_breast_cancer de sklearn solo como ejercicio tabular: baseline DummyClassifier y Pipeline de StandardScaler + LogisticRegression. Fijá split y semilla antes de comparar.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/04-particion-sin-fuga/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Cambiá la distribución de clases o el costo del falso negativo. Elegí un umbral usando solo validación y reportá una vez el resultado de test. No usar el ejercicio como herramienta médica.

### Rúbrica de salida

Sin grupos compartidos ni preprocesamiento ajustado con test; baseline y modelo comparables; matriz de confusión y métrica justificadas; semillas/versiones registradas. No se exige ganar al baseline.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si el score parece perfecto, buscar fuga de etiquetas y duplicados; si no mejora, inspeccionar etiquetas y curva de aprendizaje antes de agregar modelos.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Regresion, clasificacion, clustering y reduccion de dimensionalidad.
- Feature engineering y pipelines.
- Train/validation/test, cross-validation y data leakage.
- Metricas: RMSE, MAE, accuracy, precision, recall, F1, ROC-AUC, PR-AUC, calibration.
- Modelos: linear/logistic regression, trees, random forest, gradient boosting, k-means, PCA.
- Interpretabilidad basica: feature importance, SHAP con cautela, partial dependence.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Modelo de churn, fraude, precios o demanda con scikit-learn.
- Pipeline reproducible con versionado de dataset.
- Comparar baseline, modelo simple y modelo complejo.
- Entrar a una competencia de Kaggle ya cerrada y comparar tu score contra el
  leaderboard. Es una referencia opcional de desempeño; no sustituye una evaluación propia ni exige participar en una competencia.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Google ML Crash Course: <https://developers.google.com/machine-learning/crash-course>
- scikit-learn User Guide: <https://scikit-learn.org/stable/user_guide.html>
- Hands-On Machine Learning notebooks: <https://github.com/ageron/handson-ml3>
- Kaggle Learn: <https://www.kaggle.com/learn>
- Kaggle competitions, para que tus modelos los evalue alguien que no seas vos:
  <https://www.kaggle.com/competitions>
