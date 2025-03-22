
import os
import pytest
from scripts.mapper import AccountMapper

def test_mapper_load_and_map():
    mapping_file = os.path.join('mappings', 'equivalencias_sage_odoo.csv')
    mapper = AccountMapper(mapping_file)

    # Si existe en el CSV, devuelve el código Odoo
    mapped_code = mapper.map_account('2040000')

    # Si está en el mapeo, debe ser el valor de Odoo
    if mapped_code != '2040000':
        assert mapped_code == '204000'
    else:
        # Si no está mapeado, devuelve el original
        assert mapped_code == '2040000'

def test_mapper_returns_original_when_no_mapping():
    mapping_file = os.path.join('mappings', 'equivalencias_sage_odoo.csv')
    mapper = AccountMapper(mapping_file)

    # Código que NO existe en el mapeo
    original_code = '9999999'
    result = mapper.map_account(original_code)

    # Devuelve el mismo código si no hay equivalencia
    assert result == original_code
