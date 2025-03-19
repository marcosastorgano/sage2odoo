
import pandas as pd
import pytest
import os

def test_asientos_cuadran():
    csv_file = 'output/asientos_odoo.csv'

    assert os.path.exists(csv_file), "El archivo de asientos no existe."

    df = pd.read_csv(csv_file, sep=';')

    resumen = df.groupby('Número Asiento').agg({
        'Debe': 'sum',
        'Haber': 'sum'
    }).reset_index()

    resumen['Diferencia'] = (resumen['Debe'] - resumen['Haber']).round(2)

    descuadrados = resumen[resumen['Diferencia'] != 0]

    assert descuadrados.empty, f"Asientos descuadrados detectados: {descuadrados}"
