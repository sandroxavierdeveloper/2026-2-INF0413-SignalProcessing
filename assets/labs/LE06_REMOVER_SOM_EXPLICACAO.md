# Remover um som com a DFT — violão + guitarra → só o violão

Explicação detalhada da tarefa de aula de separação de som do lab 6: o que foi pedido, a ideia, cada passo do código,
os números medidos, como foi conferido, os limites do método e como apresentar.

As fórmulas estão em caracteres comuns (Σ, π, ², ·), sem LaTeX, para aparecerem iguais em qualquer editor.

**Onde está:**

| arquivo | o quê |
|---|---|
| `le06_DFT/le06_01_DFT-four-versions.ipynb` | seção **"Remover um som com a DFT: violão + guitarra → só o violão"**, células 53 a 60 |
| `le06_DFT/le06_remover_guitarra.py` | a mesma tarefa em script Python, com som pelo alto-falante |
| `LE06_TAREFA_DUAS_FREQUENCIAS.md`, parte 2 | versão curta, para revisar antes da aula |

---

## 1. O que foi pedido

> Gerar um sinal oscilatório com duas frequências, admitindo que uma delas é outro som que se quer remover, para o
> final ficar puro. Por exemplo: o som conjunto de um violão e uma guitarra, do qual se exclui a guitarra. Uma das
> frequências é gerada com `osc`. Usar a DFT. A saída deve ter apenas uma frequência.

Traduzindo para o que foi feito:

| instrumento | frequência | como é gerado | papel |
|---|---|---|---|
| violão | 900 Hz | `np.sin` direto | o som que **fica** |
| guitarra | 1200 Hz | primitiva `osc` da biblioteca do curso (`SIGNALgenerate`) | o som que **sai** |

Cada instrumento é representado por **uma senoide pura**. Um instrumento de verdade é mais complicado (seção 10), mas
a ideia é a mesma.

---

## 2. Vocabulário: os conceitos usados nesta tarefa

Em ordem de leitura: cada termo usa os anteriores.

### O sinal

**Sinal** — uma grandeza que varia: aqui, a pressão do ar que vira som. No computador ele é uma **lista de números**.

**Amostra** — cada número da lista, x[n]. O índice **n** (0, 1, 2, …) diz a posição da amostra.

**Frequência de amostragem (fs)** — quantas amostras por segundo. fs = 8192 Hz significa 8192 números para cada segundo
de som. A amostra n acontece no instante **t = n/fs**.

**Senoide** (ou **sinal oscilatório**) — o sinal sen(2π·f·t): sobe e desce suavemente, repetindo sempre igual. É o som
mais simples que existe, um tom puro. Nesta tarefa, o violão e a guitarra são, cada um, uma senoide.

**Frequência (f)**, em **hertz (Hz)** — quantas vezes por segundo a senoide se repete. 900 Hz = 900 ciclos por segundo.
Frequência alta = som agudo; baixa = grave. A guitarra (1200 Hz) é mais aguda que o violão (900 Hz).

**Período (P)** — o tamanho de um ciclo. Em segundos, 1/f; em amostras, **P = fs/f**. A guitarra tem período de
8192/1200 = 6,83 amostras.

**Amplitude (A)** — a altura da senoide: o volume. As duas senoides daqui têm A = 1.

**`osc`** — o nome, na biblioteca do curso, do gerador de senoide (*oscilador*): `SIGNALgenerate(N, 'osc', period=P)`
devolve A·sen(2π·n/P + φ).

**Mistura** (ou **superposição**) — a soma de dois sinais amostra por amostra: mistura[n] = violão[n] + guitarra[n]. É
o que acontece no ar quando dois instrumentos tocam juntos: as pressões se somam.

**Teorema da amostragem (Nyquist)** — para representar uma frequência f, é preciso fs > 2·f. A maior frequência que
fs consegue representar é **fs/2** (a *frequência de Nyquist*). Aqui, fs/2 = 4096 Hz, folgado para 1200 Hz.

**Aliasing** — o que acontece quando Nyquist é violado: a frequência alta aparece disfarçada de outra, mais baixa.
Não acontece nesta tarefa, mas é a razão de escolher fs com folga.

### Os dois domínios

**Domínio do tempo** — o sinal visto como "valor em cada instante", x[n]. É como o som chega ao microfone.

**Domínio da frequência** — o mesmo sinal visto como "quanto de cada frequência ele tem". É como o ouvido percebe
(distinguimos notas, não amostras).

**Espectro** — o gráfico do domínio da frequência: no eixo horizontal as frequências, no vertical quanto de cada uma.
Um tom puro aparece como um **pico** só.

### A transformada

**Número complexo** — um número com duas partes, a + b·j (com j² = −1). Pode ser visto como uma **seta** no plano:
**módulo** = tamanho da seta, **fase** = ângulo dela.

**Módulo** — |z| = √(a² + b²). No espectro, o módulo de X[k] diz **quanto** da frequência k existe.

**Fase** — o ângulo da seta. No espectro, diz **onde** a senoide começa. Nesta tarefa ela não é usada: só importa
apagar ou manter.

**Conjugado** — conj(a + b·j) = a − b·j: a mesma seta, espelhada no eixo horizontal.

**Exponencial complexa** — e^(jθ) = cos θ + j·sen θ (fórmula de Euler): uma seta de tamanho 1 no ângulo θ. Quando θ
cresce com o tempo, a seta **gira** — e^(jωn) é uma "senoide complexa".

**DFT (Transformada Discreta de Fourier)** — a conta que leva o sinal do tempo para a frequência:
X[k] = Σ x[n]·e^(−j·2π·k·n/N). Compara o sinal com N senoides e diz quanto de cada uma ele contém. O resultado são N
números complexos.

**IDFT (DFT inversa)** — a conta de volta, da frequência para o tempo: soma as senoides com os pesos X[k]. Aplicar
DFT e depois IDFT devolve o sinal original.

**FFT (Fast Fourier Transform)** — um jeito **rápido** de calcular a mesma DFT (Cooley-Tukey: divide o sinal em
amostras pares e ímpares, recursivamente). Mesmo resultado, custo N·log₂N em vez de N². Exige N potência de 2.

**N** — o número de amostras que entram na DFT. Também é o número de bins que saem.

**Bin** — é o conceito mais usado neste texto. A palavra é inglesa e quer dizer **caixa** ou **compartimento**
(como as caixas de separar parafusos por tamanho). Em processamento de sinais, cada bin é **uma posição do resultado da
DFT**: o número X[k], com k = 0, 1, …, N − 1.

- **Quantos bins existem:** a DFT de N amostras devolve **N bins**, um para cada valor de k. Aqui N = 8192, então
  X tem 8192 bins.
- **O que cada bin guarda:** um número complexo cujo **módulo** diz quanto do sinal está naquela frequência. Se
  |X[k]| é grande, o sinal tem muito daquela frequência; se é zero, não tem nada.
- **A que frequência cada bin corresponde:** o bin k representa a frequência **k·Δf** (Δf é a resolução, definida
  logo abaixo). É como uma régua com marcas a cada Δf Hz: o bin 0 é a marca de 0 Hz, o bin 1 a de Δf, o bin 2 a de
  2·Δf, e assim por diante.
- **O índice é inteiro:** existe o bin 1200, mas não existe o bin 1200,5. Por isso uma frequência pode "cair num bin
  exato" (quando f/Δf dá inteiro) ou "cair entre dois bins" (quando não dá — e aí acontece o vazamento espectral).
- **Metade dos bins é espelho:** para sinal real, os bins de N/2 + 1 até N − 1 repetem os de 1 até N/2 espelhados
  (as frequências negativas). Os bins com informação nova são os de 0 até N/2 = 4096, que vão de 0 Hz até fs/2.
- **Por que o nome "caixa":** a DFT separa a energia do sinal em N caixas, uma por frequência. Uma senoide pura cujo
  f/Δf é inteiro coloca toda a energia numa caixa só (e no espelho).

**Os bins desta tarefa** (Δf = 1 Hz, então bin k = k Hz):

| bin k | frequência | o que tem dentro | \|X[k]\| |
|---|---|---|---|
| 0 a 899 | 0 a 899 Hz | nada | 0 |
| **900** | 900 Hz | o violão | 4096 |
| 901 a 1199 | 901 a 1199 Hz | nada | 0 |
| **1200** | 1200 Hz | a guitarra — **zerado na remoção** | 4096 → 0 |
| 1201 a 6991 | (inclui de 1201 Hz até Nyquist e o começo do espelho) | nada | 0 |
| **6992** | espelho de 1200 Hz (8192 − 1200) | a outra seta da guitarra — **zerado na remoção** | 4096 → 0 |
| 6993 a 7291 | espelho | nada | 0 |
| **7292** | espelho de 900 Hz (8192 − 900) | a outra seta do violão | 4096 |
| 7293 a 8191 | espelho | nada | 0 |

Remover a guitarra é exatamente isto: zerar o que está dentro dos bins 1200 e 6992 e deixar todos os outros como
estão.

**Resolução (Δf)** — a distância em Hz entre dois bins vizinhos: **Δf = fs/N**. O bin k corresponde à frequência
**k·Δf**. Aqui Δf = 8192/8192 = 1 Hz: o bin 1200 é exatamente 1200 Hz. Com N maior a régua tem marcas mais juntas
(resolução mais fina); com N menor, marcas mais espaçadas. No script, fs = 8000 e N = 800 dão Δf = 10 Hz, e a guitarra
fica no bin 120 (= 1200/10).

**Frequência negativa** / **espelho** — um seno real é a soma de duas setas girando em sentidos opostos. A DFT mostra
uma no bin k e a outra no bin **N − k**. Por isso o espectro de um sinal real é espelhado e só a metade 0 … N/2 é
"nova".

**Simetria conjugada** — o nome formal do espelho: para sinal real, X[N − k] = conj(X[k]). Se um lado é mexido e o
outro não, a simetria quebra e a IDFT devolve um sinal **complexo** — que não é um som.

**Linearidade** — a DFT de uma soma é a soma das DFTs: DFT{a + b} = DFT{a} + DFT{b}. É o que garante que, apagando a
parte da guitarra, sobra exatamente a do violão.

### A operação

**Filtro** — um sistema que deixa passar umas frequências e bloqueia outras.

**Filtro rejeita-faixa** (ou ***notch***) — o filtro que bloqueia uma frequência (ou faixa estreita) e deixa passar todo
o resto. É o que esta tarefa construiu.

**Filtragem no domínio da frequência** — fazer o filtro do jeito desta tarefa: DFT, zerar bins, IDFT.

**Vazamento espectral** (*leakage*) — quando a frequência do sinal cai **entre** dois bins (f/Δf não inteiro), a
energia dela se espalha pelos bins vizinhos em vez de ficar num só. Aí zerar um bin não remove a frequência inteira.

**Janela** (*window*) — uma curva suave que multiplica o sinal antes da DFT, para concentrar o vazamento. Não usada
aqui, porque os parâmetros foram escolhidos para não haver vazamento.

**Bloco** — um pedaço do sinal processado de cada vez (no script, 800 amostras). Permite usar uma DFT lenta em sinais
longos.

**Ciclo inteiro** — um bloco que contém um número inteiro de períodos de cada senoide. Assim cada bloco começa e
termina "no mesmo ponto" da onda e os blocos se emendam sem degrau.

### O som de verdade

**Fundamental** — a frequência principal de uma nota (a que dá o nome à nota).

**Harmônicos** — frequências múltiplas da fundamental (2×, 3×, 4×…) que um instrumento real produz junto.

**Timbre** — a "cor" do som, dada pela altura de cada harmônico. É o que diferencia um violão de uma guitarra tocando
a mesma nota.

### A conferência

**Ponto flutuante** — o formato em que o computador guarda números reais, com cerca de 16 dígitos de precisão.

**Erro de arredondamento** — a diferença minúscula (10⁻¹³, 10⁻¹⁶) que aparece porque cada conta em ponto flutuante
arredonda o último dígito. Um erro desse tamanho significa "igual".

---

### Juntando os conceitos

O objetivo era gerar um som com duas fontes e depois separá-las. Comecei pelo **seno**, a função que sobe e desce suavemente, e com ele criei duas **senoides**, cada uma um tom puro com frequência própria: 900 Hz para o violão e 1200 Hz para a guitarra, esta gerada com o `osc`. O computador guarda cada senoide como uma sequência de **amostras**, 8192 números por segundo. Somando as duas amostra por amostra, obtive a **mistura**, o som das duas fontes tocando juntas. Nela, cada amostra é um único número em que não dá mais para saber quanto veio de cada instrumento, e por isso não há como separá-las olhando o tempo. A separação acontece na frequência. A DFT distribui a mistura em 8192 **bins**, caixas de 1 Hz cada, e como as duas fontes têm frequências diferentes, cada uma cai numa caixa diferente: o violão no bin 900 e a guitarra no bin 1200, além dos espelhos em 7292 e 6992. Para remover a guitarra, basta zerar os bins 1200 e 6992 e voltar ao tempo com a IDFT. O resultado é uma senoide de 900 Hz igual ao violão original: as duas fontes, misturadas no tempo, ficaram separáveis na frequência.

---

## 3. A ideia em uma frase

> No tempo, os dois sons estão misturados **em cada amostra** e não dá para separá-los. Na frequência, cada um é um
> **pico num lugar diferente**. Então: vai para a frequência (DFT), apaga o pico da guitarra, volta para o tempo
> (IDFT).

### Por que no tempo não dá

Cada amostra da mistura é uma soma:

```
mistura[n] = violão[n] + guitarra[n]
```

Olhando só o número `mistura[n]`, não há como saber quanto dele veio de cada instrumento — infinitas combinações dão a
mesma soma. Não existe "a amostra da guitarra" para apagar.

### Por que na frequência dá

A DFT reescreve o sinal como uma soma de senoides, uma por frequência:

```
         N-1
X[k]  =   Σ   x[n] · e^(−j·2π·k·n/N)
         n=0
```

Cada X[k] diz **quanto da frequência k** existe no sinal. Como o violão e a guitarra têm frequências diferentes, eles
caem em **bins diferentes** de X — ficam separados. Apagar a guitarra vira zerar os números do bin dela.

E como a DFT é **linear**, a DFT da mistura é a soma das DFTs:

```
DFT{violão + guitarra} = DFT{violão} + DFT{guitarra}
```

Zerar os bins da guitarra deixa exatamente DFT{violão}, e a IDFT disso é o violão.

Isto é um **filtro**: um sistema que deixa passar algumas frequências e bloqueia outras. Este é do tipo mais seletivo
possível — remove uma frequência exata e não encosta em nenhuma outra.

---

## 4. A escolha dos parâmetros

```
fs = 8192 Hz      N = 8192 amostras (1 segundo)      Δf = fs/N = 1 Hz
```

Cada escolha tem um motivo:

| escolha | por quê |
|---|---|
| fs = 8192 Hz | maior que 2 × 1200 = 2400 Hz (Nyquist): as duas frequências podem ser representadas |
| N = fs (1 s de som) | dá para **ouvir** a mistura e a saída; com 1024 amostras seria 0,12 s, quase um estalo |
| N = 8192 = 2¹³ | é potência de 2, então a versão `fft` do lab processa o segundo inteiro de uma vez |
| Δf = 1 Hz | o bin k corresponde exatamente a k Hz: a guitarra cai **exatamente** no bin 1200 e o violão no 900 |

O último ponto é o mais importante. Se a frequência caísse **entre** dois bins (por exemplo 1200,5 Hz com Δf = 1 Hz),
a energia dela se espalharia pelos bins vizinhos — o **vazamento espectral** — e zerar um bin só não bastaria
(seção 9 mede isso).

---

## 5. O código, passo a passo (notebook)

### 4.1 Gerar os sons e a mistura

```python
fs3 = 8192
N3  = fs3
df3 = fs3 / N3                                   # 1 Hz por bin

f_violao, f_guitarra = 900, 1200

n3 = np.arange(N3)
violao      = np.sin(2 * np.pi * f_violao * n3 / fs3)
guitarra, _ = SIGNALgenerate(N3, 'osc', period=fs3 / f_guitarra)
mistura     = violao + guitarra
```

- `np.sin(2π·f·n/fs)` é uma senoide de f Hz amostrada a fs: a amostra n acontece no instante t = n/fs.
- A primitiva `osc` (do le03/le04) gera `sin(2π·n/P)`, onde P é o **período em amostras**. Para 1200 Hz,
  P = fs/f = 8192/1200 = 6,83 amostras. As duas formas dão a mesma senoide; usar o `osc` numa delas foi pedido na
  tarefa.
- A célula toca três sons: o violão, a guitarra e a mistura.

### 4.2 Análise: DFT da mistura

```python
X_mistura = myDFT(mistura, 'fft')
```

`myDFT` é a DFT implementada no próprio lab (a versão `fft`, Cooley-Tukey). O resultado tem 8192 números complexos.
Os quatro bins com conteúdo valem, em módulo:

| bin k | frequência | o que é | \|X[k]\| |
|---|---|---|---|
| 900 | 900 Hz | violão | 4096 |
| 1200 | 1200 Hz | guitarra | 4096 |
| 6992 | (= 8192 − 1200) | espelho da guitarra | 4096 |
| 7292 | (= 8192 − 900) | espelho do violão | 4096 |

Todo o resto é zero (10⁻¹¹, arredondamento). A altura 4096 = A·N/2 = 1 × 8192/2.

### 4.3 Remoção: zerar o bin da guitarra e o espelho

```python
k_guitarra = int(round(f_guitarra / df3))       # 1200
X_limpo = X_mistura.copy()
X_limpo[k_guitarra]      = 0                    # 1200
X_limpo[N3 - k_guitarra] = 0                    # 6992, o espelho
```

- `k = f/Δf` converte a frequência em índice de bin.
- `.copy()` preserva o espectro original, para comparar depois.
- **São dois bins, não um** — a razão está na seção 7.

### 4.4 Síntese: IDFT de volta ao tempo

```python
saida = myIDFT(X_limpo, 'fft')
```

A IDFT soma de volta as senoides que sobraram. A `myIDFT` devolve só a parte real, porque o sinal é real; a parte
imaginária que sobra é arredondamento (da ordem de 10⁻¹³).

### 4.5 Conferência

```
bins zerados: k = 1200 e k = 6992
saida = violao puro?  True   (erro max 6.3e-13)
```

O `np.allclose(saida, violao)` compara a saída, amostra por amostra, com o violão gerado no passo 1. O erro máximo de
6,3 × 10⁻¹³ é arredondamento de ponto flutuante: a saída **é** o violão.

### 4.6 O gráfico

Um gráfico 2 × 2:

| | no tempo (10 ms) | na frequência (0 a 2000 Hz) |
|---|---|---|
| **entrada** | violão + guitarra misturados, forma irregular | dois picos: violão 900 Hz e guitarra 1200 Hz |
| **saída** | senoide limpa, sobreposta ao violão original (as duas curvas coincidem) | um pico só: violão 900 Hz |

O espectro da saída é **medido de novo** (DFT da saída), não copiado do espectro editado — assim o gráfico prova que a
guitarra saiu do sinal, não só que o número foi zerado.

---

## 6. As funções usadas, e por que cada uma

Na ordem em que aparecem no código.

### Gerar os sons

| função | o que faz | por que foi usada |
|---|---|---|
| `np.arange(N3)` | cria o vetor dos índices [0, 1, …, N−1] | é o "n" das fórmulas; com ele, cada conta vale para todas as amostras de uma vez, sem laço |
| `np.sin(2*np.pi*f*n/fs)` | calcula o seno de cada elemento do vetor | gera o violão direto da definição sen(2π·f·t), com t = n/fs |
| `SIGNALgenerate(N, 'osc', period=fs/f)` | gerador de senoide da biblioteca do curso: devolve A·sen(2π·n/P + φ) e o vetor n | a tarefa pede que um dos sons seja `osc`; ele recebe o **período em amostras**, por isso `period=fs/f` |
| `+` entre dois vetores | soma amostra por amostra | é a mistura dos dois instrumentos, como no ar |
| `play(x, fs)` | toca o sinal no navegador (player do Jupyter) | para **ouvir** cada etapa; o `fs` diz quantas amostras por segundo tocar. O player ajusta o volume ao pico do sinal |

### Ir para a frequência

| função | o que faz | por que foi usada |
|---|---|---|
| `myDFT(x, 'fft')` | a DFT implementada no lab, versão FFT (Cooley-Tukey) | é a DFT **do próprio lab**, não a do numpy — a tarefa é mostrar o uso da DFT estudada. A versão `fft` porque N = 8192: as versões de laço (`signal`, `basis`) levariam minutos, e a `matrix` precisaria de uma matriz de 8192 × 8192 (1 GB). A FFT exige N potência de 2, e 8192 = 2¹³ |
| `f_guitarra / df3` com `int(round(...))` | converte a frequência em número de bin (k = f/Δf) | o `round` protege contra arredondamento (1199,9999 viraria 1199 com `int` sozinho); o `int` porque índice de vetor tem de ser inteiro |

### Remover

| função | o que faz | por que foi usada |
|---|---|---|
| `X_mistura.copy()` | faz uma cópia independente do vetor | sem a cópia, `X_limpo = X_mistura` seria **o mesmo vetor** com outro nome, e zerar um zeraria o outro — o espectro original se perderia, e ele é usado depois para o gráfico e para a demonstração do espelho |
| `X_limpo[k] = 0` e `X_limpo[N3 - k] = 0` | zera o bin da guitarra e o espelho | é a remoção propriamente dita; os dois bins porque o seno real tem uma seta em cada lado (seção 7) |

### Voltar ao tempo

| função | o que faz | por que foi usada |
|---|---|---|
| `myIDFT(X, 'fft')` | a IDFT do lab, versão FFT: calcula conj(DFT{conj(X)})/N e devolve a **parte real** | a volta pela mesma família de funções da ida. Reaproveita a FFT por um atalho (conjugar, transformar, conjugar, dividir por N) em vez de escrever outra. Devolve só a parte real porque o sinal é real — a parte imaginária que sobra é arredondamento |

### Conferir

| função | o que faz | por que foi usada |
|---|---|---|
| `np.allclose(saida, violao)` | diz se dois vetores são iguais a menos de uma tolerância minúscula | comparar com `==` falharia por causa do arredondamento (10⁻¹³); o `allclose` responde "igual" quando a diferença é só arredondamento |
| `np.max(np.abs(saida - violao))` | o maior erro, amostra a amostra | mostra **quanto** a saída difere; complementa o True/False do `allclose` com o número |
| `COMPLEXmagnitude(X)` | o módulo √(a² + b²) de cada X[k] (função feita no lab) | o espectro mostra o **módulo**: quanto de cada frequência. Usada a função do próprio lab, em vez de `np.abs` |
| `myDFT(saida, 'fft')` de novo | recalcula o espectro **da saída** | para provar que a guitarra saiu **do sinal**: mostrar o espectro editado provaria só que zeramos um número |

### A demonstração do erro do espelho

| função | o que faz | por que foi usada |
|---|---|---|
| `np.fft.ifft(X_errado)` | a IDFT do numpy, que devolve o resultado **complexo** inteiro | aqui não dá para usar a `myIDFT`: ela descarta a parte imaginária, e é justamente a parte imaginária que mostra o erro. A do numpy deixa ver as duas partes |
| `.imag` e `.real` | separam as partes imaginária e real | a parte imaginária ≠ 0 prova que a saída deixou de ser um som; a parte real mostra a metade da guitarra que sobrou |

### A versão geral

| função | o que faz | por que foi usada |
|---|---|---|
| `np.minimum(k, N - k)` | para cada bin, o menor entre k e N − k | converte cada bin na frequência **positiva** que ele representa: o bin 1200 e o 6992 dão os dois 1200 Hz. Assim um único teste zera o bin e o espelho, sem precisar lembrar do espelho |
| `np.abs(fk - f_apagar) <= largura` | marca os bins dentro da faixa a remover | permite remover uma faixa, para quando há vazamento; `max(largura, fs/N/2)` garante que, com largura 0, ao menos o bin mais próximo é pego |
| `X[faixa] = 0` | zera todos os bins marcados de uma vez | indexação por máscara: sem laço, os dois lados do espectro juntos |

### O gráfico

| função | o que faz | por que foi usada |
|---|---|---|
| `plt.subplots(2, 2)` | cria 4 gráficos numa grade | entrada × saída nas linhas, tempo × frequência nas colunas: dá para comparar tudo de uma vez |
| `zoom3 = n3 < fs3 * 0.01` | escolhe as amostras dos primeiros 10 ms | 1 s inteiro teria 900 ciclos espremidos e viraria um borrão; 10 ms mostram 9 ciclos do violão |
| `set_xlim([0, 2000])` | limita o eixo do espectro a 0–2000 Hz | os picos estão em 900 e 1200 Hz; até 4096 Hz eles ficariam espremidos à esquerda |
| `annotate(...)` | escreve "violão 900 Hz" e "guitarra 1200 Hz" ao lado dos picos | quem olha o gráfico sabe qual pico é qual instrumento |
| `figureFormat(ax, fig, tight=True)` | função da biblioteca do curso: liga a grade e ajusta os espaços | o padrão visual dos gráficos do curso |

### Só no script (`le06_remover_guitarra.py`)

| função | o que faz | por que foi usada |
|---|---|---|
| `dft_v1` e `idft_v1` | a fórmula do slide "v1", com dois laços, em Python puro | é a DFT na forma em que foi ensinada; o script mostra que a tarefa funciona com ela |
| fatiar `mistura[i:i + N]` | pega um bloco de 800 amostras | a v1 custa N²: o segundo inteiro (8000 amostras) seria 64 milhões de termos; em blocos de 800 são 10 × 640 mil, cerca de 4 s |
| `np.concatenate([...])` | junta os blocos processados num sinal só | refaz o segundo inteiro para tocar e conferir |
| `tocar(x, fs, rótulo)` | toca pelo player do sistema (`pw-play`, `paplay`, `aplay` ou `ffplay`) | fora do Jupyter não existe o player do navegador, e o ambiente Python não tem biblioteca de áudio; o player do sistema não precisa instalar nada |
| `ax.stem(...)` | gráfico de hastes | no script N = 800, poucos bins: as hastes mostram cada bin separado |

---

## 7. Por que zerar dois bins (k e N − k)

É o ponto que mais provavelmente o professor vai perguntar.

Pela fórmula de Euler, um seno real é a soma de **duas setas complexas girando em sentidos opostos**:

```
sen(ω·n) = ( e^(jωn) − e^(−jωn) ) / 2j
```

A DFT mostra cada seta num bin:

- a que gira para um lado, e^(+jωn), aparece no bin **k**;
- a que gira para o outro, e^(−jωn), aparece no bin **N − k** (as "frequências negativas" — por isso o espectro de um
  sinal real é espelhado).

As duas juntas formam o seno real. Se zerar só o bin k, sobra a outra seta **sozinha**:

- uma seta sozinha é um número complexo girando, não um sinal real: a saída fica **complexa**;
- e ela carrega metade do seno: a guitarra continua lá com **metade da amplitude**.

O notebook mede exatamente isso:

```
parte imaginaria da saida: ate 0.50  (deveria ser 0)
a guitarra continua na parte real, com amplitude 0.50  (era 1.00)
```

Regra prática: **para sinal real, tudo o que se faz no bin k se faz também no bin N − k.**

---

## 8. A versão geral: `apagar_frequencia`

```python
def apagar_frequencia(x, fs, f_apagar, largura=0.0, version='fft'):
    N  = len(x)
    X  = myDFT(x, version)
    k  = np.arange(N)
    fk = np.minimum(k, N - k) * fs / N           # frequência de cada bin, espelho incluído
    faixa = np.abs(fk - f_apagar) <= max(largura, fs / N / 2)
    X[faixa] = 0
    return myIDFT(X, version)
```

O que ela tem de diferente da versão passo a passo:

- **Trata os dois lados de uma vez.** `min(k, N − k)` dá a frequência positiva de cada bin: o bin 1200 e o bin 6992 dão
  os dois 1200 Hz. Comparar com f_apagar zera os dois juntos, sem precisar lembrar do espelho.
- **Aceita uma faixa** (`largura`, em Hz): zera todos os bins a até `largura` Hz da frequência indesejada. Serve para
  quando a frequência não cai num bin exato (seção 9).
- **Serve para qualquer frequência.** O notebook a usa nos dois sentidos:

```
remover a guitarra -> sobra o violao puro?   True
remover o violao   -> sobra a guitarra pura? True
```

---

## 9. O limite: quando a frequência não cai num bin exato

Com fs = 8192 e N = 8192, tudo cai em bins exatos e a remoção é perfeita. Mas se os parâmetros não fecham, a frequência
fica **entre** dois bins e a energia dela se espalha pelos vizinhos (vazamento espectral).

Foi medido com o teste feito em aula — 800 Hz + 2400 Hz, fs = 9600, N = 2048, removendo o 800 Hz. Aqui
Δf = 4,6875 Hz e 800/Δf = 170,67, que não é inteiro:

| faixa removida (`largura`) | bins zerados | quanto do 800 Hz sobra |
|---|---|---|
| 0 Hz (só o bin mais próximo) | 2 | **56 %** |
| 10 Hz | 8 | 27 % |
| 20 Hz | 16 | 20 % |
| 50 Hz | 44 | 12 % |
| 100 Hz | 86 | 8 % |

Lições:

1. **Zerar o bin mais próximo não resolve**: mais da metade do som indesejado continua.
2. **Alargar a faixa ajuda, mas devagar**: mesmo zerando 86 bins sobram 8 %. O vazamento se espalha por muitos bins,
   cada vez mais fraco.
3. **A solução certa é escolher fs e N para cair em bins exatos.** Para 800 + 2400 Hz, fs = 8192 e N = 2048 dão
   Δf = 4 Hz, bins 200 e 600, e a remoção volta a ser perfeita.

Em sinais reais, onde não se controla a frequência, usam-se **janelas** (multiplicar o sinal por uma curva suave antes
da DFT, para concentrar o vazamento) ou filtros projetados para isso. Isso vai além deste lab.

---

## 10. E um violão e uma guitarra de verdade?

Aqui cada instrumento é uma senoide pura. Um instrumento de verdade tem:

- **harmônicos**: a nota de 900 Hz soa também em 1800, 2700, 3600 Hz… — é o **timbre** (visto no le04, na forma de
  onda aleatória e no Karplus-Strong);
- **decaimento**: a corda perde energia, e o som não é uma senoide eterna;
- **variações**: vibrato, ataque da palheta, ruído.

Para remover uma guitarra de verdade seria preciso zerar a fundamental **e todos os harmônicos dela**. E onde um
harmônico da guitarra coincide com um do violão (900 e 1200 Hz têm em comum todos os múltiplos de 3600 Hz), remover um
apaga um pedaço do outro. Por isso separar instrumentos reais é um problema difícil, resolvido hoje com técnicas mais
avançadas — mas a ideia de base, **separar pela frequência**, é esta.

---

## 11. O script `le06_remover_guitarra.py`

A mesma tarefa fora do Jupyter, com duas diferenças.

**Usa a DFT v1 do slide** (`dft_v1` e `idft_v1`, de `le06_v1_signal_notation.py`), a fórmula ao pé da letra, com dois
laços. Ela custa N² operações: para 1 s inteiro a 8000 Hz seriam 64 milhões de termos, lento demais em Python puro.

**Por isso processa em blocos** de N = 800 amostras, com fs = 8000 Hz:

- Δf = 8000/800 = 10 Hz: o violão cai no bin 90, a guitarra no 120 (e o espelho no 680);
- 1 s = 10 blocos, processados em 3,6 s;
- **os blocos se emendam sem defeito** porque cada um contém um número **inteiro** de ciclos das duas senoides
  (900 Hz × 0,1 s = 90 ciclos; 1200 Hz × 0,1 s = 120 ciclos). Se não fosse inteiro, cada bloco teria vazamento e as
  emendas teriam degraus audíveis.

Resultado:

```
fs = 8000 Hz, blocos de N = 800 (Δf = 10 Hz), 10 blocos em 3.6 s
bins zerados em cada bloco: k = 120 (1200 Hz) e k = 680 (espelho)
saída = violão puro?  True  (erro máx 7.0e-13)
```

O script toca a mistura e depois a saída, pelo player do sistema (`pw-play`, `paplay`, `aplay` ou `ffplay`), e mostra
o mesmo gráfico 2 × 2. Para rodar, de dentro da pasta `le06_DFT`:

```
python le06_remover_guitarra.py            # com som
python le06_remover_guitarra.py --sem-som  # só gráficos e conferências
```

---

## 12. Como foi conferido

| conferência | resultado |
|---|---|
| saída × violão original, amostra por amostra (`np.allclose`) | iguais; erro máximo 6,3 × 10⁻¹³ (notebook) e 7,0 × 10⁻¹³ (script) |
| espectro da saída, **medido de novo** | só o pico de 900 Hz |
| o caminho inverso (remover o violão) | sobra a guitarra pura |
| o erro de esquecer o espelho | demonstrado: saída complexa, guitarra com 0,50 de amplitude |
| **som no alto-falante**: a saída de áudio foi gravada enquanto o script tocava, e a frequência de cada trecho medida | 1º trecho (mistura): 900 e 1200 Hz; 2º trecho (saída): **só 900 Hz** |
| gráficos | abertos e olhados; os rótulos dos picos, que ficavam sobre as linhas, foram reposicionados |
| frequência fora do bin exato | medido (seção 9): é o limite do método |

---

## 13. Como explicar ao professor

### Em 1 minuto

> "Gerei um violão de 900 Hz e uma guitarra de 1200 Hz, a guitarra com o `osc`, e somei. No tempo, os dois estão
> misturados em cada amostra e não dá para separar. Com a DFT, cada um vira um pico num bin diferente. Escolhi
> fs = N = 8192, então cada bin é 1 Hz e as frequências caem em bins exatos. Para remover a guitarra, zerei o bin 1200
> **e o espelho, 6992**, porque um seno real aparece nos dois lados do espectro — se esquecer o espelho, sobra metade
> da guitarra e a saída fica complexa. Com a IDFT voltei ao tempo, e a saída é igual ao violão original, com erro de
> 10⁻¹³. É um filtro feito na frequência."

### Perguntas prováveis

**Por que não dá para remover no tempo?** Cada amostra é a soma dos dois sons; um número não diz de onde veio cada
parte.

**Por que funciona na frequência?** Cada som está num bin diferente, e a DFT é linear: zerar os bins de um deixa
exatamente a DFT do outro.

**Por que zerar dois bins?** Um seno real é a soma de duas setas girando em sentidos opostos; a DFT mostra uma em k e a
outra em N − k.

**Por que fs = 8192 e N = 8192?** Nyquist (maior que 2400), 1 s para ouvir, potência de 2 para a FFT e resolução de
1 Hz para as frequências caírem em bins exatos.

**E se a frequência não caísse num bin exato?** Vazamento espectral: a energia se espalha, e zerar o bin mais próximo
deixa mais da metade do som (medido: 56 %). Ou se escolhem fs e N para cair em bins exatos, ou se usam janelas.

**Isso funciona com instrumentos de verdade?** A ideia sim, mas seria preciso remover também os harmônicos da guitarra,
e os que coincidem com os do violão levariam junto um pedaço dele.

**O que é isso, em nome técnico?** Um **filtro rejeita-faixa** (ou *notch*) aplicado no domínio da frequência.

---

## 14. Resumo do que foi entregue

- **Notebook** (`le06_01_DFT-four-versions.ipynb`, células 53 a 60): explicação, geração com som, remoção com
  conferência, gráfico 2 × 2, demonstração do erro do espelho, função geral `apagar_frequencia` e o caminho inverso.
- **Script** (`le06_remover_guitarra.py`): a tarefa com a DFT v1 do slide, em blocos, com som e gráfico.
- **Textos**: este arquivo (explicação detalhada) e a parte 2 de `LE06_TAREFA_DUAS_FREQUENCIAS.md` (versão curta).
- **Commit** `cb74ace` na branch `main` do `sentinela`.
