import xml.etree.ElementTree as ET
import pandas as pd
import os
from datetime import datetime

def parse_fecha(fecha_raw):
    formatos = ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"]
    for fmt in formatos:
        try:
            return datetime.strptime(fecha_raw, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no reconocido: {fecha_raw}")

def parse_facturas(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')

    facturas = []

    for row in data_node:
        fecha_raw = row.attrib.get('FechaFactura', '')
        fecha_formateada = parse_fecha(fecha_raw) if fecha_raw else ''

        factura = {
            'Número Factura': row.attrib.get('NumeroFactura', ''),
            'Fecha Factura': fecha_formateada,
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
    df_facturas = parse_facturas(facturas_path)

    output_file_name = facturas_file.replace('.xml', '.csv').replace('.XML', '.csv')
    output_file = os.path.join(output_folder, output_file_name)

    df_facturas.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")
