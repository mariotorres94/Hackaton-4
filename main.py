"""
Crea una programa que permita registrar productos y generar un factura con el monto total, calculando el igv
(18% del monto total) , el subtotal la suma de todos los precios sin incluir IGV y el Total la suma total incluido
IGV.
Los productos contienen los atributos: nombre, precio
Para emitir una factura es necesario al menos un producto (pueden ser mas)
La Factura tiene como datos:
Nro factura, fecha de factura , igv y los productos asociados a esta.
El alumno tendrá que crear el mantenimiento de las entidades e ingresar al menos 6 productos como mínimo.
La factura se mostrará en el siguiente formato.
"""
from acciones import Acciones

menu = Acciones()
menu.menu()