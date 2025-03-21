import xml.etree.ElementTree as ET
import pandas as pd
import os

def parse_facturas(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')

    facturas = []

    for row in data_node:
        factura = {
            'Número Factura': row.attrib.get('NumeroFactura', ''),
            'Fecha Factura': row.attrib.get('FechaFactura', ''),
            'Cliente': row.attrib.get('CodigoCliente', ''),
            'Base Imponible': row.attrib.get('BaseImponible', '0.0'),
            'IVA': row.attrib.get('IVA', '0.0'),
            'Total Factura': row.attrib.get('TotalFactura', '0.0'),
            'Descripción': row.attrib.get('Descripcion', '')
        }

        facturas.append(factura)

    df_facturas = pd.DataFrame(facturas)

    return df_facturas


def run_parser(facturas_path, output_folder, facturas_file='MovimientosFacturasTest.xml'):
    # Ya no concatenamos input_folder aquí porque el path viene completo
    df_facturas = parse_facturas(facturas_path)

    # Usamos el nombre de facturas_file para construir el nombre del CSV de salida
    output_file_name = facturas_file.replace('.xml', '.csv').replace('.XML', '.csv')
    output_file = os.path.join(output_folder, output_file_name)

    df_facturas.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")
