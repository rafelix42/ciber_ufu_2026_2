# [S3_11] Álgebra Linear III: Determinantes e Invertibilidade

---

## Exercício 1 — Determinante e inversa de uma matriz 2×2

$$A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$$

### 1.1 Determinante

$$\det A = ad - bc = 2\cdot 1 - 1\cdot 1 = 2 - 1 = 1$$

Como $\det A = 1 \neq 0$, a matriz é **invertível**.

### 1.2 Inversa pela fórmula 2×2

Troca-se a posição dos elementos da diagonal principal, troca-se o sinal dos elementos da diagonal secundária e divide-se pelo determinante:

$$A^{-1} = \frac{1}{\det A}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} = \frac{1}{1}\begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$$

### 1.3 Inversa por Gauss-Jordan (conferência)

Escalona-se $[\,A \mid I\,]$ até obter $[\,I \mid A^{-1}\,]$:

$$\left[\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{array}\right]
\xrightarrow{L_1 \leftrightarrow L_2}
\left[\begin{array}{cc|cc} 1 & 1 & 0 & 1 \\ 2 & 1 & 1 & 0 \end{array}\right]
\xrightarrow{L_2 \leftarrow L_2 - 2L_1}
\left[\begin{array}{cc|cc} 1 & 1 & 0 & 1 \\ 0 & -1 & 1 & -2 \end{array}\right]$$

$$\xrightarrow{L_2 \leftarrow -L_2}
\left[\begin{array}{cc|cc} 1 & 1 & 0 & 1 \\ 0 & 1 & -1 & 2 \end{array}\right]
\xrightarrow{L_1 \leftarrow L_1 - L_2}
\left[\begin{array}{cc|cc} 1 & 0 & 1 & -1 \\ 0 & 1 & -1 & 2 \end{array}\right]$$

O bloco da direita coincide com a inversa obtida em 1.2. ✓

### 1.4 Verificação: $A \cdot A^{-1} = I$

$$A\,A^{-1} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}
= \begin{bmatrix} 2\cdot1 + 1\cdot(-1) & 2\cdot(-1) + 1\cdot 2 \\ 1\cdot 1 + 1\cdot(-1) & 1\cdot(-1) + 1\cdot 2 \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I \;✓$$

Também vale $A^{-1}A = I$, conferido da mesma forma.

---

## Exercício 2 — Determinante 3×3 por Sarrus e por cofatores; comparação com uma matriz singular

### 2.1 Matriz invertível

$$B = \begin{bmatrix} 2 & 1 & 3 \\ 0 & -1 & 4 \\ 1 & 2 & 0 \end{bmatrix}$$

**Regra de Sarrus.** Repetem-se as duas primeiras colunas à direita:

$$\begin{array}{ccc|cc} 2 & 1 & 3 & 2 & 1 \\ 0 & -1 & 4 & 0 & -1 \\ 1 & 2 & 0 & 1 & 2 \end{array}$$

- Diagonais que descem: $2\cdot(-1)\cdot 0 + 1\cdot 4\cdot 1 + 3\cdot 0\cdot 2 = 0 + 4 + 0 = 4$
- Diagonais que sobem: $3\cdot(-1)\cdot 1 + 2\cdot 4\cdot 2 + 1\cdot 0\cdot 0 = -3 + 16 + 0 = 13$

$$\det B = 4 - 13 = -9$$

**Expansão por cofatores.** A linha 2 tem um zero, então é a escolha mais econômica. Os sinais da linha 2 são $(-, +, -)$:

$$\det B = -0\cdot\begin{vmatrix} 1 & 3 \\ 2 & 0 \end{vmatrix} + (-1)\cdot\begin{vmatrix} 2 & 3 \\ 1 & 0 \end{vmatrix} - 4\cdot\begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix}$$

$$= 0 + (-1)(0 - 3) - 4(4 - 1) = 3 - 12 = -9 \;✓$$

Os dois métodos concordam: $\det B = -9 \neq 0$, então $B$ é **invertível**.

**Inversa pela adjunta.** Cofatores $C_{ij} = (-1)^{i+j}\det(B_{ij})$:

| | $j=1$ | $j=2$ | $j=3$ |
|---|---|---|---|
| $i=1$ | $+(-1\cdot0 - 4\cdot2) = -8$ | $-(0\cdot0 - 4\cdot1) = 4$ | $+(0\cdot2 - (-1)\cdot1) = 1$ |
| $i=2$ | $-(1\cdot0 - 3\cdot2) = 6$ | $+(2\cdot0 - 3\cdot1) = -3$ | $-(2\cdot2 - 1\cdot1) = -3$ |
| $i=3$ | $+(1\cdot4 - 3\cdot(-1)) = 7$ | $-(2\cdot4 - 3\cdot0) = -8$ | $+(2\cdot(-1) - 1\cdot0) = -2$ |

A adjunta é a transposta da matriz dos cofatores:

$$\text{adj}(B) = \begin{bmatrix} -8 & 6 & 7 \\ 4 & -3 & -8 \\ 1 & -3 & -2 \end{bmatrix}
\qquad
B^{-1} = \frac{1}{-9}\,\text{adj}(B) = \frac{1}{9}\begin{bmatrix} 8 & -6 & -7 \\ -4 & 3 & 8 \\ -1 & 3 & 2 \end{bmatrix}$$

Conferência de uma entrada: linha 1 de $B$ vezes coluna 1 de $B^{-1}$ dá $\frac{1}{9}(2\cdot8 + 1\cdot(-4) + 3\cdot(-1)) = \frac{9}{9} = 1$. ✓

### 2.2 Matriz singular

$$S = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$

**Regra de Sarrus:**
- Diagonais que descem: $1\cdot5\cdot9 + 2\cdot6\cdot7 + 3\cdot4\cdot8 = 45 + 84 + 96 = 225$
- Diagonais que sobem: $3\cdot5\cdot7 + 1\cdot6\cdot8 + 2\cdot4\cdot9 = 105 + 48 + 72 = 225$

$$\det S = 225 - 225 = 0$$

**Expansão por cofatores, pela linha 1:**

$$\det S = 1\begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} - 2\begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} + 3\begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix} = 1(-3) - 2(-6) + 3(-3) = -3 + 12 - 9 = 0 \;✓$$

**Por que é singular.** As linhas estão em progressão aritmética: $L_1 - 2L_2 + L_3 = \mathbf{0}$. O mesmo vale para as colunas, então o vetor $(1, -2, 1)$ está no núcleo:

$$S\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 - 4 + 3 \\ 4 - 10 + 6 \\ 7 - 16 + 9 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

### 2.3 Comparação

| | $B$ | $S$ |
|---|---|---|
| Determinante | $-9$ | $0$ |
| Posto | 3 | 2 |
| Núcleo | $\{\mathbf{0}\}$ | $\text{span}\{(1,-2,1)\}$ |
| Inversa | existe | não existe |
| $M\mathbf{x} = \mathbf{b}$ | solução única para todo $\mathbf{b}$ | nenhuma ou infinitas soluções |
| Geometria | leva o espaço no espaço | achata o espaço num plano |

---

## Exercício 3 — Determinante como área (2×2) e volume (3×3)

### 3.1 Área em 2D

As colunas de uma matriz 2×2 formam um paralelogramo cuja área é $|\det|$.

**Para a matriz $A$ do Exercício 1,** as colunas são $\mathbf{u} = (2, 1)$ e $\mathbf{w} = (1, 1)$:

$$\text{Área} = |\det A| = |2\cdot1 - 1\cdot1| = 1$$

A transformação leva o quadrado unitário (área 1) num paralelogramo de mesma área. Ela **deforma, mas preserva a área**. Como $\det A > 0$, a orientação também é preservada.

**Contraexemplo singular:** $P = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}$ tem colunas $(2,1)$ e $(4,2) = 2\,(2,1)$, que são paralelas.

$$\text{Área} = |2\cdot2 - 4\cdot1| = 0$$

O "paralelogramo" degenera num segmento de reta: todo o plano é achatado numa reta, e por isso não há como desfazer a transformação.

### 3.2 Volume em 3D

As colunas de uma matriz 3×3 formam um paralelepípedo cujo volume é $|\det|$.

- **Para $B$:** $\text{Volume} = |-9| = 9$. A transformação multiplica volumes por 9. O sinal negativo indica que ela **inverte a orientação** (como um espelho combinado com uma deformação).
- **Para $S$:** $\text{Volume} = 0$. As três colunas estão num mesmo plano, então o paralelepípedo é "achatado" e não tem volume.

### 3.3 Resumo da interpretação

| $\det$ | Significado geométrico |
|---|---|
| $\lvert\det\rvert > 1$ | amplia áreas/volumes |
| $0 < \lvert\det\rvert < 1$ | reduz áreas/volumes |
| $\det < 0$ | inverte a orientação |
| $\det = 0$ | achata o espaço numa dimensão menor; sem inversa |

---

## Exercício 4 — Matriz de dependências que torna I − A singular

### 4.1 Construção

Para $I - A$ ser singular, basta que exista $\mathbf{x} \neq \mathbf{0}$ com $(I - A)\mathbf{x} = \mathbf{0}$, ou seja, $A\mathbf{x} = \mathbf{x}$. Escolhendo $\mathbf{x} = (1, 1, 1)$, a condição $A\mathbf{x} = \mathbf{x}$ significa que **cada linha de $A$ soma exatamente 1**.

Uma escolha com todos os pesos em $[0, 1)$ e $A_{ii} = 0$: três equipamentos que transmitem 50% do risco a cada um dos outros dois.

$$A = \begin{bmatrix} 0 & 0{,}5 & 0{,}5 \\ 0{,}5 & 0 & 0{,}5 \\ 0{,}5 & 0{,}5 & 0 \end{bmatrix}
\quad\Rightarrow\quad
I - A = \begin{bmatrix} 1 & -0{,}5 & -0{,}5 \\ -0{,}5 & 1 & -0{,}5 \\ -0{,}5 & -0{,}5 & 1 \end{bmatrix}$$

### 4.2 Verificação de que é singular

**Por Sarrus:**
- Descem: $1\cdot1\cdot1 + (-0{,}5)(-0{,}5)(-0{,}5) + (-0{,}5)(-0{,}5)(-0{,}5) = 1 - 0{,}125 - 0{,}125 = 0{,}75$
- Sobem: $(-0{,}5)\cdot1\cdot(-0{,}5) + 1\cdot(-0{,}5)(-0{,}5) + (-0{,}5)(-0{,}5)\cdot 1 = 0{,}25 + 0{,}25 + 0{,}25 = 0{,}75$

$$\det(I - A) = 0{,}75 - 0{,}75 = 0$$

**Pelo núcleo:** $(I - A)(1,1,1)^T = (1 - 0{,}5 - 0{,}5,\; \dots) = (0, 0, 0)$. ✓

### 4.3 O que acontece com o sistema

Com $b = (14{,}8;\; 12{,}5;\; 17{,}3)$, escalona-se $[\,I - A \mid b\,]$:

$$\left[\begin{array}{ccc|c} 1 & -0{,}5 & -0{,}5 & 14{,}8 \\ -0{,}5 & 1 & -0{,}5 & 12{,}5 \\ -0{,}5 & -0{,}5 & 1 & 17{,}3 \end{array}\right]
\xrightarrow[L_3 \leftarrow L_3 + 0{,}5L_1]{L_2 \leftarrow L_2 + 0{,}5L_1}
\left[\begin{array}{ccc|c} 1 & -0{,}5 & -0{,}5 & 14{,}8 \\ 0 & 0{,}75 & -0{,}75 & 19{,}9 \\ 0 & -0{,}75 & 0{,}75 & 24{,}7 \end{array}\right]$$

$$\xrightarrow{L_3 \leftarrow L_3 + L_2}
\left[\begin{array}{ccc|c} 1 & -0{,}5 & -0{,}5 & 14{,}8 \\ 0 & 0{,}75 & -0{,}75 & 19{,}9 \\ 0 & 0 & 0 & 44{,}6 \end{array}\right]$$

A última linha diz $0 = 44{,}6$: o sistema é **impossível (SI)**. Pelo critério de Rouché–Capelli, $\text{posto}(I - A) = 2 < 3 = \text{posto}([\,I - A \mid b\,])$.

**Observação.** Somando as três equações, o lado esquerdo dá zero, porque as colunas de $I - A$ somam zero. Logo, o sistema só teria solução se $b_1 + b_2 + b_3 = 0$. Como riscos próprios são não negativos e aqui somam 44,6, nesse modelo o sistema é **sempre impossível** para dados reais.

### 4.4 Interpretação no modelo de risco

- Cada equipamento repassa 100% do risco que recebe para os outros, **sem nenhuma perda**. O risco circula indefinidamente pelo ciclo e cresce sem limite.
- Não existe um risco efetivo finito: a equação $x = b + Ax$ não tem solução.
- A aplicação **não deve tentar resolver** o sistema. Deve informar o usuário de que a configuração de dependências é inconsistente (item b do requisito 4).
- Repare que nenhum peso individual viola $[0, 1)$. O problema está na **soma** de cada linha, e é por isso que a regra de cadastro precisa olhar a linha inteira, não cada peso isolado.

**Curiosidade:** com só dois equipamentos e pesos em $[0, 1)$, $I - A$ nunca é singular, pois $\det(I - A) = 1 - A_{12}A_{21} > 0$. A singularidade exige redes com três ou mais equipamentos.

### 4.5 Cenário vizinho: quase singular

Trocando 0,5 por 0,495, as linhas passam a somar 0,99. Agora $I - A$ é EDD e invertível, mas para $b = (1, 1, 1)$:

$$(I - A)\,b = 0{,}01\,b \quad\Rightarrow\quad x = 100\,b = (100;\; 100;\; 100)$$

O risco efetivo fica 100 vezes o próprio. Quanto mais as somas se aproximam de 1, mais o risco "explode" — o sintoma numérico da proximidade da singularidade.

---

## Exercício 5 — Soma das linhas < 1 implica I − A estritamente diagonal dominante

### 5.1 Enunciado

Seja $A \in \mathbb{R}^{n\times n}$ com $A_{ii} = 0$, $A_{ij} \in [0, 1)$ e $\sum_j A_{ij} < 1$ para toda linha $i$. Então $I - A$ é estritamente diagonal dominante (EDD) e, portanto, invertível.

### 5.2 Demonstração de que I − A é EDD

Os elementos de $C = I - A$ são:
- na diagonal: $C_{ii} = 1 - A_{ii} = 1$;
- fora da diagonal: $C_{ij} = -A_{ij}$, com $|C_{ij}| = A_{ij}$, porque $A_{ij} \ge 0$.

A condição EDD exige, para cada linha $i$:

$$|C_{ii}| > \sum_{j \neq i} |C_{ij}| \iff 1 > \sum_{j\neq i} A_{ij} = \sum_{j} A_{ij}$$

(a última igualdade usa $A_{ii} = 0$). Essa é exatamente a hipótese, então $I - A$ é EDD. ∎

### 5.3 Por que EDD garante invertibilidade

**Teorema (Lévy–Desplanques):** toda matriz EDD é invertível.

**Demonstração por contradição:**
1. Suponha que $C\mathbf{x} = \mathbf{0}$ para algum $\mathbf{x} \neq \mathbf{0}$.
2. Escolha o índice $k$ em que $|x_k|$ é máximo. Então $|x_k| > 0$ e $|x_j| \le |x_k|$ para todo $j$.
3. A $k$-ésima equação dá $C_{kk}x_k = -\sum_{j\neq k} C_{kj}x_j$.
4. Tomando módulos e usando a desigualdade triangular:
$$|C_{kk}|\,|x_k| \le \sum_{j\neq k}|C_{kj}|\,|x_j| \le \Big(\sum_{j\neq k}|C_{kj}|\Big)|x_k| < |C_{kk}|\,|x_k|$$
5. Obtivemos $|C_{kk}||x_k| < |C_{kk}||x_k|$, o que é impossível.

Logo, $\ker(C) = \{\mathbf{0}\}$. Para matriz quadrada, núcleo trivial equivale a $\det C \neq 0$, ou seja, $C$ é invertível, e $(I - A)\mathbf{x} = \mathbf{b}$ tem **solução única para qualquer $\mathbf{b}$**. ∎

### 5.4 Consequências para o Trabalho 2

- A regra "soma de cada linha de $A$ < 1" pode ser imposta **no cadastro das dependências**. Com ela, o sistema sempre tem solução, para qualquer conjunto de vulnerabilidades.
- O critério é **suficiente, mas não necessário**: há matrizes invertíveis que não são EDD (por exemplo, $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, com $\det = -2$). Por isso, mesmo com a regra, a aplicação mantém a checagem numérica de $\det$ e do número de condição antes de resolver.
- O Exercício 4 mostra o caso limite: com somas iguais a 1, a desigualdade estrita falha e $I - A$ deixa de ser invertível.

### 5.5 Aplicação ao cenário invertível

$$A = \begin{bmatrix} 0 & 0 & 0{,}5 \\ 0{,}8 & 0 & 0 \\ 0 & 0{,}5 & 0 \end{bmatrix}
\qquad
I - A = \begin{bmatrix} 1 & 0 & -0{,}5 \\ -0{,}8 & 1 & 0 \\ 0 & -0{,}5 & 1 \end{bmatrix}$$

**Checagem EDD, linha a linha:**

| Linha | Soma em $A$ | Diagonal de $I - A$ | Soma dos módulos fora da diagonal | EDD? |
|---|---|---|---|---|
| 1 | 0,5 | 1 | 0,5 | $1 > 0{,}5$ ✓ |
| 2 | 0,8 | 1 | 0,8 | $1 > 0{,}8$ ✓ |
| 3 | 0,5 | 1 | 0,5 | $1 > 0{,}5$ ✓ |

**Determinante por Sarrus:**
- Descem: $1\cdot1\cdot1 + 0\cdot0\cdot0 + (-0{,}5)(-0{,}8)(-0{,}5) = 1 - 0{,}2 = 0{,}8$
- Sobem: $(-0{,}5)\cdot1\cdot0 + 1\cdot0\cdot(-0{,}5) + 0\cdot(-0{,}8)\cdot1 = 0$

$$\det(I - A) = 0{,}8 - 0 = 0{,}8 \neq 0 \;✓$$

**Determinante por cofatores, pela linha 1:**

$$\det(I - A) = 1\begin{vmatrix} 1 & 0 \\ -0{,}5 & 1 \end{vmatrix} - 0 + (-0{,}5)\begin{vmatrix} -0{,}8 & 1 \\ 0 & -0{,}5 \end{vmatrix} = 1\cdot 1 + (-0{,}5)(0{,}4) = 0{,}8 \;✓$$

**Inversa pela adjunta:**

$$\text{adj}(I - A) = \begin{bmatrix} 1 & 0{,}25 & 0{,}5 \\ 0{,}8 & 1 & 0{,}4 \\ 0{,}4 & 0{,}5 & 1 \end{bmatrix}
\qquad
(I - A)^{-1} = \frac{1}{0{,}8}\,\text{adj} = \begin{bmatrix} 1{,}25 & 0{,}3125 & 0{,}625 \\ 1 & 1{,}25 & 0{,}5 \\ 0{,}5 & 0{,}625 & 1{,}25 \end{bmatrix}$$

**Risco efetivo** $x = (I - A)^{-1} b$, com $b = (14{,}8;\; 12{,}5;\; 17{,}3)$:
- $x_1 = 1{,}25(14{,}8) + 0{,}3125(12{,}5) + 0{,}625(17{,}3) = 18{,}5 + 3{,}90625 + 10{,}8125 = 33{,}21875$
- $x_2 = 1(14{,}8) + 1{,}25(12{,}5) + 0{,}5(17{,}3) = 14{,}8 + 15{,}625 + 8{,}65 = 39{,}075$
- $x_3 = 0{,}5(14{,}8) + 0{,}625(12{,}5) + 1{,}25(17{,}3) = 7{,}4 + 7{,}8125 + 21{,}625 = 36{,}8375$

| Equipamento | Risco próprio $b_i$ | Risco efetivo $x_i$ |
|---|---|---|
| E1 | 14,8 | 33,22 |
| E2 | 12,5 | 39,08 |
| E3 | 17,3 | 36,84 |

E2 tem o menor risco próprio, mas o maior risco efetivo, porque herda 80% do risco de E1.

---

## Exercício 6 — Conferência com NumPy

### 6.1 Código

```python
import numpy as np

np.set_printoptions(precision=4, suppress=True)

def titulo(t):
    print(f"\n=== {t} ===")

# 1) Matriz 2x2
titulo("Exercício 1 — A = [[2,1],[1,1]]")
A2 = np.array([[2, 1], [1, 1]], dtype=float)
A2inv = np.linalg.inv(A2)
print("det(A) =", round(np.linalg.det(A2), 10))
print("inv(A) =\n", A2inv)
print("A @ inv(A) =\n", A2 @ A2inv)
print("É a identidade?", np.allclose(A2 @ A2inv, np.eye(2)))

# 2) Matriz 3x3 invertível e matriz singular
titulo("Exercício 2 — B (invertível) e S (singular)")
B = np.array([[2, 1, 3], [0, -1, 4], [1, 2, 0]], dtype=float)
S = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print("det(B) =", round(np.linalg.det(B), 10))
print("inv(B) =\n", np.linalg.inv(B))
print("inv(B) * 9 =\n", np.linalg.inv(B) * 9)
print("B @ inv(B) = I ?", np.allclose(B @ np.linalg.inv(B), np.eye(3)))
print("det(S) bruto =", np.linalg.det(S))
print("posto(S) =", np.linalg.matrix_rank(S))
print("S @ [1,-2,1] =", S @ np.array([1, -2, 1]))
print("cond(S) =", f"{np.linalg.cond(S):.3e}")

# 3) Área e volume
titulo("Exercício 3 — área e volume")
print("Área do paralelogramo de A =", abs(np.linalg.det(A2)))
P = np.array([[2, 4], [1, 2]], dtype=float)
print("Área do paralelogramo de P =", abs(round(np.linalg.det(P), 10)))
print("Volume do paralelepípedo de B =", abs(round(np.linalg.det(B), 10)))

# 4) e 5) Modelo de risco
b = np.array([14.8, 12.5, 17.3])

def analisar(nome, A, b, tol=1e-12, cond_max=1e12):
    titulo(nome)
    n = len(A)
    C = np.eye(n) - A
    somas = A.sum(axis=1)
    edd = all(abs(C[i, i]) > abs(C[i]).sum() - abs(C[i, i]) for i in range(n))
    det = np.linalg.det(C)
    cond = np.linalg.cond(C)
    print("Somas das linhas de A:", somas)
    print("I - A é EDD?", edd)
    print("det(I - A) =", det)
    print("cond(I - A) =", f"{cond:.3e}")
    if abs(det) < tol or cond > cond_max:
        print("=> I - A singular (ou numericamente singular): sistema NÃO resolvido.")
        print("   posto(I - A) =", np.linalg.matrix_rank(C),
              "| posto([I - A | b]) =", np.linalg.matrix_rank(np.column_stack([C, b])))
        return
    Cinv = np.linalg.inv(C)
    print("inv(I - A) =\n", Cinv)
    print("(I - A) @ inv(I - A) = I ?", np.allclose(C @ Cinv, np.eye(n)))
    x = np.linalg.solve(C, b)
    print("Risco próprio  b =", b)
    print("Risco efetivo  x =", x)
    print("Confere x = b + A x ?", np.allclose(x, b + A @ x))

A_ok = np.array([[0, 0, 0.5], [0.8, 0, 0], [0, 0.5, 0]])
A_sing = np.array([[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]])
analisar("Exercício 4/6 — Cenário 1 (invertível)", A_ok, b)
analisar("Exercício 4/6 — Cenário 2 (singular)", A_sing, b)

titulo("Extra — cenário quase singular (somas = 0,99)")
A_quase = np.full((3, 3), 0.495) - np.diag([0.495] * 3)
C = np.eye(3) - A_quase
print("det(I - A) =", round(np.linalg.det(C), 6), "| cond =", round(np.linalg.cond(C), 2))
print("x para b = [1,1,1]:", np.linalg.solve(C, np.ones(3)))
```

### 6.2 Saída obtida

```text
=== Exercício 1 — A = [[2,1],[1,1]] ===
det(A) = 1.0
inv(A) =
 [[ 1. -1.]
 [-1.  2.]]
A @ inv(A) =
 [[1. 0.]
 [0. 1.]]
É a identidade? True

=== Exercício 2 — B (invertível) e S (singular) ===
det(B) = -9.0
inv(B) =
 [[ 0.8889 -0.6667 -0.7778]
 [-0.4444  0.3333  0.8889]
 [-0.1111  0.3333  0.2222]]
inv(B) * 9 =
 [[ 8. -6. -7.]
 [-4.  3.  8.]
 [-1.  3.  2.]]
B @ inv(B) = I ? True
det(S) bruto = 0.0
posto(S) = 2
S @ [1,-2,1] = [0. 0. 0.]
cond(S) = 5.052e+16

=== Exercício 3 — área e volume ===
Área do paralelogramo de A = 1.0
Área do paralelogramo de P = 0.0
Volume do paralelepípedo de B = 9.0

=== Exercício 4/6 — Cenário 1 (invertível) ===
Somas das linhas de A: [0.5 0.8 0.5]
I - A é EDD? True
det(I - A) = 0.8
cond(I - A) = 3.709e+00
inv(I - A) =
 [[1.25   0.3125 0.625 ]
 [1.     1.25   0.5   ]
 [0.5    0.625  1.25  ]]
(I - A) @ inv(I - A) = I ? True
Risco próprio  b = [14.8 12.5 17.3]
Risco efetivo  x = [33.2188 39.075  36.8375]
Confere x = b + A x ? True

=== Exercício 4/6 — Cenário 2 (singular) ===
Somas das linhas de A: [1. 1. 1.]
I - A é EDD? False
det(I - A) = 0.0
cond(I - A) = 4.679e+32
=> I - A singular (ou numericamente singular): sistema NÃO resolvido.
   posto(I - A) = 2 | posto([I - A | b]) = 3

=== Extra — cenário quase singular (somas = 0,99) ===
det(I - A) = 0.02235 | cond = 149.5
x para b = [1,1,1]: [100. 100. 100.]
```

### 6.3 Comparação entre cálculo à mão e NumPy

| Item | À mão | NumPy | Confere? |
|---|---|---|---|
| $\det A$ (2×2) | 1 | 1.0 | ✓ |
| $A^{-1}$ | $\begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$ | `[[1,-1],[-1,2]]` | ✓ |
| $\det B$ | −9 | −9.0 | ✓ |
| $9\,B^{-1}$ | $\begin{bmatrix} 8 & -6 & -7 \\ -4 & 3 & 8 \\ -1 & 3 & 2 \end{bmatrix}$ | idem | ✓ |
| $\det S$ | 0 | 0.0 (posto 2) | ✓ |
| $\det(I - A)$, cenário 1 | 0,8 | 0.8 | ✓ |
| $(I - A)^{-1}$, cenário 1 | tabela da seção 5.5 | idem | ✓ |
| $x$, cenário 1 | (33,22; 39,08; 36,84) | (33.2188; 39.075; 36.8375) | ✓ |
| $\det(I - A)$, cenário 2 | 0 | 0.0 | ✓ |
| Classificação, cenário 2 | SI (linha $0 = 44{,}6$) | posto 2 < posto 3 | ✓ |

### 6.4 Observações sobre a parte numérica

- **Número de condição.** No cenário 1, $\text{cond}(I - A) \approx 3{,}7$: a solução é muito confiável (perde-se menos de um dígito de precisão). Em $S$ e no cenário 2, o número de condição é da ordem de $10^{16}$ a $10^{32}$, o sinal numérico de matriz singular.
- **Determinante com tolerância.** Aqui `det(S)` saiu exatamente `0.0`, mas isso é sorte do arredondamento. Em geral, um determinante teoricamente nulo sai como algo do tipo `6.66e-16`. Por isso o código compara `abs(det) < tol` em vez de `det == 0`.
- **`solve` em vez de `inv`.** A inversa foi calculada aqui só para conferir os cálculos à mão. Para obter o risco efetivo na aplicação, usa-se `np.linalg.solve`, que é mais rápido e mais preciso.
- **Checagem final.** A linha `Confere x = b + A x ? True` valida a solução diretamente na equação original do modelo.

---

## Conclusões

1. O determinante decide a invertibilidade: $\det \neq 0 \iff$ inversa existe $\iff$ $A\mathbf{x} = \mathbf{b}$ tem solução única.
2. Geometricamente, $|\det|$ é o fator de mudança de área ou volume; $\det = 0$ significa que o espaço foi achatado e a transformação não pode ser desfeita.
3. No modelo de risco, a regra **"soma de cada linha de $A$ < 1"** torna $I - A$ estritamente diagonal dominante e, portanto, sempre invertível. Ela deve ser imposta no cadastro das dependências.
4. Quando as somas chegam a 1, o risco circula sem perdas, $I - A$ fica singular e o sistema não tem solução. A aplicação deve detectar isso (determinante com tolerância e número de condição) e avisar o usuário em vez de resolver.
