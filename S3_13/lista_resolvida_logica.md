# [S3_13] Lógica Proposicional e Argumentação

## Exercício 1 — Tabelas-verdade de proposições compostas

### 1a) $\neg p \lor (p \land q)$

| p | q | ¬p | p ∧ q | ¬p ∨ (p ∧ q) | p → q |
|---|---|---|---|---|---|
| V | V | F | V | **V** | V |
| V | F | F | F | **F** | F |
| F | V | V | F | **V** | V |
| F | F | V | F | **V** | V |

**Observação:** a coluna do resultado é idêntica à de $p \to q$. Logo, $\neg p \lor (p \land q) \equiv p \to q$. Por leis lógicas: $\neg p \lor (p \land q) \equiv (\neg p \lor p) \land (\neg p \lor q) \equiv V \land (\neg p \lor q) \equiv \neg p \lor q \equiv p \to q$.

### 1b) $(p \lor q) \to (p \land r)$ — três variáveis, $2^3 = 8$ linhas

| p | q | r | p ∨ q | p ∧ r | (p ∨ q) → (p ∧ r) |
|---|---|---|---|---|---|
| V | V | V | V | V | **V** |
| V | V | F | V | F | **F** |
| V | F | V | V | V | **V** |
| V | F | F | V | F | **F** |
| F | V | V | V | F | **F** |
| F | V | F | V | F | **F** |
| F | F | V | F | F | **V** |
| F | F | F | F | F | **V** |

**Leitura:** o condicional só é falso quando o antecedente $p \lor q$ é V e o consequente $p \land r$ é F. Isso acontece em 4 das 8 linhas, então a fórmula é uma **contingência**.

### 1c) $(p \to q) \leftrightarrow (q \to p)$

| p | q | p → q | q → p | (p → q) ↔ (q → p) |
|---|---|---|---|---|
| V | V | V | V | **V** |
| V | F | F | V | **F** |
| F | V | V | F | **F** |
| F | F | V | V | **V** |

**Observação:** o resultado é V exatamente quando $p$ e $q$ têm o mesmo valor, ou seja, a fórmula equivale a $p \leftrightarrow q$. Ela **não** é uma tautologia. Isso confirma que um condicional e sua **recíproca** não são equivalentes.

### 1d) $\neg(p \oplus q)$ comparado com $p \leftrightarrow q$

| p | q | p ⊕ q | ¬(p ⊕ q) | p ↔ q |
|---|---|---|---|---|
| V | V | F | **V** | **V** |
| V | F | V | **F** | **F** |
| F | V | V | **F** | **F** |
| F | F | F | **V** | **V** |

As duas últimas colunas são iguais: $\neg(p \oplus q) \equiv p \leftrightarrow q$. Em Python, isso é o fato de `not (p != q)` ser o mesmo que `p == q`.

---

## Exercício 2 — Demonstração de equivalências por leis lógicas

Leis usadas (abreviações):

| Abrev. | Lei |
|---|---|
| CD | condicional como disjunção: $p \to q \equiv \neg p \lor q$ |
| DM | De Morgan: $\neg(p \land q) \equiv \neg p \lor \neg q$ e $\neg(p \lor q) \equiv \neg p \land \neg q$ |
| DN | dupla negação: $\neg\neg p \equiv p$ |
| Dist | distributiva |
| Assoc / Com | associativa / comutativa |
| Comp | complemento: $p \lor \neg p \equiv V$, $p \land \neg p \equiv F$ |
| Id | identidade: $V \land p \equiv p$, $F \lor p \equiv p$ |

### 2a) $\neg(p \to q) \equiv p \land \neg q$

$$\begin{aligned}
\neg(p \to q) &\equiv \neg(\neg p \lor q) && \text{CD} \\
&\equiv \neg\neg p \land \neg q && \text{DM} \\
&\equiv p \land \neg q && \text{DN} \quad ∎
\end{aligned}$$

**Interpretação:** negar "se chove, a rua molha" é afirmar "chove **e** a rua não molha".

### 2b) $p \lor (\neg p \land q) \equiv p \lor q$

$$\begin{aligned}
p \lor (\neg p \land q) &\equiv (p \lor \neg p) \land (p \lor q) && \text{Dist} \\
&\equiv V \land (p \lor q) && \text{Comp} \\
&\equiv p \lor q && \text{Id} \quad ∎
\end{aligned}$$

### 2c) $(p \to q) \land (p \to r) \equiv p \to (q \land r)$

$$\begin{aligned}
(p \to q) \land (p \to r) &\equiv (\neg p \lor q) \land (\neg p \lor r) && \text{CD} \\
&\equiv \neg p \lor (q \land r) && \text{Dist (pondo } \neg p \text{ em evidência)} \\
&\equiv p \to (q \land r) && \text{CD} \quad ∎
\end{aligned}$$

**Interpretação:** "se é servidor, tem IP" **e** "se é servidor, tem responsável" equivale a "se é servidor, tem IP **e** responsável".

### 2d) Exportação: $(p \land q) \to r \equiv p \to (q \to r)$

$$\begin{aligned}
(p \land q) \to r &\equiv \neg(p \land q) \lor r && \text{CD} \\
&\equiv (\neg p \lor \neg q) \lor r && \text{DM} \\
&\equiv \neg p \lor (\neg q \lor r) && \text{Assoc} \\
&\equiv \neg p \lor (q \to r) && \text{CD} \\
&\equiv p \to (q \to r) && \text{CD} \quad ∎
\end{aligned}$$

**Em código:** dois `if` aninhados equivalem a um `if` com `and`.
```python
if p:                       # equivale a:   if p and q:
    if q:                   #                   r()
        r()
```

### 2e) $\neg[p \lor (\neg p \land q)] \equiv \neg p \land \neg q$

$$\begin{aligned}
\neg[p \lor (\neg p \land q)] &\equiv \neg p \land \neg(\neg p \land q) && \text{DM} \\
&\equiv \neg p \land (\neg\neg p \lor \neg q) && \text{DM} \\
&\equiv \neg p \land (p \lor \neg q) && \text{DN} \\
&\equiv (\neg p \land p) \lor (\neg p \land \neg q) && \text{Dist} \\
&\equiv F \lor (\neg p \land \neg q) && \text{Comp} \\
&\equiv \neg p \land \neg q && \text{Id} \quad ∎
\end{aligned}$$

(Atalho: pelo item 2b, $p \lor (\neg p \land q) \equiv p \lor q$, e por De Morgan $\neg(p \lor q) \equiv \neg p \land \neg q$.)

### 2f) $(p \to r) \land (q \to r) \equiv (p \lor q) \to r$

$$\begin{aligned}
(p \to r) \land (q \to r) &\equiv (\neg p \lor r) \land (\neg q \lor r) && \text{CD} \\
&\equiv (\neg p \land \neg q) \lor r && \text{Dist (pondo } r \text{ em evidência)} \\
&\equiv \neg(p \lor q) \lor r && \text{DM} \\
&\equiv (p \lor q) \to r && \text{CD} \quad ∎
\end{aligned}$$

**Interpretação:** "se é servidor, precisa de backup" e "se é banco de dados, precisa de backup" equivale a "se é servidor **ou** banco de dados, precisa de backup".

### 2g) Uma "equivalência" falsa: $p \to q \equiv q \to p$?

Para refutar uma equivalência, basta **uma linha** em que os valores diferem. Com $p = V$ e $q = F$:
- $p \to q = V \to F = F$
- $q \to p = F \to V = V$

Logo, $p \to q \not\equiv q \to p$. O condicional não é equivalente à sua recíproca. (Conferido no script: `equivalentes: False`.)

### Conferência automática

```text
2a ¬(p→q) ≡ p∧¬q                 equivalentes: True
2b p∨(¬p∧q) ≡ p∨q                equivalentes: True
2c (p→q)∧(p→r) ≡ p→(q∧r)         equivalentes: True
2d (p∧q)→r ≡ p→(q→r)             equivalentes: True
2e ¬(p∨(¬p∧q)) ≡ ¬p∧¬q           equivalentes: True
2f (p→r)∧(q→r) ≡ (p∨q)→r         equivalentes: True
2g (contraex.) p→q ≡ q→p ?       equivalentes: False
```

---

## Exercício 3 — Tautologias, contradições e contingências

Classifique cada fórmula.

### 3a) $[p \land (p \to q)] \to q$ — **tautologia** (modus ponens)

Por leis lógicas:
$$\begin{aligned}
[p \land (\neg p \lor q)] \to q &\equiv [(p \land \neg p) \lor (p \land q)] \to q && \text{Dist} \\
&\equiv (p \land q) \to q && \text{Comp, Id} \\
&\equiv \neg p \lor \neg q \lor q && \text{CD, DM} \\
&\equiv \neg p \lor V \equiv V && \text{Comp, dominação}
\end{aligned}$$

### 3b) $(p \to q) \land (p \land \neg q)$ — **contradição**

Pelo item 2a, $p \land \neg q \equiv \neg(p \to q)$. Então a fórmula tem a forma $X \land \neg X$, com $X = p \to q$, que é sempre F.

### 3c) $(p \to q) \to (q \to p)$ — **contingência**

| p | q | p → q | q → p | (p→q)→(q→p) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | V |
| F | V | V | F | **F** |
| F | F | V | V | V |

Tem linhas V e uma linha F. Saber que $p \to q$ vale não garante que a recíproca valha.

### 3d) $[(p \to q) \land (q \to r)] \to (p \to r)$ — **tautologia** (silogismo hipotético)

| p | q | r | p→q | q→r | (p→q)∧(q→r) | p→r | fórmula |
|---|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V | **V** |
| V | V | F | V | F | F | F | **V** |
| V | F | V | F | V | F | V | **V** |
| V | F | F | F | V | F | F | **V** |
| F | V | V | V | V | V | V | **V** |
| F | V | F | V | F | F | V | **V** |
| F | F | V | V | V | V | V | **V** |
| F | F | F | V | V | V | V | **V** |

A última coluna é toda V. Repare que, sempre que a conjunção das hipóteses é V, $p \to r$ também é V.

### 3e) $(p \leftrightarrow q) \land (p \oplus q)$ — **contradição**

Pelo item 1d, $p \leftrightarrow q \equiv \neg(p \oplus q)$. A fórmula é $\neg X \land X$, sempre F.

### 3f) $p \to (q \to p)$ — **tautologia**

$$p \to (q \to p) \equiv \neg p \lor (\neg q \lor p) \equiv (\neg p \lor p) \lor \neg q \equiv V \lor \neg q \equiv V$$

### Conferência automática

```text
3a [p ∧ (p→q)] → q               TAUTOLOGIA
3b (p→q) ∧ (p ∧ ¬q)              CONTRADIÇÃO
3c (p→q) → (q→p)                 CONTINGÊNCIA
3d [(p→q)∧(q→r)] → (p→r)         TAUTOLOGIA
3e (p↔q) ∧ (p⊕q)                 CONTRADIÇÃO
3f p → (q → p)                   TAUTOLOGIA
```

---

## Exercício 4 — Validade de argumentos

**Método:** um argumento é válido se, em **toda linha em que todas as premissas são V** (linha crítica), a conclusão também é V. Uma linha crítica com conclusão F é um **contraexemplo** e prova a invalidade.

### 4a) Modus tollens — **válido**

> Se o servidor está exposto à internet, então ele tem firewall. O servidor não tem firewall. Logo, o servidor não está exposto à internet.

$p$: está exposto; $q$: tem firewall. Forma: $p \to q,\; \neg q \;\vdash\; \neg p$.

| p | q | p → q | ¬q | ¬p (concl.) | |
|---|---|---|---|---|---|
| V | V | V | F | F | |
| V | F | F | V | F | |
| F | V | V | F | V | |
| F | F | V | V | **V** | linha crítica ✓ |

Há uma única linha crítica, e nela a conclusão é V. **Válido.**

### 4b) Afirmação do consequente — **inválido**

> Se a matriz é estritamente diagonal dominante, então ela é invertível. A matriz é invertível. Logo, ela é estritamente diagonal dominante.

$p$: é EDD; $q$: é invertível. Forma: $p \to q,\; q \;\vdash\; p$.

| p | q | p → q | q | p (concl.) | |
|---|---|---|---|---|---|
| V | V | V | V | V | linha crítica ✓ |
| V | F | F | F | V | |
| F | V | V | V | **F** | **contraexemplo** ✗ |
| F | F | V | F | F | |

**Inválido.** Contraexemplo concreto: $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ é invertível ($\det = -2$), mas não é EDD.

### 4c) Negação do antecedente — **inválido**

> Se a matriz é EDD, então é invertível. A matriz não é EDD. Logo, não é invertível.

Forma: $p \to q,\; \neg p \;\vdash\; \neg q$. O contraexemplo é a mesma linha $p = F,\; q = V$: as premissas são V e a conclusão $\neg q$ é F. A mesma matriz $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ serve de exemplo.

### 4d) $p \lor q,\;\; p \to r,\;\; q \to r \;\vdash\; r$ — **válido** (prova por casos)

| p | q | r | p∨q | p→r | q→r | r (concl.) | |
|---|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V | crítica ✓ |
| V | V | F | V | F | F | F | |
| V | F | V | V | V | V | V | crítica ✓ |
| V | F | F | V | F | V | F | |
| F | V | V | V | V | V | V | crítica ✓ |
| F | V | F | V | V | F | F | |
| F | F | V | F | V | V | V | |
| F | F | F | F | V | V | F | |

Nas três linhas críticas, $r = V$. **Válido.**

**Exemplo:** "O risco vem de uma vulnerabilidade própria ou de uma dependência. Se vem de vulnerabilidade própria, o equipamento precisa de correção. Se vem de dependência, o equipamento precisa de correção. Logo, o equipamento precisa de correção."

### 4e) $p \to q,\;\; r \to q,\;\; q \;\vdash\; p \lor r$ — **inválido**

| p | q | r | p→q | r→q | q | p∨r (concl.) | |
|---|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V | crítica ✓ |
| V | V | F | V | V | V | V | crítica ✓ |
| V | F | V | F | F | F | V | |
| V | F | F | F | V | F | V | |
| F | V | V | V | V | V | V | crítica ✓ |
| F | V | F | V | V | V | **F** | **contraexemplo** ✗ |
| F | F | V | V | F | F | V | |
| F | F | F | V | V | F | F | |

**Inválido.** É uma afirmação do consequente "com duas causas": saber que o efeito $q$ ocorreu não garante que uma das causas conhecidas ocorreu, pois $q$ pode ter outra causa.

### 4f) $p \to (q \lor r),\;\; \neg q,\;\; \neg r \;\vdash\; \neg p$ — **válido**

Verificação por linhas críticas: as premissas $\neg q$ e $\neg r$ forçam $q = r = F$. Então $p \to F$ só é V se $p = F$. Na única linha crítica ($p = q = r = F$), a conclusão $\neg p$ é V. **Válido.**

(A derivação formal está no Exercício 5, que usa a mesma estrutura.)

### Conferência automática

```text
4a MT: p→q, ¬q ⊢ ¬p            VÁLIDO
4b AC: p→q, q ⊢ p              INVÁLIDO  contraexemplo: p=F, q=V
4c NA: p→q, ¬p ⊢ ¬q            INVÁLIDO  contraexemplo: p=F, q=V
4d p∨q, p→r, q→r ⊢ r           VÁLIDO
4e p→q, r→q, q ⊢ p∨r           INVÁLIDO  contraexemplo: p=F, q=V, r=F
4f p→(q∨r), ¬q, ¬r ⊢ ¬p        VÁLIDO
```

---

## Exercício 5 — Regras de inferência (derivações formais)

Regras usadas:

| Sigla | Regra | Forma |
|---|---|---|
| MP | modus ponens | $p \to q,\; p \;\vdash\; q$ |
| MT | modus tollens | $p \to q,\; \neg q \;\vdash\; \neg p$ |
| SH | silogismo hipotético | $p \to q,\; q \to r \;\vdash\; p \to r$ |
| SD | silogismo disjuntivo | $p \lor q,\; \neg p \;\vdash\; q$ |
| Conj | conjunção | $p,\; q \;\vdash\; p \land q$ |
| Simp | simplificação | $p \land q \;\vdash\; p$ |

Além delas, qualquer equivalência do Exercício 2 pode ser usada para reescrever uma linha.

### 5a) $p \to q,\;\; q \to r,\;\; p \;\vdash\; r$

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $p \to q$ | premissa |
| 2 | $q \to r$ | premissa |
| 3 | $p$ | premissa |
| 4 | $q$ | MP 1, 3 |
| 5 | $r$ | MP 2, 4 ∎ |

(Alternativa: SH em 1 e 2 dá $p \to r$; depois MP com 3.)

### 5b) $p \lor q,\;\; \neg p,\;\; q \to s \;\vdash\; s$

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $p \lor q$ | premissa |
| 2 | $\neg p$ | premissa |
| 3 | $q \to s$ | premissa |
| 4 | $q$ | SD 1, 2 |
| 5 | $s$ | MP 3, 4 ∎ |

### 5c) $(p \land q) \to r,\;\; \neg r,\;\; q \;\vdash\; \neg p$

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $(p \land q) \to r$ | premissa |
| 2 | $\neg r$ | premissa |
| 3 | $q$ | premissa |
| 4 | $\neg(p \land q)$ | MT 1, 2 |
| 5 | $\neg p \lor \neg q$ | De Morgan em 4 |
| 6 | $\neg q \lor \neg p$ | comutativa em 5 |
| 7 | $\neg\neg q$ | dupla negação em 3 |
| 8 | $\neg p$ | SD 6, 7 ∎ |

### 5d) $p \to q,\;\; \neg p \to r,\;\; r \to s \;\vdash\; \neg q \to s$

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $p \to q$ | premissa |
| 2 | $\neg p \to r$ | premissa |
| 3 | $r \to s$ | premissa |
| 4 | $\neg q \to \neg p$ | contrapositiva de 1 |
| 5 | $\neg q \to r$ | SH 4, 2 |
| 6 | $\neg q \to s$ | SH 5, 3 ∎ |

### 5e) $p \to (q \lor r),\;\; \neg q,\;\; \neg r \;\vdash\; \neg p$ (o argumento 4f)

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $p \to (q \lor r)$ | premissa |
| 2 | $\neg q$ | premissa |
| 3 | $\neg r$ | premissa |
| 4 | $\neg q \land \neg r$ | Conj 2, 3 |
| 5 | $\neg(q \lor r)$ | De Morgan em 4 |
| 6 | $\neg p$ | MT 1, 5 ∎ |

### 5f) Aplicação ao Trabalho 2

Proposições:
- $e$: as dependências passaram na validação de cadastro (a soma de cada linha de $A$ é menor que 1);
- $i$: $I - A$ é invertível;
- $c$: o vetor de riscos próprios $b = Mv$ foi calculado;
- $a$: o risco efetivo $x$ é obtido como solução única de $(I - A)x = b$.

Premissas:
1. $e \to i$ (teorema: matriz EDD é invertível)
2. $(i \land c) \to a$ (matriz invertível e $b$ conhecido dão solução única)
3. $e$
4. $c$

Conclusão: $a$.

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $e \to i$ | premissa |
| 2 | $(i \land c) \to a$ | premissa |
| 3 | $e$ | premissa |
| 4 | $c$ | premissa |
| 5 | $i$ | MP 1, 3 |
| 6 | $i \land c$ | Conj 5, 4 |
| 7 | $a$ | MP 2, 6 ∎ |

Isso formaliza a justificativa do projeto: **validar no cadastro garante que o sistema sempre terá solução**.

### Conferência automática

```text
5a p→q, q→r, p ⊢ r               VÁLIDO
5b p∨q, ¬p, q→s ⊢ s              VÁLIDO
5c (p∧q)→r, ¬r, q ⊢ ¬p           VÁLIDO
5d p→q, ¬p→r, r→s ⊢ ¬q→s         VÁLIDO
5e p→(q∨r), ¬q, ¬r ⊢ ¬p         VÁLIDO
5f Trabalho 2 (e,i,c,a)          VÁLIDO
```

---

## Exercício 6 — Problemas de lógica na Computação

### 6a) Simplificar uma condição

Simplifique `if (a and b) or (a and not b) or (not a and b):`.

$$\begin{aligned}
(a \land b) \lor (a \land \neg b) \lor (\neg a \land b) &\equiv [a \land (b \lor \neg b)] \lor (\neg a \land b) && \text{Dist} \\
&\equiv a \lor (\neg a \land b) && \text{Comp, Id} \\
&\equiv a \lor b && \text{item 2b}
\end{aligned}$$

```python
if a or b:      # mesma lógica, muito mais legível
```

Conferido: `6a (a∧b)∨(a∧¬b)∨(¬a∧b) ≡ a∨b : True`.

### 6b) De Morgan na validação de dependências

Uma dependência $A_{ij}$ só deve ser **aceita** se:
- $f$: $0 \le$ fração $< 1$;
- $d$: $i \ne j$;
- $s$: a nova soma da linha é menor que 1.

Aceitar é $f \land d \land s$. Rejeitar é a negação, que por De Morgan vale:
$$\neg(f \land d \land s) \equiv \neg f \lor \neg d \lor \neg s$$

Negando cada parte:
- $\neg(0 \le \text{fração} < 1) \equiv \text{fração} < 0 \;\lor\; \text{fração} \ge 1$
- $\neg(i \ne j) \equiv i = j$
- $\neg(\text{nova\_soma} < 1) \equiv \text{nova\_soma} \ge 1$

```python
# CORRETO: rejeita se QUALQUER condição falhar
if fracao < 0 or fracao >= 1 or i == j or nova_soma >= 1:
    raise ValueError("Dependência inválida")

# ERRADO: só rejeita se TODAS falharem ao mesmo tempo
if fracao < 0 and i == j and nova_soma >= 1:   # ¬f ∧ ¬d ∧ ¬s
    raise ValueError("Dependência inválida")
```

Conferido: `rejeitar ≡ ¬aceitar : True` e `versão errada ≡ ¬aceitar : False`. A versão errada aceitaria, por exemplo, um equipamento dependendo de si mesmo com fração válida.

### 6c) Erro de parênteses numa política de acesso

Regra: "pode editar o inventário quem é administrador, **ou** quem é dono do equipamento e o equipamento não está bloqueado".

$$\text{correta: } adm \lor (dono \land \neg bloq) \qquad \text{com erro: } (adm \lor dono) \land \neg bloq$$

As duas fórmulas diferem quando $adm = V$ e $bloq = V$ (conferido: `difere em: adm=V, dono=V, bloq=V` e `adm=V, dono=F, bloq=V`). A versão com erro **impede o administrador** de editar equipamentos bloqueados.

Em Python, `adm or dono and not bloq` é lido corretamente como `adm or (dono and (not bloq))`, porque `and` tem precedência maior que `or`. O erro só aparece quando alguém acrescenta parênteses no lugar errado. Por isso, em regras de segurança, **escreva os parênteses explicitamente** e teste a regra com a tabela-verdade.

### 6d) Curto-circuito: $\land$ é comutativo, mas o código não é

```python
equip = None
equip is not None and equip.risco > 30     # False  (para na 1ª parte)
equip.risco > 30 and equip is not None     # AttributeError: 'NoneType' object has no attribute 'risco'
```

Na lógica, $p \land q \equiv q \land p$. No código, `and` e `or` avaliam da esquerda para a direita e param assim que o resultado está decidido. A primeira condição funciona como **guarda** da segunda, então a ordem importa.

### 6e) Precedência de `not` em Python

```python
x, y = -5, False
not x > 0 or y        # True:  lido como  (not (x > 0)) or y
(not x) > 0 or y      # False: not -5 é False, e False > 0 é False
```

Em Python, os operadores de comparação têm precedência **maior** que `not`, então `not x > 0` significa $\neg(x > 0)$. Isso é diferente de linguagens como C, em que `!x > 0` aplica a negação primeiro. Na dúvida, use parênteses.

### 6f) Enigma: qual servidor foi comprometido?

Uma auditoria encontrou três registros, todos confiáveis:
1. "O servidor A ou o servidor B foi comprometido." → $A \lor B$
2. "Se A foi comprometido, então C também foi." → $A \to C$
3. "C não foi comprometido." → $\neg C$

| # | Fórmula | Justificativa |
|---|---|---|
| 1 | $A \lor B$ | premissa |
| 2 | $A \to C$ | premissa |
| 3 | $\neg C$ | premissa |
| 4 | $\neg A$ | MT 2, 3 |
| 5 | $B$ | SD 1, 4 |

**Conclusão:** A e C estão íntegros, e **B foi comprometido**.

Conferência por força bruta (testando as $2^3 = 8$ combinações):
```text
6f soluções do enigma:
   A=F B=V C=F
```
A solução é única e coincide com a derivação.

### 6g) Um raciocínio errado sobre o modelo de risco

> "A regra de cadastro diz: se as linhas de $A$ somam menos de 1, então $I - A$ é invertível. Esta matriz tem uma linha que soma 1,5. Logo, $I - A$ não é invertível."

É a **negação do antecedente**, que é inválida (item 4c). Contraexemplo verificado no NumPy:

$$A = \begin{bmatrix} 0 & 1{,}5 \\ 0 & 0 \end{bmatrix}, \quad I - A = \begin{bmatrix} 1 & -1{,}5 \\ 0 & 1 \end{bmatrix}$$

```text
6g somas das linhas: [1.5 0. ] | det(I-A) = 1.0
```

A primeira linha soma 1,5, e mesmo assim $\det(I - A) = 1 \neq 0$. O critério das somas é **suficiente, mas não necessário**.

O que se pode concluir validamente é a **contrapositiva**: se $I - A$ **não** é invertível, então alguma linha de $A$ soma 1 ou mais.

### 6h) Um verificador de tautologias em Python

```python
from itertools import product

def imp(a, b):
    return (not a) or b

def classificar(n_vars, formula):
    valores = [formula(*v) for v in product([True, False], repeat=n_vars)]
    if all(valores):
        return "tautologia"
    if not any(valores):
        return "contradição"
    return "contingência"

def valido(n_vars, premissas, conclusao):
    """Válido se não existe linha com todas as premissas V e conclusão F."""
    return not any(all(p(*v) for p in premissas) and not conclusao(*v)
                   for v in product([True, False], repeat=n_vars))

print(classificar(2, lambda p, q: imp(p and imp(p, q), q)))          # tautologia
print(valido(2, [lambda p, q: imp(p, q), lambda p, q: q],
             lambda p, q: p))                                         # False (afirmação do consequente)
```

O custo é de $2^n$ linhas. Para algumas dezenas de variáveis isso já é inviável, e esse é o motivo de o problema da satisfatibilidade (SAT) ser central na teoria da computação.
