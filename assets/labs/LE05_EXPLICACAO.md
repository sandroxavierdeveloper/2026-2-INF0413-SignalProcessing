# LE05 — Números complexos (e exponenciais complexas), explicados

Texto de estudo de `le05_complex-exponentials/`:

- `le05_complex-numbers.ipynb` — o lab completo, executado;
- `le05_desafio1_modulo_e_fase.py` — Desafio 1 em Python (módulo e fase sem funções prontas);
- `le05_desafio2_j_elevado_a_j.py` — Desafio 2 em Python (antecipar o gráfico de $j^j$).

Os números citados são os que o notebook e os scripts produzem.

---

## 1. A ideia em uma frase

> Um número complexo é um **ponto no plano** — ou uma **seta** com tamanho e direção. Multiplicar complexos
> **escala e gira** a seta. É por isso que eles servem para descrever **oscilações**: uma senoide é uma seta
> girando.

Este lab é o pré-requisito direto do le06: a DFT é feita de setas girando, $e^{-j\frac{2\pi}{N}kn}$, e o resultado
dela é lido por **módulo** e **fase**.

---

## 2. As duas formas de escrever um complexo

**Cartesiana** — as coordenadas do ponto:

$$
z = a + bj, \qquad a = \mathrm{Re}\{z\}, \quad b = \mathrm{Im}\{z\}, \quad j^2 = -1
$$

**Polar** — o tamanho e o ângulo da seta:

$$
z = r\,e^{j\theta}, \qquad r = |z| \text{ (módulo)}, \quad \theta = \angle z \text{ (fase)}
$$

A ponte entre as duas é a **fórmula de Euler**:

$$
e^{j\theta} = \cos\theta + j\sin\theta
\quad\Rightarrow\quad
a = r\cos\theta, \quad b = r\sin\theta
$$

No Python, `j` se escreve `1j`: `z1 = 3 + 4j`. O tipo é `complex`.

### O exemplo do lab: $z_1 = 3 + 4j$

- módulo $|z_1| = \sqrt{3^2 + 4^2} = 5$;
- fase $\angle z_1 = 0{,}927$ rad $= 53{,}13°$.

---

## 3. Módulo e fase — e o erro clássico do `arctan`

**Módulo** — Pitágoras: $|z| = \sqrt{a^2 + b^2}$. No notebook, `COMPLEXmagnitude` tem duas versões
(Pitágoras e `np.abs`) que dão o mesmo resultado.

**Fase** — `COMPLEXphase` tem três versões:

| versão | código | problema |
|---|---|---|
| 1 | `np.arctan(b / a)` | **erra no 2º e no 3º quadrantes** |
| 2 | `np.arctan2(b, a)` | correta, em $(-\pi, \pi]$ |
| 3 | `np.angle(z)` | correta (é o `arctan2` por dentro) |

**Por que o `arctan(b/a)` erra:** ele recebe só a **razão** e perde os sinais: $\frac{-4}{-3} = \frac{4}{3}$.
Então $-3-4j$ (3º quadrante) e $3+4j$ (1º) dão o mesmo ângulo. A tabela do notebook mostra:

| $z$ | `arctan` | `arctan2` / `angle` |
|---|---|---|
| $3 + 4j$ | 53,13° | 53,13° |
| $-3 + 4j$ | **−53,13°** | 126,87° |
| $-3 - 4j$ | **53,13°** | −126,87° |
| $3 - 4j$ | −53,13° | −53,13° |

O `arctan2(b, a)` recebe as duas componentes **separadas** e decide o quadrante pelos sinais.

---

## 4. Desafio 1 — módulo e fase **sem funções prontas**

Enunciado: *"Crie funções customizadas para calcular o módulo e fase de um complexo. Obs: ñ funções prontas!"*

A solução (`myMagnitude`, `myPhase`) usa **só operadores** (`+ - * / **`) e comparações. Nada de `abs`, `sqrt`,
`arctan`, `arctan2`, `angle` — **nem a constante $\pi$**, que é calculada.

1. **Módulo:** `(a**2 + b**2) ** 0.5` — a raiz é o operador `** 0.5`, não uma função.

2. **arctan pela série de Taylor:**

   $$
   \arctan u = u - \frac{u^3}{3} + \frac{u^5}{5} - \frac{u^7}{7} + \dots
   $$

   Ela só converge rápido para $|u|$ pequeno, então primeiro se reduz $u$:
   - se $|u| > 1$: $\arctan u = \pm\frac{\pi}{2} - \arctan\frac{1}{u}$;
   - **meio ângulo**: $\arctan u = 2\arctan\dfrac{u}{1 + \sqrt{1+u^2}}$ — aplicado 3 vezes, leva $|u| \le 1$ para
     $|u| \le 0{,}1$, e o resultado é multiplicado por $2^3 = 8$.

3. **$\pi$ pela fórmula de Machin**, usando a própria série:

   $$
   \pi = 16\arctan\frac{1}{5} - 4\arctan\frac{1}{239}
   $$

   Resultado: `3.141592653589794` (o do Python é `…793`: diferença na última casa).

4. **arctan2 próprio** — decide o quadrante pelos sinais, que é exatamente o que faltava à versão 1:

   | caso | fase |
   |---|---|
   | $a > 0$ | $\arctan(b/a)$ |
   | $a < 0,\ b \ge 0$ | $\arctan(b/a) + \pi$ |
   | $a < 0,\ b < 0$ | $\arctan(b/a) - \pi$ |
   | $a = 0$ | $\pm\pi/2$ (ou 0 na origem, onde a fase é indefinida) |

**Conferência:** em **100 mil** complexos aleatórios, em todos os quadrantes e em escalas de $10^{-6}$ a $10^6$,
o erro máximo foi $2{,}2\times10^{-16}$ no módulo e $1{,}3\times10^{-15}$ rad na fase — o limite da precisão do
computador.

---

## 5. Potência e raiz no plano complexo

Na forma polar, potências viram regras simples:

$$
z^n = r^n e^{jn\theta} \qquad \text{(módulo elevado a } n\text{, fase multiplicada por } n\text{)}
$$

**Potência** — $z_2 = z_1^2 = (3+4j)^2 = -7 + 24j$:
- $|z_2| = 25 = 5^2$;
- $\angle z_2 = 106{,}26° = 2 \times 53{,}13°$.

Multiplicar complexos **escala e gira**. Isso é o coração das oscilações: multiplicar repetidamente por
$e^{j\omega}$ faz a seta girar $\omega$ a cada passo — uma senoide.

**Raiz** — $z_3 = \sqrt{z_1} = 2 + j$:
- $|z_3| = \sqrt{5} = 2{,}236$;
- $\angle z_3 = 26{,}57° = 53{,}13°/2$.

**Mas a raiz tem duas respostas.** A fase só é definida a menos de voltas inteiras: $\theta$ e $\theta + 2\pi$ são
o mesmo ponto. As $n$ raízes $n$-ésimas são

$$
z^{1/n} = r^{1/n}\, e^{j\frac{\theta + 2\pi k}{n}}, \qquad k = 0, 1, \dots, n-1
$$

$n$ pontos igualmente espaçados num círculo — um **polígono regular**. As raízes quadradas de $3+4j$ são
$2+j$ e $-2-j$. O Python (`z1 ** 0.5`) devolve só a **principal**. O notebook desenha as raízes para $n = 2, 3, 6$
e confere que cada uma, elevada a $n$, volta a $z_1$.

---

## 6. Desafio 2 — antecipar o gráfico de $j^j$

Enunciado: *"Curioso, não é? Antecipar o gráfico do seguinte número no plano complexo: `z = 1j ** 1j`"*.

**Antecipação, antes de perguntar ao Python.** Na forma polar, $j = e^{j\pi/2}$ (módulo 1, fase 90°). Então

$$
j^{\,j} = \left(e^{j\pi/2}\right)^{j} = e^{j\cdot j\cdot\pi/2} = e^{-\pi/2} \approx 0{,}2079
$$

porque $j \cdot j = -1$. **Um número real e positivo**: o ponto cai **sobre o eixo real**, com fase zero. Um número
"imaginário elevado a imaginário" dá real.

**Conferência:** previsto $e^{-\mathrm{fase}(j)} = 0{,}20787957635076\ldots$; o Python dá
`(0.20787957635076193+0j)`.

**Mais curioso ainda: $j^j$ tem infinitos valores.** A fase de $j$ não é só $\frac{\pi}{2}$, é
$\frac{\pi}{2} + 2\pi k$ para qualquer inteiro $k$. Cada escolha dá um valor, **todos reais e positivos**:

| $k$ | $j^j = e^{-(\pi/2 + 2\pi k)}$ |
|---|---|
| −2 | 59 609,74 |
| −1 | 111,32 |
| **0** | **0,2079** ← o que o Python devolve (ramo principal) |
| 1 | 0,000388 |
| 2 | 0,000000725 |

É a mesma ideia das raízes com várias respostas: a fase "dá voltas", e funções como potência e logaritmo herdam
essa ambiguidade.

---

## 7. Sinais periódicos e não periódicos

Um sinal discreto $x[n] = \cos(\omega n + \phi)$ só é periódico se existir um inteiro $P$ com $x[n + P] = x[n]$,
ou seja, $\omega P = 2\pi k$. Isso só acontece se a frequência for uma **fração racional** de $2\pi$:

$$
\omega = 2\pi\frac{K_1}{K_2}, \quad K_1, K_2 \text{ inteiros} \quad\Rightarrow\quad \text{período } K_2 \text{ (se a fração for irredutível)}
$$

- $\omega = 2\pi\cdot\frac{1}{10}$: **periódico**, período fundamental $P = 10$ (conferido por código).
- $\omega = 1$ rad/amostra: $\frac{2\pi}{\omega} = 2\pi$ é **irracional**, não existe $P$ inteiro, e o sinal
  **nunca se repete exatamente** (o código confere: nenhum $P < 50$ funciona).

**A pegadinha:** a curva contínua $\cos(t)$ é periódica (período $2\pi$), mas **as amostras** dela em
$n = 0, 1, 2, \dots$ nunca caem no mesmo lugar da curva — porque $2\pi$ não é um número inteiro de amostras.
Isso é diferente do mundo contínuo, onde **toda** senoide é periódica.

---

## 8. Perguntas que o professor pode fazer

**O que é o módulo e a fase de um complexo?** O tamanho da seta e o ângulo dela com o eixo real.

**Por que não usar `arctan(b/a)` para a fase?** Perde o sinal de $a$ e $b$ e erra no 2º e no 3º quadrantes; o
`arctan2(b, a)` olha os dois separadamente.

**Como você calculou o arctan sem função pronta?** Série de Taylor, com redução do argumento (inverso e
meio ângulo) para convergir rápido; e $\pi$ pela fórmula de Machin.

**O que acontece com módulo e fase ao elevar ao quadrado?** O módulo é elevado ao quadrado e a fase dobra.

**Por que a raiz quadrada tem duas respostas?** Porque a fase é definida a menos de $2\pi$; dividir por 2 dá dois
ângulos diferentes, separados de 180°.

**Quanto vale $j^j$ e por quê?** $e^{-\pi/2} \approx 0{,}2079$, real: $j = e^{j\pi/2}$ e $j\cdot j = -1$. E tem
infinitos valores, $e^{-(\pi/2 + 2\pi k)}$.

**Quando uma senoide discreta é periódica?** Quando $\omega/2\pi$ é um número racional; com $\omega = 1$ ela não é.

**Qual a relação disso com a DFT (le06)?** A DFT compara o sinal com setas girando, $e^{-j\frac{2\pi}{N}kn}$, e o
resultado é lido por módulo (quanto de cada frequência) e fase (onde a senoide começa).

---

## 9. Roteiro de 3 minutos

1. **O que é** (30 s): "um complexo é um ponto ou uma seta: $a + bj$ ou $re^{j\theta}$, ligados pela fórmula de
   Euler. $3+4j$ tem módulo 5 e fase 53,13°."
2. **Desafio 1** (60 s): "fiz módulo e fase sem funções prontas: módulo por Pitágoras, arctan por série de Taylor
   com redução do argumento, $\pi$ pela fórmula de Machin, e um arctan2 que decide o quadrante pelos sinais —
   porque o `arctan(b/a)` erra no 2º e 3º quadrantes. Erro de $10^{-15}$ em 100 mil casos."
3. **Potência e raiz** (30 s): "elevar ao quadrado eleva o módulo ao quadrado e dobra a fase; a raiz tem duas
   respostas, as $n$ raízes formam um polígono regular."
4. **Desafio 2** (40 s): "$j^j = e^{-\pi/2} \approx 0{,}2079$, real, porque $j = e^{j\pi/2}$ e $j\cdot j = -1$.
   Previ antes e o Python confirmou. E tem infinitos valores, um por volta da fase."
5. **Periodicidade** (20 s): "senoide discreta só é periódica se $\omega/2\pi$ for racional; com $\omega = 1$
   nunca se repete."

---

## 10. Onde está cada coisa

| arquivo | o que tem |
|---|---|
| `le05_complex-exponentials/le05_complex-numbers.ipynb` | o lab completo, executado, com gráficos |
| `le05_complex-exponentials/le05_desafio1_modulo_e_fase.py` | Desafio 1 em Python puro; roda com `python le05_desafio1_modulo_e_fase.py` |
| `le05_complex-exponentials/le05_desafio2_j_elevado_a_j.py` | Desafio 2; importa o Desafio 1, então rode de dentro da pasta |
| `LE04_EXPLICACAO.md` | o lab anterior: tom digital, FFT como prova, Karplus-Strong |
| `LE06_DFT_EXPLICACAO.md` | o próximo lab: a DFT em quatro versões |
