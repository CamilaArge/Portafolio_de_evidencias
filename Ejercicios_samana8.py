
def dec_a_bin(num):
    binario = ""
    num = int(num)
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num //= 2
    return binario

num = input("Ingrese un número: ")
resultado = dec_a_bin(num)
print("El resultado es:", resultado)


def obtener_caracter_hexadecimal(valor):
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def deci_a_hexa(decimal):
    decimal = int(decimal)
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


num = int(input("Ingrese un número: "))
resultado = deci_a_hexa(num)
print("El resultado es:", resultado)

def deci_a_octa(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

num = int(input("Ingrese un número: "))
resultado = deci_a_octa(num)
print("El resultado es:", resultado)











