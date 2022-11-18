#Calculadora ESA

# Adicionar 2 numeros
def add(x, y):
    return x + y

# Subtrair 2 numeros
def subtract(x, y):
    return x - y

# Multiplicar 2 numeros
def multiply(x, y):
    return x * y

# Dividir 2 numeros
def divide(x, y):
    return x / y

# Potencias
def potency(base, expoente):
    potencia = 1
    count = 1
    while count <= expoente:
        potencia *= base
        count +=1
    return potencia

# Percentagens
def percentage(value, percentage):
    return value * (percentage/100)

print("Selecione a operação: ")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")
print("5.Potência")
print("6.Percentagens")

while True:
    # Escolha
    choice = input("Escolha(1/2/3/4/5/6): ")

    # verifição da escolha
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Primeiro numero: "))
        num2 = float(input("Segundo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # verificar se utilizador quer executar mais calculos
        # parar o loop caso não queira
        # next_calculation = input("Executar mais cálculos? (s/n): ")
        # if next_calculation == "n":
        #    break

    elif choice == '5':
        base = float(input("Base: "))
        expoente = float(input("Expoente: "))
        print(base, "^", expoente, "=", potency(base, expoente))

        # verificar se utilizador quer executar mais calculos
        # parar o loop caso não queira
        # next_calculation = input("Executar mais cálculos? (s/n): ")
        # if next_calculation == "n":
        #    break


    elif choice == '6':
        valor = float(input("Numero: "))
        percentagem = float(input("Percentagem:" ))
        print(percentagem, "% de", valor, " = ", percentage(valor, percentagem))

        # verificar se utilizador quer executar mais calculos
        # parar o loop caso não queira
        # next_calculation = input("Executar mais cálculos? (s/n): ")
        # if next_calculation == "n":
        #   break

    else:
        print("Input Inválido")

    # verificar se utilizador quer executar mais calculos
    # parar o loop caso não queira
    next_calculation = input("Executar mais cálculos? (s/n): ")
    if next_calculation == "n":
        break