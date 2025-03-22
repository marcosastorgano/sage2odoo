
import os
from scripts.parser_asientos import parse_asientos
from scripts.mapper import AccountMapper

def test_parse_asientos_aplica_mapeo():
    asientos_xml = 'tests/data/MovimientosAsientosTest.xml'
    mapping_file = 'mappings/equivalencias_sage_odoo.csv'
    mapper = AccountMapper(mapping_file)

    df_asientos = parse_asientos(asientos_xml, mapper)

    assert not df_asientos.empty

    cuentas = df_asientos['Cuenta Contable'].unique()

    for cuenta in cuentas:
        # Si la cuenta está en el resultado del mapeo, debe tener longitud 6 (Odoo)
        if cuenta in mapper.equivalencias.values():
            assert len(cuenta) == 6
        else:
            # Si no está mapeada, debe aparecer en el listado de no mapeadas
            assert cuenta in mapper.no_mapeadas
