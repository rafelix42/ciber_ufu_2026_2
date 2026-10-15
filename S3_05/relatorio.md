# Relatório: Algoritmos de Busca e Ordenação

## 1. Introdução

Este relatório compara os algoritmos implementados em [`busca_ord.py`](busca_ord.py):

- **Ordenação:** Bubble Sort, Insertion Sort e Selection Sort.
- **Busca:** Busca Binária (comparada com a busca linear, vista no relatório anterior).

Em vez de medir tempo em segundos, que depende da máquina, contamos **operações básicas**:

- **Comparações:** quantas vezes dois elementos do vetor são comparados (`vetor[j] > vetor[j + 1]`, `vetor[j] > chave` etc.).
- **Trocas / movimentações:** quantas vezes elementos mudam de posição.
  - No Bubble e no Selection, cada troca é um `a, b = b, a`.
  - No Insertion, cada movimentação é um deslocamento `vetor[j + 1] = vetor[j]`.

---

## 2. Metodologia

Cada função foi copiada com contadores adicionados, sem mudar a lógica. Cada algoritmo foi executado com vetores de tamanho **n = 10, 100, 1.000 e 5.000**, em três situações:

| Caso | Entrada | Representa |
|---|---|---|
| **Ordenado** | `[0, 1, 2, …, n-1]` | Melhor caso para Bubble e Insertion |
| **Aleatório** | Valores distintos sorteados (média de 5 execuções) | Caso médio |
| **Inverso** | `[n, n-1, …, 1]` | Pior caso |

---

## 3. Algoritmos de ordenação

### 3.1 Bubble Sort

Percorre o vetor comparando pares vizinhos e trocando os que estão fora de ordem. Ao final de cada passada, o maior elemento restante "flutua" para o fim. A flag `trocou` encerra o algoritmo quando uma passada inteira não faz nenhuma troca.

### 3.2 Insertion Sort

Mantém o início do vetor ordenado. A cada passo, pega o próximo elemento (`chave`) e o desloca para a esquerda até encontrar sua posição, como quem organiza cartas na mão.

### 3.3 Selection Sort

A cada passada, procura o **menor** elemento da parte não ordenada e o coloca na posição `i` com **uma única troca**. Ele sempre percorre toda a parte restante, mesmo que o vetor já esteja ordenado.

---

## 4. Resultados

### 4.1 Número de comparações

| n | Caso | Bubble | Insertion | Selection |
|---:|---|---:|---:|---:|
| 10 | Ordenado | 9 | 9 | 45 |
| 10 | Aleatório | 43 | 30 | 45 |
| 10 | Inverso | 45 | 45 | 45 |
| 100 | Ordenado | 99 | 99 | 4.950 |
| 100 | Aleatório | 4.878 | 2.707 | 4.950 |
| 100 | Inverso | 4.950 | 4.950 | 4.950 |
| 1.000 | Ordenado | 999 | 999 | 499.500 |
| 1.000 | Aleatório | 498.106 | 254.014 | 499.500 |
| 1.000 | Inverso | 499.500 | 499.500 | 499.500 |
| 5.000 | Ordenado | 4.999 | 4.999 | 12.497.500 |
| 5.000 | Aleatório | 12.493.999 | 6.260.322 | 12.497.500 |
| 5.000 | Inverso | 12.497.500 | 12.497.500 | 12.497.500 |

### 4.2 Número de trocas / movimentações

| n | Caso | Bubble (trocas) | Insertion (deslocamentos) | Selection (trocas) |
|---:|---|---:|---:|---:|
| 10 | Ordenado | 0 | 0 | 0 |
| 10 | Aleatório | 25 | 23 | 7 |
| 10 | Inverso | 45 | 45 | 5 |
| 100 | Ordenado | 0 | 0 | 0 |
| 100 | Aleatório | 2.473 | 2.612 | 95 |
| 100 | Inverso | 4.950 | 4.950 | 50 |
| 1.000 | Ordenado | 0 | 0 | 0 |
| 1.000 | Aleatório | 245.601 | 253.021 | 995 |
| 1.000 | Inverso | 499.500 | 499.500 | 500 |
| 5.000 | Ordenado | 0 | 0 | 0 |
| 5.000 | Aleatório | 6.293.201 | 6.255.332 | 4.989 |
| 5.000 | Inverso | 12.497.500 | 12.497.500 | 2.500 |

### 4.3 Fórmulas que explicam os números

| Algoritmo | Comparações (melhor) | Comparações (médio) | Comparações (pior) | Trocas (pior) |
|---|---|---|---|---|
| Bubble | `n - 1` | ≈ `n²/2` | `n(n-1)/2` | `n(n-1)/2` |
| Insertion | `n - 1` | ≈ `n²/4` | `n(n-1)/2` | `n(n-1)/2` |
| Selection | `n(n-1)/2` | `n(n-1)/2` | `n(n-1)/2` | `n - 1` |

Por exemplo, para n = 1.000: `n(n-1)/2 = 1.000 × 999 / 2 = 499.500`, exatamente o valor medido no pior caso dos três algoritmos.

---

## 5. Análise

**Crescimento quadrático.** Quando `n` é multiplicado por 10 (de 100 para 1.000), as comparações no caso médio e no pior caso crescem cerca de **100 vezes** (de 4.950 para 499.500). Esse é o comportamento esperado de O(n²). De 1.000 para 5.000 (5×), o crescimento é de cerca de 25×.

**Entrada já ordenada.** Bubble (graças à flag `trocou`) e Insertion detectam a ordem em uma única passada: `n - 1` comparações e nenhuma troca, ou seja, **O(n)**. O Selection não tem como saber que o vetor já está ordenado e faz as mesmas 12,5 milhões de comparações para n = 5.000.

**Caso aleatório.** O Insertion faz cerca de **metade das comparações** do Bubble e do Selection (≈ n²/4 contra ≈ n²/2). Em média, cada elemento só precisa recuar metade da parte já ordenada antes de encontrar sua posição.

**Trocas.** O Selection faz no máximo `n - 1` trocas, enquanto Bubble e Insertion fazem uma troca ou deslocamento para cada par fora de ordem (inversão), o que dá até `n(n-1)/2`. Para n = 5.000 no pior caso, são **2.500 trocas contra 12,5 milhões**. Isso importa quando escrever na memória é caro, como em memória flash ou com registros grandes.

**Custo real de cada troca.** Um deslocamento do Insertion é **uma** atribuição. Uma troca do Bubble envolve **três** atribuições (com uma variável temporária implícita). Por isso, mesmo com contagens parecidas na tabela 4.2, o Insertion é na prática mais rápido que o Bubble.

---

## 6. Busca binária

A busca binária divide o intervalo pela metade a cada comparação. No pior caso (elemento ausente), ela faz no máximo `⌊log₂ n⌋ + 1` comparações:

| n | Busca linear (pior caso) | Busca binária (pior caso) |
|---:|---:|---:|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1.000 | 1.000 | 10 |
| 10.000 | 10.000 | 14 |
| 100.000 | 100.000 | 17 |
| 1.000.000 | 1.000.000 | 20 |

**Pré-requisito:** o vetor precisa estar ordenado. Ordenar com um dos algoritmos acima custa O(n²), o que só compensa se o vetor for consultado muitas vezes. Para uma única busca, a busca linear O(n) é mais barata.

---

## 7. Tabela comparativa

| Algoritmo | Complexidade (melhor / médio / pior) | Vantagens | Limitações |
|---|---|---|---|
| **Bubble Sort** | O(n) / O(n²) / O(n²) | • Muito simples de entender e implementar<br>• Com a flag `trocou`, detecta vetor ordenado em O(n)<br>• Estável (não inverte elementos iguais)<br>• In-place: memória extra O(1) | • O mais lento na prática: muitas comparações **e** muitas trocas<br>• Cada troca custa 3 atribuições<br>• Inviável para entradas grandes |
| **Insertion Sort** | O(n) / O(n²) / O(n²) | • Excelente para vetores pequenos ou **quase ordenados**<br>• No caso médio faz ~metade das comparações dos outros dois<br>• Estável e in-place<br>• *Online*: ordena conforme os dados chegam | • Pior caso (vetor inverso) ainda é O(n²)<br>• Muitos deslocamentos quando os dados estão muito desordenados |
| **Selection Sort** | O(n²) / O(n²) / O(n²) | • Número mínimo de trocas: no máximo `n - 1`<br>• Desempenho previsível (não depende da entrada)<br>• In-place | • Sempre O(n²) comparações, mesmo com o vetor já ordenado<br>• **Não é estável** (a troca à distância pode inverter elementos iguais)<br>• Não se beneficia de dados parcialmente ordenados |
| **Busca Binária** | O(1) / O(log n) / O(log n) | • Extremamente rápida: 20 comparações para 1 milhão de elementos<br>• Memória extra O(1) (versão iterativa) | • Exige vetor **ordenado**<br>• Exige acesso direto por índice (não funciona bem em lista encadeada)<br>• Manter o vetor ordenado após inserções tem custo |

---

## 8. Conclusão

Os três algoritmos de ordenação são O(n²) no pior caso. As contagens confirmam o valor exato `n(n-1)/2` de comparações para o vetor inverso. Mesmo assim, eles se comportam de forma bem diferente:

- O **Insertion Sort** é a melhor escolha geral entre os três: menos comparações no caso médio e O(n) para dados quase ordenados. Por isso ele é usado dentro de algoritmos híbridos como o Timsort (o `sorted()` do Python) para ordenar pequenos trechos.
- O **Selection Sort** só se destaca quando **trocas são caras**, pois faz no máximo `n - 1` trocas.
- O **Bubble Sort** tem valor principalmente didático.

Para entradas grandes, o caminho é usar algoritmos O(n log n), como Merge Sort ou Quick Sort. Para buscas repetidas, vale ordenar uma vez e usar a **busca binária**, que reduz 1.000.000 de comparações para 20.
