
import os
import argparse
from scripts import parser_facturas, parser_asientos

def resolve_path(base_folder, file_path):
    # Si el path es absoluto, lo devolvemos tal cual
    if os.path.isabs(file_path):
        return file_path

    # Si el path ya empieza con el folder base, no lo duplicamos
    if file_path.startswith(base_folder):
        return file_path

    # Normaliza la ruta relativa combinada
    return os.path.normpath(os.path.join(base_folder, file_path))


def main(input_folder, output_folder, facturas_file, asientos_file):
    # Resolviendo rutas de entrada
    facturas_path = resolve_path(input_folder, facturas_file)
    asientos_path = resolve_path(input_folder, asientos_file)

    print(f"Facturas path: {facturas_path}")
    print(f"Asientos path: {asientos_path}")

    # Procesos normales
    parser_facturas.run_parser(facturas_path, output_folder, facturas_file)
    parser_asientos.run_parser(asientos_path, output_folder, asientos_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa XMLs de Sage y genera CSVs para Odoo.")
    
    parser.add_argument("--input_folder", required=True, help="Carpeta de entrada de los XML.")
    parser.add_argument("--output_folder", required=True, help="Carpeta de salida para los CSV.")
    parser.add_argument("--facturas_file", required=True, help="Archivo XML de facturas.")
    parser.add_argument("--asientos_file", required=True, help="Archivo XML de asientos.")

    args = parser.parse_args()

    main(
        args.input_folder,
        args.output_folder,
        args.facturas_file,
        args.asientos_file
    )
