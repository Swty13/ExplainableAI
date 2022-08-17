# ExplainableAI

## Introduction
`explainerdashboard` is a library for quickly building interactive dashboards for analyzing and explaining the predictions and workings of (scikit-learn compatible) machine learning models, including xgboost, catboost and lightgbm. This makes your model transparant and explainable with just two lines of code.

### Installation
You can install the package through pip:

pip install explainerdashboard


### Command line tool

* 1st Argument is Test data (X_test,y_test)
* 2nd Argument is Model

```commandline
python main.py "testdata_dict.pickle" "classifier_model.pickle"
```
You will get interactive dashboard on below link:

` Running on http://10.70.70.77:8050/ 
`

### For Reference:

1. https://github.com/oegedijk/explainerdashboard
