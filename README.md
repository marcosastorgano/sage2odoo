
# XML Parser para Sage -> Odoo

Este proyecto contiene scripts en Python para convertir los archivos XML exportados desde Sage en CSVs listos para importar en Odoo.

## Estructura del Proyecto
- `scripts/` -> Contiene los scripts de procesamiento de XML.
- `data/` -> Carpeta de entrada/salida para los XML y los CSV resultantes.
- `tests/` -> Pruebas unitarias.
- `.github/workflows/` -> Flujos de GitHub Actions.

## Cómo empezar
1. Crea el entorno virtual: `python -m venv venv`
2. Activa el entorno: `source venv/bin/activate` o `venv\Scripts\activate`
3. Instala dependencias: `pip install -r requirements.txt`
4. Ejecuta el script principal: `python scripts/main.py`

## Pendiente
- Mejorar la asignación de centros de coste.
- Añadir integración con Odoo vía API (opcional).
