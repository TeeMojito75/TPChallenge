import pandas as pd
import random

# Cargar el archivo CSV
df = pd.read_csv("old_dataset.csv")

# Lista de deportes disponibles
deportes = ["Soccer", "Basketball", "Volleyball"]

# Generar valores aleatorios para la nueva columna 'Sport'
df['Sport'] = [random.choice(deportes) for _ in range(len(df))]

# Guardar el archivo CSV modificado
df.to_csv("dataset.csv", index=False)

