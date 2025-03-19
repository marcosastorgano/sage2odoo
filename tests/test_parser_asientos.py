
import pytest
import pandas as pd
from scripts import parser_asientos

@pytest.fixture
def sample_xml(tmp_path):
    xml_content = '''
    <root xmlns:rs="urn:schemas-microsoft-com:rowset" xmlns:z="#RowsetSchema">
        <rs:data>
            <z:row Asiento="1" FechaAsiento="2024-10-01" CodigoCuenta="7000001"
                   Comentario="VENTA" ImporteAsiento="1000.00" CargoAbono="D"/>
            <z:row Asiento="1" FechaAsiento="2024-10-01" CodigoCuenta="4300001"
                   Comentario="VENTA" ImporteAsiento="1000.00" CargoAbono="H"/>
        </rs:data>
    </root>
    '''
    file_path = tmp_path / "sample_asientos.xml"
    file_path.write_text(xml_content)
    return file_path

def test_parse_asientos(sample_xml):
    df = parser_asientos.parse_asientos(str(sample_xml))

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2

    # Debe / Haber correctos
    assert df.loc[0, 'Debe'] == 1000.00
    assert df.loc[0, 'Haber'] == 0.00
    assert df.loc[1, 'Debe'] == 0.00
    assert df.loc[1, 'Haber'] == 1000.00
