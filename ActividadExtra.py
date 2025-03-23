import sys
acciones = [
"Salir",
"Agregar producto",
"Eliminar producto",
"Mostrar inventario",]
inventario = {}
respuesta = ""
print("--- inventario de productos ---")
print()
print(" puede realizar una de estas 4 acciones")
for accion in acciones:
    print(f". {accion} ")
#while en bucle para usarlo hasta que ingrese la palabra "salir"
while respuesta != "Salir":
    respuesta = input("ingrese una accion a realizar:")
#si la accion a realizar es valida, la realizo
    if respuesta in acciones:
#Elijo la accion que quiero hacer 
        if (respuesta == "Agregar producto" or  respuesta =="Eliminar producto"):
            producto = input("ingrese el nombre del producto:")

            if respuesta == "Agregar producto":
                if producto in inventario:
                    print("ya existe un producto con ese nombre: ")
                else:
                    cu_producto = input("ingrese la cantidad de unidades: ")
                    if(cu_producto.isnumeric()) and (int(cu_producto)>0):
                        cu_producto = int(cu_producto)
                        inventario[producto] = cu_producto
                    else:
                        print("no es una cantidad de unidades valida") 
            else: 
                if producto in inventario.keys():
                    inventario.pop(producto)
                    print(" Se elimino el producto: ",producto )
                else:
                    print("No existe este producto en el inventario")

        elif respuesta == "Mostrar inventario":
            print("........INVENTARIO.......")
            for produ, unidades in (inventario.items()):
                print(f"Producto : {produ} y quedan: {unidades}")

        elif respuesta == "Salir":
            sys.exit(1)
#termina la eleccion de que accion hacer
    else:
            print("comando no valido")
    
            