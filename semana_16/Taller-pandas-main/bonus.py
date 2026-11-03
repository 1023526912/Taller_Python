from carga import cargar_datos
from limpieza import limpiar_datos
from merge import unir
from analisis import ventas_por_mes
clientes, ventas = limpiar_datos(*cargar_datos())
df = unir(clientes, ventas)
if df is not None:
    ventas_por_mes(df).to_csv("Data/processed/ventas_por_mes.csv")
