
import argparse
from scripts import parser_facturas, parser_asientos

def main(input_folder, output_folder, facturas_file, asientos_file):
    parser_facturas.run_parser(input_folder, output_folder, facturas_file)
    parser_asientos.run_asientos_parser(input_folder, output_folder, asientos_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa XML de Sage y genera CSV para Odoo.")
    
    parser.add_argument('--input_folder', type=str, required=True, help='Carpeta de entrada con los XML de Sage.')
    parser.add_argument('--output_folder', type=str, required=True, help='Carpeta de salida para los CSV.')
    parser.add_argument('--facturas_file', type=str, required=True, help='Nombre del XML de facturas.')
    parser.add_argument('--asientos_file', type=str, required=True, help='Nombre del XML de asientos.')

    args = parser.parse_args()

    main(
        input_folder=args.input_folder,
        output_folder=args.output_folder,
        facturas_file=args.facturas_file,
        asientos_file=args.asientos_file
    )
