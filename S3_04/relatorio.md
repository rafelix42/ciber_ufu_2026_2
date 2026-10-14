# Relatório: Análise de Algoritmos e Notação Assintótica

## 1. Introdução

A **análise de algoritmos** estima quanto recurso (principalmente tempo e memória) um algoritmo consome em função do **tamanho da entrada `n`**. O tempo exato em segundos depende da máquina, da linguagem e do compilador. Por isso, contamos **operações básicas** (comparações, atribuições, acessos à memória) e observamos como esse número **cresce** quando `n` aumenta.

Esse crescimento é chamado de **comportamento assintótico**: interessa o que acontece para valores grandes de `n`, quando constantes e termos de menor ordem deixam de importar.

> Exemplo: se um algoritmo executa `T(n) = 3n² + 5n + 20` operações, para `n` grande o termo `3n²` domina. Descartando constantes, dizemos que ele é **O(n²)**.

---

## 2. Notação Big-O

**Definição:** `f(n) = O(g(n))` se existem constantes `c > 0` e `n₀` tais que

```
f(n) ≤ c · g(n)   para todo n ≥ n₀
```

Ou seja, a partir de certo ponto, `f` cresce **no máximo** tão rápido quanto `g` (limite superior).

Notações relacionadas:

| Notação | Significado | Interpretação |
|---|---|---|
| **O(g)** | Limite superior | "cresce no máximo como g" |
| **Ω(g)** | Limite inferior | "cresce no mínimo como g" |
| **Θ(g)** | Limite justo | "cresce exatamente como g" (O e Ω ao mesmo tempo) |

**Regras práticas de simplificação:**
1. Descartar constantes multiplicativas: `O(5n) = O(n)`.
2. Manter apenas o termo dominante: `O(n² + n) = O(n²)`.
3. Laços sequenciais **somam**: `O(n) + O(n) = O(n)`.
4. Laços aninhados **multiplicam**: `O(n) · O(n) = O(n²)`.
5. A base do logaritmo é irrelevante: `O(log₂ n) = O(log₁₀ n)`, pois diferem por uma constante.

---

## 3. Melhor caso, caso médio e pior caso

Para um mesmo `n`, o custo pode variar conforme a **disposição dos dados**:

- **Melhor caso:** a entrada mais favorável (ex.: o elemento buscado está na primeira posição).
- **Caso médio:** custo esperado considerando todas as entradas possíveis (exige hipótese sobre a distribuição dos dados).
- **Pior caso:** a entrada mais desfavorável. É o mais usado na prática, pois oferece uma **garantia**: o algoritmo nunca será mais lento que isso.

---

## 4. Análise dos algoritmos estudados

### 4.1 Acesso a elemento de vetor — O(1)

```python
def acessar(vetor, i):
    return vetor[i]
```

**Justificativa:** o endereço de `vetor[i]` é calculado diretamente (`base + i × tamanho_do_elemento`). Uma única operação, independentemente de o vetor ter 10 ou 10 milhões de elementos.

| Melhor | Médio | Pior |
|---|---|---|
| O(1) | O(1) | O(1) |

Outros exemplos O(1): empilhar/desempilhar, consulta média em tabela hash.

---

### 4.2 Busca binária — O(log n)

```python
def busca_binaria(vetor, alvo):      # vetor ORDENADO
    ini, fim = 0, len(vetor) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if vetor[meio] == alvo:
            return meio
        elif vetor[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1
```

**Justificativa:** a cada iteração o intervalo de busca é **dividido pela metade**: `n → n/2 → n/4 → … → 1`. O número de divisões até chegar a 1 é `k` tal que `n / 2ᵏ = 1`, ou seja, `k = log₂ n`. Para `n = 1.000.000`, bastam cerca de **20 comparações**.

| Melhor | Médio | Pior |
|---|---|---|
| O(1) — alvo no meio | O(log n) | O(log n) |

**Pré-requisito:** o vetor precisa estar ordenado.

---

### 4.3 Busca linear (sequencial) — O(n)

```python
def busca_linear(vetor, alvo):
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            return i
    return -1
```

**Justificativa:** no pior caso (alvo no fim ou ausente), percorre os `n` elementos. No caso médio, examina cerca de `n/2` elementos — e `n/2` ainda é O(n), pois a constante ½ é descartada.

| Melhor | Médio | Pior |
|---|---|---|
| O(1) — alvo na 1ª posição | O(n) | O(n) |

Outros exemplos O(n): soma de elementos, encontrar máximo/mínimo, percorrer lista encadeada.

---

### 4.4 Merge Sort — O(n log n)

```python
def merge_sort(v):
    if len(v) <= 1:
        return v
    meio = len(v) // 2
    esq = merge_sort(v[:meio])
    dir = merge_sort(v[meio:])
    return intercalar(esq, dir)      # O(n)

def intercalar(a, b):
    res, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    return res + a[i:] + b[j:]
```

**Justificativa:** recorrência `T(n) = 2T(n/2) + O(n)`.
- O vetor é dividido ao meio repetidamente → **log₂ n níveis** de recursão.
- Em cada nível, a intercalação processa ao todo **n elementos** → O(n) por nível.
- Total: `n × log n` = **O(n log n)**.

| Melhor | Médio | Pior |
|---|---|---|
| O(n log n) | O(n log n) | O(n log n) |

Observação: o **Quick Sort** também é O(n log n) no caso médio, mas O(n²) no pior caso (pivô sempre ruim). O(n log n) é o limite inferior para ordenação baseada em comparações.

---

### 4.5 Bubble Sort — O(n²)

```python
def bubble_sort(v):
    n = len(v)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocou = True
        if not trocou:      # já ordenado: encerra
            break
    return v
```

**Justificativa:** dois laços aninhados. O número de comparações no pior caso é

```
(n-1) + (n-2) + … + 1 = n(n-1)/2 = (n² - n)/2  →  O(n²)
```

Com a otimização da flag `trocou`, se o vetor já estiver ordenado, basta **uma passada** → melhor caso O(n).

| Melhor | Médio | Pior |
|---|---|---|
| O(n) — já ordenado | O(n²) | O(n²) — ordem inversa |

Outros exemplos O(n²): Selection Sort, Insertion Sort (pior caso), comparar todos os pares de um conjunto.

---

### 4.6 Fibonacci recursivo ingênuo — O(2ⁿ)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Justificativa:** cada chamada gera **duas** novas chamadas, formando uma árvore binária de profundidade ≈ `n`. O número de chamadas cresce aproximadamente como `2ⁿ` (mais precisamente ~1,618ⁿ, mas O(2ⁿ) é um limite superior válido). O mesmo subproblema é recalculado muitas vezes: `fib(50)` exigiria dezenas de bilhões de chamadas.

| Melhor | Médio | Pior |
|---|---|---|
| O(2ⁿ) | O(2ⁿ) | O(2ⁿ) |

**Solução eficiente para o mesmo problema** (programação dinâmica / iterativa):

```python
def fib_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

Complexidade **O(n)** de tempo e **O(1)** de memória — de exponencial para linear apenas evitando recálculos.

Outros exemplos exponenciais: gerar todos os subconjuntos de um conjunto, resolver o problema da mochila por força bruta.

---

## 5. Tabela comparativa das classes assintóticas

### 5.1 Resumo das classes

| Classe | Nome | Exemplo típico | Comportamento ao dobrar `n` |
|---|---|---|---|
| **O(1)** | Constante | Acesso a vetor por índice | Não muda |
| **O(log n)** | Logarítmica | Busca binária | Aumenta +1 passo |
| **O(n)** | Linear | Busca linear | Dobra |
| **O(n log n)** | Linearítmica | Merge Sort | Um pouco mais que dobra |
| **O(n²)** | Quadrática | Bubble Sort | Quadruplica |
| **O(2ⁿ)** | Exponencial | Fibonacci recursivo | Eleva ao quadrado |

Ordem de crescimento: `O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)`

### 5.2 Número aproximado de operações

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|---|---|---|---|---|---|
| 10 | 1 | 3 | 10 | 33 | 100 | 1.024 |
| 100 | 1 | 7 | 100 | 664 | 10.000 | ≈ 1,3 × 10³⁰ |
| 1.000 | 1 | 10 | 1.000 | ≈ 10.000 | 1.000.000 | ≈ 10³⁰¹ |
| 1.000.000 | 1 | 20 | 10⁶ | ≈ 2 × 10⁷ | 10¹² | inviável |

### 5.3 Tempo estimado (computador com 10⁹ operações/segundo)

| n | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|---|---|---|---|---|
| 10 | instantâneo | instantâneo | instantâneo | instantâneo | ≈ 1 µs |
| 100 | instantâneo | instantâneo | instantâneo | 10 µs | ≈ 4 × 10¹³ anos |
| 1.000.000 | instantâneo | 1 ms | ≈ 0,02 s | ≈ 17 minutos | — |
| 10⁹ | instantâneo | 1 s | ≈ 30 s | ≈ 32 anos | — |

---

## 6. Comparação de soluções para um mesmo problema

| Problema | Solução A | Solução B | Ganho |
|---|---|---|---|
| Buscar elemento em vetor ordenado | Busca linear — O(n) | Busca binária — O(log n) | 1 milhão de elementos: 10⁶ → 20 comparações |
| Ordenar vetor | Bubble Sort — O(n²) | Merge Sort — O(n log n) | 1 milhão de elementos: ~17 min → ~0,02 s |
| Calcular Fibonacci(n) | Recursivo — O(2ⁿ) | Iterativo — O(n) | n = 50: bilhões de chamadas → 50 iterações |
| Verificar duplicatas | Comparar todos os pares — O(n²) | Usar conjunto/hash — O(n) médio | Troca memória extra por tempo |

**Ponto importante:** para entradas **pequenas**, algoritmos "piores" podem ser mais rápidos, porque têm constantes menores e código mais simples (por isso bibliotecas usam Insertion Sort em subvetores pequenos). A notação assintótica descreve o comportamento para `n` grande.

---

## 7. Impacto da complexidade na escalabilidade

**Escalabilidade** é a capacidade de um sistema continuar eficiente quando o volume de dados cresce. A complexidade determina diretamente esse limite:

- **O(1) e O(log n):** escalam praticamente sem limites. Base de índices de bancos de dados (árvores B) e tabelas hash.
- **O(n):** escala bem; o custo cresce na mesma proporção dos dados.
- **O(n log n):** escala bem; é o padrão aceitável para ordenação e muitos problemas de processamento de dados.
- **O(n²):** funciona para milhares de elementos, mas torna-se proibitivo em milhões. Um sistema que leva 1 s com 10 mil registros levará ~2,8 horas com 1 milhão.
- **O(2ⁿ):** inviável a partir de poucas dezenas de elementos. Cada elemento a mais **dobra** o tempo.

**Hardware não resolve complexidade ruim:** um computador 1.000× mais rápido permite processar, no mesmo tempo:

| Classe | Aumento do tamanho de entrada tratável |
|---|---|
| O(n) | 1.000× maior |
| O(n²) | ≈ 32× maior (√1000) |
| O(2ⁿ) | apenas ≈ +10 elementos (log₂ 1000) |

Ou seja, **escolher um algoritmo melhor vale mais do que comprar uma máquina mais rápida**.

---

## 8. Conclusão

A notação Big-O permite comparar algoritmos de forma independente de máquina, focando em como o custo cresce com a entrada. Os algoritmos analisados mostram que um mesmo problema pode ter soluções com custos radicalmente diferentes: busca linear O(n) versus busca binária O(log n); Bubble Sort O(n²) versus Merge Sort O(n log n); Fibonacci recursivo O(2ⁿ) versus iterativo O(n). Para sistemas que precisam lidar com grandes volumes de dados, identificar e reduzir a classe de complexidade é a decisão de maior impacto no desempenho — muito maior que otimizações pontuais ou melhorias de hardware.