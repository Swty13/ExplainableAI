from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = datasets.load_breast_cancer()
# Read the DataFrame, first using the feature data
df = pd.DataFrame(data.data, columns=data.feature_names)
# Store the feature data
X = df
# store the target data
y = data.target
# split the data using Scikit-Learn's train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)
##Save test data in pickle
data_dict={"X_test":X_test,"Y_test":y_test}
with open('testdata_dict.pickle', 'wb') as file:
    pickle.dump(data_dict, file)
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
## Saving Model
with open('classifier_model.pickle', 'wb') as file:
    pickle.dump(rf_model, file)

