   #Semana 11

def crearArchivo():
    file = open("datosCurso.txt", "w")
    print("El archivo está listo")
    file.close()

def agregarInfo():
    nombre = input("Digite el nombre: ")
    grupo = input("Digite el numero de grupo: ")
    calificacion = input("Digite la calificación: ")
    file = open("datosCurso.txt", "a")
    file.write(nombre)
    file.write("\n")
    file.write(grupo)
    file.write("\n\n")
    file.write(calificacion)
    file.write("\n")
    print("\nLa información fue grabada correctamente")
    file.close()

def mostrar_info():  
    file = open("datosCurso.txt", "r")
    mensaje = file.read()
    print(mensaje)
    file.close()

def menu_acciones():
    print("\nMenú:")
    print("1. Agregar")
    print("2. Mostrar")


    
    
while True:
    menu_acciones()
    opc = input("Seleccione una opción: ")

    if opc == "1":
        agregarInfo()
    elif opc == "2":
        mostrar_info()
         
        
           
    
