import pandas as pd
import os

def test_asientos_cuadran():
    csv_file = 'output/asientos_odoo.csv'

    assert os.path.exists(csv_file), "El archivo de asientos no existe."

    df = pd.read_csv(csv_file, sep=';')

    resumen = df.groupby('ref').agg({
        'line_ids/debit': 'sum',
        'line_ids/credit': 'sum'
    }).reset_index()

    resumen['Diferencia'] = (resumen['line_ids/debit'] - resumen['line_ids/credit']).round(2)

    descuadrados = resumen[resumen['Diferencia'] != 0]

    assert descuadrados.empty, f"Asientos descuadrados detectados: {descuadrados}"
