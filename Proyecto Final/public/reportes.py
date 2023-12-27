from connectionbd import BaseDatos
from informes import generate_general_report, generate_billing_report

def main():
    db = BaseDatos()
    db.connect()

    # Puedes cambiar el valor de 'tipo_informe' según el informe que desees generar
    tipo_informe = input("Seleccione el tipo de informe (general/billing): ").lower()

    if tipo_informe == 'general':
        generate_general_report(db)
    elif tipo_informe == 'billing':
        generate_billing_report(db)
    else:
        print("Tipo de informe no válido.")

    db.disconnect()

if __name__ == "__main__":
    main()