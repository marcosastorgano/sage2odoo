import os
from scripts.parser_asientos import parse_asientos
from scripts.mapper import AccountMapper

def test_parse_asientos_aplica_mapeo():
    asientos_xml = 'tests/data/MovimientosAsientosTest.xml'
    mapping_file = 'mappings/equivalencias_sage_odoo.csv'
    mapper = AccountMapper(mapping_file)

    df_asientos = parse_asientos(asientos_xml, mapper)

    assert not df_asientos.empty

    # Comprobamos que todas las columnas esperadas existen
    columnas_esperadas = [
        'Fecha',
        'Asiento',
        'Cuenta',
        'Etiqueta',
        'Débito',
        'Crédito',
        'Centro de coste'
    ]

    for columna in columnas_esperadas:
        assert columna in df_asientos.columns, f"Falta la columna esperada: {columna}"

    # Validamos que las cuentas están mapeadas correctamente
    cuentas = df_asientos['Cuenta'].unique()
    for cuenta in cuentas:
        if cuenta in mapper.equivalencias.values():
            assert len(cuenta) == 6
        else:
            assert cuenta in mapper.no_mapeadas
