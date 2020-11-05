from conn import Conexion

class Productos(Conexion):
    def crear_tabla_producto(self):
        query = """
            CREATE TABLE IF NOT EXISTS productos(
                id_producto SERIAL NOT NULL,
                nombre VARCHAR(200) NOT NULL,
                precio REAL NOT NULL,
                descripcion VARCHAR(255) NULL,
                codigo VARCHAR(4) NOT NULL,
                PRIMARY KEY(id_producto)
            );
        """
        self.cursor.execute(query)
        self.conn.commit()
    
    def ingresar_datos_productos(self,nombre,precio,descripcion,codigo):
        query = "INSERT INTO productos(nombre,precio,descripcion,codigo) VALUES(%s,%s,%s,%s);"
        self.cursor.execute(query,[nombre,precio,descripcion,codigo])
        self.conn.commit()

    def crear_tabla_clientes(self):
        query = """
            CREATE TABLE IF NOT EXISTS clientes(
                id_cliente SERIAL NOT NULL,
                nombres VARCHAR(200) NOT NULL,
                apellidos VARCHAR(200) NULL,
                dni VARCHAR(8) NOT NULL,
                PRIMARY KEY(id_cliente)
            );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def ingresar_clientes(self, nombres,apellidos,dni):
        query = "INSERT INTO clientes(nombres,apellidos,dni) VALUES(%s,%s,%s);"
        self.cursor.execute(query,[nombres,apellidos,dni])
        self.conn.commit()

    def crear_tabla_facturas(self):
        query = """
            CREATE TABLE IF NOT EXISTS facturas(
                id_factura SERIAL NOT NULL,
                fecha DATE,
                subtotal REAL NOT NULL,
                igv REAL NOT NULL,
                total REAL NOT NULL,
                cliente_id SERIAL NOT NULL,
                producto_id SERIAL NOT NULL,
                PRIMARY KEY(id_factura),
                FOREIGN KEY(cliente_id) REFERENCES clientes(id_cliente),
                FOREIGN KEY(producto_id) REFERENCES productos(id_producto)
            );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def ingresar_datos_factura(self,fecha,subtotal,igv,total):
        query = "INSERT INTO facturas(fecha,subtotal,igv,total) VALUES(%s,%s,%s,%s);"
        self.cursor.execute(query,[fecha,subtotal,igv,total])
        self.conn.commit()

    def emitir_factura(self,fecha,subtotal,igv,total):
        query = "SELECT * FROM facturas ORDER BY id_factura DESC LIMIT 1;"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        print(f"""
            Nro. Factura        |       Fecha          |   Subtotal      |  IGV            |  Total    
            ============================================================================================
        """)
        for i in records:
            print(f"""
                {i[0]}       \t|      {i[1]}      \t|     {i[2]}  \t|  {i[3]}  \t|  {i[4]} 
            """)