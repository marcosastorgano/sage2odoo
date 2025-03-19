
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
- (Recomendado) Virtualenv

---

## ✅ Instalación y Setup Inicial

1. Clona el repositorio:
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
├── requirements.txt
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

| Campo                | Descripción                        |
|----------------------|------------------------------------|
| Fecha Factura        | Fecha de emisión de la factura     |
| Fecha Vencimiento    | Fecha de vencimiento de la factura |
| Número Factura       | Nº de factura                     |
| Partner              | Cliente o Proveedor               |
| Diario               | Compras / Ventas / Abono          |
| Base Imponible       | Base imponible de la factura       |
| IVA Cuota            | Importe del IVA                   |
| Tipo IVA             | % de IVA aplicado                 |
| Importe Total        | Total de la factura (base + IVA)  |
| Concepto / Descripción | Descripción de la factura        |
| Centro de Coste      | Si aplica                         |

---

### 📂 asientos_odoo.csv

| Campo                | Descripción                      |
|----------------------|----------------------------------|
| Fecha Asiento        | Fecha del asiento contable       |
| Número Asiento       | Nº de asiento                   |
| Cuenta Contable      | Código de la cuenta contable     |
| Descripción          | Descripción del asiento          |
| Debe                | Importe en el debe               |
| Haber               | Importe en el haber              |
| Centro de Coste      | Si aplica                       |

---

## ✅ Troubleshooting

### ModuleNotFoundError: No module named 'scripts'
```bash
python -m scripts.main
```
➡️ Asegúrate de lanzar el script desde la raíz del proyecto usando el flag `-m`.

### OSError: Cannot save file into a non-existent directory: 'output'
```bash
mkdir output
```
➡️ Crea la carpeta `output` antes de ejecutar el script si no existe.

### ModuleNotFoundError: No module named 'pandas'
```bash
pip install -r requirements.txt
```
➡️ Activa tu entorno virtual antes de instalar dependencias.

---

## ✅ Mejoras futuras

- Integración vía API con Odoo para automatizar la carga de los CSV.
- Asignación dinámica de centros de coste según departamentos o proyectos.
- Validaciones automáticas y tests en GitHub Actions.
- Soporte para archivos adicionales de Sage como BABEL.

---

## ✅ Licencia

MIT License

---
