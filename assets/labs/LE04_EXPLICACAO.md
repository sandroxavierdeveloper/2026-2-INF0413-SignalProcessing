# LE04 — Do digital ao som, e o algoritmo de Karplus-Strong, explicados

Texto de estudo dos dois notebooks de `le04_karplus-strong/`:

1. `le04_01_signal-reconstruction.ipynb` — criar um tom com frequência e duração controladas, plotar no tempo e **provar a frequência com a FFT**.
2. `le04_karplus-strong.ipynb` — sintetizar som de **corda de violão** com um laço de realimentação (Karplus-Strong) e tocar acordes famosos.

Os números citados foram conferidos no Python. A seção 4 lista **o que foi corrigido no notebook** em relação à versão original — vale saber, caso o professor compare.

As fórmulas estão escritas com caracteres comuns (Σ, π, ², ·), sem LaTeX, para aparecerem iguais em qualquer editor ou visualizador.

---

## 1. A ideia em duas frases

> **Parte 1:** um sinal digital é só uma lista de números x[n]; ele vira **som** quando dizemos **quantas amostras por segundo** tocar (fs). A frequência que se ouve depende de **quantas amostras cabem num período**: f = fs/P.
>
> **Parte 2:** se você pega um pedaço de **ruído** de M amostras e o repete sem parar, ele vira uma **nota** de frequência fs/M. Se a cada repetição ele perde um pouco de energia, soa como uma **corda dedilhada**.

---

## 2. Parte 1 — `le04_01_signal-reconstruction.ipynb`

### 2.1 As três relações que o lab inteiro usa

| relação | significado |
|---|---|
| x[n] = A·sen(2π·n/P + φ) | senoide discreta: repete a cada P amostras |
| f = fs / P  ⇔  P = fs / f | frequência (Hz) ↔ período (amostras) |
| d = N·Ts = N / fs  ⇔  N = d·fs | duração (s) ↔ número de amostras |

Ts = 1/fs é o tempo entre duas amostras, e o instante da amostra n é t = n·Ts = n/fs.

### 2.2 `create_sine_signal(f, dur, fs)`

```python
N = int(dur * fs)          # quantas amostras para durar 'dur' segundos
P = fs / f                 # quantas amostras por período
n = np.arange(N)
x = np.sin(2 * np.pi / P * n)
```

Com f = 220 Hz, d = 1,5 s e fs = 48 kHz:

- P₁ = 48000/220 = 218,18 amostras por período (não precisa ser inteiro — o seno aceita qualquer valor);
- N₁ = 1,5 × 48000 = 72000 amostras;
- **frequência audível = 220 Hz** (nota Lá 3).

### 2.3 "Se mudar a frequência de amostragem, o que acontece?" — duas respostas diferentes

1. **Gerando de novo com outro fs** (a função recalcula P e N): o som **não muda** — continua 220 Hz e 1,5 s. Muda só a quantidade de amostras: com fs = 24 kHz, P = 109,09 e N = 36000.
2. **Tocando o mesmo x[n] com outro fs**: o som **muda**. Com 2·fs, as mesmas amostras passam duas vezes mais rápido — o tom sobe **uma oitava** (440 Hz) e dura **metade** (0,75 s). É o efeito "esquilo" de acelerar uma gravação.

### 2.4 O mesmo tom com a primitiva `SIGNALgenerate` (do le03)

Com fs = 44,1 kHz (padrão do CD): P₂ = 200,45 e N₂ = 66150. Comparando com o anterior: **mesma frequência e mesma duração** (N/fs = 1,5 s nos dois), só que com **menos amostras por período**, porque fs é menor.

### 2.5 Plotar no tempo e recortar

- Eixo em segundos: `t = n / fs`.
- **1 período** = recortar `ceil(P)` amostras; **2,5 períodos** = `round(2.5 * P)` amostras.
- O recorte é necessário porque 72000 amostras num gráfico viram um borrão.

### 2.6 Desafio — `SIGNALtone(f, dur)`

```python
fs = 44.1e3
x, _ = SIGNALgenerate(int(dur * fs), 'osc', period=fs / f)
```

É o `create_sine_signal` reaproveitando a biblioteca: N = d·fs e período P = fs/f, com fs fixo no padrão do CD. O notebook testa com 330 Hz e 3 s, como pede o enunciado.

### 2.7 "Revelando a velocidade dos sinais" — a FFT como prova

Como provar que o tom gerado tem mesmo a frequência pedida? Com a **FFT** (a DFT rápida — o le06 explica por dentro).

1. `X = np.fft.fft(x)` e `Xmag = np.abs(X)` → o **módulo** mostra quanto de cada frequência existe.
2. **Metade**: o espectro de um sinal real é simétrico; os dois picos são espelhos. Basta `Xmag[:N//2]`.
3. **Eixo em Hz**: o índice vira frequência com

   ```
   f = (n / N) · fs
   ```

4. Recorte no domínio da frequência: `xlim=[0, 1100]` para enxergar o pico.

### 2.8 Um sinal com quatro frequências (200, 400, 600, 800 Hz)

Soma de quatro senoides, 1 s a 44,1 kHz. No tempo, a forma de onda é complexa; no espectro, **quatro picos exatamente em 200, 400, 600 e 800 Hz**, cada um de altura N/2 = 22050. É a mesma ideia da tarefa 900 + 1200 Hz do le06.

- O notebook usou `phase=-np.pi/2`, que transforma sen em −cos. Por isso `x[1] ≈ −3,99`: no início as quatro valem quase −1 e somam quase −4.
- X[0] ≈ 10⁻¹¹: a média do sinal é zero, não há componente DC.

### 2.9 Bônus — `SIGNALwaveform`: um período de ruído repetido

```python
P = int(np.round(fs / f))                  # período em amostras
waveform, _ = SIGNALgenerate(P, 'random')  # UM período de ruído
x = np.concatenate([waveform] * reps)[:N]  # repetido até a duração
```

**O que tem de diferente no espectro:** o tom senoidal dá **um** pico; esta forma de onda dá picos na fundamental (**110 Hz**) **e em todos os harmônicos** (220, 330, 440 Hz…), cada um com altura aleatória.

**Por quê:** todo sinal periódico de período P se decompõe em senoides de frequências fs/P, 2·fs/P, 3·fs/P, … (série de Fourier). A **altura** dos harmônicos é o que distingue um instrumento do outro: é o **timbre**. A mesma nota no violão e no piano tem os mesmos harmônicos com alturas diferentes.

Detalhe: P = 44100/110 = 400,9 é arredondado para 401, então a frequência real é 44100/401 = 109,98 Hz.

Essa é exatamente a ponte para a Parte 2: **um pedaço de ruído repetido vira uma nota**.

---

## 3. Parte 2 — `le04_karplus-strong.ipynb`

### 3.1 KS_1 — repetir o buffer

```python
y = x
while len(y) < N:
    y = np.append(y, x)
```

Um buffer de M = 50 números aleatórios, repetido até 2 segundos. Com fs = 16000 Hz, ele cabe 16000/50 = 320 vezes por segundo:

```
f₀ = fs / M = 16000 / 50 = 320 Hz   (≈ E4)
```

**Dobrar o buffer** (M = 100) dá metade da frequência (160 Hz): **uma oitava abaixo**. **Metade do buffer** (M = 25) → 640 Hz, uma oitava acima.

### 3.2 Perguntas do notebook

1. **Qual distribuição segue x[n]?** `np.random.randn` → **Normal (Gaussiana)**, média 0 e variância 1.
2. **E se mudar a distribuição?** A **altura da nota não muda** — ela depende só de M. O que muda é o **timbre**: a distribuição define as alturas dos harmônicos do primeiro período (seção 2.9).

### 3.3 KS_2 — a mesma coisa como sistema com realimentação

```
y[n] = x[n] + y[n − M]
```

Lendo: "a saída agora é a entrada mais **a própria saída de M amostras atrás**". Como x[n] só existe nos primeiros M instantes, depois disso cada amostra é a cópia da de um período antes — idêntico ao KS_1, mas escrito como **laço de realimentação** (o diagrama de blocos do notebook: um atraso de M amostras que volta para a soma). É um sistema **recursivo** (filtro IIR): a saída depende de saídas passadas.

### 3.4 KS_3 — o decaimento α: soa como violão

```
y[n] = x[n] + α · y[n − M]          0 < α < 1
```

A cada volta no laço o sinal é multiplicado por α: a nota **morre aos poucos**, como uma corda que perde energia por atrito e pelo som que irradia. Desenrolando o laço:

```
y[n] = α^⌊n/M⌋ · x[n mod M]
```

"o buffer original (x[n mod M]), atenuado por α uma vez a cada período que já passou (⌊n/M⌋ voltas)".

- α = 0,99: decaimento longo, corda solta.
- α = 0,85: decaimento curto, corda abafada.

O notebook também mostra uma **variação**, o `KS_media`: o Karplus-Strong original de 1983, que além de atenuar tira a média de duas amostras vizinhas, y[n] = α·(y[n−M] + y[n−M−1])/2. A média é um filtro passa-baixas — os agudos morrem antes e soa mais como corda real — e atrasa meia amostra: com M = 50, a nota sai em fs/(M + 0,5) = 316,8 Hz.

### 3.5 Por que precisa compensar α (a versão final `KS`)

O sinal perde um fator α **por período**, e notas agudas têm **mais períodos por segundo**. Em 1 segundo, com α = 0,99:

| M | nota | voltas por segundo | sobra após 1 s (α^(fs/M)) |
|---|---|---|---|
| 100 | 160 Hz | 160 | 0,20 |
| 50 | 320 Hz | 320 | 0,04 |
| 25 | 640 Hz | 640 | 0,0016 |

A nota aguda morre **25× mais rápido** que a de 320 Hz — num acorde, as agudas sumiriam primeiro. O notebook mostra isso com M = 50 e M = 25, com o gráfico dos dois envelopes. A versão final ajusta α pelo tamanho do buffer:

```python
a = alpha ** (M / buff_size)      # buff_size = 50 = referência
```

Com isso, **todas as notas sobram 0,04 após 1 segundo**, qualquer que seja M.

### 3.6 Tocando acordes

**Notas → frequências** (temperamento igual, A4 = 440 Hz, n = meios-tons de distância até A4):

```
f(n) = 440 · 2^(n/12)
```

Cada oitava acima dobra a frequência (2^(12/12) = 2). `nota2freq('D2')` = 73,42 Hz.

**Cada nota = um KS** com M = round(fs/f) e um buffer de ruído próprio. O acorde é a **soma** (superposição) das notas, cada uma com seu **ganho**; no fim o sinal é **normalizado** (dividido pelo pico) para não passar de 1 e distorcer (*clipping*). No acorde dos Beatles, o D2 do baixo tem ganho 1,5 e α = 0,998, para soar mais forte e por mais tempo.

| acorde | notas |
|---|---|
| *A Hard Day's Night* (Beatles) | D2, D3, F3, G3, F4, A4, C5, G5 |
| **Desafio 1** — Hendrix (E7♯9, *Purple Haze*) | E2, E3, G♯3, D4, G4 |
| **Desafio 2** — acorde místico (Scriabin) | C3, F♯3, B♭3, E4, A4, D5 |

O voicing do Hendrix corresponde ao desenho na guitarra 0-7-6-7-8-x: E2 (6ª corda solta), E3, G♯3, D4, G4.

### 3.7 Teste final — "o que está acontecendo aqui?"

```python
a = np.random.rand(100)
b = np.random.rand(80)
c = np.concatenate((a, a, a, a)) + np.concatenate((b, b, b, b, b))   # 400 amostras
KS_1(c, 2*fs)
```

**Resposta:**

- `a` repetido 4× é um sinal de **período 100** → nota de 16000/100 = 160 Hz.
- `b` repetido 5× é um sinal de **período 80** → nota de 16000/80 = 200 Hz.
- A soma tem 400 amostras, e 400 é o **mínimo múltiplo comum** de 100 e 80, então `c` é um período completo das duas. O KS_1 repete `c`, mantendo as duas periodicidades.
- **Ouve-se duas notas ao mesmo tempo**: 160 e 200 Hz, razão 200/160 = 5/4 — uma **terça maior**. É um acorde de duas notas feito com **um só** buffer.
- **Conferido no espectro:** todos os picos são múltiplos de 160 Hz ou de 200 Hz (alguns, como 800 e 4800 Hz, são múltiplos dos dois).

---

## 4. O que foi corrigido no notebook (09/10/2026)

Estes pontos foram achados conferindo o notebook e já estão corrigidos. Vale saber o que mudou, caso o professor compare com a versão original.

1. **`le04_01`, desafio `SIGNALtone`:** o enunciado pede 330 Hz com 3 s, e o código usava `f = 220.0`. Agora é `f = 330.0`.

2. **`KS_3` era redefinido no meio do notebook.** A célula do gráfico do envelope trocava a fórmula do slide (y[n] = x[n] + α·y[n−M]) pelo Karplus-Strong original de 1983, que também tira a média de duas amostras vizinhas — e todas as células seguintes passavam a usar essa outra versão sem avisar. Agora o `KS_3` fica sendo a fórmula do slide, e a versão com média virou uma função própria, **`KS_media`**, numa seção "Variação: o Karplus-Strong original (1983), com média", que toca as duas para comparar.

3. **As duas células "quanto mais alto o tom, mais rápido o decaimento" eram idênticas** (M = 50 nas duas). Agora uma usa M = 50 (320 Hz) e a outra M = 25 (640 Hz), e um gráfico mostra os dois envelopes. Medido: após 1 s sobra 0,04 da amplitude com M = 50 e só 0,0016 com M = 25 — 25 vezes menos.

4. **Ganho e sustentação do baixo:** o texto dizia que cada nota tinha um ganho e que o D2 soava mais tempo, mas o código usava ganho 1 e o mesmo α para tudo. Agora o `ks_acorde` aceita ganho por nota e um α próprio por nota (`sustentar`): D2 com ganho 1,5 e α = 0,998, G5 com ganho 0,6, as demais com 1,0 e α = 0,99.

5. **Comentários sobre outro projeto removidos:** havia um comentário no `ks_acorde` e uma seção final sobre um software sem relação com a disciplina.

6. **Resposta do "Teste final" reescrita:** a anterior falava em "filtro comb", mas o `KS_1` só repete, não filtra. A resposta nova (seção 3.7) vem com a conferência no espectro.

7. **Afinação:** como M precisa ser inteiro, a nota sai em fs/M, nem sempre a frequência pedida. Isso é limitação do algoritmo, não erro de código, então não foi "consertado" — foi **medido**: uma tabela nova mostra o erro em *cents* (1/100 de semitom; acima de ~10 cents já se percebe). Os graves ficam quase exatos (D2: −0,5 cent); os agudos desafinam: A4 sai 444,4 Hz (+17 cents), C5 516,1 Hz (−24 cents), G5 800 Hz (+35 cents).

Também foi corrigido o `KS_1`, que cortava o resultado com `y[0:N+1]` e podia devolver uma amostra a mais que o pedido; agora é `y[0:N]`.

---

## 5. Perguntas que o professor pode fazer

**Como se calcula a frequência de um tom digital?** f = fs/P: amostras por segundo dividido por amostras por período.

**O que acontece se eu tocar o mesmo sinal com o dobro de fs?** Sobe uma oitava e dura metade.

**Por que só metade do espectro?** Para sinal real, a segunda metade é espelho da primeira.

**Como transformo o índice da FFT em Hz?** f = (n/N)·fs.

**Por que a forma de onda aleatória tem vários picos e o seno só um?** Todo sinal periódico é soma da fundamental com seus harmônicos; o seno é o único que só tem a fundamental. As alturas dos harmônicos são o timbre.

**Por que um buffer de ruído repetido vira nota?** Porque repetir torna o sinal periódico, com período M; a frequência é fs/M. O ruído só define o timbre.

**O que o α faz?** Atenua o sinal a cada volta no laço: é o decaimento da corda.

**Por que compensar o α?** Porque ele age por período, e notas agudas têm mais períodos por segundo — sem compensar, elas morrem mais rápido.

**Como se calcula a frequência de uma nota?** 440·2^(n/12), com n meios-tons a partir do A4.

**Por que normalizar o acorde?** A soma de várias notas pode passar de 1 e distorcer (*clipping*).

**Por que as notas agudas saem desafinadas?** Porque M = round(fs/f) tem de ser inteiro; quanto menor M, maior o erro relativo do arredondamento.

---

## 6. Roteiro de 3 minutos

1. **Tom digital** (40 s): "um sinal digital vira som com fs; a frequência é fs/P e a duração N/fs. Gerei 220 Hz por 1,5 s: P = 218, N = 72000 a 48 kHz."
2. **Provando com a FFT** (40 s): "o espectro tem um pico só em 220 Hz; com 200+400+600+800 Hz, quatro picos. Mostro só a metade e converto o índice em Hz com f = n·fs/N."
3. **Ruído repetido vira nota** (40 s): "um período de ruído repetido dá a fundamental e todos os harmônicos — é o timbre. O Karplus-Strong usa isso: M amostras de ruído repetidas dão fs/M = 320 Hz com M = 50."
4. **A corda** (40 s): "y[n] = x[n] + α·y[n−M]: a realimentação repete, o α faz a nota morrer. Como ele age por período, compensei com α^(M/50) para todas as notas decaírem igual."
5. **Acordes** (20 s): "cada nota é um KS com M = fs/f, f = 440·2^(n/12); o acorde é a soma normalizada."

---

## 7. Onde está cada coisa

| arquivo | o que tem |
|---|---|
| `le04_karplus-strong/le04_01_signal-reconstruction.ipynb` | tom com frequência e duração, FFT, quatro frequências, forma de onda aleatória |
| `le04_karplus-strong/le04_karplus-strong.ipynb` | KS_1 → KS_2 → KS_3 → KS, KS_media, acordes, tabela de afinação, desafios, teste final |
| `le04_karplus-strong/figures/` | as figuras de referência do professor (`sine_*`, `spec_*`, `ks.png`) |
| `LE05_EXPLICACAO.md` | o próximo lab: números complexos |
| `LE06_DFT_EXPLICACAO.md` | a FFT por dentro (DFT em quatro versões) |
