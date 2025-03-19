
# Sage2Odoo XML Parser

Parser en Python para convertir los archivos XML exportados desde **Sage Despachos** en archivos CSV listos para importar en **Odoo**.

---

## ✅ Descripción
Este script procesa los datos de:
- **Facturas** (`MovimientosFacturas*.XML`)
- **IVA** (`MovimientosIva*.XML`)
- **Asientos contables** (`Movimientos*.XML`)

Genera un CSV consolidado que puede importarse en Odoo para mejorar la gestión analítica y el control de costes.

---

## ✅ Requisitos Previos
- Python 3.10 o superior
- pip
- (Recomendado) Virtualenv

---

## ✅ Instalación y Setup Inicial

1. **Clona el repositorio**:
   ```bash
   git clone git@github.com:TUUSUARIO/sage2odoo.git
   cd sage2odoo
   ```

2. **Crea un entorno virtual** (recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ✅ Estructura del Proyecto

```
sage2odoo/
├── data/                 # XML de entrada desde Sage
├── output/               # CSV generado para Odoo
├── scripts/              # Código fuente
│   ├── main.py           # Script principal
│   ├── parser_facturas.py # Parser de facturas
│   └── parser_asientos.py # Parser de asientos (opcional)
├── requirements.txt
└── README.md
```

---

## ✅ Cómo ejecutar el parser

1. Coloca los XML en la carpeta `data/`.
   - `MovimientosFacturasE244A1FB-...XML`
   - `MovimientosIvaE244A1FB-...XML`
   - `MovimientosE244A1FB-...XML`

2. Lanza el parser:
   ```bash
   python -m scripts.main
   ```

3. El resultado estará en la carpeta `output/` con el nombre:
   ```
   facturas_odoo.csv
   ```

---

## ✅ Formato del CSV generado

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
| Concepto / Descripción | Descripción del asiento o factura |
| Centro de Coste      | Si aplica, se puede completar     |

---

## ✅ Troubleshooting

**ModuleNotFoundError: No module named 'scripts'**
```bash
python -m scripts.main
```
➡️ Lanza siempre desde la raíz del proyecto usando el flag `-m`.

**ModuleNotFoundError: No module named 'pandas'**
```bash
pip install -r requirements.txt
```
➡️ Asegúrate de tener el entorno virtual activo.

**OSError: Cannot save file into a non-existent directory**
```bash
mkdir output
```
➡️ Crea la carpeta `output` antes de lanzar el script si no existe.

---

## ✅ Mejoras futuras
- Integración vía API con Odoo para subir el CSV automáticamente.
- Asignación de centros de coste dinámicos según reglas personalizadas.
- Mejora de validación de datos (tests unitarios).
- Adaptación para nuevas versiones de Sage o formatos BABEL.

---

## ✅ Licencia
MIT License
