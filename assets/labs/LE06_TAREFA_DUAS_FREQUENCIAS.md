# Tarefa: criar um sinal de 900 Hz + 1200 Hz e mostrar as frequências

Preparação para a tarefa que o professor pediu em aula (e que deve pedir de novo, talvez com variações).
Os números das tabelas foram testados no Python.

**Onde está no notebook:** `le06_DFT/le06_01_DFT-four-versions.ipynb`, no fim:

- seção **"Um sinal com duas frequências: 900 Hz + 1200 Hz"** — célula 48 = explicação; 49 = sinal e som;
  50 = DFT e frequências encontradas; 51 = gráfico;
- seção **"Remover um som com a DFT: violão + guitarra → só o violão"** — células 53 a 60 (a parte 2 abaixo).

Em script: `le06_DFT/le06_duas_frequencias.py` (parte 1) e `le06_DFT/le06_remover_guitarra.py` (parte 2).

> Os números entre colchetes ao lado das células no JupyterLab (`[88]`, `[93]`…) **não são linhas**: contam
> quantas vezes você executou algo no kernel. Para ver a posição de uma célula, use o sumário
> (*Table of Contents*, ícone de lista na barra da esquerda).

---

## O código para digitar na hora

Curto o bastante para escrever de memória:

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 8000                 # taxa de amostragem (Hz)
N  = 800                  # número de amostras  -> resolução fs/N = 10 Hz
n  = np.arange(N)

x = np.sin(2*np.pi*900*n/fs) + np.sin(2*np.pi*1200*n/fs)   # o sinal

X   = np.fft.fft(x)                  # a DFT
mag = np.abs(X[:N//2 + 1])           # só a metade (sinal real)
f   = np.arange(N//2 + 1) * fs / N   # converte k em Hz

plt.stem(f, mag)
plt.xlabel('f (Hz)'); plt.ylabel('|X[k]|')
plt.show()
```

O gráfico mostra **dois picos, em 900 e 1200 Hz**, de altura 400. Fora deles tudo é zero.

---

## Linha por linha: o que dizer

1. **`fs = 8000` — a taxa de amostragem.** Pelo teorema de Nyquist, fs precisa ser maior que o dobro da maior
   frequência: 2 × 1200 = 2400, e 8000 sobra. A maior frequência que a DFT consegue mostrar é fs/2 = 4000 Hz.

2. **`N = 800` — quantas amostras.** É a escolha mais importante. A resolução é **Δf = fs/N = 10 Hz**: a DFT só
   "enxerga" múltiplos de 10 Hz. Como 900 e 1200 são múltiplos de 10, cada frequência cai **exatamente** num bin:
   k = 90 e k = 120.

3. **`n = np.arange(N)`** — os índices das amostras, 0, 1, …, 799. A amostra n acontece no instante t = n/fs.

4. **O sinal** — sin(2π·f·t) com t = n/fs vira `sin(2*np.pi*f*n/fs)`. Somar as duas senoides é o que faz o sinal
   "ter duas frequências".

5. **`np.fft.fft(x)` — a DFT.** Compara o sinal com N senoides e devolve N números complexos. O `abs` pega o
   módulo: "quanto existe" de cada frequência.

6. **`X[:N//2 + 1]` — só a metade.** O sinal é real, então a segunda metade do espectro é o espelho da primeira
   (os mesmos picos reapareceriam em k = 800 − 90 e 800 − 120).

7. **`f = k * fs / N` — de índice para Hz.** Sem essa linha, o eixo do gráfico mostraria k (90 e 120), não Hz.

8. **A altura do pico** é A·N/2 = 1 × 800/2 = **400**. Daí se recupera a amplitude: 2·400/800 = 1.

---

## Variações que o professor pode pedir

| Se ele pedir… | O que acontece | Números testados |
|---|---|---|
| **Outras frequências** (ex.: 500 + 700 Hz) | Mesmo código, só troca os números. Confira se são múltiplos de fs/N. | — |
| **Resolução que não fecha** (fs = 8000, N = 1024 → 7,8125 Hz) | **Vazamento espectral:** 900/7,8125 = 115,2 não é inteiro. A energia se espalha pelos bins vizinhos e os picos ficam mais baixos e largos. | Picos em 898 e 1203 Hz; **22 bins** acesos em vez de 2. |
| **fs baixo demais** (fs = 2000) | **Aliasing:** fs/2 = 1000 < 1200. O 1200 Hz "dobra" e aparece em 2000 − 1200 = **800 Hz**. O espectro mente. | Picos em **800** e 900 Hz. |
| **Frequências muito próximas** (900 + 1000 com N pequeno) | Com N = 80 (Δf = 100 Hz) os dois picos aparecem separados. Com N = 40 (Δf = 200 Hz) eles se misturam. | N = 40: picos em 800 e 1000 Hz, com 9 bins acesos. |
| **Usar a DFT do lab em vez do numpy** | `myDFT(x, 'signal')` dá o mesmo resultado. Para usar `'fft'`, N tem de ser potência de 2: fs = 9600 e N = 1024 (Δf = 9,375 Hz, k = 96 e 128). | Picos de 512 em 900 e 1200 Hz. |
| **Ouvir o sinal** | No Jupyter: `from IPython.display import Audio; Audio(x, rate=fs)`. Com N = 800 dura só 0,1 s; para ouvir bem, gere 1 s com `n = np.arange(fs)`. | — |

**A regra que cobre quase todas as variações:** escolha **fs maior que o dobro** da maior frequência e escolha
**N de modo que fs/N divida as frequências**.

---

## Como explicar em 1 minuto

> "Somei duas senoides, de 900 e 1200 Hz, amostradas a 8000 Hz — acima do dobro de 1200, por causa de Nyquist.
> No tempo elas se misturam e não dá para ver as frequências. A DFT compara o sinal com senoides de cada
> frequência e mostra quanto de cada uma existe. Escolhi N = 800 para a resolução fs/N dar 10 Hz; assim 900 e
> 1200 caem exatamente nos bins 90 e 120 e os picos saem limpos, sem vazamento. Mostro só a metade do espectro
> porque, para sinal real, a outra metade é espelho. E converto o índice k em Hz com f = k·fs/N."

Se ele perguntar *"e se a frequência não caísse num bin?"*, a resposta é **vazamento espectral** (segunda linha
da tabela).

---

## Como treinar

1. Digite o código do zero, sem olhar.
2. Troque 900/1200 por outros valores e confira os picos.
3. Rode o caso de **aliasing** (fs = 2000) — é o que mais costuma surpreender.
4. Rode o caso de **vazamento** (N = 1024 com fs = 8000) e compare com N = 800.

Para a teoria por trás (as quatro versões da DFT, simetria, Parseval), ver `LE06_DFT_EXPLICACAO.md`.

---

# Parte 2: remover uma das frequências (violão + guitarra → só o violão)

A continuação da tarefa: **um dos sons é indesejado e tem de sair**. Exemplo: a gravação pegou um **violão** e uma
**guitarra** tocando juntos, e se quer só o violão. Cada instrumento é um sinal oscilatório:

| instrumento | frequência | como é gerado | papel |
|---|---|---|---|
| violão | 900 Hz | `np.sin` direto | fica |
| guitarra | 1200 Hz | primitiva `osc` | sai |

## O código para digitar na hora

```python
import numpy as np

fs = 8192                      # 1 s de sinal = 8192 amostras -> resolução fs/N = 1 Hz
N  = fs
n  = np.arange(N)

violao   = np.sin(2*np.pi*900*n/fs)
guitarra = np.sin(2*np.pi*1200*n/fs)          # no notebook: SIGNALgenerate(N, 'osc', period=fs/1200)
mistura  = violao + guitarra

X = np.fft.fft(mistura)        # 1. análise: para a frequência
k = round(1200 / (fs/N))       #    bin da guitarra = 1200
X[k]     = 0                   # 2. remover: a frequência positiva...
X[N - k] = 0                   #    ...e o espelho
saida = np.fft.ifft(X).real    # 3. síntese: de volta ao tempo

print(np.allclose(saida, violao))   # True: sobrou só o violão
```

## Linha por linha: o que dizer

1. **No tempo não dá para separar**: cada amostra da mistura é a soma das duas. Não existe "a amostra da guitarra".
2. **Na frequência, cada som é um pico num bin diferente**: violão em k = 900, guitarra em k = 1200 (com fs/N = 1 Hz, o
   bin é a própria frequência).
3. **Remover = zerar o bin da guitarra.** Zerar um número no espectro é tirar aquela frequência do sinal.
4. **Zerar também o espelho, N − k.** Um seno real é a soma de duas setas girando em sentidos opostos:

       sen(ωn) = ( e^(jωn) − e^(−jωn) ) / 2j

   A DFT mostra uma seta no bin k e a outra no bin N − k. Se zerar só o k, a saída fica **complexa** e a guitarra
   continua lá com **metade** da amplitude (medido no notebook: parte imaginária até 0,50, guitarra com 0,50 em vez
   de 1,00).
5. **IDFT de volta ao tempo**: a saída é o violão puro (erro de 10⁻¹³). O `.real` só descarta o arredondamento.

Isso é um **filtro**: um sistema que deixa passar umas frequências e bloqueia outras. Este, que zera um bin, é o filtro
mais seletivo possível — tira uma frequência e não encosta em nenhuma outra.

## Variações que o professor pode pedir

| Se ele pedir… | Resposta |
|---|---|
| **Remover o violão em vez da guitarra** | Zerar o bin 900 e o N − 900. Sobra a guitarra pura (o notebook faz os dois). |
| **Frequência que não cai num bin exato** | Ela vaza para os bins vizinhos; zerar um só deixa resto. É preciso zerar uma **faixa** em volta — é o que faz a função `apagar_frequencia(x, fs, f, largura)` do notebook. |
| **Com N pequeno, sem ser 1 s inteiro** | Processar em **blocos** (o script faz blocos de 800 com fs = 8000). Funciona limpo porque cada bloco tem um número inteiro de ciclos das duas frequências (90 e 120). |
| **E um violão e uma guitarra de verdade?** | Um instrumento real tem a fundamental **e os harmônicos** (2×, 3×… — o timbre, do le04). Seria preciso zerar todos os harmônicos da guitarra; onde um coincide com um do violão, remover um apaga um pedaço do outro. Por isso separar instrumentos reais é difícil. |

## Como explicar em 1 minuto

> "Somei um violão de 900 Hz e uma guitarra de 1200 Hz, gerada com o `osc`. No tempo eles estão misturados em cada
> amostra e não dá para separar. Com a DFT, cada um vira um pico num bin diferente. Para remover a guitarra, zerei o
> bin dela — e também o espelho, N − k, porque um seno real aparece nos dois lados do espectro; se esquecer o
> espelho, sobra metade da guitarra. Com a IDFT voltei ao tempo, e a saída é igual ao violão original. Isso é um
> filtro feito na frequência."
