import xml.etree.ElementTree as ET
import pandas as pd
import os
from scripts.mapper import AccountMapper

def parse_asientos(xml_path, mapper):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')

    asientos = []

    for row in data_node:
        importe = float(row.attrib.get('ImporteAsiento', 0))
        cargo_abono = row.attrib.get('CargoAbono', '').strip().upper()
        codigo_sage = row.attrib.get('CodigoCuenta')

        asiento = {
            'Fecha': row.attrib.get('FechaAsiento'),
            'Asiento': row.attrib.get('Asiento'),
            'Cuenta': mapper.map_account(codigo_sage),
            'Etiqueta': row.attrib.get('Comentario'),
            'Débito': importe if cargo_abono == 'D' else 0.0,
            'Crédito': importe if cargo_abono == 'H' else 0.0,
            'Centro de coste': row.attrib.get('CodigoDepartamento', '')
        }

        asientos.append(asiento)

    df_asientos = pd.DataFrame(asientos)

    return df_asientos

def run_parser(asientos_path, output_folder, output_file_name='asientos_odoo.csv'):
    # Cargar el mapper de cuentas contables
    mapping_file = os.path.join('mappings', 'equivalencias_sage_odoo.csv')
    mapper = AccountMapper(mapping_file)

    df_asientos = parse_asientos(asientos_path, mapper)

    # Exportar el CSV de asientos contables
    output_file = os.path.join(output_folder, output_file_name)
    df_asientos.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")

    # Exportar informe de cuentas no mapeadas
    reportes_folder = os.path.join(output_folder, 'reportes')
    os.makedirs(reportes_folder, exist_ok=True)

    no_mapeadas_file = os.path.join(reportes_folder, 'cuentas_no_mapeadas.csv')
    mapper.export_no_mapeadas(no_mapeadas_file)
