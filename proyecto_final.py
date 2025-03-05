import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#<- Breakpoint
# Cargar y explorar el dataset
print("########################### Cargar y Explorar el Dataset ##################")
# Cargar dataset
df = sns.load_dataset("iris")

# Mostrar primeras filas
print("Primeras filas del dataset:\n", df.head())

# Mostrar información del dataset
print("\nInformación del dataset:")
df.info()

# Ver estadísticas generales
print("\nEstadísticas del dataset:\n", df.describe())

#<- Breakpoint
# Identificación de la Mejor Característica para Clasificación
print("########################### Identificación de la Mejor Característica ##################")
# Calcular la correlación entre características numéricas y la clasificación
df_numeric = df.drop(columns=["species"])
correlacion = df_numeric.corr()
print("\nMatriz de correlación:\n", correlacion)

# Visualizar la correlación en un mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación entre Características")
plt.show()

# Explicación
print("\nExplicación:")
print("La característica con mayor correlación con la clasificación es petal_length.")
print("Al analizar la distribución de los valores, se observa que petal_length < 2 agrupa a Setosa,"
      " mientras que petal_length >= 5 agrupa a Virginica y los valores intermedios a Versicolor.")
print("Por esta razón, petal_length será el principal criterio de clasificación.")

#<- Breakpoint
# Visualización de Datos
print("########################### Visualización de Datos ##################")
# Crear un gráfico de dispersión
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="Dark2")
plt.title("Relación entre la Longitud del Sépalo y del Pétalo")
plt.xlabel("Longitud del Sépalo")
plt.ylabel("Longitud del Pétalo")
plt.legend()
plt.grid(True)
plt.show()

#<- Breakpoint
# Creación del Clasificador
print("########################### Creación del Clasificador ##################")
# Clasificador basado en los umbrales identificados
def clasificar_flor(petal_length):
    if petal_length < 2:
        return "setosa"
    elif petal_length >= 5:
        return "virginica"
    else:
        return "versicolor"

# Aplicar la función a todo el dataset usando directamente la columna
predicciones = df["petal_length"].apply(clasificar_flor)
df["prediccion"] = predicciones

# Calcular precisión comparando con la columna real "species"
precision = (df["species"] == df["prediccion"]).mean() * 100
print(f"\nPrecisión del modelo: {precision:.2f}%")

#<- Breakpoint
# Interacción con el Usuario
print("########################### Interacción con el Usuario ##################")
# Pedir datos al usuario
petal_length = float(input("\nIngrese la longitud del pétalo: "))

# Clasificar la flor según las reglas anteriores
especie_predicha = clasificar_flor(petal_length)
print(f"La flor ingresada es probablemente una {especie_predicha}.")
