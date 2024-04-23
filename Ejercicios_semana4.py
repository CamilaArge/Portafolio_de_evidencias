salario= input("Ingrese su salario: ")
salario= float(salario)

if salario < 1000:
    salario = salario * 1.05

print("Su salario es: ", salario)
    
salario= input("Ingrese su salario: ")
salario= float(salario)

if salario >= 1000:
    salario = salario * 1.15
    print("Su salario aplicando un 15%: ", salario)
else:
     salario = salario * 1.20
     print("Su salario aplicando un 20%: ", salario)
          
        
print ("ejercicio 3")
salario = input("Ingrese su salario: ")
salario = float(salario)
categoria = input("Ingrese la categoria: ")
categoria = int(categoria)  

if categoria == 1:  
    aumento = salario * 0.10
    salario += aumento
    print("Su salario es:", salario)
elif categoria == 2:
    aumento = salario * 0.12
    salario += aumento
    print("Su salario es:", salario)
elif categoria == 3:
    aumento = salario * 0.15
    salario += aumento
    print("Su salario es:", salario)
elif categoria == 4:
    aumento = salario * 0.20
    salario += aumento
    print("Su salario es:", salario)

print ("ejercicio 1")
num1 = input("Ingrese un numero: ")
num2 = input("Ingrese un numero: ")
num3 = input("Ingrese un numero: ")
num4 = input("Ingrese un numero: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

if num1>num2 and num1> num3 and num1>num3:  
    print("El numero mayor es el:", num1)
elif num2>num3 and num2> num4 :  
    print("El numero mayor es el:", num2)
elif num3>num4  :  
    print("El numero mayor es el:", num3)
else:
    print("El numero mayor es:", num4)

print ("ejercicio 2")
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("Los números ordenados de forma descendente son:", num1, num2, num3)
    else:
        print("Los números ordenados de forma descendente son:", num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("Los números ordenados de forma descendente son:", num2, num1, num3)
    else:
        print("Los números ordenados de forma descendente son:", num2, num3, num1)
else:
    if num1 >= num2:
        print("Los números ordenados de forma descendente son:", num3, num1, num2)
    else:
        print("Los números ordenados de forma descendente son:", num3, num2, num1)


print ("ejercicio 3")
an = int(input("Ingrese su año de nacimiento: "))
an= int(an)

if an % 4 == 0:
    if an % 100 == 0:
        if an % 400 == 0:
            print("Su año de nacimiento es un año bisiesto")
    else:
        print("Su año de nacimiento es un año bisiesto")
else:
    print("Su año de nacimiento no es un año bisiesto.")












 

           
