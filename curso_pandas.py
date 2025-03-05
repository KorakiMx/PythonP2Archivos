import pandas as pd
import numpy as np

#<- Breakpoint
# Ejemplos de Series y DataFrames
print("###########################Creación de Series##################")
serie = pd.Series([10, 20, 30, 40])
print("Serie creada:\n", serie, "\n")
#<- Breakpoint
data = {"a": 10, "b": 20, "c": 30}
serie_dict = pd.Series(data)
print("Serie creada desde un diccionario:\n", serie_dict, "\n")
#<- Breakpoint
# Información de la Serie
print("Índices de la Serie:", serie.index)
print("Valores de la Serie:", serie.values)
print("Tipo de datos de la Serie:", serie.dtype)
print("Dimensión de la Serie:", serie.shape)
print("Primer elemento usando iloc:", serie.iloc[0], "\n")

#<- Breakpoint
# Operaciones matemáticas en Series
print("###########################Operaciones matemáticas en Series##################")
serie2 = pd.Series([1, 2, 3, 4])
print("Suma de Series:\n", serie + serie2, "\n")
print("Multiplicación por escalar:\n", serie * 2, "\n")
print("Raíz cuadrada de la Serie:\n", np.sqrt(serie), "\n")
print("Media de la Serie:", serie.mean())
print("Suma de todos los valores:", serie.sum(), "\n")

#<- Breakpoint
# Ejemplo de creación de un DataFrame
print("###########################Creación de un DataFrame##################")
data_df = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 35],
    "Ciudad": ["CDMX", "Guadalajara", "Monterrey"]
}
df_simple = pd.DataFrame(data_df)
print("DataFrame creado:\n", df_simple, "\n")

# Información del DataFrame
print("Información del DataFrame:")
df_simple.info()
print("Descripción estadística del DataFrame:")
print(df_simple.describe(), "\n")

#<- Breakpoint
# Operaciones matemáticas en DataFrames
print("###########################Operaciones matemáticas en DataFrames##################")
data_num = {
    "A": [10, 20, 30, 40],
    "B": [5, 15, 25, 35]
}
df_math = pd.DataFrame(data_num)
print("DataFrame original:\n", df_math, "\n")
print("Suma de columnas:\n", df_math["A"] + df_math["B"], "\n")
print("Multiplicación de columnas:\n", df_math["A"] * df_math["B"], "\n")
print("Promedio de cada columna:\n", df_math.mean(), "\n")
print("Suma total de valores:\n", df_math.sum(), "\n")

#<- Breakpoint
# Acceso a columnas y filas en DataFrames
print("###########################Acceso a Columnas y Filas##################")
print("Columna Edad:\n", df_simple["Edad"], "\n")
print("Fila con índice 1 usando loc:\n", df_simple.loc[1], "\n")
print("Fila con índice 1 usando iloc:\n", df_simple.iloc[1], "\n")
print("Valor específico (fila 1, columna 'Ciudad'):\n", df_simple.at[1, "Ciudad"], "\n")



##############################################################################Ejemplo final de pandas #########################################################

#<- Breakpoint
# Creación del DataFrame más grande para las siguientes pruebas
print("###########################Creación del DataFrame##################")
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Nombre": ["Ana", "Luis", "Carlos", "Maria", "Jose", "Sofia", "Raul", "Pedro", "Elena", "Laura"],
    "Edad": [25, 30, 35, np.nan, 40, 22, 27, np.nan, 33, 28],
    "Ciudad": ["CDMX", "Guadalajara", "Monterrey", "CDMX", np.nan, "CDMX", "Tijuana", "CDMX", "Puebla", "CDMX"],
    "Ingreso": [50000, 60000, 75000, 80000, 45000, 55000, 70000, 72000, np.nan, 62000]
}
df = pd.DataFrame(data)
print(df, "\n")

#<- Breakpoint
# Escritura de archivos
print("###########################Escritura de archivos##################")
df.to_csv("datos.csv", index=False)
df.to_excel("datos.xlsx", sheet_name="Hoja1", index=False)
print("Archivos CSV y Excel creados.\n")


# Lectura de archivos
print("###########################Lectura de archivos##################")
df_csv = pd.read_csv("datos.csv")
df_excel = pd.read_excel("datos.xlsx")
print("Datos CSV:\n", df_csv.head(), "\n")
print("Datos Excel:\n", df_excel.head(), "\n")




#              
#   _____      ___    _____   ___  ___  ______    _        _____ 
#  |  ___|    |_  |  |  ___|  |  \/  |  |  _  \  | |      |  _  |
#  | |__        | |  | |__    | .  . |  | | | |  | |      | | | |
#  |  __|       | |  |  __|   | |\/| |  | | | |  | |      | | | |
#  | |___   /\__/ /  | |___   | |  | |  | |/ /   | |____  | |_| |
#  \____/   \____/   \____/   \_|  |_/  |___/    \_____/  |_____|
#




#<- Breakpoint
# Exploración de datos
print("###########################Exploración de datos##################")
print("Primeras 5 filas:\n", df.head(), "\n")
print("Últimas 5 filas:\n", df.tail(), "\n")
print("Información general:\n")
df.info()
print("Estadísticas descriptivas:\n", df.describe(), "\n")
print("Columnas:\n", df.columns, "\n")
print("Valores nulos por columna:\n", df.isnull().sum(), "\n")

#<- Breakpoint
# Manejo de valores nulos
print("###########################Manejo de valores nulos##################")
df_cleaned = df.copy()
df_cleaned.dropna(inplace=True)
print("DataFrame después de eliminar valores nulos:\n", df_cleaned, "\n")

df_filled = df.copy()
df_filled["Edad"].fillna(df["Edad"].mean(), inplace=True)
df_filled["Ciudad"].fillna("Desconocido", inplace=True)
df_filled["Ingreso"].fillna(df["Ingreso"].median(), inplace=True)
print("DataFrame después de rellenar valores nulos:\n", df_filled, "\n")

#<- Breakpoint
# Eliminación de duplicados
print("###########################Eliminación de duplicados##################")
df_dup = df.copy()
df_dup = pd.concat([df_dup, df.iloc[[0]]], ignore_index=True)
print("DataFrame con duplicado agregado:\n", df_dup, "\n")
df_dup.drop_duplicates(inplace=True)
print("DataFrame después de eliminar duplicados:\n", df_dup, "\n")

#<- Breakpoint
# Conversión de tipos de datos
print("###########################Conversión de tipos de datos##################")
df_filled["Edad"] = df_filled["Edad"].astype(int)
print("DataFrame con Edad convertida a entero:\n", df_filled.dtypes, "\n")

#<- Breakpoint
# Filtrado de datos
print("###########################Filtrado de datos##################")
df_mayores_30 = df[df["Edad"] > 30]
print("Personas mayores de 30 años:\n", df_mayores_30, "\n")

df_filtrado = df[(df["Edad"] > 25) & (df["Ciudad"] == "CDMX")]
print("Personas mayores de 25 años en CDMX:\n", df_filtrado, "\n")
