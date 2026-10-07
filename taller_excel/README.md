# Taller práctico de Python y Excel

Lectura de la hoja activa de `personas.xlsx`, almacenamiento en listas y visualización en consola con `tabulate`. Se resuelven los cinco retos de la guía evaluativa.

## Abrir en Visual Studio Code (Windows)

1. Instala Python 3.12 y la extensión **Python**, de Microsoft, en VS Code.
2. Extrae el ZIP. No ejecutes archivos desde la vista del ZIP.
3. En VS Code selecciona **Archivo > Abrir carpeta** y abre `taller_excel`.
4. Ejecuta `preparar_entorno.bat` haciendo doble clic desde el Explorador. Espera a que indique que el entorno está listo.
5. En VS Code pulsa `Ctrl+Shift+P`, busca **Python: Select Interpreter** y selecciona `.venv`. Si no aparece, selecciona **Enter interpreter path** y busca `.venv\Scripts\python.exe` dentro de esta carpeta.
6. Abre `TallerExcel_Python_NombreApellido.py` y pulsa **Run Python File in Terminal** (triángulo arriba a la derecha). Escribe las opciones en la terminal.

También puedes ejecutarlo desde la terminal de VS Code:

```powershell
.\.venv\Scripts\python.exe TallerExcel_Python_NombreApellido.py
```

## Instalación manual

Abre **Terminal > Nueva terminal** dentro de `taller_excel`:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe TallerExcel_Python_NombreApellido.py
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python TallerExcel_Python_NombreApellido.py
```

## Retos resueltos

| Reto | Opción del menú |
| --- | --- |
| Mostrar solo Name y Email | 2 |
| Contar registros | 3 |
| Filtrar empresas que contienen Group | 4 |
| Pedir un ID y buscar la persona | 5 |
| Menú con consultas y salida | 1 a 5 y 0 |

La opción 1 muestra la tabla completa. Para probar una búsqueda, copia el ID de la primera persona:

`05936c10-1f8e-4a4c-95e4-e677f04f17a6`

Los nombres, empresas y correos son datos ficticios para el taller. Se conservan los 35 ID y las direcciones MAC del Excel suministrado. Algunas empresas conservan la palabra Group para demostrar el filtro solicitado.

## Explicación del código

- `cargar_datos()` abre el Excel, selecciona su hoja activa y recorre filas y columnas con dos ciclos. Cada fila temporal se agrega a la lista principal. Omite los encabezados e incluye la última fila.
- `mostrar_tabla()` usa `tabulate` para dibujar la tabla.
- `mostrar_nombre_email()`, `contar_registros()`, `filtrar_empresa()` y `buscar_id()` resuelven los retos.
- `menu()` recibe opciones con `input()` hasta elegir 0.
- `main()` carga los datos y maneja errores de archivo. El Excel se localiza junto al script aunque se ejecute desde otra carpeta.

## Antes de entregar

1. Renombra `TallerExcel_Python_NombreApellido.py` con tu nombre y apellido, como pide la guía. El programa sigue funcionando después del cambio. Usa el nuevo nombre al ejecutarlo desde la terminal.
2. En `evidencias` están las imágenes de la salida real del programa y la transcripción. Las imágenes se generaron a partir de esa salida. Si el profesor pide una captura de tu propia pantalla, ejecuta la opción 1 y toma una captura de la terminal de VS Code con `Win+Shift+S`.
3. Entrega el Python, `personas.xlsx`, las evidencias y `requirements.txt`. No incluyas `.venv` en GitHub.

Referencia consultada: https://github.com/LeoT360/Taller-Practico-Python. La solución se elaboró siguiendo la guía evaluativa adjunta.
