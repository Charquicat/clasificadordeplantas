from sklearn import tree
//Medidas: ancho máximo, largo máximo
X = [[0.7,2],[0.5,2.5],[0.7,2.3],[4,8],[5,9],[6,9],[4.5,45],[4.2,44],[2.5,22]]
//Clasificación de cada dato
Y = ['Ruda','Ruda','Ruda','Rosa','Rosa','Rosa','Palo de agua','Palo de agua','Palo de agua']
//Funcion para usar el árbol de decisión
clf = tree.DecisionTreeClassifier()
//Entrenamiento con los datos dados
clf = clf.fit(X,Y)
//Los datos entre paréntesis son el ancho máximo de la hoja y el largo máximo de la hoja, estos datos deberían entregar la especie 
prediction = clf.predict([[4.5,44]])
//Escritura de el resultado 
print prediction