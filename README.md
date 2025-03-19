
# Sage2Odoo XML Parser

Automatiza la conversión de los datos contables de **Sage Despachos** a un formato compatible con **Odoo**.

## ✅ Qué hace
Procesa:
- **Facturas** (`MovimientosFacturas*.XML` + `MovimientosIva*.XML` + `Movimientos*.XML`)
- **Asientos contables** (`Movimientos*.XML`)

Genera **dos archivos CSV**:
- `facturas_odoo.csv`
- `asientos_odoo.csv`

## ✅ Instalación y Setup Inicial
1. Clona el repo:
    ```bash
    git clone git@github.com:TUUSUARIO/sage2odoo.git
    cd sage2odoo
    ```

2. Crea un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## ✅ Cómo ejecutar el parser (CLI)

Coloca los XML de Sage en la carpeta que tú quieras (ejemplo `data/`). Luego ejecuta:

```bash
python3 -m scripts.main \
  --input_folder data \
  --output_folder output \
  --facturas_file MovimientosFacturasE244A1FB-DEA2-4139-9CF8-C95CBCC555A5.XML \
  --asientos_file MovimientosE244A1FB-DEA2-4139-9CF8-C95CBCC555A5.XML
```

Los CSV se exportarán en `output/`:
- `facturas_odoo.csv`
- `asientos_odoo.csv`

## ✅ Estructura del Proyecto
```
sage2odoo/
├── data/                 # XML de entrada desde Sage
├── output/               # CSV generados para Odoo
├── scripts/              # Código fuente
│   ├── main.py
│   ├── parser_facturas.py
│   └── parser_asientos.py
├── tests/                # Pruebas unitarias
├── requirements.txt
└── README.md
```
