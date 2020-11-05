import psycopg2

class Conexion:
    def __init__(self):
        self.conn = psycopg2.connect(host="127.0.0.1",user="postgres",password="mysql",database="factura")
        self.cursor = self.conn.cursor()

        print("Conexion Exitosa")