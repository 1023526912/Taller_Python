"""Exploración adicional escrita para el taller; ejecutar por separado."""
import pandas as pd
from carga import cargar_datos
pd.set_option("display.width", 180)
pd.set_option("display.max_columns", None)
clientes, ventas = cargar_datos()
for nombre, tabla in [("clientes", clientes), ("ventas", ventas)]:
    print("\nDataset:", nombre, "\n.shape:", tabla.shape)
    tabla.info()
    print("\n.describe():\n", tabla.describe().to_string())
print("\nLectura parcial con usecols:")
from carga import RAW
print(pd.read_csv(RAW / "ventas.csv", usecols=["id_venta", "total"]).head())
# Líneas propias de selección y concatenación, adicionales al ejemplo original.
print("\nSelección propia con loc: ventas Online")
print(ventas.loc[ventas["canal"] == "Online", ["id_venta", "total"]].head())
reconstruidas = pd.concat([ventas.iloc[:34], ventas.iloc[34:]], ignore_index=True)
print("Concat propio conserva todos los datos:", reconstruidas.equals(ventas))
