# Grupo8TP4SIM

Trabajo práctico 4 de simulación, implementado en Python.

## Preparar el entorno en Windows

Requiere Python 3.10 o superior. Desde la carpeta del proyecto, ejecutar:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m unittest discover -v
```

No se necesitan paquetes externos: el proyecto utiliza la biblioteca estándar
de Python. La carpeta `.vscode` configura el intérprete esperado y la detección
de pruebas unitarias. Si VS Code no detecta el entorno automáticamente, usar
**Python: Select Interpreter** y seleccionar `.venv\Scripts\python.exe`.
