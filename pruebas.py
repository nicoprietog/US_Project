import pandas as pd

# DataFrame existente
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Nueva fila como un diccionario
new_row = {'A': 7, 'B': 8}

# Agregar la nueva fila al DataFrame utilizando _append()
df = df._append(new_row, ignore_index=True)

print(df)
