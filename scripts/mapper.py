
import csv
import os

class AccountMapper:
    def __init__(self, mapping_file_path):
        self.mapping_file_path = mapping_file_path
        self.equivalencias = {}
        self.no_mapeadas = set()
        self.load_equivalencias()

    def load_equivalencias(self):
        if not os.path.exists(self.mapping_file_path):
            raise FileNotFoundError(f"Archivo de equivalencias no encontrado: {self.mapping_file_path}")

        with open(self.mapping_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                codigo_sage = row['Codigo_Sage'].strip()
                codigo_odoo = row['Codigo_Odoo'].strip()
                if codigo_sage and codigo_odoo:
                    self.equivalencias[codigo_sage] = codigo_odoo

    def map_account(self, sage_code):
        mapped = self.equivalencias.get(sage_code)
        if mapped:
            return mapped
        else:
            self.no_mapeadas.add(sage_code)
            return sage_code

    def export_no_mapeadas(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Cuenta Sage sin mapeo'])
            for cuenta in sorted(self.no_mapeadas):
                writer.writerow([cuenta])
        print(f"[INFO] Exportado informe de cuentas no mapeadas en: {output_path}")
