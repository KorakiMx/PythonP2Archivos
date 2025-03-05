import matplotlib.pyplot as plt
import numpy as np

#<- Breakpoint
# Gráfico de Línea
print("###########################Gráfico de Línea##################")
# Definir datos para los ejes X e Y
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 25]
# Crear un gráfico de línea con personalización
plt.plot(x, y, marker='o', linestyle='-', color='purple', linewidth=2, markersize=8, label="Tendencia")
plt.xlabel("Tiempo (días)")  # Etiqueta del eje X
plt.ylabel("Ventas ($)")  # Etiqueta del eje Y
plt.title("Tendencia de Ventas en 5 días")  # Título del gráfico
plt.legend()  # Mostrar leyenda
plt.grid(True, linestyle="--", alpha=0.7)  # Agregar cuadrícula punteada
plt.show()  # Mostrar gráfico

#<- Breakpoint
# Gráfico de Dispersión
print("###########################Gráfico de Dispersión##################")
# Generar datos aleatorios para los ejes X e Y
x = np.random.rand(50) * 10  # Valores entre 0 y 10
y = np.random.rand(50) * 100  # Valores entre 0 y 100
colores = np.random.rand(50)  # Colores aleatorios
tamaño = np.random.rand(50) * 300  # Tamaño aleatorio de los puntos
# Crear gráfico de dispersión
plt.scatter(x, y, c=colores, s=tamaño, cmap="viridis", alpha=0.7, edgecolors="black")
plt.xlabel("Horas de estudio")  # Etiqueta del eje X
plt.ylabel("Calificación obtenida")  # Etiqueta del eje Y
plt.title("Relación entre horas de estudio y calificación")  # Título
plt.colorbar(label="Intensidad del color")  # Agregar barra de colores
plt.show()

#<- Breakpoint
# Gráfico de Barras
print("###########################Gráfico de Barras##################")
# Definir categorías y valores asociados
categorias = ["Manzanas", "Plátanos", "Naranjas", "Uvas"]
valores = [50, 75, 30, 90]
# Crear gráfico de barras
plt.bar(categorias, valores, color=["red", "yellow", "orange", "purple"], edgecolor="black", linewidth=1.5)
plt.xlabel("Frutas")  # Etiqueta del eje X
plt.ylabel("Cantidad vendida")  # Etiqueta del eje Y
plt.title("Ventas de frutas en la semana")  # Título del gráfico
plt.xticks(rotation=45)  # Rotar etiquetas del eje X
plt.show()

#<- Breakpoint
# Histograma
print("###########################Histograma##################")
# Generar 500 datos con distribución normal
datos = np.random.normal(50, 15, 500) # Media=50, Desviación estándar=15, 500 valores
# Crear histograma con personalización
plt.hist(datos, bins=20, color="teal", edgecolor="black", alpha=0.75) #alpha es transparencia de las barras
plt.xlabel("Valores")  # Etiqueta del eje X
plt.ylabel("Frecuencia")  # Etiqueta del eje Y
plt.title("Distribución de datos simulados")  # Título del gráfico
plt.show()

#<- Breakpoint
# Boxplot
print("###########################Boxplot##################")
# Generar datos para tres grupos
data = [np.random.normal(60, 10, 100), np.random.normal(75, 12, 100), np.random.normal(50, 8, 100)]
# Crear gráfico de caja con personalización
plt.boxplot(data, patch_artist=True, notch=True, vert=True, labels=["Grupo A", "Grupo B", "Grupo C"],
            boxprops=dict(facecolor="lightblue", color="blue"),
            medianprops=dict(color="red", linewidth=2))
plt.ylabel("Puntajes")  # Etiqueta del eje Y
plt.title("Distribución de Puntajes por Grupo")  # Título del gráfico
plt.show()

#<- Breakpoint
# Gráfico de Pastel
print("###########################Gráfico de Pastel##################")
# Definir categorías y proporciones
etiquetas = ["Producto A", "Producto B", "Producto C", "Producto D"]
tamaños = [30, 25, 35, 10]
colores = ["gold", "lightcoral", "lightskyblue", "lightgreen"]
# Crear gráfico de pastel con personalización
plt.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%", startangle=90, explode=[0, 0.1, 0, 0])
plt.title("Distribución de Ventas por Producto")  # Título del gráfico
plt.show()




#                        
#   _____   ______     ___    ______    _____    _____    _____    _____             ___     _   _    _   _ 
#  |  __ \  | ___ \   / _ \   |  ___|  |_   _|  /  __ \  |  _  |  /  ___|           / _ \   | | | |  | \ | |
#  | |  /   | |_/ /  / /_\ \  | |_       | |    | /  \/  | | | |  \ `--.           / /_\ \  | | | |  |  \| |
#  | | __   |    /   |  _  |  |  _|      | |    | |      | | | |   `--. \          |  _  |  | | | |  | . ` |
#  | |_\ \  | |\ \   | | | |  | |       _| |_   | \__/\  | |_| |  /\__/ /          | | | |  | |/ /   | |\  |
#   \____/  |_| \_\  \_| |_/  \_|      \_____/   \____/  |_____|  \____/           \_| |_/  |___/    \_| \_/
#


import matplotlib.pyplot as plt
import numpy as np

#<- Breakpoint
# Histograma de una Distribución Normal
print("###########################Histograma de Distribución Normal##################")
datos = np.random.normal(50, 15, 1000)  # Media=50, Desviación estándar=15, 1000 valores
plt.hist(datos, bins=30, color="skyblue", edgecolor="black", alpha=0.7, density=True)
plt.xlabel("Valores")
plt.ylabel("Frecuencia relativa")
plt.title("Histograma de una Distribución Normal")
plt.show()

#<- Breakpoint
# Histograma de una Distribución Uniforme
print("###########################Histograma de Distribución Uniforme##################")
datos = np.random.uniform(10, 100, 1000)  # Valores entre 10 y 100
plt.hist(datos, bins=30, color="green", edgecolor="black", alpha=0.7, density=True)
plt.xlabel("Valores")
plt.ylabel("Frecuencia relativa")
plt.title("Histograma de una Distribución Uniforme")
plt.show()

#<- Breakpoint
# Histograma de una Distribución Exponencial
print("###########################Histograma de Distribución Exponencial##################")
datos = np.random.exponential(scale=10, size=1000)  # Media=10
plt.hist(datos, bins=30, color="red", edgecolor="black", alpha=0.7, density=True)
plt.xlabel("Tiempo")
plt.ylabel("Frecuencia relativa")
plt.title("Histograma de una Distribución Exponencial")
plt.show()

#<- Breakpoint
# Histograma de una Distribución de Poisson
print("###########################Histograma de Distribución de Poisson##################")
datos = np.random.poisson(lam=5, size=1000)  # Lambda=5 (promedio de eventos)
plt.hist(datos, bins=15, color="purple", edgecolor="black", alpha=0.7, density=True)
plt.xlabel("Número de eventos")
plt.ylabel("Frecuencia relativa")
plt.title("Histograma de una Distribución de Poisson")
plt.show()

#<- Breakpoint
# Histograma de una Distribución Binomial
print("###########################Histograma de Distribución Binomial##################")
datos = np.random.binomial(n=10, p=0.5, size=1000)  # 10 intentos, probabilidad de éxito 0.5
plt.hist(datos, bins=10, color="orange", edgecolor="black", alpha=0.7, density=True)
plt.xlabel("Número de éxitos")
plt.ylabel("Frecuencia relativa")
plt.title("Histograma de una Distribución Binomial")
plt.show()


#              
#  ______    _____   __   __  ______    _        _____    _____ 
#  | ___ \  |  _  |  \ \ / /  |  _  \  | |      |  _  |  |_   _|
#  | |_/ /  | | | |   \ V /   | | | |  | |      | | | |    | |  
#  | ___ \  | | | |   /   \   | | | |  | |      | | | |    | |  
#  | |_/ /  | |_| |  / /^\ \  | |/ /   | |____  | |_| |    | |  
#  \____/   |_____|  \/   \/  |___/    \_____/  |_____|    \_/  
#
#####################################################################
#<- Breakpoint
# Boxplot de tres Distribucióoes normales

import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo para tres grupos con distribución normal
data = [np.random.normal(60, 10, 100),  # Grupo A
        np.random.normal(75, 12, 100),  # Grupo B
        np.random.normal(50, 8, 100)]   # Grupo C

# Crear boxplot con personalización
plt.boxplot(data, patch_artist=True, notch=True, vert=True, labels=["Grupo A", "Grupo B", "Grupo C"],
            boxprops=dict(facecolor="lightblue", color="blue"),  # Color de las cajas
            medianprops=dict(color="red", linewidth=2))  # Color de la mediana

# Personalización del gráfico
plt.ylabel("Puntajes")  # Etiqueta del eje Y
plt.title("Distribución de Puntajes por Grupo")  # Título del gráfico

# Mostrar gráfico
plt.show()

#              
#   _____    _   _   ______   ______    _        _____    _____ 
#  /  ___|  | | | |  | ___ \  |  _  \  | |      |  _  |  |_   _|
#  \ `--.   | | | |  | |_/ /  | | | |  | |      | | | |    | |  
#   `--. \  | | | |  | ___ \  | | | |  | |      | | | |    | |  
#  /\__/ /  | |_| |  | |_/ /  | |/ /   | |____  | |_| |    | |  
#  \____/    \___/   \____/   |___/    \_____/  |_____|    \_/  
#
######################################################################
#<- Breakpoint
#Crear 4 gráficos en una figura
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 * y2
y4 = np.exp(-x) * np.sin(2*x)

# Crear figura con 4 subgráficos (2 filas, 2 columnas)
plt.figure(figsize=(10, 8))  # Tamaño de la figura

# Gráfico 1: Seno
plt.subplot(2, 2, 1)  # (filas, columnas, índice)
plt.plot(x, y1, color="blue", linestyle="--")
plt.title("Función Seno")
plt.grid(True)

# Gráfico 2: Coseno
plt.subplot(2, 2, 2)
plt.plot(x, y2, color="red", linestyle="-.")
plt.title("Función Coseno")
plt.grid(True)

# Gráfico 3: Producto seno * coseno
plt.subplot(2, 2, 3)
plt.plot(x, y3, color="green", linestyle=":")
plt.title("Seno * Coseno")
plt.grid(True)

# Gráfico 4: Señal amortiguada
plt.subplot(2, 2, 4)
plt.plot(x, y4, color="purple", linestyle="-")
plt.title("Señal Amortiguada")
plt.grid(True)

# Ajustar los espacios entre gráficos
plt.tight_layout()
plt.show()



#        
#   _____   ______    _____    _____ 
#  |_   _|  | ___ \  |_   _|  /  ___|
#    | |    | |_/ /    | |    \ `--. 
#    | |    |    /     | |     `--. \
#   _| |_   | |\ \    _| |_   /\__/ /
#  \_____/  |_| \_\  \_____/  \____/ 
#
###########################Aplicacion en un dataset real######################
#<- Breakpoint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset de Iris desde Seaborn
df = sns.load_dataset("iris")

# Mostrar las primeras filas del dataset
print(df.head())

# Descripción estadística de los datos
print(df.describe())



#<- Breakpoint
##### Histogramas por tipo de flor #####

plt.figure(figsize=(12, 6))

# Crear histogramas para cada especie
species = df["species"].unique()
colors = ["blue", "green", "red"]

for i, specie in enumerate(species):
    subset = df[df["species"] == specie]
    plt.hist(subset["sepal_length"], bins=10, alpha=0.5, label=specie, color=colors[i], edgecolor="black")

# Personalización
plt.xlabel("Longitud del Sépalo")
plt.ylabel("Frecuencia")
plt.title("Distribución de la Longitud del Sépalo por Especie")
plt.legend()
plt.show()
#<- Breakpoint
#Boxplot para Comparar Tamaños de Pétalos

plt.figure(figsize=(8, 6))
sns.boxplot(x="species", y="petal_length", data=df, palette="Set2")
plt.xlabel("Especie de Flor")
plt.ylabel("Longitud del Pétalo")
plt.title("Distribución de la Longitud del Pétalo por Especie")
plt.grid(True)
plt.show()
#<- Breakpoint
#Gráfico de Dispersión con Relación entre Pétalo y Sépalo
plt.figure(figsize=(8, 6))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="Dark2")
plt.xlabel("Longitud del Sépalo")
plt.ylabel("Longitud del Pétalo")
plt.title("Relación entre Longitud del Sépalo y Pétalo por Especie")
plt.legend()
plt.grid(True)
plt.show()
#<- Breakpoint
#Gráfico de Barras Comparando el Promedio de Sépalo


df.groupby("species")["sepal_length"].mean().plot(kind="bar", color=["blue", "green", "red"], edgecolor="black")
plt.xlabel("Especie de Flor")
plt.ylabel("Longitud Promedio del Sépalo")
plt.title("Longitud Promedio del Sépalo por Especie")
plt.xticks(rotation=0)
plt.show()