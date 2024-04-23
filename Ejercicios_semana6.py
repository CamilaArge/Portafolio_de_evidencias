#Practica1
vueltas = 10
TiempoVueltas = [float(input("Ingrese el tiempo por vuelta : ") )           
for i in range (vueltas)]

pits = 10
Tiempopits = [float(input("Ingrese el tiempo por pits: "))
for i in range (pits)]
tiempopromediovuelta = sum(TiempoVueltas) / vueltas
tiempopromediopits = sum(Tiempopits) / pits

for i in range(vueltas):
    if TiempoVueltas[i] <= Tiempopits[i]:
        print("Error: El tiempo de vuelta debe ser mayor que el tiempo en los pits.")
else:
    porcentaje_pits_vueltas= [(Tiempopits[i] / TiempoVueltas[i]) * 100 for i in range(vueltas)]

print("Tiempo promedio por vuelta:", tiempopromediovuelta)
print("Tiempo promedio por pits: ", tiempopromediopits )
print("Porcentaje del tiempo: ", tiempopromediopits )

#Practica2
niños = int(input("Ingrese la cantidad de niños : "))
estaturas = [float(input("Ingrese las estaturas de los niños : ")) for i in range(niños)]  
menosde100 = 0
entre100y120 = 0
entre121y130 = 0
entre131y140 = 0
masde140 = 0


for estatura in estaturas:
    if estatura < 100:
        menosde100 += 1
    elif 100 <= estatura <= 120:
        entre100y120 += 1
    elif 121 <= estatura <= 130:
        entre121y130 += 1
    elif 131 <= estatura <= 140:
        entre131y140 += 1
    else:
        masde140 += 1

promedio = sum(estaturas) / niños
print("Cantidad de niños que miden menos de 100 cm:",  menosde100)
print("Cantidad de niños que miden entre 100 y 120 cm:", entre100y120)
print("Cantidad de niños que miden entre 121 y 130 cm:", entre121y130)
print("Cantidad de niños que miden entre 131 y 140 cm:", entre131y140)
print("Cantidad de niños que miden más de 140 cm:", masde140)
print("Promedio de estaturas:", promedio)

#Practica3
valor = input("Ingrese un valor entero: ")
valor = int(valor)
divisibles = [num for num in range(1, valor*11) if num % valor == 0]
print(f"Los primeros 10 números divisibles entre {valor} son:")
print(divisibles[:10])


#Practica4
total_salarios = 0  
cont = 0 

print("Ingrese los 15 salarios:")

while cont < 15:
    salario = float(input(f"Ingrese el salario {cont + 1}: "))
    total_salarios += max(0, 500 - salario)
    total_salarios = int(total_salarios)
    cont += 1

print(f"Se necesitan:", total_salarios, "en total para que al menos todos ganen $500.")





