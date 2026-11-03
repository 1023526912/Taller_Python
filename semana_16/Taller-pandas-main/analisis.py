import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\nIngresos por categoría:\n", datos.to_string())
    print("Categoría con más ingresos:", datos.index[0])
    return datos


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    datos = df.groupby("canal").agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
    datos = datos.sort_values("ingresos", ascending=False)
    print("\nVentas e ingresos por canal:\n", datos.to_string())
    print("Mayor canal por ingresos:", datos.index[0])
    return datos


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    datos = df.groupby("segmento_cliente").agg(clientes=("id_cliente", "nunique"), compras=("id_venta", "count"), gasto_total=("total", "sum"))
    datos["compras_por_cliente"] = datos["compras"] / datos["clientes"]
    datos["gasto_por_cliente"] = datos["gasto_total"] / datos["clientes"]
    print("\nComparación por segmento (clientes que compraron):\n", datos.to_string())
    return datos


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    datos = df["metodo_pago"].value_counts()
    print("\nMétodos de pago:\n", datos.to_string())
    print("Método más usado:", datos.index[0])
    return datos


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    datos = df.groupby(["id_cliente", "nombre_cliente"]).agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
    datos = datos.sort_values(["compras", "gasto_total"], ascending=[False, False]).head(5)
    print("\nTop 5 clientes:\n", datos.to_string())
    return datos


def ventas_por_mes(df):
    datos = df.assign(mes=df["fecha_venta"].dt.to_period("M")).groupby("mes")["total"].sum()
    print("\nBonus: ventas por mes:\n", datos.to_string())
    print("Mes con más ingresos:", datos.idxmax())
    return datos
