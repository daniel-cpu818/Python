# calculadora_terminal.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def calculadora():
    print("Bienvenido a la Calculadora en Python")
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        operacion = input("Ingrese el número de la operación (1/2/3/4) o 'q' para salir: ")

        if operacion == 'q':
            print("Gracias por usar la calculadora.")
            break

        if operacion not in ['1', '2', '3', '4']:
            print("Operación no válida. Inténtelo de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor ingrese números válidos.")
            continue

        if operacion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif operacion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif operacion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif operacion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

if __name__ == "__main__":
    calculadora()
