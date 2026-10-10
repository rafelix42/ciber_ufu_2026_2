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
