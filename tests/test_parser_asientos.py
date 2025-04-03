import re
import pandas as pd

def test_formato_fechas():
    csv_file = 'output/asientos_odoo.csv'
    df = pd.read_csv(csv_file, sep=';')

    patron_fecha = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    for fecha in df['date']:
        if pd.notna(fecha):
            assert patron_fecha.match(str(fecha)), f"Formato de fecha incorrecto: {fecha}"

def test_asignacion_journal_por_cuenta():
    from scripts import parser_asientos
    from scripts import mapper
    import tempfile
    import shutil
    import os

    # Crear un entorno temporal con un archivo XML de prueba mínimo
    tmpdir = tempfile.mkdtemp()
    xml_prueba = os.path.join(tmpdir, "MovimientosTest.XML")
    with open(xml_prueba, "w", encoding="utf-8") as f:
        f.write('''<?xml version="1.0"?>
        <root xmlns:rowset="urn:schemas-microsoft-com:rowset">
            <rowset:data>
                <row Asiento="1" CodigoCuenta="623000" Fecha="2024-10-23" Comentario="Gasto proveedor" Debe="100.00" Haber="0.00" />
                <row Asiento="1" CodigoCuenta="410000" Fecha="2024-10-23" Comentario="Gasto proveedor" Debe="0.00" Haber="100.00" />
                <row Asiento="2" CodigoCuenta="551000" Fecha="2024-10-24" Comentario="Pago factura" Debe="0.00" Haber="50.00" />
                <row Asiento="2" CodigoCuenta="410000" Fecha="2024-10-24" Comentario="Pago factura" Debe="50.00" Haber="0.00" />
            </rowset:data>
        </root>
        ''')

    mapping_path = os.path.join(tmpdir, "dummy_mapping.csv")
    with open(mapping_path, "w", encoding="utf-8") as f_map:
        f_map.write("CuentaSage,CuentaOdoo\n")

    mapeador_dummy = mapper.AccountMapper(mapping_path)

    # Ejecutar el parseo
    asientos = parser_asientos.parse_asientos(xml_prueba, mapeador_dummy)

    # Comprobaciones
    print(asientos)
    diarios = set(asientos['journal_id'])
    assert "Ajustes Manuales" in diarios
    assert diarios == {"", "Ajustes Manuales"}

    shutil.rmtree(tmpdir)
