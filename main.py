# Tratamiento de datos
import pandas as pd
import numpy as np

# Gráficos
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn import tree
import graphviz
from graphviz import Source


# Configuración warnings
import warnings
warnings.filterwarnings('ignore')

#Cargar los datos del csv
df = pd.read_csv('smoking_driking_dataset_Ver01.csv')

#Creamos nuestro dataframe con nuestras varaibles eliminando las columnas que no se van a utilizar del dataset original
data=df.drop(['DRK_YN','sex','SMK_stat_type_cd'], axis=1)

#Guardamos nuestras variable Y en otro dataframe
true_label_str=df['DRK_YN']

#Pasamos las categorias de string a valor numerico 
label_encoder = LabelEncoder() 
true_labels = label_encoder.fit_transform(true_label_str)

#dividimos nuestro dataset en train y test
x_train=data[:990000]
y_train=true_labels[:990000]

#Vamos a utilizar 50 datos para el test
x_test=data[990000:990050]
y_test=true_labels[990000: 990050]


#Creamos nuestro modelo de árbol desición 
# Hiperparametro es max depth de nuestro árbol
tree_clf = DecisionTreeClassifier(max_depth = 5)
tree_clf.fit(x_train,y_train)

# dot es un lenguaje de descripción gráfica
dot = tree.export_graphviz(tree_clf, out_file=None,
                           feature_names=data.columns.values,
                           class_names=label_encoder.classes_,
                           filled=True, rounded=True,
                           special_characters=True)


#Hacemos predicciones con nuestro modelo
pred =  tree_clf.predict(x_test)
result=pd.DataFrame(y_test,columns=['Real Y'])
result['Predict Y']=pred
print(result.head())

#Guardamos los resultados reales y los obtenidos del modelo 
arr_x=np.array(range(0,len(result-1)))
plt.scatter(arr_x,result['Predict Y'].values,alpha=0.5,c='blue')
plt.scatter(arr_x,result['Real Y'].values,alpha=0.5,c='red')
plt.legend(["Predict Y" , "Real Y"])
plt.show()

#Ver el nivel de acurrancy para el train y test al correr nuestro modelo 
from sklearn.metrics import accuracy_score
print("Train Accuracy:", tree_clf.score(x_train, y_train))
print("Test Accuracy:", accuracy_score(result['Real Y'].values, result['Predict Y'].values))