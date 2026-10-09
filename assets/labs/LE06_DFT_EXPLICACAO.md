# LE06 — A Transformada Discreta de Fourier (DFT), explicada

Texto de estudo do notebook `le06_DFT/le06_01_DFT-four-versions.ipynb`. Os números citados aqui são os que o notebook produz quando executado.

Este texto está organizado na ordem em que dá para **explicar ao professor**: primeiro a ideia, depois as fórmulas, depois cada versão do código, depois o que os resultados mostram. No fim há uma lista de perguntas prováveis com respostas curtas e um roteiro de 3 minutos.

As fórmulas estão escritas com caracteres comuns (Σ, π, ², ·), sem LaTeX, para aparecerem iguais em qualquer editor ou visualizador.

---

## 1. A ideia em uma frase

> A DFT pega um sinal de **N amostras no tempo** e responde: **"quanto de cada frequência existe nele?"**
> A resposta são **N números complexos** — um por frequência. O módulo diz *quanto*, a fase diz *em que posição* a senoide começa.

No tempo, um som é uma mistura: olhando o gráfico de x[n] não dá para dizer quais tons estão ali. Na frequência, cada tom vira um **pico** separado. É isso que o último exemplo do notebook mostra: 900 Hz + 1200 Hz, que no tempo viram uma curva confusa, aparecem como dois picos limpos.

---

## 2. Pré-requisito: a exponencial complexa (le05)

A fórmula de Euler junta seno e cosseno num único número complexo:

```
e^(jθ) = cos θ + j·sen θ
```

É um ponto no círculo de raio 1 do plano complexo, no ângulo θ. Quando θ cresce, o ponto **gira**. Por isso e^(j·2π·k·n/N), com n = 0, 1, 2, …, é um ponteiro que gira k voltas a cada N amostras: é uma **senoide complexa de frequência k**.

Do le05, duas coisas que a DFT usa o tempo todo:

- **Módulo** |z| = √(a² + b²) → o tamanho (amplitude).
- **Fase** ∠z = ângulo do ponto, calculado com `arctan2(b, a)`, **não** com `arctan(b/a)`, que erra no 2º e no 3º quadrantes (perde o sinal: (−4)/(−3) = 4/3).

---

## 3. As duas fórmulas (o slide "v1 – Signal notation")

**Análise** — do tempo para a frequência:

```
         N-1
X[k]  =   Σ   x[n] · e^(−j·2π·k·n/N)          k = 0, 1, ..., N−1
         n=0
```

**Síntese** — da frequência de volta para o tempo:

```
         1   N-1
x[n]  =  — ·  Σ   X[k] · e^(+j·2π·k·n/N)      n = 0, 1, ..., N−1
         N   k=0
```

### Como ler a análise em palavras

Para **cada** frequência k:

1. gere uma senoide complexa que dá k voltas em N amostras;
2. multiplique amostra por amostra pelo sinal;
3. some tudo.

Se o sinal "anda junto" com aquela senoide, os produtos se somam e |X[k]| fica **grande**. Se não anda, os produtos se cancelam e |X[k]| fica **perto de zero**. A DFT é uma **medida de semelhança** (correlação) entre o sinal e cada uma das N senoides.

### Como ler a síntese em palavras

O sinal é a **soma** das N senoides, cada uma com o peso X[k] que a análise mediu. O fator 1/N e o sinal **+** no expoente são as únicas diferenças em relação à análise.

### Exemplo à mão (está no notebook)

x = [1, 2, 3, 4], N = 4. Com N = 4, o fator e^(−j·2π·n·k/4) = (−j)^(n·k), que só vale 1, −j, −1 ou j:

| k | conta | X[k] |
|---|---|---|
| 0 | 1 + 2 + 3 + 4 | 10 |
| 1 | 1 + 2·(−j) + 3·(−1) + 4·(j) | −2 + 2j |
| 2 | 1 + 2·(−1) + 3·(1) + 4·(−1) | −2 |
| 3 | 1 + 2·(j) + 3·(−1) + 4·(−j) | −2 − 2j |

Duas coisas para apontar ao professor:

- X[0] é a **soma** das amostras: a frequência zero é o "nível médio" (componente DC).
- X[3] = conj(X[1]) (o conjugado: −2 − 2j é o espelho de −2 + 2j): para sinal **real**, a segunda metade do espectro é o espelho da primeira.

---

## 4. As quatro versões do código

O lab pede a **mesma** DFT calculada de quatro jeitos. Todas dão o mesmo resultado (o notebook confere contra `np.fft.fft`: diferença máxima de 10⁻¹¹, só arredondamento). O que muda é **como** a conta é organizada e **quanto custa**.

### v1 — `signal`: a fórmula ao pé da letra

```python
for k in range(N):                    # para cada frequência
    for m in range(N):                # soma sobre as amostras
        X[k] += x[m] * np.exp(-2j * np.pi * k * m / N)
```

Dois laços, exatamente o somatório do slide. São N × N termos: para N = 1024, mais de 1 milhão. É a versão mais lenta (~0,6 s), mas a mais fácil de ler.

### v2 — `basis`: produto interno com a base

```python
for k in range(N):
    e_k  = np.exp(2j * np.pi * k * n / N)   # k-ésimo vetor da base, inteiro
    X[k] = np.vdot(e_k, x)                  # <x, e_k> = Σ x[n] · conj(e_k[n])
```

Mesma conta, outra leitura: as N senoides **e**ₖ formam uma **base** (como os eixos x, y, z, mas com N eixos). X[k] é a **projeção** do sinal no eixo k — o produto interno. O laço interno some porque o `vdot` faz a soma de uma vez. O `conj` aparece porque o produto interno complexo conjuga um dos vetores: é daí que vem o **menos** do expoente.

**Por que funciona:** a base é **ortogonal**. Dois vetores diferentes têm produto interno zero, e cada um com ele mesmo dá N:

```
⟨eₖ, eₗ⟩ = N   se k = l
⟨eₖ, eₗ⟩ = 0   se k ≠ l
```

O notebook confere: ⟨e₃, e₃⟩ = 16 e ⟨e₃, e₅⟩ = 0 para N = 16. Ortogonal quer dizer que uma frequência **não contamina** a medida da outra.

### v3 — `matrix`: multiplicação matriz × vetor

```python
nk = n[:, np.newaxis] @ n[np.newaxis, :]   # tabela de todos os produtos k·n
W  = np.exp(-2j * np.pi * nk / N)          # matriz da DFT
X  = W @ x
```

Os N somatórios viram **uma** multiplicação: **X** = **W**·**x**, onde o elemento da linha k e coluna n de **W** é e^(−j·2π·k·n/N). A célula `A = n @ n.T` do lab mostra o truque: o produto de um vetor-coluna pelo seu transposto gera a tabela de todos os k·n de uma vez:

```
[[ 0  0  0  0  0]
 [ 0  1  2  3  4]
 [ 0  2  4  6  8]
 [ 0  3  6  9 12]
 [ 0  4  8 12 16]]
```

A inversa é fácil por causa da ortogonalidade: **W**·**W**ᴴ = N·**I**, então **W**⁻¹ = **W**ᴴ / N (ᴴ = transposta conjugada). É exatamente a fórmula de síntese.

Rápida para N pequeno (a multiplicação de matrizes do numpy é muito otimizada), mas ocupa N² números de memória: com N = 2¹⁶ seriam 64 GB.

### v4 — `fft`: Cooley-Tukey radix-2 (dividir para conquistar)

```python
Xe = myDFT(x[0::2], version='fft')        # DFT das amostras PARES  (tamanho N/2)
Xo = myDFT(x[1::2], version='fft')        # DFT das amostras ÍMPARES (tamanho N/2)
basis = np.exp(-2j * np.pi * n / N)       # fatores de giro ("twiddle factors")
return np.append(Xe + basis[0:N//2] * Xo,     # X[k]       , k < N/2
                 Xe - basis[0:N//2] * Xo)     # X[k + N/2]
```

A ideia: separar a soma em amostras pares e ímpares. Cada metade é **uma DFT de tamanho N/2**, e as duas se juntam assim (com W = e^(−j·2π/N)):

```
X[k]        = E[k] + Wᵏ · O[k]
X[k + N/2]  = E[k] − Wᵏ · O[k]
```

O **mesmo** par E[k], O[k] serve para duas saídas (só muda o sinal) — é aí que está a economia. A função chama a si mesma (recursão) até sobrar tamanho 2, onde a DFT é só [x₀ + x₁, x₀ − x₁].

- São log₂N níveis de divisão, cada um com ~N operações → custo N·log₂N em vez de N².
- Para N = 1024: N² / (N·log₂N) = 1024/10 ≈ **102× menos operações**. Medido no notebook: a v1 ficou ~73× mais lenta que a nossa FFT.
- **Exige N potência de 2** (radix-2). Com 1000 amostras dá erro; a saída usual é completar com zeros até 1024 (*zero-padding*) — o notebook mostra que o resultado bate com `np.fft.fft(s, 1024)`.

### A inversa (IDFT) nas quatro versões

É a mesma conta com **+** no expoente e **÷ N**. Na versão FFT foi usado um atalho:

```
IDFT{X} = (1/N) · conj( DFT{ conj(X) } )
```

(conjugar, aplicar a DFT, conjugar de novo, dividir por N) — reaproveita a FFT sem escrever outra. As quatro devolvem o sinal original com erro de ~10⁻¹³. A função devolve só a parte real porque o sinal é real; a parte imaginária que sobra é arredondamento.

---

## 5. Interpretando o espectro

### De k para Hz

O índice k não é uma frequência em Hz. A conversão é:

```
fₖ = k · fs / N
```

e Δf = fs / N é a **resolução**: a distância entre dois bins vizinhos. No trem, fs = 8192 Hz e N = 1024 → **8 Hz por bin**.

### Por que só a metade importa

Para sinal real, X[N−k] = conj(X[k]): o módulo é **simétrico** em torno de N/2. Os bins acima de N/2 são as "frequências negativas", espelho das positivas. Toda a informação está em k = 0, …, N/2, que vai de 0 Hz até fs/2 (**frequência de Nyquist**, a maior que a amostragem consegue representar).

O notebook **prova** isso: guarda só 513 dos 1024 coeficientes, reconstrói o resto pela simetria e devolve o sinal com erro de 3 × 10⁻¹⁶.

### O que o espectro do trem mostra

Na metade do espectro aparecem três tons fortes — **704, 888 e 1176 Hz** — e um mais fraco em **2120 Hz**. São as frequências do apito.

### Módulo e fase nos gráficos

- O **módulo** é o gráfico útil: mostra quais frequências existem e com que força.
- A **fase** parece ruído. Nos bins onde o módulo é quase zero, a fase é o ângulo de um número minúsculo, dominado por arredondamento — não carrega informação.

### Teorema de Parseval

A energia é a mesma nos dois domínios:

```
 N-1              1   N-1
  Σ  |x[n]|²  =   — ·  Σ  |X[k]|²
 n=0              N   k=0
```

No trem: **30,264588** dos dois lados. Consequência direta da base ser ortogonal: a DFT só "gira" o sinal para outros eixos, não cria nem perde energia.

---

## 6. Os sinais básicos (o que esperar de cada um)

Com N = 64, o notebook calcula e **confere por código** cada previsão:

| sinal | espectro \|X[k]\| | por quê |
|---|---|---|
| impulso δ[n] | **plano**, 1 em todo k | só n = 0 sobra na soma, e e⁰ = 1: contém todas as frequências por igual |
| degrau (32 uns) | pico 32 em k = 0, zeros em todo k par | X[0] = soma = 32; a forma de "porta" cancela as frequências pares |
| exponencial 0,8ⁿ | máximo 5 em k = 0, decai | soma geométrica: 1/(1 − a) = 5; é um sinal "lento" → passa-baixas |
| senoide de período 8 | **só dois picos**, k = 8 e k = 56, altura 32 | cabem 64/8 = 8 ciclos; o pico vale A·N/2 e aparece espelhado em N − k |
| ruído | espalhado, sem estrutura | em média \|X[k]\|² ≈ N·σ² = 64 (medido: 64,2) |

A regra que aparece nos extremos: **estreito no tempo ↔ largo na frequência**. O impulso (o mais estreito possível) tem o espectro mais largo possível; a senoide (que dura o tempo todo) tem o espectro mais estreito.

---

## 7. O exemplo final: 900 Hz + 1200 Hz

```
x(t) = sen(2π·900·t) + sen(2π·1200·t)
```

**Escolha dos parâmetros** — é a parte que mostra que você entendeu:

- fs = 9600 Hz: maior que 2 × 1200 = 2400 Hz (Nyquist).
- N = 1024: potência de 2, para a versão FFT funcionar.
- Resolução Δf = 9600/1024 = 9,375 Hz, e as frequências caem **exatamente** em bins inteiros: 900/9,375 = 96 e 1200/9,375 = 128.

**Resultado:**

```
k =  96  ->  f =  900 Hz   |X[k]| = 512.0   amplitude = 2|X|/N = 1.00
k = 128  ->  f = 1200 Hz   |X[k]| = 512.0   amplitude = 2|X|/N = 1.00
maior |X[k]| fora desses bins: 1.6e-11   (zero)
```

- Altura do pico = A·N/2 = 1 × 512. Daí a amplitude se recupera com 2·|X[k]|/N.
- **Vazamento espectral (leakage):** se a frequência **não** caísse num bin inteiro (por exemplo fs = 8192, N = 1024 → 900/8 = 112,5), a DFT não teria um bin exatamente em 900 Hz e a energia se **espalharia** pelos vizinhos: o pico ficaria mais baixo e largo. Escolher fs e N para cair em bin inteiro evita isso.

O notebook toca os três sons (900, 1200 e os dois juntos) e mostra: as duas senoides separadas, a soma no tempo (confusa) e o espectro (dois picos limpos).

---

## 8. Perguntas que o professor pode fazer

**Por que o resultado da DFT é complexo se o sinal é real?**
Porque cada X[k] guarda duas informações: módulo (quanto daquela frequência) e fase (onde a senoide começa). Um número complexo carrega as duas.

**Por que as quatro versões dão o mesmo resultado?**
Porque são a mesma soma organizada de jeitos diferentes: laço duplo, produto interno, produto matriz-vetor e dividir-para-conquistar. A diferença é só de custo.

**Por que a FFT é mais rápida?**
Ela divide a DFT de tamanho N em duas de tamanho N/2 (pares e ímpares) e reaproveita cada resultado para duas saídas. Repetindo até o fim, são log₂N níveis de N operações: N·log N em vez de N².

**Por que a FFT exige N potência de 2?**
Porque ela divide ao meio a cada nível até chegar a 2. Para outro N, completa-se com zeros (zero-padding).

**O que é X[0]?**
A soma de todas as amostras: a componente de frequência zero (o nível médio, DC).

**Por que plotar só a metade do espectro?**
Para sinal real, X[N−k] = conj(X[k]): a segunda metade é o espelho da primeira. A metade 0 … N/2 (0 a fs/2) tem tudo; o notebook reconstrói o sinal só com ela.

**Como transformo k em Hz?**
f = k·fs/N. A resolução é fs/N.

**O que é vazamento espectral?**
Quando a frequência do sinal não cai num bin inteiro, a energia se espalha pelos bins vizinhos.

**Por que a síntese tem 1/N?**
Porque a base não é normalizada: ⟨eₖ, eₖ⟩ = N. Sem dividir por N o sinal voltaria N vezes maior.

**Por que `arctan2` e não `arctan` na fase?**
O `arctan(b/a)` perde os sinais de a e b e erra no 2º e no 3º quadrantes; o `arctan2(b, a)` olha os dois.

---

## 9. Roteiro de 3 minutos para explicar

1. **O que é** (30 s): "A DFT mede quanto de cada frequência há num sinal de N amostras. Ela compara o sinal com N senoides complexas e devolve N números: o módulo é a força, a fase é a posição."
2. **As fórmulas** (30 s): mostrar análise e síntese; "a síntese é a mesma conta com + no expoente e ÷ N". Fazer o exemplo [1, 2, 3, 4] → [10, −2+2j, −2, −2−2j].
3. **As quatro versões** (60 s): laço duplo → produto interno com a base (que é ortogonal) → matriz **W**·**x** → FFT pares/ímpares. "Todas dão o mesmo resultado; a FFT custa N·log N em vez de N² — cerca de 100× menos para 1024 pontos."
4. **Interpretação** (30 s): f = k·fs/N; só a metade importa por simetria; o trem tem tons em 704, 888 e 1176 Hz.
5. **Exemplo final** (30 s): 900 + 1200 Hz; no tempo é confuso, na frequência são dois picos em k = 96 e k = 128; escolhi fs e N para cair em bin inteiro e evitar vazamento.

---

## 10. Onde está cada coisa

| arquivo | o que tem |
|---|---|
| `le06_DFT/le06_01_DFT-four-versions.ipynb` | o lab completo, executado, com áudio e gráficos |
| `le06_DFT/le06_v1_signal_notation.py` | a v1 do slide em Python puro; toca o som do trem original e reconstruído |
| `le06_DFT/le06_duas_frequencias.py` | 900 + 1200 Hz em script, com som (fs = 8000, N = 800, Δf = 10 Hz) |
| `le05_complex-exponentials/` | números complexos: módulo, fase, j^j (pré-requisito) |
| `LE06_TAREFA_DUAS_FREQUENCIAS.md` | preparação focada na tarefa de aula: código para digitar, variações, fala de 1 minuto |
