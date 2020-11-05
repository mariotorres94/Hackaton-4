from productos import Productos
import datetime 
class Acciones(Productos):
    
    def menu(self):
        print("\n\tBienvenido al Sistema")
        print("\t--------------------")
        print("""
        1. Registro de Productos
        2. Salir
        """)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            self.registro_productos("")
        elif opcion == "2":
            print("Gracias Vuelva Pronto")
            exit()
        else:
            print("Opcion digitada no se encuentra, Vuelva a Intentarlo ...")

    def registro_productos(self, fecha):
        self.crear_tabla_producto()
        while True:
            cant_productos = int(input("Ingrese cantidad de productos a registrar: "))
            lista_productos = []
            subtotal = 0
            igv = 0.18
            if cant_productos > 0:
                for i in range(cant_productos):
                    while True:
                        try:
                            print(f"\n\tDatos del Producto {i+1}")
                            print("\t--------------------")
                            nombre = input("\n\tIngrese nombre de producto: ")
                            precio = float(input(f"\tIngrese precio de {nombre}: "))
                            descripcion = input(f"\tIngrese descripcion de {nombre}: ")

                            for i in nombre:
                                codigo = nombre[0]+nombre[1].upper()

                            datos_productos = {
                                "Nombre": nombre,
                                "Precio": precio,
                                "Descripcion": descripcion,
                                "Codigo": codigo
                            }                    
                            lista_productos.append(datos_productos)
                            self.ingresar_datos_productos(nombre,precio,descripcion,codigo)
                            break
                        except ValueError:
                            print("\nIngrese solo numeros, Vuelva a Intentarlo...")
                        finally:
                            pass
                for a in lista_productos:
                    subtotal += a['Precio']
                    total = (subtotal * igv) + subtotal
                self.registro_clientes(cant_productos,fecha, lista_productos, subtotal, igv, total)
                break
            else:
                print("Debe ingresar un producto a más, Intenten nuevamente ...")
            
                
    def registro_clientes(self, cant_productos,fecha, lista_productos, subtotal, igv, total):
        self.crear_tabla_clientes()
        while True:
            lista_clientes = []
            if cant_productos > 0:
                print("\n\tDatos de Cliente")
                print("\t-----------------")
                nombres = input("\tIngrese nombre de Cliente: ")
                apellidos = input("\tIngrese apellido de Cliente: ")
                dni = input("\tIngrese Documento de Identidad: ")

                datos_cliente = {
                    "Nombre": nombres,
                    "Apellido": apellidos,
                    "DNI": dni
                }
                lista_clientes.append(datos_cliente)
                print(lista_clientes)
                self.ingresar_clientes(nombres,apellidos,dni)
                self.ingresar_datos_facturas(cant_productos,fecha,lista_productos,subtotal,igv,total)
                break
            else:
                print("No puede registrar cliente, ya que no hay ningun producto registrado")

    def ingresar_datos_facturas(self,cant_productos,fecha,lista_productos,subtotal,igv,total):
        self.crear_tabla_facturas()
        lista_factura = []
        if cant_productos > 0:
            fecha = datetime.datetime.now()
            datos_factura = {
                "Fecha": fecha,
                "Subtotal": subtotal,
                "IGV": igv,
                "Total": total,
            }
            lista_factura.append(datos_factura)
            self.ingresar_datos_factura(fecha,subtotal,igv,total)
            self.emision_factura(cant_productos,fecha,lista_productos,subtotal,igv,total)
            

    def emision_factura(self, cant_productos,fecha, lista_productos, subtotal, igv, total):
        if cant_productos > 0:
            self.emitir_factura(fecha,subtotal,igv,total)
            """print("\n\tEmision Factura")
            print("\t---------------")
            for i in lista_productos:
                print("\n\tSubtotal      |      IGV        |     Total")
                print("\t-----------------------------------------------")
                print(f"\t{subtotal}                  {igv}            {total}")"""
        else:
            print("No se tiene ningun producto")
               








