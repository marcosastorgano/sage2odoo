import xml.etree.ElementTree as ET
import pandas as pd
import os

def parse_asientos(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')

    asientos = []

    for row in data_node:
        importe = float(row.attrib.get('ImporteAsiento', 0))
        cargo_abono = row.attrib.get('CargoAbono', '').strip().upper()

        asiento = {
            'Fecha Asiento': row.attrib.get('FechaAsiento'),
            'Número Asiento': row.attrib.get('Asiento'),
            'Cuenta Contable': row.attrib.get('CodigoCuenta'),
            'Descripción': row.attrib.get('Comentario'),
            'Debe': importe if cargo_abono == 'D' else 0.0,
            'Haber': importe if cargo_abono == 'H' else 0.0,
            'Centro de Coste': row.attrib.get('CodigoDepartamento', '')
        }

        asientos.append(asiento)

    df_asientos = pd.DataFrame(asientos)

    return df_asientos


def run_parser(asientos_path, output_folder, asientos_file='MovimientosAsientosTest.xml'):
    # Este es el path del XML ya resuelto que le pasa main.py
    df_asientos = parse_asientos(asientos_path)

    # Generamos el nombre del CSV de salida, igual que en facturas
    output_file_name = asientos_file.replace('.xml', '.csv').replace('.XML', '.csv')
    output_file = os.path.join(output_folder, output_file_name)

    df_asientos.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")
