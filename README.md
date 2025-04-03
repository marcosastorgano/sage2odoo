# Sage2Odoo

Este proyecto permite convertir datos contables de Sage a Odoo, incluyendo la transformación de facturas y asientos contables, aplicando mapeos de cuentas para asegurar la compatibilidad con el Plan General Contable Español (PGCE) en Odoo.

## ✅ Funcionalidades principales

- Parser de facturas desde XML de Sage a CSV compatible con Odoo.
- Parser de asientos contables desde XML de Sage a CSV compatible con Odoo.
    - Las líneas se agrupan por asiento.
    - Solo la primera línea de cada asiento incluye los campos `ref`, `date` y `journal_id` como exige Odoo.
- Mapeo de códigos de cuentas Sage a Odoo mediante el fichero `mappings/equivalencias_sage_odoo.csv`.
- Generación automática de informes de cuentas no mapeadas para control y revisión.

## 📝 Informe de Cuentas no Mapeadas

Durante el procesamiento de los asientos contables, el sistema aplica un mapeo de códigos de cuentas desde Sage a Odoo según el fichero de equivalencias `mappings/equivalencias_sage_odoo.csv`.

Si el código Sage **no tiene equivalencia** definida, el proceso:
- Mantiene el código Sage original en la exportación de asientos.
- Registra esa cuenta en un informe para revisión manual.
- Validación automática de que los asientos están cuadrando (debe = haber), mediante test `test_validador_asientos.py`.

### 📂 Ubicación del informe
El informe se genera automáticamente en la siguiente ruta:
```
output/reportes/cuentas_no_mapeadas.csv
```

### 📄 Contenido del informe
El archivo contiene una única columna:
```
Cuenta Sage sin mapeo
2040000
4300001
7000001
```

### ✅ ¿Qué hacer con el informe?
- Revisar el listado después de cada ejecución.
- Evaluar si es necesario:
  - **Completar el mapeo** en `mappings/equivalencias_sage_odoo.csv`.
  - **Crear nuevas cuentas** en Odoo y actualizar el mapeo en consecuencia.
- Reejecutar el proceso para validar que no queden cuentas sin mapear.

### ⚠️ Notas
- Las cuentas sin equivalencia **no detienen el proceso**, pero deben gestionarse para mantener la consistencia contable.
- Por defecto, todos los asientos se asignan al diario "Ajustes Manuales". Puedes modificar esto en `parser_asientos.py` si necesitas asignar diarios según tipo de asiento o cuenta.

## 🚀 Cómo ejecutar

```bash
python -m scripts.main   --input_folder tests/data   --output_folder output   --facturas_file MovimientosFacturasTest.xml   --asientos_file MovimientosAsientosTest.xml
```

## ✅ Estructura del proyecto

```
sage2odoo/
├── mappings/
│   └── equivalencias_sage_odoo.csv
├── output/
│   ├── facturas_odoo.csv
│   ├── asientos_odoo.csv
│   └── reportes/
│       └── cuentas_no_mapeadas.csv
├── scripts/
│   ├── main.py
│   ├── parser_asientos.py
│   ├── parser_facturas.py
│   └── mapper.py
└── tests/
    ├── test_mapper.py
    ├── test_parser_asientos.py
    └── test_validador_asientos.py
```
