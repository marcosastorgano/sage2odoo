
import os
import argparse
from scripts import parser_facturas, parser_asientos

def main():
    parser = argparse.ArgumentParser(description="Parser de Sage a Odoo")
    parser.add_argument("--input_folder", type=str, required=True, help="Carpeta de entrada de los XML")
    parser.add_argument("--output_folder", type=str, required=True, help="Carpeta de salida de los CSV")
    parser.add_argument("--facturas_file", type=str, required=True, help="Archivo XML de facturas")
    parser.add_argument("--asientos_file", type=str, required=True, help="Archivo XML de asientos")

    args = parser.parse_args()

    facturas_path = os.path.join(args.input_folder, args.facturas_file)
    asientos_path = os.path.join(args.input_folder, args.asientos_file)

    print(f"Facturas path: {facturas_path}")
    print(f"Asientos path: {asientos_path}")

    # Ejecutar parser de facturas
    parser_facturas.run_parser(facturas_path, args.output_folder, 'facturas_odoo.csv')

    # Ejecutar parser de asientos con nombre fijo para CI/test
    parser_asientos.run_parser(asientos_path, args.output_folder, 'asientos_odoo.csv')

if __name__ == "__main__":
    main()
