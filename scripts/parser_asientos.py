
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
        
        asiento = {
            'Fecha Asiento': row.attrib.get('FechaAsiento'),
            'Número Asiento': row.attrib.get('Asiento'),
            'Cuenta Contable': row.attrib.get('CodigoCuenta'),
            'Descripción': row.attrib.get('Comentario'),
            'Debe': importe if importe > 0 else 0.0,
            'Haber': abs(importe) if importe < 0 else 0.0,
            'Centro de Coste': row.attrib.get('CodigoDepartamento', '')
        }
        
        asientos.append(asiento)

    df_asientos = pd.DataFrame(asientos)

    return df_asientos


def run_asientos_parser(input_folder, output_folder):
    asientos_file = os.path.join(input_folder, 'MovimientosE244A1FB-DEA2-4139-9CF8-C95CBCC555A5.XML')
    
    df_asientos = parse_asientos(asientos_file)

    output_file = os.path.join(output_folder, 'asientos_odoo.csv')
    df_asientos.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")
