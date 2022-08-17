from explainerdashboard import ClassifierExplainer, ExplainerDashboard
import pickle

def ai_explain(model, data_path):
    loaded_model = pickle.load(open(model, 'rb'))
    with open(data_path, 'rb') as file:
        dataset_dict = pickle.load(file)
    X = dataset_dict['X_test']
    y = dataset_dict['Y_test']
    explainer = ClassifierExplainer(loaded_model, X, y)
    ExplainerDashboard(explainer).run()