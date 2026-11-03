from pathlib import Path

import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def grafico_ventas_por_categoria(df):
    """Gráfico de barras: total vendido por categoría.

    Pistas:
    - Calcular datos = df.groupby("categoria")["total"].sum()
    - datos.plot(kind="bar") dibuja las barras.
    - plt.title, plt.xlabel y plt.ylabel ponen los textos.
    - plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight") guarda la imagen.
    - plt.show() la muestra en pantalla y plt.close() la cierra.
    """
    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    SALIDA.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    datos.plot(kind="bar", color="#2878a5", rot=0)
    plt.title("Ingresos por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Ingresos (unidades monetarias del dataset)")
    plt.ticklabel_format(axis="y", style="plain")
    plt.tight_layout()
    plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight", dpi=150)
    print("Gráfico guardado:", SALIDA / "ventas_por_categoria.png")
    plt.show()
    plt.close()


def grafico_ventas_por_canal(df):
    """Gráfico de barras: total vendido por canal (Online contra Tienda).

    Usa los mismos pasos que la función anterior, cambiando la columna "categoria" por "canal".
    """
    datos = df.groupby("canal")["total"].sum().sort_values(ascending=False)
    SALIDA.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    datos.plot(kind="bar", color="#2878a5", rot=0)
    plt.title("Ingresos por canal")
    plt.xlabel("Canal")
    plt.ylabel("Ingresos (unidades monetarias del dataset)")
    plt.ticklabel_format(axis="y", style="plain")
    plt.tight_layout()
    plt.savefig(SALIDA / "ventas_por_canal.png", bbox_inches="tight", dpi=150)
    print("Gráfico guardado:", SALIDA / "ventas_por_canal.png")
    plt.show()
    plt.close()


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)
