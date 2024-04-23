
#Ejercicio1
kilometros_por_dia = []

for dia in range(1, 8):
    kilometros = int(input(f"Ingrese los kilómetros recorridos el día {dia}: "))
    kilometros_por_dia.append(kilometros)


total_semana = sum(kilometros_por_dia)
for dia in range(len(kilometros_por_dia)):
    print("Día {dia + 1}: {kilometros_por_dia[dia]} kilómetros")

print(f"Total de la semana: {total_semana} kilómetros")

#Ejercicio2
butacas = [[] for _ in range(10)]  

butacas[0].append("Juan")
butacas[1].append("Lili Rojas")
butacas[2].append("Jhon Dar")
butacas[3].append("Robb Paz")
butacas[4].append("Ana Hernadez")
butacas[5].append("Lucia Cartin")
butacas[6].append("Pablo Calderon")
butacas[7].append("Dany Corona")
butacas[8].append("Karly Writ")
butacas[9].extend(["Emanuel Lopez", "Ema Davira"])
print(butacas)

#Ejercicio3
palabra = input("Ingrese una palabra: ")  
palabrareves = palabra[::-1]  

print("La palabra al revés es:", palabrareves)

#Ejercicio4
montos = []

for dia in range(1, 8):
    monto = int(input(f"Ingrese el monto del día {dia}: "))
    montos.append(monto)

total_semana = sum(montos)
dia_menos_ganancia = montos.index(min(montos)) + 1
menor_ganancia = min(montos)
for dia in range(len(montos)):
    print(f"Día {dia + 1}: {montos[dia]} ")
    
print("Total de la semana:", total_semana)
print("Menor ganacia es:", menor_ganancia)
