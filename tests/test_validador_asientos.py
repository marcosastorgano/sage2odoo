import pandas as pd
import os

def test_asientos_cuadran():
    csv_file = 'output/asientos_odoo.csv'

    assert os.path.exists(csv_file), "El archivo de asientos no existe."

    df = pd.read_csv(csv_file, sep=';')

    # Rellenar hacia adelante los campos ref y journal_id para poder agrupar
    df['ref'] = df['ref'].ffill()
    df['journal_id'] = df['journal_id'].ffill()

    resumen = df.groupby(['ref', 'journal_id']).agg({
        'line_ids/debit': 'sum',
        'line_ids/credit': 'sum'
    }).reset_index()

    resumen['Diferencia'] = (resumen['line_ids/debit'] - resumen['line_ids/credit']).round(2)

    descuadrados = resumen[resumen['Diferencia'] != 0]

    if not descuadrados.empty:
        print("Asientos descuadrados detectados:")
        print(descuadrados.to_string(index=False))

    assert descuadrados.empty, (
        "\n\nAsientos descuadrados detectados:\n"
        f"{descuadrados.to_string(index=False)}\n"
    )
