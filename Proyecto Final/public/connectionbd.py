import pyodbc

class BaseDatos():
    def __init__(self):
        #parametros de conexion
        self.server = 'SA'
        self.database = 'Contenido'

        self.conn = None
        self.cursor = None

    #Metodo para conexion
    def connect(self):
        try:
            connection_string = f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"
            self.conn = pyodbc.connect(connection_string)
            self.cursor = self.conn.cursor()
            print("Conexión establecida correctamente.")

        except pyodbc.ProgrammingError as pe:
            if "Invalid object name" in str(pe):
                print(f"La base de datos '{self.database}' no existe '{self.server}'.")
            else:
                print("Error de programación:", pe)
        except pyodbc.Error as e:
            print("Error:", e)

    #Metodo para la consulta de una tabla
    def query_table(self,table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    #Metodo para insertar en cualquier tabla
    def insert(self, table_name, column_names, values):
        placeholders = ', '.join(['?' for _ in column_names])
        query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
        self.cursor.execute(query,values)
        self.conn.commit()
        print("Inserción completada con éxito")

    #Metodo para cerrar conexion
    def disconnect(self):
        if 'conn' in locals():
            self.conn.close()
            print("Conexión cerrada.")
    
    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()