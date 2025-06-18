lista_productos = []

#coigo debe tener 3 validacines:
#debe tener 5 caracteres, 2 mayusculas y al menos un número
opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
"Cambia las listar para crear el producto or un diccionario"
"Agregar una lista para almacenar los dicionarios de productos"
"Agregar un codigo al diccionario del producto"
"Modificar las funciones para que utilicen la nueva estructura de dicionario"

def validarcodigo(codigo):
 
    
    contador_mayusculas=0
    contador_números= 0
    for l in codigo:
        if l.isupper():
            contador_mayusculas +=1
        if l.isnumeric():
            contador_números +=1
    if contador_mayusculas <2:
        print("El codigo debe tener al menos 2 mayusculas.")
        return False
    elif contador_números==0:
        print("El codigo debe teer al menos un número.")
        return False
    elif len(codigo) <5:
        print("El codigo debe tener al menos 5 caracteres.")
        return False
    else:
        return True


def solicitarProducto():
        nombre=input("Ingrese el nombre del producto: ")
        while True:
            codigo = input("Ingrese el codigo del producto: ")
            if validarcodigo(codigo)== True:
                print("Codigo correcto.")
                break
            else:
                print("El codigo es incorreto, vuelva a ingresar.")
        try:
            stock=int(input("Ingrese el stock del producto: "))
            precio=int(input("Ingrese el precio del producto: "))
            
            if stock<0 or precio <0:
                raise ValueError
                
            else:
                producto=[nombre,precio,stock,codigo]
                return producto

        except ValueError:
            print("Debe ingresar valores enteros positivos")
    
def guardarProducto(nombre,precio,stock,codigo):
    productobuscado=buscarProducto(codigo)
    if productobuscado!=None:
         print("El proucto se encuentra en la lista.")
         return False
        
    producto = {"Nombre:":nombre,"Precio:":precio,"Cantidad:":stock,"Codigo:":codigo}
    lista_productos.append(producto)
    return True


   

def buscarProducto(codigo):
    for dictProducto in lista_productos:
        if codigo==dictProducto["Codigo"]:
            return dictProducto
    return None

def mostrarproducto(codigo):
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
        print("-"*60)
        print(f"Cod: {productoBuscado["Codigo"]}\tNombre: {productoBuscado["Nombre"]}\tPrecio: {productoBuscado["Precio"]}")
        print("-"*60)
    









while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    
            
   
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)
        case "3":


