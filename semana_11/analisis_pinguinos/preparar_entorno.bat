@echo off
cd /d "%~dp0"
py -3.12 -m venv .venv
if errorlevel 1 goto error
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto error
.venv\Scripts\python.exe -m pip check
if errorlevel 1 goto error

.venv\Scripts\python.exe verificar_entorno.py
if errorlevel 1 goto error
.venv\Scripts\python.exe -m pip freeze > requirements.txt
echo.
echo Entorno listo. Selecciona .venv como interprete en VS Code.
pause
exit /b 0
:error
echo.
echo No fue posible preparar el entorno. Revisa Python 3.12 y tu conexion.
pause
exit /b 1
