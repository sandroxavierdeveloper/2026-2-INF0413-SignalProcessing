# LE05 — Números complexos (e exponenciais complexas), explicados

Texto de estudo de `le05_complex-exponentials/`:

- `le05_complex-numbers.ipynb` — o lab completo, executado;
- `le05_desafio1_modulo_e_fase.py` — Desafio 1 em Python (módulo e fase sem funções prontas);
- `le05_desafio2_j_elevado_a_j.py` — Desafio 2 em Python (antecipar o gráfico de jʲ).

Os números citados são os que o notebook e os scripts produzem.

As fórmulas estão escritas com caracteres comuns (Σ, π, ², ·), sem LaTeX, para aparecerem iguais em qualquer editor ou visualizador.

---

## 1. A ideia em uma frase

> Um número complexo é um **ponto no plano** — ou uma **seta** com tamanho e direção. Multiplicar complexos **escala e gira** a seta. É por isso que eles servem para descrever **oscilações**: uma senoide é uma seta girando.

Este lab é o pré-requisito direto do le06: a DFT é feita de setas girando, e^(−j·2π·k·n/N), e o resultado dela é lido por **módulo** e **fase**.

---

## 2. As duas formas de escrever um complexo

**Cartesiana** — as coordenadas do ponto:

```
z = a + b·j        a = Re{z},  b = Im{z},  j² = −1
```

**Polar** — o tamanho e o ângulo da seta:

```
z = r · e^(jθ)     r = |z| (módulo),  θ = ∠z (fase)
```

A ponte entre as duas é a **fórmula de Euler**:

```
e^(jθ) = cos θ + j·sen θ      ⇒      a = r·cos θ,   b = r·sen θ
```

No Python, j se escreve `1j`: `z1 = 3 + 4j`. O tipo é `complex`.

### O exemplo do lab: z₁ = 3 + 4j

- módulo |z₁| = √(3² + 4²) = 5;
- fase ∠z₁ = 0,927 rad = 53,13°.

---

## 3. Módulo e fase — e o erro clássico do `arctan`

**Módulo** — Pitágoras: |z| = √(a² + b²). No notebook, `COMPLEXmagnitude` tem duas versões (Pitágoras e `np.abs`) que dão o mesmo resultado.

**Fase** — `COMPLEXphase` tem três versões:

| versão | código | problema |
|---|---|---|
| 1 | `np.arctan(b / a)` | **erra no 2º e no 3º quadrantes** |
| 2 | `np.arctan2(b, a)` | correta, em (−π, π] |
| 3 | `np.angle(z)` | correta (é o `arctan2` por dentro) |

**Por que o `arctan(b/a)` erra:** ele recebe só a **razão** e perde os sinais: (−4)/(−3) = 4/3. Então −3 − 4j (3º quadrante) e 3 + 4j (1º) dão o mesmo ângulo. A tabela do notebook mostra:

| z | `arctan` | `arctan2` / `angle` |
|---|---|---|
| 3 + 4j | 53,13° | 53,13° |
| −3 + 4j | **−53,13°** | 126,87° |
| −3 − 4j | **53,13°** | −126,87° |
| 3 − 4j | −53,13° | −53,13° |

O `arctan2(b, a)` recebe as duas componentes **separadas** e decide o quadrante pelos sinais.

---

## 4. Desafio 1 — módulo e fase **sem funções prontas**

Enunciado: *"Crie funções customizadas para calcular o módulo e fase de um complexo. Obs: ñ funções prontas!"*

A solução (`myMagnitude`, `myPhase`) usa **só operadores** (`+ - * / **`) e comparações. Nada de `abs`, `sqrt`, `arctan`, `arctan2`, `angle` — **nem a constante π**, que é calculada.

1. **Módulo:** `(a**2 + b**2) ** 0.5` — a raiz é o operador `** 0.5`, não uma função.

2. **arctan pela série de Taylor:**

   ```
   arctan u = u − u³/3 + u⁵/5 − u⁷/7 + ...
   ```

   Ela só converge rápido para |u| pequeno, então primeiro se reduz u:
   - se |u| > 1: arctan u = ±π/2 − arctan(1/u);
   - **meio ângulo**: arctan u = 2·arctan( u / (1 + √(1 + u²)) ) — aplicado 3 vezes, leva |u| ≤ 1 para |u| ≤ 0,1, e o resultado é multiplicado por 2³ = 8.

3. **π pela fórmula de Machin**, usando a própria série:

   ```
   π = 16·arctan(1/5) − 4·arctan(1/239)
   ```

   Resultado: `3.141592653589794` (o do Python é `…793`: diferença na última casa).

4. **arctan2 próprio** — decide o quadrante pelos sinais, que é exatamente o que faltava à versão 1:

   | caso | fase |
   |---|---|
   | a > 0 | arctan(b/a) |
   | a < 0, b ≥ 0 | arctan(b/a) + π |
   | a < 0, b < 0 | arctan(b/a) − π |
   | a = 0 | ±π/2 (ou 0 na origem, onde a fase é indefinida) |

**Conferência:** em **100 mil** complexos aleatórios, em todos os quadrantes e em escalas de 10⁻⁶ a 10⁶, o erro máximo foi 2,2 × 10⁻¹⁶ no módulo e 1,3 × 10⁻¹⁵ rad na fase — o limite da precisão do computador.

---

## 5. Potência e raiz no plano complexo

Na forma polar, potências viram regras simples:

```
zⁿ = rⁿ · e^(j·n·θ)        (módulo elevado a n, fase multiplicada por n)
```

**Potência** — z₂ = z₁² = (3 + 4j)² = −7 + 24j:

- |z₂| = 25 = 5²;
- ∠z₂ = 106,26° = 2 × 53,13°.

Multiplicar complexos **escala e gira**. Isso é o coração das oscilações: multiplicar repetidamente por e^(jω) faz a seta girar ω a cada passo — uma senoide.

**Raiz** — z₃ = √z₁ = 2 + j:

- |z₃| = √5 = 2,236;
- ∠z₃ = 26,57° = 53,13° / 2.

**Mas a raiz tem duas respostas.** A fase só é definida a menos de voltas inteiras: θ e θ + 2π são o mesmo ponto. As n raízes n-ésimas são

```
z^(1/n) = r^(1/n) · e^( j·(θ + 2π·k) / n )        k = 0, 1, ..., n−1
```

n pontos igualmente espaçados num círculo — um **polígono regular**. As raízes quadradas de 3 + 4j são 2 + j e −2 − j. O Python (`z1 ** 0.5`) devolve só a **principal**. O notebook desenha as raízes para n = 2, 3, 6 e confere que cada uma, elevada a n, volta a z₁.

---

## 6. Desafio 2 — antecipar o gráfico de jʲ

Enunciado: *"Curioso, não é? Antecipar o gráfico do seguinte número no plano complexo: `z = 1j ** 1j`"*.

**Antecipação, antes de perguntar ao Python.** Na forma polar, j = e^(jπ/2) (módulo 1, fase 90°). Então

```
jʲ = ( e^(jπ/2) )ʲ = e^(j·j·π/2) = e^(−π/2) ≈ 0,2079
```

porque j·j = −1. **Um número real e positivo**: o ponto cai **sobre o eixo real**, com fase zero. Um número "imaginário elevado a imaginário" dá real.

**Conferência:** previsto e^(−fase(j)) = 0,20787957635076…; o Python dá `(0.20787957635076193+0j)`.

**Mais curioso ainda: jʲ tem infinitos valores.** A fase de j não é só π/2, é π/2 + 2π·k para qualquer inteiro k. Cada escolha dá um valor, **todos reais e positivos**:

| k | jʲ = e^(−(π/2 + 2π·k)) |
|---|---|
| −2 | 59 609,74 |
| −1 | 111,32 |
| **0** | **0,2079** ← o que o Python devolve (ramo principal) |
| 1 | 0,000388 |
| 2 | 0,000000725 |

É a mesma ideia das raízes com várias respostas: a fase "dá voltas", e funções como potência e logaritmo herdam essa ambiguidade.

---

## 7. Sinais periódicos e não periódicos

Um sinal discreto x[n] = cos(ω·n + φ) só é periódico se existir um inteiro P com x[n + P] = x[n], ou seja, ω·P = 2π·k. Isso só acontece se a frequência for uma **fração racional** de 2π:

```
ω = 2π · K₁/K₂   (K₁, K₂ inteiros)   ⇒   período K₂ (se a fração for irredutível)
```

- ω = 2π·(1/10): **periódico**, período fundamental P = 10 (conferido por código).
- ω = 1 rad/amostra: 2π/ω = 2π é **irracional**, não existe P inteiro, e o sinal **nunca se repete exatamente** (o código confere: nenhum P < 50 funciona).

**A pegadinha:** a curva contínua cos(t) é periódica (período 2π), mas **as amostras** dela em n = 0, 1, 2, … nunca caem no mesmo lugar da curva — porque 2π não é um número inteiro de amostras. Isso é diferente do mundo contínuo, onde **toda** senoide é periódica.

---

## 8. Perguntas que o professor pode fazer

**O que é o módulo e a fase de um complexo?** O tamanho da seta e o ângulo dela com o eixo real.

**Por que não usar `arctan(b/a)` para a fase?** Perde o sinal de a e b e erra no 2º e no 3º quadrantes; o `arctan2(b, a)` olha os dois separadamente.

**Como você calculou o arctan sem função pronta?** Série de Taylor, com redução do argumento (inverso e meio ângulo) para convergir rápido; e π pela fórmula de Machin.

**O que acontece com módulo e fase ao elevar ao quadrado?** O módulo é elevado ao quadrado e a fase dobra.

**Por que a raiz quadrada tem duas respostas?** Porque a fase é definida a menos de 2π; dividir por 2 dá dois ângulos diferentes, separados de 180°.

**Quanto vale jʲ e por quê?** e^(−π/2) ≈ 0,2079, real: j = e^(jπ/2) e j·j = −1. E tem infinitos valores, e^(−(π/2 + 2π·k)).

**Quando uma senoide discreta é periódica?** Quando ω/2π é um número racional; com ω = 1 ela não é.

**Qual a relação disso com a DFT (le06)?** A DFT compara o sinal com setas girando, e^(−j·2π·k·n/N), e o resultado é lido por módulo (quanto de cada frequência) e fase (onde a senoide começa).

---

## 9. Roteiro de 3 minutos

1. **O que é** (30 s): "um complexo é um ponto ou uma seta: a + bj ou r·e^(jθ), ligados pela fórmula de Euler. 3 + 4j tem módulo 5 e fase 53,13°."
2. **Desafio 1** (60 s): "fiz módulo e fase sem funções prontas: módulo por Pitágoras, arctan por série de Taylor com redução do argumento, π pela fórmula de Machin, e um arctan2 que decide o quadrante pelos sinais — porque o `arctan(b/a)` erra no 2º e 3º quadrantes. Erro de 10⁻¹⁵ em 100 mil casos."
3. **Potência e raiz** (30 s): "elevar ao quadrado eleva o módulo ao quadrado e dobra a fase; a raiz tem duas respostas, as n raízes formam um polígono regular."
4. **Desafio 2** (40 s): "jʲ = e^(−π/2) ≈ 0,2079, real, porque j = e^(jπ/2) e j·j = −1. Previ antes e o Python confirmou. E tem infinitos valores, um por volta da fase."
5. **Periodicidade** (20 s): "senoide discreta só é periódica se ω/2π for racional; com ω = 1 nunca se repete."

---

## 10. Onde está cada coisa

| arquivo | o que tem |
|---|---|
| `le05_complex-exponentials/le05_complex-numbers.ipynb` | o lab completo, executado, com gráficos |
| `le05_complex-exponentials/le05_desafio1_modulo_e_fase.py` | Desafio 1 em Python puro; roda com `python le05_desafio1_modulo_e_fase.py` |
| `le05_complex-exponentials/le05_desafio2_j_elevado_a_j.py` | Desafio 2; importa o Desafio 1, então rode de dentro da pasta |
| `LE04_EXPLICACAO.md` | o lab anterior: tom digital, FFT como prova, Karplus-Strong |
| `LE06_DFT_EXPLICACAO.md` | o próximo lab: a DFT em quatro versões |
