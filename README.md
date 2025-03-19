
# Sage2Odoo XML Parser

Parser en Python para convertir los archivos XML exportados desde **Sage Despachos** en archivos CSV listos para importar en **Odoo**.

---

## ✅ Descripción

Este proyecto automatiza la conversión de los datos contables de **Sage Despachos** a un formato compatible con **Odoo**.

Actualmente el script procesa:
- **Facturas** (`MovimientosFacturas*.XML` + `MovimientosIva*.XML` + `Movimientos*.XML`)
- **Asientos Contables** (`Movimientos*.XML`)

Genera **dos archivos CSV**:
- `facturas_odoo.csv`
- `asientos_odoo.csv`

---

## ✅ Requisitos Previos

- Python 3.10 o superior
- pip
- Recomendado: Virtualenv
- GitHub Actions (si quieres CI/CD automático)

---

## ✅ Instalación y Setup Inicial

1. Clona el repositorio:
   ```bash
   git clone git@github.com:TUUSUARIO/sage2odoo.git
   cd sage2odoo
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ✅ Estructura del Proyecto

```
sage2odoo/
├── data/                 # XML de entrada desde Sage
│   ├── MovimientosFacturas*.XML
│   ├── MovimientosIva*.XML
│   └── Movimientos*.XML
├── output/               # CSV generados para Odoo
│   ├── facturas_odoo.csv
│   └── asientos_odoo.csv
├── scripts/              # Código fuente
│   ├── main.py
│   ├── parser_facturas.py
│   └── parser_asientos.py
├── tests/                # Pruebas unitarias e integración
│   ├── test_parser_asientos.py
│   └── test_validador_asientos.py
├── .github/workflows/    # CI/CD para GitHub Actions
│   └── ci.yml
├── requirements.txt      # Dependencias del proyecto
└── README.md
```

---

## ✅ Cómo ejecutar el parser

1. Coloca los XML en la carpeta `data/`:
   - `MovimientosFacturasE244A1FB-....XML`
   - `MovimientosIvaE244A1FB-....XML`
   - `MovimientosE244A1FB-....XML`

2. Lanza el parser desde la raíz del proyecto:
   ```bash
   python -m scripts.main
   ```

3. Se generarán **dos archivos CSV** en la carpeta `output/`:
   - `facturas_odoo.csv`
   - `asientos_odoo.csv`

---

## ✅ Formato de los CSV generados

### 📂 facturas_odoo.csv

| Campo                  | Descripción                          |
|------------------------|--------------------------------------|
| Fecha Factura          | Fecha de emisión de la factura       |
| Fecha Vencimiento      | Fecha de vencimiento de la factura   |
| Número Factura         | Nº de factura                       |
| Partner                | Cliente o Proveedor                 |
| Diario                 | Compras / Ventas / Abono            |
| Base Imponible         | Base imponible de la factura         |
| IVA Cuota              | Importe del IVA                     |
| Tipo IVA               | % de IVA aplicado                   |
| Importe Total          | Total de la factura (base + IVA)    |
| Concepto / Descripción | Descripción de la factura           |
| Centro de Coste        | Si aplica                           |

---

### 📂 asientos_odoo.csv

| Campo             | Descripción                      |
|-------------------|----------------------------------|
| Fecha Asiento     | Fecha del asiento contable       |
| Número Asiento    | Nº de asiento                   |
| Cuenta Contable   | Código de la cuenta contable     |
| Descripción       | Descripción del asiento          |
| Debe              | Importe en el debe               |
| Haber             | Importe en el haber              |
| Centro de Coste   | Si aplica                       |

---

## ✅ Ejecutar los tests en local

Asegúrate de tener el entorno virtual activado:
```bash
source venv/bin/activate
pytest
```

### ¿Qué validan los tests?
- **test_parser_asientos.py**: Comprueba que el parser interpreta correctamente los XML.
- **test_validador_asientos.py**: Verifica que los asientos cuadran (Debe = Haber) para todos los asientos contables del CSV.

---

## ✅ CI/CD con GitHub Actions

El repositorio incluye una pipeline (`.github/workflows/ci.yml`) que ejecuta automáticamente los tests cada vez que se hace un push o pull request sobre la rama `develop`.

```yaml
name: CI Sage2Odoo

on:
  push:
    branches:
      - develop
  pull_request:
    branches:
      - develop

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest
      - name: Run tests
        run: pytest
```

---

## ✅ Troubleshooting

### ModuleNotFoundError: No module named 'scripts'
```bash
python -m scripts.main
```
➡️ Lanza el script desde la raíz del proyecto usando `-m`.

### OSError: Cannot save file into a non-existent directory: 'output'
```bash
mkdir output
```

### Error en los tests de validación
➡️ Revisa el CSV de asientos para ver por qué hay descuadres. Normalmente hay un problema en el XML de origen o en la asignación Debe/Haber.

---

## ✅ Mejoras futuras

- Integración vía API con Odoo para automatizar la carga de los CSV.
- Asignación dinámica de centros de coste según departamentos o proyectos.
- Validaciones automáticas y tests adicionales en GitHub Actions.
- Soporte para archivos adicionales de Sage como BABEL.

---

## ✅ Licencia

MIT License

---
