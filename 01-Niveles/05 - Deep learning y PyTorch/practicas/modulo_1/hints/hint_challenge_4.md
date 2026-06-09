# 🔑 Hints — M1 Challenge 4: Evaluación de Modelos

## Confusion Matrix
```python
for true_label, pred_label in zip(y_true, y_pred):
    cm[true_label, pred_label] += 1
```

## Per-class metrics
```python
tp = cm[i, i]
fp = cm[:, i].sum() - cm[i, i]
fn = cm[i, :].sum() - cm[i, i]
```

## ROC Curve
```python
for t in thresholds:
    pred_pos = (scores >= t)
    tp = np.sum(pred_pos & (y_true_binary == 1))
    fp = np.sum(pred_pos & (y_true_binary == 0))
    tprs.append(tp / total_pos if total_pos > 0 else 0)
    fprs.append(fp / total_neg if total_neg > 0 else 0)
```

## AUC
```python
return np.trapz(tprs, fprs)
```

## ECE
```python
n_total = len(all_labels)
ece = np.sum(np.abs(accs - confs) * counts / n_total)
```
