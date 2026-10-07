# Entorno virtual para análisis de pingüinos

Ejercicio independiente de la semana 11. El objetivo es preparar un entorno reproducible con pandas, matplotlib y seaborn. `analisis.py` queda reservado para el análisis futuro, como permite la guía.

## Estructura después de la instalación

La carpeta `analisis_pinguinos` contiene `.venv/`, `requirements.txt`, `analisis.py`, este `README.md` y los archivos auxiliares de configuración y verificación.

El ZIP no incluye un entorno virtual preinstalado: `.venv` contiene rutas y ejecutables que dependen del sistema operativo. Se crea en el computador de cada desarrollador con los pasos siguientes. Tampoco se sube a GitHub.

## Preparación en Windows

Requisito: Python **3.12** instalado y conexión a Internet para descargar dependencias. Las versiones fijadas fueron instaladas y verificadas con Python 3.12.

1. Extrae el ZIP.
2. Abre `semana_11/analisis_pinguinos` con **Archivo > Abrir carpeta** en Visual Studio Code.
3. Abre **Terminal > Nueva terminal** y selecciona el perfil **Command Prompt** (Símbolo del sistema).
4. Crea y activa el entorno:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

5. Instala todas las dependencias:

```bat
python -m pip install -r requirements.txt
```

6. Verifica los paquetes y guarda la evidencia del entorno creado en tu equipo:

```bat
python verificar_entorno.py
python -m pip check
python -m pip freeze > requirements.txt
```

7. Pulsa `Ctrl+Shift+P`, busca **Python: Select Interpreter** y selecciona `.venv\Scripts\python.exe`.

Alternativa rápida: ejecuta `preparar_entorno.bat` desde el Explorador. Este archivo crea `.venv`, instala los paquetes, los verifica y guarda el resultado de `pip freeze`. Para activar el entorno en una terminal de Command Prompt usa el comando de activación anterior.

### Si usas PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python verificar_entorno.py
```

Si PowerShell bloquea la activación por su política de scripts, usa el perfil Command Prompt. También puedes trabajar sin activar, llamando directamente al intérprete:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe verificar_entorno.py
```

## Preparación en macOS o Linux

Con Python 3.12 instalado:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python verificar_entorno.py
python -m pip check
python -m pip freeze > requirements.txt
```

Para salir del entorno en cualquier sistema:

```text
deactivate
```

## requirements.txt

Se generó con `python -m pip freeze` después de instalar pandas, matplotlib y seaborn en un entorno virtual limpio. Incluye las dependencias con versiones exactas. No contiene las librerías del otro taller de Excel.

## Entrega en GitHub

La guía exige un repositorio de GitHub, dentro de la carpeta correspondiente a la semana 11. Este ZIP deja preparada la estructura `semana_11/analisis_pinguinos`.

Si ya tienes un repositorio de clase, copia `semana_11` dentro de ese repositorio y sube los archivos con Git o con **Add file > Upload files** en GitHub. Sube los archivos dentro de la carpeta correspondiente, no el ZIP. Incluye `requirements.txt`, `analisis.py`, `README.md` y los auxiliares. No subas `.venv`.

Si no tienes repositorio, crea uno en tu cuenta y sube la carpeta `semana_11`. Si el profesor utiliza otro nombre para esta carpeta, renómbrala según sus indicaciones.

La configuración se probó en Linux. Ejecuta los pasos en tu equipo para crear y verificar tu entorno local. El archivo `evidencia_entorno.txt` documenta la comprobación realizada durante la preparación.
