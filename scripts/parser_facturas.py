
import xml.etree.ElementTree as ET
import pandas as pd
import os

def parse_facturas(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')
    
    facturas = []
    for row in data_node:
        facturas.append({
            'Proceso': row.attrib.get('Proceso'),
            'MovPosicion': row.attrib.get('MovPosicion'),
            'Factura': row.attrib.get('Factura'),
            'SuFacturaNo': row.attrib.get('SuFacturaNo'),
            'FechaFactura': row.attrib.get('FechaFactura'),
            'FechaMaxVencimiento': row.attrib.get('FechaMaxVencimiento'),
            'ImporteFactura': float(row.attrib.get('ImporteFactura', 0)),
            'Nombre': row.attrib.get('Nombre'),
            'TipoFactura': row.attrib.get('TipoFactura')
        })
    return pd.DataFrame(facturas)

def parse_iva(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')
    
    iva_lines = []
    for row in data_node:
        iva_lines.append({
            'Proceso': row.attrib.get('Proceso'),
            'MovPosicion': row.attrib.get('MovPosicion'),
            'CodigoIva': row.attrib.get('CodigoIva'),
            'BaseIva': float(row.attrib.get('BaseIva', 0)),
            'CuotaIva': float(row.attrib.get('CuotaIva', 0))
        })
    return pd.DataFrame(iva_lines)

def parse_asientos(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')
    
    asientos = []
    for row in data_node:
        asientos.append({
            'Proceso': row.attrib.get('Proceso'),
            'MovPosicion': row.attrib.get('MovPosicion'),
            'CodigoCuenta': row.attrib.get('CodigoCuenta'),
            'Comentario': row.attrib.get('Comentario')
        })
    return pd.DataFrame(asientos)

def merge_data(df_facturas, df_iva, df_asientos):
    merged = pd.merge(df_facturas, df_iva, on=['Proceso', 'MovPosicion'], how='left')
    merged = pd.merge(merged, df_asientos, on=['Proceso', 'MovPosicion'], how='left')

    # Generar columnas de salida
    merged['Fecha Factura'] = merged['FechaFactura']
    merged['Fecha Vencimiento'] = merged['FechaMaxVencimiento']
    merged['Número Factura'] = merged.apply(lambda x: x['Factura'] if x['Factura'] else x['SuFacturaNo'], axis=1)
    merged['Partner'] = merged['Nombre']
    merged['Diario'] = merged['TipoFactura'].map({'R': 'Compras', 'E': 'Ventas', 'A': 'Abono'}).fillna('Otro')
    merged['Base Imponible'] = merged['BaseIva']
    merged['IVA Cuota'] = merged['CuotaIva']
    merged['Tipo IVA'] = merged['CodigoIva']
    merged['Importe Total'] = merged['ImporteFactura'] + merged['CuotaIva']
    merged['Concepto / Descripción'] = merged['Comentario']
    merged['Centro de Coste'] = ''

    cols_export = [
        'Fecha Factura', 'Fecha Vencimiento', 'Número Factura', 'Partner',
        'Diario', 'Base Imponible', 'IVA Cuota', 'Tipo IVA', 'Importe Total',
        'Concepto / Descripción', 'Centro de Coste'
    ]
    return merged[cols_export]

def run_parser(input_folder, output_folder):
    facturas_file = os.path.join(input_folder, 'MovimientosFacturasE244A1FB-DEA2-4139-9CF8-C95CBCC555A5.XML')
    iva_file = os.path.join(input_folder, 'MovimientosIvaE244A1FB-DEA2-4139-9CF8-C95CBCC555A5.XML')
    asientos_file = os.path.join(input_folder, 'MovimientosE244A1FB-DEA2-4139-9CF8-C95CBCC555A5.XML')

    df_facturas = parse_facturas(facturas_file)
    df_iva = parse_iva(iva_file)
    df_asientos = parse_asientos(asientos_file)

    merged_data = merge_data(df_facturas, df_iva, df_asientos)

    output_file = os.path.join(output_folder, 'facturas_odoo.csv')
    merged_data.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Exportado CSV a: {output_file}")
