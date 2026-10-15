def bubble_sort(vetor):
  tamanho = len(vetor)
  for i in range(tamanho - 1):
    trocou = False
    for j in range(tamanho - 1 - i):
      if vetor[j] > vetor[j + 1]:
        vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
        trocou = True
    if not trocou:
      break
  return vetor


def insertion_sort(vetor):
  for i in range(1, len(vetor)):
    chave = vetor[i]
    j = i - 1
    while j >= 0 and vetor[j] > chave:
      vetor[j + 1] = vetor[j]
      j -= 1
    vetor[j + 1] = chave
  return vetor


def selection_sort(vetor):
  tamanho = len(vetor)
  for i in range(tamanho - 1):
    indice_menor = i
    for j in range(i + 1, tamanho):
      if vetor[j] < vetor[indice_menor]:
        indice_menor = j
    if indice_menor != i:
      vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
  return vetor


def busca_binaria(vetor, alvo): # vetor deve estar ordenado
  inicio, fim = 0, len(vetor) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if vetor[meio] == alvo:
      return meio
    elif vetor[meio] < alvo:
      inicio = meio + 1
    else:
      fim = meio - 1
  return -1

