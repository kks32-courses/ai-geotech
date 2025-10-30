# EBM Notebook - Execution Summary

## ✅ Successfully Created and Tested

**Notebook:** `00b-ebm.ipynb`

## Model Performance

- **Training Accuracy:** 87.81%
- **Testing Accuracy:** 80.12%
- **ROC-AUC Score:** 0.8843

## Key Results

### Classification Report:
```
              precision    recall  f1-score   support
No Spreading       0.80      0.88      0.84       844
Spreading          0.81      0.69      0.75       615
accuracy                               0.80      1459
```

### Confusion Matrix:
```
              Predicted
              No    Yes
Actual No    745    99
       Yes   191   424
```

## Example Predictions (with random_state=42)

### Spreading Site (index 2413):
- GWD: 2.22 m
- L: 1.28 km
- Slope: 0.45%
- PGA: 0.42g
- **Predicted probability: 47.85%**

### Non-spreading Site (index 544):
- GWD: 2.34 m
- L: 1.37 km  
- Slope: 1.02%
- PGA: 0.49g
- **Predicted probability: 20.29%**

## Notebook Features

1. **Introduction to EBM** - What it is and why use it
2. **Data loading** - Same liquefaction dataset
3. **Model training** - Simple one-liner with interactions
4. **Global explanations** - Feature importance and shapes
5. **Local explanations** - Individual prediction breakdowns
6. **Feature interactions** - 2D heatmaps of synergistic effects
7. **Performance metrics** - Classification report, confusion matrix, ROC-AUC
8. **Comparison table** - EBM vs DT/RF/XGBoost

## Running the Notebook

### In Jupyter:
```bash
jupyter notebook 00b-ebm.ipynb
```

The interactive visualizations (`show()`) will display:
- **Global explanations**: Feature shapes showing how each variable affects spreading
- **Local explanations**: Bar charts showing feature contributions for specific sites
- **Interaction heatmaps**: 2D visualizations of pairwise feature effects

### Required Packages:
```bash
pip install interpret scikit-learn pandas matplotlib numpy
```

## Key Advantages of EBM

✅ **80.12% accuracy** - Competitive with XGBoost  
✅ **Fully interpretable** - No need for SHAP/LIME  
✅ **Feature shapes** - See exact relationship curves  
✅ **Interaction detection** - Finds synergistic effects  
✅ **Engineering validation** - Verify physics learned correctly  

## Reproducibility

All results are reproducible with `random_state=42` set in:
- Train-test split
- EBM model initialization

The same examples will always be selected for demonstration.
