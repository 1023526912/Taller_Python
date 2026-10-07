"""Comprueba que se usa un entorno virtual y que las librerías están instaladas."""
import sys


def main():
    if sys.prefix == sys.base_prefix:
        print("Selecciona o activa el entorno .venv antes de verificar.")
        return 1
    try:
        import pandas
        import matplotlib
        import seaborn
    except ImportError as error:
        print(f"Falta una dependencia: {error}")
        print("Ejecuta: python -m pip install -r requirements.txt")
        return 1
    print(f"Python: {sys.version.split()[0]}")
    print("Entorno virtual: activo")
    print(f"pandas: {pandas.__version__}")
    print(f"matplotlib: {matplotlib.__version__}")
    print(f"seaborn: {seaborn.__version__}")
    print("Entorno listo para el futuro análisis de pingüinos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
