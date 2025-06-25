usuarios = {}

def ingresar():

    contador_numeros = 0
    contador_letras = 0
    while True:
        nombre = input("Ingrese nombre: ")
        if nombre not in usuarios:
            usuarios["Nombre"]=nombre
        else:
            print("El usuario ya existe.")
            continue
        sexo = str(input("Ingrese su sexo (M o F): ")).upper()
        if sexo != "M" and sexo != "F":
            print("Ingrese solo usando M o F.")
            continue
        else:
            usuarios["Sexo"] =sexo
        contraseña = input("Ingrese contraseña: ")
        if len(contraseña) < 8:
            print("La contraseña debe tener minimo 8 caracteres")
            continue
        for i in contraseña:
            if i.isnumeric:
                contador_numeros +=1
            if i.isalpha:
                contador_letras +=1
        if contador_letras <1:
            print("La contraseña necesita al menos una letra.")
            return False
        elif contador_numeros <1:
            print("La contraseña necesita al menos un número.")
            return False
        elif contraseña.isspace == False:
            print("La contraseña no debe tener espacios en blanco.")
            return True
        else:
            usuarios["contraseña"]=contraseña
        print("Usuario ingresado exitosamente")
        return True
    

def buscar():
    buscado = input("Ingrese el usuario a buscar: ")
    for buscar in usuarios:
        if buscado == buscar["Nombre"]:
            print(f"{buscado["Nombre"]}")
        else:
            print("No se encontro el usuario.")
                

def eliminar():
    eliminado = input("Ingrese el usuario para eliminar: ")
    for i in usuarios:
        if i == eliminado:
            usuarios.pop(i)
            print("Usuario eliminado")
            return
        else:
            print("No esta registrado ese usuario.")


while True:

    print("1.Ingresar usuario.")
    print("2.Buscar usuario.")
    print("3.Eliminar usuario.")
    print("4.Salir.")

    opc = input("Ingrese una opción: ")

    if opc == "1":
        ing_usuario = ingresar()
     
    elif opc == "2":
        buscar_usuario = buscar()
    
    elif opc == "3":
        elim_usuario = eliminar()

    elif opc == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Ingrese una opción valida.")
        continue