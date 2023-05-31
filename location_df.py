import pandas as pd

# Generar nombres de columnas:
num_pasillos = 50
nombres_columnas = ['Pasillo ' + str(i) for i in range(1, num_pasillos + 1)]

#Máximo por locación:
distribucion_locaciones = {
    "Hasta pasillo 15" : [20,2],
    "De 16 a 40 " : [40,4],
    "De 41 a 50" : [40,2]
}

# Generar datos para las tuplas:
datos_tuplas = []
for i in range(1, num_pasillos + 1):
    #Cantidad máxima de cajas por locación:
    a = (20 if i <= 15 else (40 if i > 15 and i <= 40 else 48))
    #Altura máxima de cajas por locación:
    b = (2 if i <= 15 else (4 if i > 15 and i <= 40 else 2))
    datos_tuplas.append((0,a,b))

# Crear el DataFrame de tuplas
df = pd.DataFrame([datos_tuplas], columns=nombres_columnas)

#Agregar filas extras:
num_filas_adicionales = 20
df = pd.concat([df] * (num_filas_adicionales), ignore_index=True)
print(df)


#Locación seleccionada:

select = df.loc[0,["Pasillo 1"]]
print(select)