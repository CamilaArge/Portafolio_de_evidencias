#Ejercicio1
matriz = [["Pablo", "Suarez", "Psuarez"],
          ["Micaela", "Paz", "MicaPaz"],
          ["Damon", "Calderon", "DCald"]]

def agregar_persona(matriz, nombre, apellido, usuario):
    for fila in matriz:
        if nombre in fila:
            print("La persona ya existe")
            return

    matriz.append([nombre, apellido, usuario])
    print("Persona agregada.")

nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
usuario = input("Ingrese el usuario de la persona: ")

agregar_persona(matriz, nombre, apellido, usuario)

print("Matriz después de agregar la persona:")
for fila in matriz:
    print(fila)


#Ejercicio2
matriz = []

def agregar_calificacion(matriz, nombre, nota1, nota2, nota3, nota4):
    for fila in matriz:
        if nombre in fila:
            print("El estudiante ya existe")
            return
    matriz.append([nombre, nota1, nota2, nota3, nota4])
    print("Persona agregada.")

for fila in range(5):  
    nombre = input("Ingrese el nombre de la persona: ")
    nota1 = float(input("Ingrese la nota1: "))
    nota2 = float(input("Ingrese la nota2: "))
    nota3 = float(input("Ingrese la nota3: "))
    nota4 = float(input("Ingrese la nota4: "))
    agregar_calificacion(matriz, nombre, nota1, nota2, nota3, nota4)

print("Matriz:")
for fila in matriz:

#Ejercicio3
matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

print("Matriz inicial:")
for fila in matriz:
    print(fila)

fila = int(input("Ingrese la fila (0-4): "))
columna = int(input("Ingrese la columna (0-4): "))

if 0 <= fila <= 4 and 0 <= columna <= 4:
    if matriz[fila][columna] == 0:
        matriz[fila][columna] = 1
        print("Espacio reservado.")
    else:
        print("Ocupado.")
        
print("Matriz después de la reserva:")
for fila in matriz:
    print(fila)

















    
