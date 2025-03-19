
from scripts import parser_facturas

def main():
    input_folder = 'data'
    output_folder = 'output'
    parser_facturas.run_parser(input_folder, output_folder)

if __name__ == '__main__':
    main()
