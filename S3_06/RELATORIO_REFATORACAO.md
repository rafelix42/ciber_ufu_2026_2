# Relatório de Refatoração — `codigo_limpo.py`

Refatoração do módulo `codigo_limpo.py` (lista encadeada e fila) com o apoio de três ferramentas de qualidade de código para Python:

| Ferramenta | Versão | Papel |
|---|---|---|
| **black** | 26.10.1 | Formatador automático (reescreve o código num estilo padronizado) |
| **flake8** | 7.4.1 | Verificador de estilo PEP 8 (pycodestyle) e erros lógicos simples (pyflakes) |
| **pylint** | 4.1.3 | Analisador estático: convenções, docstrings, más práticas e nota de 0 a 10 |

Todas as ferramentas foram usadas com a configuração padrão (flake8 com limite de 79 colunas; black com limite de 88 colunas).

## 1. Resumo dos resultados

| Métrica | Antes | Depois |
|---|---|---|
| Avisos do flake8 | **59** (54 × E111, 5 × E501) | **0** |
| Nota do pylint | **0.00/10** | **10.00/10** |
| Avisos do pylint | 140 (125 × W0311 e mais 15 outros) | **0** |
| `black --check` | arquivo seria reformatado | arquivo já formatado |
| Comportamento | — | idêntico ao original (verificado) |

## 2. Diagnóstico inicial

### 2.1 flake8

```
$ flake8 codigo_limpo.py
codigo_limpo.py:5:3: E111 indentation is not a multiple of 4
codigo_limpo.py:5:80: E501 line too long (89 > 79 characters)
codigo_limpo.py:7:3: E111 indentation is not a multiple of 4
codigo_limpo.py:11:3: E111 indentation is not a multiple of 4
codigo_limpo.py:16:3: E111 indentation is not a multiple of 4
codigo_limpo.py:18:3: E111 indentation is not a multiple of 4
codigo_limpo.py:23:7: E111 indentation is not a multiple of 4
codigo_limpo.py:25:3: E111 indentation is not a multiple of 4
... (mais 46 ocorrências de E111)
codigo_limpo.py:5:80: E501 line too long (89 > 79 characters)
codigo_limpo.py:43:80: E501 line too long (81 > 79 characters)
codigo_limpo.py:81:80: E501 line too long (83 > 79 characters)
codigo_limpo.py:109:80: E501 line too long (85 > 79 characters)
codigo_limpo.py:132:80: E501 line too long (90 > 79 characters)
```

- **E111** (54 ocorrências): a indentação usava **2 espaços**; a PEP 8 pede **4**.
- **E501** (5 ocorrências): linhas com mais de 79 caracteres (docstrings e mensagens de erro).

### 2.2 pylint

```
$ pylint codigo_limpo.py
************* Module codigo_limpo
codigo_limpo.py:1:0: C0114: Missing module docstring (missing-module-docstring)
codigo_limpo.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
codigo_limpo.py:25:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:32:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:41:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:41:2: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
codigo_limpo.py:53:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:87:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:90:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:98:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:137:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:140:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:145:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:150:2: C0116: Missing function or method docstring (missing-function-docstring)
codigo_limpo.py:153:2: C0116: Missing function or method docstring (missing-function-docstring)
... (mais 125 avisos W0311 bad-indentation)

Your code has been rated at 0.00/10
```

- **W0311** (bad-indentation, 125 ocorrências): mesmo problema da indentação de 2 espaços. Ele sozinho derrubava a nota para 0.
- **C0114 / C0116**: faltavam a docstring do módulo e as de 11 métodos públicos.
- **R1710** (inconsistent-return-statements): `inserir_posicao` fazia `return self.inserir_inicio(valor)` em alguns caminhos (retornando `None` implicitamente) e terminava sem `return` em outro.
- **R0903** (too-few-public-methods): a classe `No` tem apenas um método público.

## 3. Etapas da refatoração

### Etapa 1 — `black` (automática)

```
$ black codigo_limpo.py
reformatted codigo_limpo.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

O black converteu toda a indentação para 4 espaços. Resultado parcial:

- flake8: 59 → 5 avisos (restaram apenas os E501).
- pylint: 0.00 → **8.76/10** (restaram docstrings, R1710 e R0903).

### Etapa 2 — correções manuais guiadas por flake8 e pylint

| Aviso | Correção aplicada |
|---|---|
| C0114 | Adicionada docstring do módulo. |
| C0116 | Adicionadas docstrings curtas em todos os métodos públicos de `ListaEncadeada` e `Fila`. |
| R1710 | `inserir_posicao` reescrito com `if / elif / else`, chamando `inserir_inicio`/`inserir_fim` sem `return`. Nenhum caminho retorna valor agora. |
| R0903 | Desativado só para a classe `No` (`# pylint: disable=too-few-public-methods`). Ela é um nó de dados e não precisa de mais métodos, então o aviso não se aplica. |
| E501 (docstrings) | Docstrings longas reescritas de forma mais concisa ou quebradas em várias linhas. |
| E501 (mensagens de erro) | O limite superior do intervalo foi para uma variável local `fim`, e a mensagem coube em 79 colunas. |
| E501 (`diagrama`) | A junção dos nós foi para uma variável (`nos` / `itens`) e o retorno virou uma f-string. |

> **Conflito black × flake8:** o black aceita linhas de até 88 colunas e o flake8 de até 79. Quebrar o `raise IndexError(...)` em várias linhas satisfazia o flake8, mas o black voltava a juntá-lo numa única linha de 87 colunas. Encurtar a linha com a variável `fim` fez as duas ferramentas concordarem sem mudar a configuração de nenhuma delas.

### Etapa 3 — verificação final

```
$ black --check codigo_limpo.py
All done! ✨ 🍰 ✨
1 file would be left unchanged.

$ flake8 codigo_limpo.py
(nenhuma saída — 0 avisos)

$ pylint codigo_limpo.py
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

**Comportamento preservado:** um script carregou as versões antiga e nova e executou nas duas a mesma sequência de operações (inserções em várias posições, remoção, busca, `in`, `obter`, inversão, `repr`, operações da fila e diagramas). As saídas foram idênticas. As mensagens de `IndexError` continuam com o mesmo texto.

## 4. Código antes

```python
from collections import deque


class No:
  """Unidade básica da estrutura encadeada: um valor e a referência para o próximo nó."""

  def __init__(self, valor, proximo=None):
    self.valor = valor
    self.proximo = proximo

  def __repr__(self):
    return f"No({self.valor!r})"


class ListaEncadeada:
  """Lista simplesmente encadeada com referências para cabeça e cauda."""

  def __init__(self, valores=None):
    self.cabeca = None
    self.cauda = None
    self._tamanho = 0
    for valor in valores or []:
      self.inserir_fim(valor)

  def inserir_inicio(self, valor):
    novo = No(valor, self.cabeca)
    self.cabeca = novo
    if self.cauda is None:
      self.cauda = novo
    self._tamanho += 1

  def inserir_fim(self, valor):
    novo = No(valor)
    if self.cauda is None:
      self.cabeca = self.cauda = novo
    else:
      self.cauda.proximo = novo
      self.cauda = novo
    self._tamanho += 1

  def inserir_posicao(self, indice: int, valor):
    if indice < 0 or indice > self._tamanho:
      raise IndexError(f"Índice {indice} fora do intervalo [0, {self._tamanho}]")
    if indice == 0:
      return self.inserir_inicio(valor)
    if indice == self._tamanho:
      return self.inserir_fim(valor)

    anterior = self._no_em(indice - 1)
    anterior.proximo = No(valor, anterior.proximo)
    self._tamanho += 1

  def remover_inicio(self):
    if self.cabeca is None:
      raise IndexError("Remoção em lista vazia")
    removido = self.cabeca
    self.cabeca = removido.proximo
    if self.cabeca is None:
      self.cauda = None
    self._tamanho -= 1
    return removido.valor

  def remover(self, valor):
    """Remove a primeira ocorrência de `valor`. Retorna True se removeu."""
    anterior = None
    atual = self.cabeca
    while atual is not None:
      if atual.valor == valor:
        if anterior is None:
          self.cabeca = atual.proximo
        else:
          anterior.proximo = atual.proximo
        if atual is self.cauda:
          self.cauda = anterior
        self._tamanho -= 1
        return True
      anterior, atual = atual, atual.proximo
    return False

  def buscar(self, valor) -> int:
    """Retorna o índice da primeira ocorrência de `valor`, ou -1 se não existir."""
    for indice, item in enumerate(self):
      if item == valor:
        return indice
    return -1

  def obter(self, indice: int):
    return self._no_em(indice).valor

  def inverter(self):
    anterior = None
    atual = self.cabeca
    self.cauda = atual
    while atual is not None:
      atual.proximo, anterior, atual = anterior, atual, atual.proximo
    self.cabeca = anterior

  def vazia(self) -> bool:
    return self._tamanho == 0

  def diagrama(self) -> str:
    """Representação visual dos nós e ponteiros."""
    if self.cabeca is None:
      return "cabeca -> None"
    return "cabeca -> " + " -> ".join(f"[{v}]" for v in self) + " -> None"

  def _no_em(self, indice: int) -> No:
    if indice < 0 or indice >= self._tamanho:
      raise IndexError(f"Índice {indice} fora do intervalo [0, {self._tamanho - 1}]")
    atual = self.cabeca
    for _ in range(indice):
      atual = atual.proximo
    return atual

  def __len__(self):
    return self._tamanho

  def __iter__(self):
    atual = self.cabeca
    while atual is not None:
      yield atual.valor
      atual = atual.proximo

  def __contains__(self, valor):
    return self.buscar(valor) != -1

  def __repr__(self):
    return f"ListaEncadeada({list(self)})"


class Fila:
  """Fila FIFO (primeiro a entrar, primeiro a sair) implementada com collections.deque."""

  def __init__(self):
    self._itens = deque()

  def enfileirar(self, valor):
    self._itens.append(valor)

  def desenfileirar(self):
    if not self._itens:
      raise IndexError("Desenfileirar de fila vazia")
    return self._itens.popleft()

  def espiar(self):
    if not self._itens:
      raise IndexError("Espiar fila vazia")
    return self._itens[0]

  def vazia(self) -> bool:
    return not self._itens

  def diagrama(self) -> str:
    if not self._itens:
      return "sai <- (vazia) <- entra"
    return "sai <- " + " | ".join(f"[{v}]" for v in self._itens) + " <- entra"

  def __len__(self):
    return len(self._itens)

  def __repr__(self):
    return f"Fila({self.diagrama()})"
```

## 5. Código depois

```python
"""Estruturas lineares: lista simplesmente encadeada e fila FIFO."""

from collections import deque


class No:  # pylint: disable=too-few-public-methods
    """Unidade básica da estrutura encadeada.

    Guarda um valor e a referência para o próximo nó.
    """

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __repr__(self):
        return f"No({self.valor!r})"


class ListaEncadeada:
    """Lista simplesmente encadeada com referências para cabeça e cauda."""

    def __init__(self, valores=None):
        self.cabeca = None
        self.cauda = None
        self._tamanho = 0
        for valor in valores or []:
            self.inserir_fim(valor)

    def inserir_inicio(self, valor):
        """Insere `valor` no início da lista em O(1)."""
        novo = No(valor, self.cabeca)
        self.cabeca = novo
        if self.cauda is None:
            self.cauda = novo
        self._tamanho += 1

    def inserir_fim(self, valor):
        """Insere `valor` no fim da lista em O(1), usando a cauda."""
        novo = No(valor)
        if self.cauda is None:
            self.cabeca = self.cauda = novo
        else:
            self.cauda.proximo = novo
            self.cauda = novo
        self._tamanho += 1

    def inserir_posicao(self, indice: int, valor):
        """Insere `valor` na posição `indice` (0 <= indice <= len)."""
        if indice < 0 or indice > self._tamanho:
            fim = self._tamanho
            raise IndexError(f"Índice {indice} fora do intervalo [0, {fim}]")
        if indice == 0:
            self.inserir_inicio(valor)
        elif indice == self._tamanho:
            self.inserir_fim(valor)
        else:
            anterior = self._no_em(indice - 1)
            anterior.proximo = No(valor, anterior.proximo)
            self._tamanho += 1

    def remover_inicio(self):
        """Remove e retorna o primeiro valor da lista."""
        if self.cabeca is None:
            raise IndexError("Remoção em lista vazia")
        removido = self.cabeca
        self.cabeca = removido.proximo
        if self.cabeca is None:
            self.cauda = None
        self._tamanho -= 1
        return removido.valor

    def remover(self, valor):
        """Remove a primeira ocorrência de `valor`. Retorna True se removeu."""
        anterior = None
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self.cauda:
                    self.cauda = anterior
                self._tamanho -= 1
                return True
            anterior, atual = atual, atual.proximo
        return False

    def buscar(self, valor) -> int:
        """Retorna o índice da primeira ocorrência de `valor`, ou -1."""
        for indice, item in enumerate(self):
            if item == valor:
                return indice
        return -1

    def obter(self, indice: int):
        """Retorna o valor armazenado na posição `indice`."""
        return self._no_em(indice).valor

    def inverter(self):
        """Inverte a lista no próprio lugar, ajustando cabeça e cauda."""
        anterior = None
        atual = self.cabeca
        self.cauda = atual
        while atual is not None:
            atual.proximo, anterior, atual = anterior, atual, atual.proximo
        self.cabeca = anterior

    def vazia(self) -> bool:
        """Indica se a lista não possui elementos."""
        return self._tamanho == 0

    def diagrama(self) -> str:
        """Representação visual dos nós e ponteiros."""
        if self.cabeca is None:
            return "cabeca -> None"
        nos = " -> ".join(f"[{v}]" for v in self)
        return f"cabeca -> {nos} -> None"

    def _no_em(self, indice: int) -> No:
        if indice < 0 or indice >= self._tamanho:
            fim = self._tamanho - 1
            raise IndexError(f"Índice {indice} fora do intervalo [0, {fim}]")
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual

    def __len__(self):
        return self._tamanho

    def __iter__(self):
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __contains__(self, valor):
        return self.buscar(valor) != -1

    def __repr__(self):
        return f"ListaEncadeada({list(self)})"


class Fila:
    """Fila FIFO (primeiro a entrar, primeiro a sair) baseada em deque."""

    def __init__(self):
        self._itens = deque()

    def enfileirar(self, valor):
        """Adiciona `valor` ao final da fila."""
        self._itens.append(valor)

    def desenfileirar(self):
        """Remove e retorna o valor do início da fila."""
        if not self._itens:
            raise IndexError("Desenfileirar de fila vazia")
        return self._itens.popleft()

    def espiar(self):
        """Retorna, sem remover, o valor do início da fila."""
        if not self._itens:
            raise IndexError("Espiar fila vazia")
        return self._itens[0]

    def vazia(self) -> bool:
        """Indica se a fila não possui elementos."""
        return not self._itens

    def diagrama(self) -> str:
        """Representação visual da fila, da saída para a entrada."""
        if not self._itens:
            return "sai <- (vazia) <- entra"
        itens = " | ".join(f"[{v}]" for v in self._itens)
        return f"sai <- {itens} <- entra"

    def __len__(self):
        return len(self._itens)

    def __repr__(self):
        return f"Fila({self.diagrama()})"
```

## 6. Principais diferenças (trechos)

**Indentação (black):** 2 → 4 espaços em todo o arquivo.

**`inserir_posicao` (R1710 + E501):**

```python
# Antes
  def inserir_posicao(self, indice: int, valor):
    if indice < 0 or indice > self._tamanho:
      raise IndexError(f"Índice {indice} fora do intervalo [0, {self._tamanho}]")
    if indice == 0:
      return self.inserir_inicio(valor)
    if indice == self._tamanho:
      return self.inserir_fim(valor)

    anterior = self._no_em(indice - 1)
    anterior.proximo = No(valor, anterior.proximo)
    self._tamanho += 1
```

```python
# Depois
    def inserir_posicao(self, indice: int, valor):
        """Insere `valor` na posição `indice` (0 <= indice <= len)."""
        if indice < 0 or indice > self._tamanho:
            fim = self._tamanho
            raise IndexError(f"Índice {indice} fora do intervalo [0, {fim}]")
        if indice == 0:
            self.inserir_inicio(valor)
        elif indice == self._tamanho:
            self.inserir_fim(valor)
        else:
            anterior = self._no_em(indice - 1)
            anterior.proximo = No(valor, anterior.proximo)
            self._tamanho += 1
```

**`diagrama` (E501 + legibilidade):**

```python
# Antes
    return "cabeca -> " + " -> ".join(f"[{v}]" for v in self) + " -> None"
```

```python
# Depois
        nos = " -> ".join(f"[{v}]" for v in self)
        return f"cabeca -> {nos} -> None"
```

## 7. Conclusão

O **black** resolveu a maior parte dos problemas, todos de formatação (indentação), com um único comando. O **flake8** e o **pylint** apontaram o que um formatador não corrige: linhas longas, falta de documentação e um padrão de retorno inconsistente. O código final passa nas três ferramentas sem nenhum aviso, tem nota 10/10 no pylint e mantém o comportamento original.
