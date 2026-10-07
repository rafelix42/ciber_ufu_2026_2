# def fatorial_recursivo(numero: int):
#     if numero == 1:
#         return numero
#     return numero * fatorial_recursivo((numero - 1))

def fatorial_iterativo(numero: int):
    total = numero
    while numero > 1:
        numero -= 1
        total = total * numero
    return total

fatorial_recursivo = lambda x: 1 if x == 1 else x * fatorial_recursivo(x - 1)

while True:
    print("0 - Sair  1 - Fatorial Recursivo  2 - Fatorial Iterativo  3 - Fibonacci")
    algoritmo = int(input("Selecione o algoritmo desejado: "))

    if(algoritmo == 0):
        break
    elif(algoritmo == 1):
        n = int(input("Digite o número que deseja calcular: "))
        print(f"Fatorial de {n}: {fatorial_recursivo(n)}")
    elif(algoritmo == 2):
        n = int(input("Digite o número que deseja calcular: "))
        print(f"Fatorial de {n}: {fatorial_iterativo(n)}")
    else:
        pass