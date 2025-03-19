
from scripts import parser_asientos, parser_facturas

def main():
    print("Iniciando el parser XML para Sage -> Odoo...")
    parser_asientos.parse("data/movimientos_asientos.xml")
    parser_facturas.parse("data/movimientos_facturas.xml")
    print("Proceso completado.")

if __name__ == "__main__":
    main()
