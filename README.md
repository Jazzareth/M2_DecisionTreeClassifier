# M2_DecisionTreeClassifier
En el repositorio se encuentra en documento smoking_driking_dataset_Ver01.csv el cual fue sacado de un Dataset de Kaggle, el documento main.py que contiene el codigo de python para correr el modelo de árbol de desición para clasificación de nuestros datos y por ultimo la imagen en png del modelo del árbol de desición.

## Acerca del Dataset
Este conjunto de datos  obtenido de Kaggle se recopilo del Servicio Nacional de Seguro Médico de Corea. Se excluyó toda la información personal y los datos sensibles.
El propósito de este conjunto de datos es:
* Análisis de la señal corporal.
* Clasificación de fumador o bebedor
  
En este analisis solo clasificaremos si la persona es bebedor o no por lo que la variable SMK_stat_type_cd no se utilizo

**Variables**
* sex:male, female
* age:edad de la persona 
* height
* weight
* sight_left:nivel de vista (izquierda)
* sight_right:nivel de vista (derecha)
* hear_left:audición izquierda, 1(normal), 2(anormal)
* hear_right:audición derecha, 1(normal), 2(anormal)
* SBP:Presión arterial sistólica [mmHg]
* DBP:Presión arterial diastólica [mmHg]
* BLDS:Glucosa en sangre en ayunas [mg/dL]
* tot_chole:colesterol total[mg/dL]
* HDL_chole:Colesterol HDL[mg/dL]
* LDL_colesterol Colesterol LDL[mg/dL]
* triglyceride: triglicérido [mg/dL]
* hemoglobin: hemoglobina [g/dL]
* urine_protein:proteína en la orina, 1(-), 2(+/-), 3(+1), 4(+2), 5(+3), 6(+4)
* serum_creatinine: creatinina sérica(sangre)[mg/dL]
* SGOT_AST: Glutamato-oxalacetato transaminasa
* AST: Aspartato transaminasa[UI/L]
* SGOT_ALT: Alanina transaminasa[UI/L]
* gamma_GTP: y-glutamil transpeptidasa[UI/L]
* SMK_stat_type_cd: Estado de fumar, 1 (nunca), 2 (solía fumar pero lo dejó), 3 (todavía fuma)
* DRK_YN Bebedor o no
  
## Acerca del Documento de Python 
 El codigo contiene la implementación de un algoritmo de clasificación utilizando un árbol de desición utilizando la  biblioteca de sklearn y graphviz para el procesamiento y modelado de los datos.
 Para este ejemplo se utilizaron un nivel de profundidad de 5 para nuestro árbol y utilizamos 990000 datos para el entrenamiento del modelo y al finalizar se realizo una prueba con un fragmento del set de datos original de 50 datos para realiza algunas predicciones, para poder comparar las predicciónes del modelo con los datos reales.
Los resultados de accuracy , que es el porcentaje de casos que el modelo ha acertado, tanto con los datos de train como test son los siguientes:

* **Train Accuracy**: 0.70
* **Test Accuracy**: 0.74

