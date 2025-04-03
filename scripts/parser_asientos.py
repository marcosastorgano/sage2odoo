import xml.etree.ElementTree as ET
import pandas as pd
import os
from scripts.mapper import AccountMapper
from datetime import datetime


def parse_fecha(fecha_raw):
    """
    Intenta convertir una fecha en formato válido (YYYY-MM-DD).
    Si no se reconoce el formato, devuelve una cadena vacía.
    """
    formatos = ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]
    for fmt in formatos:
        try:
            return datetime.strptime(fecha_raw, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    print(f"Advertencia: Formato de fecha no reconocido: {fecha_raw}")
    return ''  # Devuelve una cadena vacía si no se reconoce el formato


def parse_asientos(xml_path, mapper):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_node = root.find('{urn:schemas-microsoft-com:rowset}data')

    asientos = []

    for row in data_node:
        importe = float(row.attrib.get('ImporteAsiento', 0))
        cargo_abono = row.attrib.get('CargoAbono', '').strip().upper()
        codigo_sage = row.attrib.get('CodigoCuenta')

        # Formatear fecha como YYYY-MM-DD
        fecha_raw = row.attrib.get('FechaAsiento', '')
        print(f"Depuración: Fecha cruda extraída: {fecha_raw}")  # Agregar mensaje de depuración
        fecha_formateada = parse_fecha(fecha_raw) if fecha_raw else ''

        # Determinar el diario según la cuenta contable
        if codigo_sage.startswith('6') or codigo_sage.startswith('7'):
            journal = 'Facturas de proveedores'
        elif codigo_sage.startswith('57') or codigo_sage.startswith('55'):
            journal = 'Banco'
        elif codigo_sage.startswith('1') or codigo_sage.startswith('129'):
            journal = 'Operaciones varias'
        else:
            journal = 'Ajustes Manuales'

        asiento = {
            'id': '',  # Identificador interno del asiento
            'ref': row.attrib.get('Asiento', ''),  # Referencia del asiento
            'date': fecha_formateada,  # Fecha del asiento
            'journal_id': journal,  # Libro diario asociado
            'apunte contable / cuenta': mapper.map_account(codigo_sage),  # Código de cuenta mapeado
            'line_ids/partner_id': '',  # Nombre del cliente/proveedor (vacío por defecto)
            'line_ids/name': row.attrib.get('Comentario', ''),  # Concepto o etiqueta
            'line_ids/debit': importe if cargo_abono == 'D' else 0.0,  # Importe en el debe
            'line_ids/credit': importe if cargo_abono == 'H' else 0.0,  # Importe en el haber
        }

        asientos.append(asiento)

    df_asientos = pd.DataFrame(asientos)

    # Reordenar los asientos para que los de mismo ref estén juntos
    df_asientos.sort_values(by=["ref", "journal_id", "date"], inplace=True)

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