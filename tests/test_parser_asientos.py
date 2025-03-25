import re
import pandas as pd

def test_formato_fechas():
    csv_file = 'output/asientos_odoo.csv'
    df = pd.read_csv(csv_file, sep=';')

    patron_fecha = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    for fecha in df['Fecha']:
        if pd.notna(fecha):
            assert patron_fecha.match(str(fecha)), f"Formato de fecha incorrecto: {fecha}"
