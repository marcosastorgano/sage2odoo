
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


def run_parser(input_folder, output_folder, facturas_file='MovimientosFacturasTest.xml'):
    facturas_path = os.path.join(input_folder, facturas_file)

    df_facturas = parse_facturas(facturas_path)

    output_file = os.path.join(output_folder, 'facturas_odoo.csv')
    df_facturas.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")
