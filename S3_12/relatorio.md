# [S3_12] Erros Numéricos e Representação Computacional

---

## 1. Por que 0.1 + 0.2 ≠ 0.3

### Experimento

```python
from decimal import Decimal
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
print(Decimal(0.1)); print(Decimal(0.2)); print(Decimal(0.3)); print(Decimal(0.1 + 0.2))
print((0.1).hex(), (0.5).hex())
print((0.1 + 0.2) - 0.3, math.isclose(0.1 + 0.2, 0.3))
```

`Decimal(x)` mostra o valor **exato** que está guardado no float, sem arredondar na exibição.

### Resultado

```text
0.1 + 0.2        = 0.30000000000000004
0.1 + 0.2 == 0.3 : False
Decimal(0.1)     = 0.1000000000000000055511151231257827021181583404541015625
Decimal(0.2)     = 0.200000000000000011102230246251565404236316680908203125
Decimal(0.3)     = 0.299999999999999988897769753748434595763683319091796875
Decimal(0.1+0.2) = 0.3000000000000000444089209850062616169452667236328125
0.1.hex()        = 0x1.999999999999ap-4
0.5.hex()        = 0x1.0000000000000p-1
diferença        = 5.551115123125783e-17
isclose          : True
```

### Discussão

- Em binário, $0{,}1 = 0{,}0\overline{0011}_2$ é uma dízima periódica. A mantissa de 52 bits corta essa dízima, e o valor guardado fica um pouco **acima** de 0,1. O padrão `999...9a` na representação hexadecimal é exatamente o "999..." repetido, arredondado para cima no último dígito.
- O 0,2 também fica um pouco acima, e o 0,3 fica um pouco **abaixo**. A soma dos dois primeiros, arredondada, cai no float vizinho de 0,3, e não no mesmo float.
- A diferença é $5{,}55\times10^{-17}$, ou seja, meio épsilon de máquina em torno de 0,3: um único passo de arredondamento.
- Já 0,5 tem representação exata (`0x1.0p-1` $= 2^{-1}$). Só frações com denominador potência de 2 são exatas.
- **Conclusão:** o problema não está na soma. Os três números já entram aproximados, e `==` exige igualdade bit a bit.

---

## 2. Erro absoluto e erro relativo

$$E_{abs} = |x - \tilde x| \qquad E_{rel} = \frac{|x - \tilde x|}{|x|} \qquad \text{dígitos corretos} \approx -\log_{10} E_{rel}$$

### Experimento

```python
def erros(nome, exato, aprox):
    ea = abs(exato - aprox); er = ea / abs(exato)
    print(f"{nome:<28} Eabs = {ea:.3e}   Erel = {er:.3e}   dígitos ≈ {-math.log10(er):.1f}")

erros("pi ≈ 3.14", math.pi, 3.14)
erros("pi ≈ 22/7", math.pi, 22/7)
erros("pi ≈ 355/113", math.pi, 355/113)
erros("sqrt(2) ≈ 1.414", math.sqrt(2), 1.414)
# erro de armazenamento: compara o decimal exato com o float guardado
e98 = abs(Decimal("9.8") - Decimal(9.8))
erros("ponte 1000 m medida 999 m", 1000, 999)
erros("mesa 2 m medida 1 m", 2, 1)
```

### Resultado

```text
pi ≈ 3.14                    Eabs = 1.593e-03   Erel = 5.070e-04   dígitos ≈ 3.3
pi ≈ 22/7                    Eabs = 1.264e-03   Erel = 4.025e-04   dígitos ≈ 3.4
pi ≈ 355/113                 Eabs = 2.668e-07   Erel = 8.491e-08   dígitos ≈ 7.1
sqrt(2) ≈ 1.414              Eabs = 2.136e-04   Erel = 1.510e-04   dígitos ≈ 3.8
CVSS 9.8 armazenado          Eabs = 7.105e-16   Erel = 7.250e-17
0.1 armazenado               Eabs = 5.551e-18   Erel = 5.551e-17
Mesmo Eabs = 1, escalas diferentes:
ponte 1000 m medida 999 m    Eabs = 1.000e+00   Erel = 1.000e-03   dígitos ≈ 3.0
mesa 2 m medida 1 m          Eabs = 1.000e+00   Erel = 5.000e-01   dígitos ≈ 0.3
```

### Discussão

- **O erro absoluto depende da escala; o relativo não.** A ponte e a mesa têm o mesmo erro absoluto de 1 m, mas a medida da ponte tem 3 dígitos corretos e a da mesa não tem nem 1.
- A fração $355/113$ é uma aproximação de $\pi$ excepcional: 7 dígitos corretos com números pequenos.
- **Erro de armazenamento.** A nota CVSS 9,8 e o 0,1 têm erro absoluto bem diferente ($7\times10^{-16}$ e $6\times10^{-18}$), mas erro relativo quase igual, da ordem de $10^{-16}$. Isso confirma a propriedade central do IEEE 754: o **erro relativo** de representação é sempre no máximo $\varepsilon/2 \approx 1{,}1\times10^{-16}$, qualquer que seja a magnitude.
- Para o trabalho, o erro de armazenamento das notas CVSS é desprezível diante da própria incerteza do CVSS, que tem uma casa decimal.

---

## 3. Truncamento × arredondamento

### 3a. Os dois sentidos de "truncar" um número

```python
x = 2/3
tr = math.floor(x * 1e4) / 1e4      # corta (chopping)
ar = round(x, 4)                    # arredonda ao mais próximo
```

```text
truncado = 0.6666  erro = 6.67e-05
arredondado = 0.6667  erro = 3.33e-05
```

Cortar dígitos tem erro máximo de uma unidade na última casa; arredondar tem erro máximo de meia unidade. Por isso o IEEE 754 usa arredondamento ao mais próximo como padrão.

### 3b. Erro de truncamento do método: série de $e$

$$e = \sum_{k=0}^{\infty} \frac{1}{k!} \approx \sum_{k=0}^{N-1} \frac{1}{k!}$$

```python
for N in [2, 5, 10, 15, 20]:
    s = sum(1/math.factorial(k) for k in range(N))
    print(f"N = {N:2d}   aprox = {s:.16f}   erro = {abs(math.e - s):.3e}")
```

```text
N =  2   aprox = 2.0000000000000000   erro = 7.183e-01
N =  5   aprox = 2.7083333333333335   erro = 9.948e-03
N = 10   aprox = 2.7182815255731922   erro = 3.029e-07
N = 15   aprox = 2.7182818284582297   erro = 8.153e-13
N = 20   aprox = 2.7182818284590451   erro = 0.000e+00
```

O erro vem dos termos desprezados e cai rapidamente com $N$. A partir de cerca de 18 termos, o erro de truncamento fica menor que o de arredondamento, e o resultado coincide com `math.e` até o último bit. Mais termos não ajudam a partir daí.

### 3c. Os dois erros competindo: derivada numérica

$$f'(x) \approx \frac{f(x+h) - f(x)}{h}, \qquad f = \sin,\; x = 1,\; f'(1) = \cos 1$$

```python
for k in range(1, 16):
    h = 10.0**(-k)
    d = (math.sin(1+h) - math.sin(1)) / h
    print(f"h = 1e-{k:02d}   erro = {abs(d - math.cos(1)):.3e}")
```

```text
h = 1e-01   erro = 4.294e-02
h = 1e-02   erro = 4.216e-03
h = 1e-03   erro = 4.208e-04
h = 1e-04   erro = 4.207e-05
h = 1e-05   erro = 4.207e-06
h = 1e-06   erro = 4.207e-07
h = 1e-07   erro = 4.183e-08
h = 1e-08   erro = 2.970e-09     <- mínimo
h = 1e-09   erro = 5.254e-08
h = 1e-10   erro = 5.848e-08
h = 1e-11   erro = 1.169e-06
h = 1e-12   erro = 4.324e-05
h = 1e-13   erro = 7.339e-04
h = 1e-14   erro = 3.707e-03
h = 1e-15   erro = 1.481e-02
```

### Discussão

| | Truncamento | Arredondamento |
|---|---|---|
| Origem | o **método** troca algo infinito ou contínuo por algo finito | a **máquina** guarda só 52 bits de mantissa |
| Existiria com precisão infinita? | sim | não |
| Como reduzir | mais termos, $h$ menor, método de ordem maior | mais bits, reformular as contas, ordem das operações |
| Na derivada | proporcional a $h$ | proporcional a $\varepsilon / h$ |

- De $h = 10^{-1}$ até $10^{-7}$, o erro cai exatamente 10 vezes a cada passo: é o truncamento, proporcional a $h$, dominando.
- Abaixo de $h = 10^{-8}$, o erro **volta a crescer**. O numerador $\sin(1+h) - \sin(1)$ é uma subtração de números quase iguais, e o erro de arredondamento ($\approx \varepsilon/h$) passa a dominar.
- O ótimo fica em $h \approx \sqrt{\varepsilon} \approx 1{,}5\times10^{-8}$, exatamente onde o experimento achou o mínimo.
- **Lição:** "mais fino" nem sempre é "mais exato". O erro total é a soma dos dois, e existe um ponto de equilíbrio.

---

## 4. Efeitos da precisão limitada

### Experimento e resultado

```text
eps float64        = 2.220446049250313e-16
eps float32        = 1.1920929e-07
1 + eps/2 == 1     : True
1 + eps   == 1     : False
espaçamento em 1        = 2.220e-16
espaçamento em 1000     = 1.137e-13
espaçamento em 1e+08    = 1.490e-08
espaçamento em 1e+16    = 2.000e+00
2**53 + 1 == 2**53 (float): True
1/3 float32 = 0.33333334326744079590
1/3 float64 = 0.33333333333333331483
max * 10    = inf
5e-324 / 2  = 0.0
exp(1000)   = inf
int32 max + 1 = -2147483648
uint8 200 + 100 = 44
int Python 2**100 = 1267650600228229401496703205376
```

(Código: seção 4 de `experimentos.py`, usando `np.finfo`, `np.spacing`, `np.float32` e tipos inteiros do NumPy.)

### Discussão

- **Épsilon de máquina.** Somar a 1 qualquer valor menor que $\varepsilon/2$ não muda nada: o valor "some". O `float32` tem $\varepsilon \approx 10^{-7}$, cerca de 7 dígitos; o `float64` tem cerca de 16.
- **Espaçamento não uniforme.** A distância entre floats vizinhos cresce com a magnitude, mantendo o espaçamento relativo constante. Perto de $10^{16}$, os floats vizinhos estão a 2 unidades de distância, e por isso $2^{53} + 1$ não é representável.
- **Overflow e underflow.** Passar do máximo dá `inf`; ficar abaixo do menor subnormal dá `0.0`. Nenhum dos dois gera erro, o que é perigoso, porque o programa continua com um valor sem sentido.
- **Inteiros de tamanho fixo dão a volta.** `int32` passa de $+2\,147\,483\,647$ para $-2\,147\,483\,648$, e `uint8` calcula $300 \bmod 256 = 44$. Isso é a base da vulnerabilidade CWE-190 (overflow de inteiro): um tamanho de buffer calculado com estouro gera uma alocação pequena e, em seguida, escrita fora dos limites. O `int` nativo do Python não estoura, mas os arrays NumPy de tipo fixo sim.

---

## 5. Propagação de erros

### 5a. Acúmulo numa soma longa

```python
for N in [10, 1_000, 1_000_000]:
    s64 = 0.0
    for _ in range(N): s64 += 0.1                   # float64
    s32 = np.float32(0)
    for _ in range(N): s32 += np.float32(0.1)       # float32
    fs = math.fsum([0.1] * N)                       # soma compensada
```

```text
N =        10  exato = 1          laço f64 erro = 1.11e-16  laço f32 erro = 1.19e-07  fsum erro = 0.00e+00
N =      1000  exato = 100        laço f64 erro = 1.41e-12  laço f32 erro = 9.54e-04  fsum erro = 0.00e+00
N =   1000000  exato = 100000     laço f64 erro = 1.33e-06  laço f32 erro = 9.58e+02  fsum erro = 0.00e+00
```

Cada soma introduz um pequeno erro, e eles se acumulam com $N$. Em `float32`, com um milhão de parcelas, o erro chega a 958 sobre 100 000, ou seja, quase 1%. O `math.fsum` acompanha os bits perdidos e devolve o resultado correto.

### 5b. A soma não é associativa

```text
(1e16 + 1) - 1e16 = 0.0
(1e16 - 1e16) + 1 = 1.0
(0.1 + 0.2) + 0.3 = 0.6000000000000001
0.1 + (0.2 + 0.3) = 0.6
```

A ordem das operações muda o resultado. Somar o número pequeno a um número enorme faz o pequeno se perder antes que ele possa contar.

### 5c. Raiz 50 vezes, depois quadrado 50 vezes

```python
y = 2.0
for _ in range(50): y = math.sqrt(y)
for _ in range(50): y = y * y
```

```text
após 50 raízes    = 1.0000000000000004
após 50 quadrados = 1.6487212645509468 (deveria ser 2)
```

Matematicamente, as duas etapas se cancelam. Mas após 50 raízes, o valor exato é $2^{2^{-50}} \approx 1 + 6\times10^{-16}$, e só sobram 2 ou 3 bits de informação, porque o espaçamento perto de 1 é $2{,}2\times10^{-16}$. Elevar ao quadrado 50 vezes amplifica esse erro inicial por $2^{50}$. O resultado, 1,6487, é aproximadamente $e^{0{,}5}$, sem nenhuma relação com o 2 esperado.

### 5d. Cancelamento catastrófico

```text
x = 1e-02   ingênua = 0.4999958333   estável = 0.4999958333
x = 1e-04   ingênua = 0.4999999970   estável = 0.4999999996
x = 1e-06   ingênua = 0.5000444503   estável = 0.5000000000
x = 1e-08   ingênua = 0.0000000000   estável = 0.5000000000
Bhaskara ingênua = -7.4505805969e-09   estável = -1.0000000000e-08   erro rel ingênua = 25.5%
```

- A forma ingênua calcula $(1 - \cos x)/x^2$; a estável usa a identidade $1 - \cos x = 2\sin^2(x/2)$.
- Na fórmula de Bhaskara para $x^2 + 10^8x + 1 = 0$, a forma ingênua faz $-b + \sqrt{b^2 - 4ac}$, subtraindo dois números quase iguais. A forma estável usa $x = 2c / (-b - \sqrt{b^2-4ac})$, que não tem subtração.
- Ao subtrair números quase iguais, os dígitos corretos se cancelam e sobram só os contaminados. Em $x = 10^{-8}$, a forma ingênua erra 100%. **Matematicamente equivalente não significa numericamente equivalente.**

---

## 6. Análise numérica básica com NumPy

```python
fi = np.finfo(np.float64)
print(fi.eps, fi.max, fi.tiny, fi.precision)
print(np.nextafter(1.0, 2.0) - 1.0)
v = np.full(10_000_000, 0.1, dtype=np.float32)
print(np.sum(v), np.cumsum(v)[-1], np.sum(v.astype(np.float64)))
```

```text
float64: eps = 2.220446049250313e-16 | max = 1.7976931348623157e+308 | tiny = 2.2250738585072014e-308 | precision = 15 dígitos
nextafter(1, 2) - 1 = 2.220446049250313e-16
soma de 1e7 x 0.1 em float32 com np.sum (pairwise) = 1.0000001e+06  (exato 1e6)
mesma soma com np.cumsum (sequencial)            = 1.087937e+06
mesma soma em float64                             = 1000000.0149011612
```

### Discussão

- `np.finfo` e `np.nextafter` permitem inspecionar os limites do tipo em vez de decorá-los. `nextafter(1, 2) - 1` é, por definição, o épsilon.
- **O algoritmo importa tanto quanto a precisão.** Com os mesmos dados em `float32`:
  - `np.sum` usa **soma em pares** (pairwise), em que o erro cresce como $\log N$, e acerta 7 dígitos;
  - `np.cumsum` soma sequencialmente, com erro crescendo como $N$, e erra cerca de 9%.
- O resultado em `float64` não dá exatamente $10^6$, porque cada parcela é o `float32` mais próximo de 0,1, que vale cerca de $0{,}100000001$. Esse é o erro de **representação dos dados**, e nenhuma precisão de cálculo o elimina.

---

## 7. Comparação com == e com tolerância

### Critérios

- `math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)`: simétrico, $|a-b| \le \max(\text{rel\_tol}\cdot\max(|a|,|b|),\ \text{abs\_tol})$.
- `numpy.isclose(a, b, rtol=1e-5, atol=1e-8)`: assimétrico, $|a-b| \le \text{atol} + \text{rtol}\cdot|b|$.

### Resultado

```text
caso                     ==  math.isclose   math.isclose abs_tol=1e-9  np.isclose
0.1+0.2 vs 0.3        False          True                        True        True
1e-10 vs 0            False         False                        True        True
1e20+1e4 vs 1e20      False          True                        True        True
100.0 vs 100.001      False         False                       False        True
0.5+0.25 vs 0.75       True          True                        True        True
np.isclose(0, 1e-8, atol=0, rtol=1)    = True
np.isclose(1e-8, 0, atol=0, rtol=1)    = False
nan == nan = False | math.isnan = True
```

### Discussão

1. **`==` falha para resultados de contas**, como na linha 1. Ele só é confiável quando os valores são exatos, como na linha 5, em que 0,5, 0,25 e 0,75 são potências de 2.
2. **Comparar com zero exige tolerância absoluta** (linha 2). Uma tolerância relativa vezes zero dá zero, então `math.isclose(x, 0)` é `False` para todo $x \neq 0$. O `np.isclose` só acerta por causa do `atol=1e-8` padrão.
3. **Números grandes exigem tolerância relativa** (linha 3). Uma diferença de $10^4$ parece enorme, mas em $10^{20}$ ela representa só $10^{-16}$, o nível do épsilon.
4. **Os padrões do NumPy são frouxos** (linha 4). `rtol=1e-5` aceita uma diferença de 0,001 em 100, o que pode ser inaceitável. Em código sério, passe as tolerâncias explicitamente.
5. **O `np.isclose` é assimétrico:** trocar `a` e `b` pode mudar a resposta. O `math.isclose` é simétrico.
6. **`nan` não é igual a nada, nem a si mesmo.** Use `math.isnan` ou `np.isnan`.

| Situação | Comparação adequada |
|---|---|
| inteiros, IDs, contagens, flags | `==` |
| resultado de contas com float, comparado a outro valor não nulo | `math.isclose` com `rel_tol` |
| resultado comparado com **zero**, como o determinante | tolerância **absoluta**: `abs(x) < tol` ou `abs_tol` / `atol` |
| arrays inteiros, como $x \approx b + Ax$ | `np.allclose` com `rtol` e `atol` explícitos |

---

## 8. Determinante × número de condição

### 8a. Matriz quase singular

$$M_\delta = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta \end{bmatrix}, \qquad \det M_\delta = \delta$$

```text
d = 1e-02   det =  1.000e-02   cond = 4.020e+02
d = 1e-06   det =  1.000e-06   cond = 4.000e+06
d = 1e-10   det =  1.000e-10   cond = 4.000e+10
d = 1e-14   det =  9.992e-15   cond = 4.040e+14
d = 1e-16   det =  0.000e+00   cond = 5.962e+16
```

Aqui as duas medidas contam a mesma história: $\det = \delta$ e $\kappa \approx 4/\delta$. Com $\delta = 10^{-16}$, o $1 + \delta$ é arredondado para 1, e a matriz vira **exatamente** singular na máquina. Com $\delta = 10^{-14}$, o próprio determinante já sai com erro relativo de 0,1%.

### 8b. Onde o determinante engana

```text
0.001*I(10)                det = 1.000e-30   cond = 1.000e+00
1000*I(10)                 det = 1.000e+30   cond = 1.000e+00
[[1e6,1e6],[1e6,1e6+1]]    det = 1.000e+06   cond = 4.000e+06
```

- $0{,}001\,I$ tem determinante $10^{-30}$, "praticamente zero", mas é a matriz mais bem comportada que existe: $\kappa = 1$, e a inversa é $1000\,I$.
- A última matriz tem determinante $10^6$, "grande", mas é mal condicionada ($\kappa = 4\times10^6$), porque suas linhas são quase paralelas.

### Discussão: qual medida é mais informativa?

**O número de condição.** O motivo é que:
- o determinante depende da escala ($\det(cA) = c^n \det A$); multiplicar a matriz por uma constante muda o determinante sem mudar em nada a dificuldade do problema;
- o número de condição é invariante à escala ($\kappa(cA) = \kappa(A)$) e tem significado operacional: $\|\delta x\|/\|x\| \le \kappa\,\|\delta b\|/\|b\|$, e perdem-se cerca de $\log_{10}\kappa$ dígitos.

O determinante continua útil como **teste de singularidade exata**, com tolerância, e como critério teórico ($\det \neq 0 \iff$ invertível). Mas, sozinho, ele não diz se a solução é confiável.

---

## 9. solve × inv: resíduos

Para cada matriz, define-se $b = A\cdot\mathbf{1}$, de modo que a solução verdadeira é $x = (1, \dots, 1)$. Mede-se o **resíduo** $\|Ax - b\|$ e o **erro** $\|x - \mathbf{1}\|$.

```python
xs = np.linalg.solve(H, b)          # fatoração LU com pivotamento
xi = np.linalg.inv(H) @ b           # inversa explícita e produto
np.linalg.norm(H @ xs - b), np.linalg.norm(H @ xi - b)
```

### Resultado

```text
matriz               cond   res solve     res inv   err solve     err inv
Hilbert 6        1.50e+07    5.21e-16    2.84e-11    9.99e-11    2.38e-09
Hilbert 8        1.53e+10    6.57e-16    1.12e-07    1.91e-07    1.37e-06
Hilbert 10       1.60e+13    7.36e-16    1.62e-04    3.95e-05    7.68e-03
Hilbert 12       1.62e+16    5.98e-16    2.40e-01    4.47e-01    9.44e+00
Aleatória 1000x1000: cond = 2.38e+04
  solve: resíduo = 1.70e-11  erro = 5.75e-12  tempo = 26.9 ms
  inv  : resíduo = 6.94e-09  erro = 3.31e-10  tempo = 98.0 ms
```

### Discussão

- **O resíduo do `solve` fica no nível do épsilon** ($\sim10^{-16}$) mesmo para a Hilbert 12, com $\kappa \approx 10^{16}$. Isso porque o `solve` é **backward stable**: ele devolve a solução exata de um sistema ligeiramente perturbado.
- **O resíduo do `inv` cresce junto com o número de condição**, chegando a 0,24 na Hilbert 12, ou seja, cerca de $10^{15}$ vezes maior que o do `solve`.
- **O erro na solução** cresce para os dois métodos, porque o mau condicionamento é do **problema**: na Hilbert 12, nem o `solve` acerta. Ainda assim, o erro do `inv` é sistematicamente 10 a 200 vezes maior.
- **Custo:** na matriz 1000×1000, o `inv` levou cerca de 3,6 vezes mais tempo. Isso é coerente com a teoria: aproximadamente $2n^3$ operações, contra $\tfrac{2}{3}n^3$ do `solve`.
- **Resíduo pequeno não garante erro pequeno.** Na Hilbert 12, o `solve` tem resíduo $6\times10^{-16}$ e erro 0,45. A ponte entre os dois é o número de condição: $\text{erro relativo} \lesssim \kappa \times \text{resíduo relativo}$.

---

## 10. Análise numérica do sistema de risco do Trabalho 2

O modelo é $(I - A)\,x = b$, com os riscos próprios $b = (14{,}8;\; 12{,}5;\; 17{,}3)$.

A função de verificação usada nos experimentos:

```python
def verificar(C, tol_det=1e-12, cond_max=1e12):
    det = np.linalg.det(C); cond = np.linalg.cond(C)
    ok = abs(det) > tol_det and cond < cond_max
    return det, cond, ok
```

### 10.1 Cenário do trabalho (somas das linhas 0,5; 0,8; 0,5)

```text
det = np.float64(0.8)  | det == 0.8 ? True | isclose ? True
cond = 3.7088  -> perda ≈ 0.57 dígitos | aprovado: True
x (solve) = [33.21875 39.075   36.8375 ]
resíduo solve = 3.97e-15 | resíduo inv = 3.97e-15
x == b + A x (==)       : False
x ≈ b + A x (allclose)  : True
```

- O número de condição 3,7 indica que se perde menos de 1 dígito: a solução é totalmente confiável.
- O `det == 0.8` deu `True` **por sorte**. Já a checagem do resultado com `==` falhou, embora $x$ esteja correto até o 15º dígito. A comparação correta é com `np.allclose`.

### 10.2 Tolerância no determinante: varredura com a soma das linhas $s \to 1$

Rede uniforme de 3 equipamentos, em que cada um herda $s/2$ de cada outro:

```text
                 s      det(I-A)       cond  det==0  |det|<1e-12  cond>1e12  aprovado
 0.500000000000000     7.812e-01   2.50e+00   False        False      False      True
 0.900000000000000     2.102e-01   1.45e+01   False        False      False      True
 0.990000000000000     2.235e-02   1.49e+02   False        False      False      True
 0.999000000000000     2.249e-03   1.50e+03   False        False      False      True
 0.999999000000000     2.250e-06   1.50e+06   False        False      False      True
 0.999999999900000     2.250e-10   1.50e+10   False        False      False      True
 0.999999999999900     2.251e-13   1.50e+13   False         True       True     False
 0.999999999999999     2.165e-15   1.51e+15   False         True       True     False
 1.000000000000000     0.000e+00   4.68e+32    True         True       True     False
```

- **O teste `det == 0` só detecta o caso exato** $s = 1$. Com $s = 1 - 10^{-15}$, a matriz é numericamente inútil ($\kappa \approx 10^{15}$, sobra cerca de 1 dígito correto), mas `det == 0` diz que está tudo bem.
- O teste **com tolerância** e o teste do **número de condição** rejeitam corretamente os dois casos quase singulares.
- Nesse modelo, os dois testes concordam porque a diagonal de $I - A$ é sempre 1, o que mantém a escala fixa. Mesmo assim, o número de condição é o que traduz o problema em **dígitos perdidos**, e o determinante não.
- Repare que $\det \approx 2{,}25\,(1-s)$ e $\kappa \approx 1{,}5/(1-s)$: ambos são governados pela distância $1 - s$ até a singularidade.

### 10.3 Sensibilidade a perturbações nos dados

Perturbação de $\pm 0{,}05$ em cada nota, simulando o arredondamento do CVSS a uma casa decimal:

```text
       s      cond  ||db||/||b||  ||dx||/||x||  amplificação  limite cond*rel_b
     0.5       2.5      3.33e-03      1.69e-03           0.5           8.34e-03
     0.9      14.5      3.33e-03      1.14e-03           0.3           4.83e-02
    0.99     149.5      3.33e-03      1.12e-03           0.3           4.98e-01
   0.999    1499.5      3.33e-03      1.12e-03           0.3           5.00e+00
  0.9999   14999.5      3.33e-03      1.12e-03           0.3           5.00e+01
```

**Amplificação absoluta** $\|\delta x\|/\|\delta b\|$:

```text
       s   1/(1-s)  db alternado  db uniforme
     0.5         2           1.0          2.0
     0.9        10           3.4         10.0
    0.99       100          33.3        100.0
   0.999      1000         333.3       1000.0
```

**Sensibilidade a $A$**, com a dependência estimada com erro de 0,001:

```text
s = 0.999: x = [14866.622207 14865.088363 14868.28943 ]
s = 0.998: x = [7433.288859 7431.754503 7434.956638]
```

**Discussão:**
- O número de condição é um **limite de pior caso**. Para esse $b$, o erro **relativo** de $x$ ficou bem abaixo do limite. O motivo é que $b$ já aponta quase na direção $(1,1,1)$, que é a mais amplificada, e então $x$ inteiro cresce junto e o erro relativo não aumenta.
- O erro **absoluto**, porém, é amplificado exatamente por $1/(1-s)$ na direção uniforme. Com $s = 0{,}999$, uma incerteza de 0,05 nas notas vira uma incerteza de cerca de 50 no risco efetivo.
- O efeito mais grave vem de $A$: errar a fração de dependência em só 0,001 **divide o risco efetivo pela metade**. Perto de $s = 1$, o resultado do modelo deixa de refletir as vulnerabilidades e passa a refletir quase só a estimativa das dependências.
- **Implicação prática:** a regra "soma das linhas < 1" evita a singularidade, mas não o mau condicionamento. Vale a pena exibir o número de condição ao usuário, ou adotar uma margem no cadastro (por exemplo, soma ≤ 0,95, que dá $\kappa \lesssim 30$).

### 10.4 solve × inv no modelo de risco

```text
cenário                     cond   res solve     res inv
trabalho (3 equip.)     3.71e+00    3.97e-15    3.97e-15
uniforme s=0.99         1.49e+02    1.29e-13    1.85e-13
uniforme s=0.9999       1.50e+04    1.52e-11    1.52e-11
uniforme s=0.99999999   1.50e+08    1.28e-07    1.28e-07
aleatória 200 equip.    2.12e+01    1.57e-12    1.16e-12
```

- Nessas matrizes, os resíduos dos dois métodos são praticamente iguais. Isso é esperado: $I - A$ é estritamente diagonal dominante, uma classe de matrizes "benigna", em que até a inversa explícita se comporta bem. É diferente da Hilbert.
- **Ainda assim, `solve` é a escolha correta**, por três motivos:
  1. é cerca de 3 vezes mais barato, o que importa quando o inventário crescer para centenas ou milhares de equipamentos;
  2. nunca é pior, e é muito melhor quando a matriz é mal condicionada (seção 9);
  3. é o que o enunciado recomenda e o que reflete a boa prática.
- A inversa só tem uso para **interpretação**: $[(I-A)^{-1}]_{ij}$ é a contribuição do equipamento $j$ para o risco efetivo de $i$.

### 10.5 Caso singular ($s = 1$)

```text
det bruto = np.float64(0.0) | cond = 4.679e+32
solve -> LinAlgError: Singular matrix
posto(I-A) = 2 | posto([I-A|b]) = 3
```

- O `np.linalg.solve` lança `LinAlgError` só quando encontra um pivô **exatamente** nulo. Para matrizes quase singulares, ele devolve um resultado sem nenhum aviso. Por isso a aplicação precisa fazer a própria verificação antes de resolver, em vez de depender da exceção.
- Como $\text{posto}(I - A) < \text{posto}([I - A \mid b])$, o sistema é impossível, como mostrado à mão na lista anterior.

---

## 11. Conclusões e decisões de implementação

**Sobre erros numéricos:**
1. Floats representam a maioria dos decimais só aproximadamente. O erro relativo de cada representação ou operação é no máximo $\approx 1{,}1\times10^{-16}$, mas esses erros se **acumulam** (seção 5a) e podem ser **amplificados** (5c, 5d).
2. O truncamento vem do método; o arredondamento, da máquina. Os dois competem, e reduzir um pode aumentar o outro (seção 3c).
3. Fórmulas matematicamente equivalentes podem ter comportamentos numéricos muito diferentes: cancelamento, ordem das somas, soma pairwise contra sequencial.
4. `==` só serve para valores exatos. Para floats, use tolerância **relativa** em comparações gerais e **absoluta** em comparações com zero.

**Sobre o sistema de risco:**
5. O número de condição é a medida mais informativa de confiabilidade: não depende da escala e se traduz em dígitos perdidos. O determinante serve como teste de singularidade, **sempre com tolerância**.
6. `solve` é preferível a `inv`: é mais barato e nunca menos preciso.

**Decisões para o código do Trabalho 2:**

```python
TOL_DET = 1e-12        # tolerância absoluta para "det ≈ 0"
COND_MAX = 1e12        # acima disso, perde-se mais de 12 dos ~16 dígitos

def calcular_risco_efetivo(A, b):
    C = np.eye(len(A)) - A
    det, cond = np.linalg.det(C), np.linalg.cond(C)
    if abs(det) < TOL_DET or cond > COND_MAX:
        raise ValueError(f"I - A singular ou mal condicionada (det={det:.2e}, cond={cond:.2e})")
    x = np.linalg.solve(C, b)                         # nunca inv(C) @ b
    assert np.allclose(x, b + A @ x, rtol=1e-9, atol=1e-9)   # checagem do resíduo
    return x, cond
```

| Etapa | Medida |
|---|---|
| Cadastro | $0 \le A_{ij} < 1$, $A_{ii} = 0$, soma de cada linha < 1 (de preferência com margem, como ≤ 0,95) |
| Montagem | matrizes em `float64` (`dtype=float`); IDs e contagens em `int` do Python |
| Antes de resolver | `abs(det) < tol` **e** `cond > limite`, avisando o usuário |
| Resolução | `np.linalg.solve` |
| Verificação | `np.allclose(x, b + A @ x)` com tolerâncias explícitas |
| Exibição | arredondar a 2 casas e mostrar o número de condição como indicador de confiabilidade |
