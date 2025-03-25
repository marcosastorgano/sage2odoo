import pandas as pd
import os
import re

def test_columnas_esperadas_en_asientos():
    csv_file = 'output/asientos_odoo.csv'
    assert os.path.exists(csv_file), "El archivo de asientos no existe."

    df = pd.read_csv(csv_file, sep=';')
    columnas_esperadas = ['Fecha', 'Asiento', 'Cuenta', 'Etiqueta', 'Débito', 'Crédito', 'Centro de coste']
    assert list(df.columns) == columnas_esperadas, f"Las columnas no coinciden: {list(df.columns)}"

def test_formato_fechas():
    csv_file = 'output/asientos_odoo.csv'
    df = pd.read_csv(csv_file, sep=';')
    # Verifica que todas las fechas cumplen el formato YYYY-MM-DD
    patron_fecha = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    for fecha in df['Fecha']:
        assert patron_fecha.match(fecha), f"Formato de fecha incorrecto: {fecha}"
