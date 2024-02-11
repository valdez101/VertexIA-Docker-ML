import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

bucket_root ='/gcs/tottus-backet-iris'

data_dir = f'{bucket_root}/datos'
archivo_dir = f'{bucket_root}/datos/iris.csv'

def create_dataset(archivo_dir):

    #cargando dataset
    iris = load_iris()

    data_encoded=pd.read_csv(archivo_dir)

    #creando entrenamiento de dataset
    X_train, X_test, y_train, y_test = train_test_split(data_encoded[iris.feature_names], data_encoded['target'],test_size = 0.3)

    return X_train, X_test, y_train, y_test


def create_model():
    #llamamos al modelo
    model = DecisionTreeClassifier()

    return model

#creamos dataset
X_train, X_test, y_train, y_test = create_dataset(archivo_dir)

model = create_model()


#train model
model.fit(X_train, y_train)

#predicciones
y_pred=model.predict(X_test)
predictions_df = pd.DataFrame({'predicted': y_pred})

#guardamos la prediccion correspondiente
predictions_df.to_csv(f'{bucket_root}/predictions', index=False)


# Guardar el modelo
dump(model, f'{bucket_root}/model_output/model.joblib')


