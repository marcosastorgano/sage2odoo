
from scripts import parser_facturas, parser_asientos

def main(input_folder='data', output_folder='output', asientos_file='MovimientosAsientosTest.xml'):
    # Ejecuta parser de facturas
    parser_facturas.run_parser(input_folder, output_folder)

    # Ejecuta parser de asientos contables
    parser_asientos.run_asientos_parser(input_folder, output_folder, asientos_file)

if __name__ == '__main__':
    main()
