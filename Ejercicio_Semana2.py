# Ejercicio 1
a= input("Ingrese el valor: ")
b= input("Ingrese el valor: ")
c= input("Ingrese el valor: ")
d= input("Ingrese el valor: ")

print(d, c, b, a)

#Ejercicio 2
edad= input("Ingrese su edad: ")
suma=5
edad= int(edad)
total= edad+suma

print ("Dentro de 5 años, tendra: ", total)

#Ejercicio 3
a= input("Ingrese el valor: ")
b= input("Ingrese el valor: ")
a = int(a)
b= int(b)
suma= a+b
suma= suma ** 2
suma= suma /3

print ("El resultado es: ", suma)

#Ejercicio 4
num= input("Ingrese un numero: ")
num= int(num)
cuadrado= num*num
cubo= num*num*num
print ("El resultado es: ", cuadrado)
print ("El resultado es: ", cubo)


#Ejercicio 5

base=4
altura=10
area= base*altura
perimetro= 2*base
perimetro1=2*altura
total= perimetro+perimetro1
print ("El resultado es: ", area)
print ("El resultado es: ", total)

#Ejercicio 6
distancia= input("Ingrese la distancia: ")
distancia= int(distancia)
costo= input("Ingrese el costo:")
dias= input("Ingrese los dias:")
costo= int(costo)
dias= int(dias)
total1=distancia*costo
total1=total1*2
total1=total1*dias
total1=total1
total=total1*15
print ("El resultado es: ", total)


#Ejercicio 7
edad1= input("Ingrese la edad1:")
edad2= input("Ingrese la edad2:")
edad3= input("Ingrese la edad3:")
edad4= input("Ingrese la edad4:")
edad5= input("Ingrese la edad5:")
edad1= int(edad1)
edad2= int(edad2)
edad3= int(edad3)
edad4= int(edad4)
edad5= int(edad5)
total= edad1+edad2+edad3+edad4+edad5
total= total/5
print ("El resultado es: ", total)

#Ejercicio 8
cantidadh = input("Ingrese la cantidad de horas semanales trabajadas: ")
precioxhora = input("Ingrese el precio por hora: ")
cantidadh = int(cantidadh)
precioxhora = int(precioxhora)
salario_semanal = cantidadh * precioxhora
salario_mensual = salario_semanal * 4.2
salario_mensual -= salario_mensual * 0.105
salario_mensual -= salario_mensual * 0.05

print("El resultado es:", salario_mensual)

#Ejercicio 9
ingresos = input("Ingrese la cantidad de ingresos: ")
gastos_alimentacion = input("Ingrese la cantidad de gastos mensuales en alimentación: ")
ingresos = int(ingresos)
gastos_alimentacion = int(gastos_alimentacion)
porcentaje_gasto_alimentacion = (gastos_alimentacion / ingresos) * 100
porcentaje_disponible = 100 - porcentaje_gasto_alimentacion
print("Porcentaje de gasto en alimentación: ", porcentaje_gasto_alimentacion, "%")
print("Porcentaje disponible para otros rubros: ", porcentaje_disponible, "%")






