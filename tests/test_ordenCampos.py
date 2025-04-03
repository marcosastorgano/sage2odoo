def test_orden_asientos_por_ref_journal_fecha():
    from scripts import parser_asientos
    from scripts import mapper
    import tempfile
    import os

    # Crear un entorno temporal con un archivo XML de prueba mínimo
    tmpdir = tempfile.mkdtemp()
    xml_prueba = os.path.join(tmpdir, "MovimientosOrden.XML")
    with open(xml_prueba, "w", encoding="utf-8") as f:
        f.write('''<?xml version="1.0"?>
        <root xmlns:rowset="urn:schemas-microsoft-com:rowset">
            <rowset:data>
                <row Asiento="2" CodigoCuenta="623000" Fecha="2024-10-25" Comentario="A" Debe="50.00" Haber="0.00" />
                <row Asiento="1" CodigoCuenta="623000" Fecha="2024-10-24" Comentario="B" Debe="75.00" Haber="0.00" />
                <row Asiento="1" CodigoCuenta="551000" Fecha="2024-10-24" Comentario="C" Debe="0.00" Haber="75.00" />
                <row Asiento="2" CodigoCuenta="551000" Fecha="2024-10-25" Comentario="D" Debe="0.00" Haber="50.00" />
            </rowset:data>
        </root>
        ''')

    # Crear mapping vacío
    mapping_path = os.path.join(tmpdir, "dummy_mapping.csv")
    with open(mapping_path, "w", encoding="utf-8") as f_map:
        f_map.write("CuentaSage,CuentaOdoo\n")

    mapeador_dummy = mapper.AccountMapper(mapping_path)

    # Ejecutar el parseo
    df_asientos = parser_asientos.parse_asientos(xml_prueba, mapeador_dummy)

    # Verificar orden
    ordenado = df_asientos.sort_values(by=["ref", "journal_id", "date"]).reset_index(drop=True)
    assert df_asientos.reset_index(drop=True).equals(ordenado), "Los asientos no están correctamente ordenados"
