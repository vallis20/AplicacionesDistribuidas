# Importa la clase BaseDatos
from connectionbd import BaseDatos

# Crea una instancia de la clase
mi_bd = BaseDatos()

# Intenta establecer la conexión
mi_bd.connect()

# Realiza una consulta en una tabla (reemplaza 'NombreDeTuTabla' con el nombre real de tu tabla)
resultados = mi_bd.query_table('Streaming')
if(resultados!=0):
    print("Resultados de la consulta:")
    print(resultados)
else:
    print("No hay resultados")


# Inserta datos en la tabla (reemplaza 'NombreDeTuTabla' con el nombre real de tu tabla)
#columnas = ['Columna1', 'Columna2', 'Columna3']  # Reemplaza con nombres reales de columnas
#valores = ('Valor1', 'Valor2', 'Valor3')  # Reemplaza con los valores que desees insertar
#mi_bd.insert('NombreDeTuTabla', columnas, valores)

# Cierra la conexión
mi_bd.disconnect()
