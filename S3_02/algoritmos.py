import logging
import time
import tracemalloc
from functools import reduce

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# fatorial_recursivo = lambda x: 1 if x == 1 else x * fatorial_recursivo(x - 1)


def fatorial_iterativo(numero: int):
  tracemalloc.start()
  inicio = time.perf_counter()

  total = numero
  while numero > 1:
    numero -= 1
    total = total * numero

  tempo = time.perf_counter() - inicio
  _, pico = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  logging.info(f"Fatorial Iterativo -> tempo: {tempo * 1000:.4f} ms | memória (pico): {pico} bytes")
  return total


def fatorial_recursivo(numero: int):
  # A recursão fica numa função interna para medir o desempenho apenas uma vez, e não a cada chamada
  def calcular(x: int):
    if x == 1:
      return x
    return x * calcular(x - 1)

  tracemalloc.start()
  inicio = time.perf_counter()

  total = calcular(numero)

  tempo = time.perf_counter() - inicio
  _, pico = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  logging.info(f"Fatorial Recursivo -> tempo: {tempo * 1000:.4f} ms | memória (pico): {pico} bytes")
  return total


def fibonacci_sem_memoizacao(n: int):
  def calcular(x: int):
    if x < 2:
      return x
    return calcular(x - 1) + calcular(x - 2)

  tracemalloc.start()
  inicio = time.perf_counter()

  resultado = calcular(n)

  tempo = time.perf_counter() - inicio
  _, pico = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  logging.info(f"Fibonacci sem memoização -> tempo: {tempo * 1000:.4f} ms | memória (pico): {pico} bytes")
  return resultado


def fibonacci_com_memoizacao(n: int):
  def calcular(x: int, memo: dict):
    if x < 2:
      return x
    if x not in memo:
      memo[x] = calcular(x - 1, memo) + calcular(x - 2, memo)
    return memo[x]

  tracemalloc.start()
  inicio = time.perf_counter()

  resultado = calcular(n, {})

  tempo = time.perf_counter() - inicio
  _, pico = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  logging.info(f"Fibonacci com memoização -> tempo: {tempo * 1000:.4f} ms | memória (pico): {pico} bytes")
  return resultado


def sequencia_fib(n):
  return reduce(
    lambda acc, _: acc + [acc[-1] + acc[-2]],
    range(n - 2),
    [0, 1]
  )


while True:
  print("0 - Sair")
  print("1 - Fatorial Recursivo")
  print("2 - Fatorial Iterativo")
  print("3 - Fibonacci com memoização")
  print("4 - Fibonacci sem memoização")
  print("5 - Comparar todos")
  print("6 - Sequência de Fibonacci\n")

  algoritmo = int(input("Selecione o algoritmo desejado: "))

  if algoritmo == 1:
    n = int(input("Digite o número que deseja calcular: "))
    print(f"Fatorial de {n}: {fatorial_recursivo(n)}\n")
  elif algoritmo == 2:
    n = int(input("Digite o número que deseja calcular: "))
    print(f"Fatorial de {n}: {fatorial_iterativo(n)}\n")
  elif algoritmo == 3:
    n = int(input("Digite o número que deseja calcular: "))
    print(f"Fibonacci de {n}: {fibonacci_com_memoizacao(n)}\n")
  elif algoritmo == 4:
    n = int(input("Digite o número que deseja calcular: "))
    print(f"Fibonacci de {n}: {fibonacci_sem_memoizacao(n)}\n")
  elif algoritmo == 5:
    n = int(input("Digite o número que deseja calcular: "))
    fatorial_recursivo(n)
    fatorial_iterativo(n)
    fibonacci_com_memoizacao(n)
    if n <= 35:
      fibonacci_sem_memoizacao(n)
    else:
      logging.warning("Fibonacci sem memoização ignorado: para n > 35 demora demais")
    print()
  elif algoritmo == 6:
    n = int(input("Digite quantos números da sequência deseja calcular: "))
    print(f"Sequência de Fibonacci de {n} termos: {sequencia_fib(n)}\n")
  elif algoritmo == 0:
    break
  else:
    pass
