# Relatório do trabalho — labs 4, 5 e 6 (09/10/2026)

Registro detalhado do que foi feito nos laboratórios da disciplina de Processamento de Sinais (INF0413), no repositório
`/home/deck/dev/sentinela`, em 09/10/2026. Diz o que foi pedido, o que foi feito, como foi conferido e onde está cada
coisa.

As fórmulas estão em caracteres comuns (Σ, π, ², ·), sem LaTeX, para aparecerem iguais em qualquer editor.

---

## 1. Resumo

| lab | assunto | o que foi feito |
|---|---|---|
| **le05** | números complexos | notebook completado; desafio 1 (módulo e fase **sem funções prontas**) e desafio 2 (antecipar jʲ) resolvidos no notebook e em scripts Python |
| **le06** | DFT (Transformada Discreta de Fourier) | as **quatro versões** da DFT e da inversa implementadas e conferidas; slide "v1 – Signal notation" em Python com som; tarefa de aula **900 + 1200 Hz**; tarefa **remover um som** (violão + guitarra → só o violão) |
| **le04** | tom digital e Karplus-Strong | sete pontos errados ou inconsistentes no notebook corrigidos |
| todos | estudo | quatro textos de explicação, para estudar e apresentar ao professor |

Tudo foi **executado e conferido**: os notebooks rodam de ponta a ponta sem erro, os resultados numéricos foram
comparados com o numpy, e o som foi verificado **gravando a saída do alto-falante** e medindo as frequências que
realmente tocaram.

---

## 2. Ponto de partida

- O material da disciplina vem do repositório `github.com/2026-2-INF0413-SignalProcessing/assets`. Os labs pedidos
  foram `labs/le05_complex-exponentials` e `labs/le06_DFT` (este último na versão do commit `5ad28fe`).
- No `sentinela`, os dois notebooks estavam soltos na raiz de `assets/labs/`, fora das pastas do curso. O do le05 tinha
  sido começado (forma polar, fase, gráficos); o do le06 era a cópia intacta do professor, só com `...` nos lugares a
  completar.
- Os notebooks do le04 já estavam resolvidos, mas com problemas que só apareceram ao conferir (seção 6).

---

## 3. Lab 5 — Números complexos

Notebook: `le05_complex-exponentials/le05_complex-numbers.ipynb` (movido para a pasta do curso).

### 3.1 Exercícios do roteiro

- **Forma polar** de z₁ = 3 + 4j: módulo 5, fase 0,927 rad = 53,13°.
- `COMPLEXmagnitude` (Pitágoras e `np.abs`) e `COMPLEXphase` (`arctan`, `arctan2`, `angle`, em radianos ou graus).
- **Tabela das três versões da fase nos quatro quadrantes**: mostra que `arctan(b/a)` erra no 2º e no 3º quadrantes,
  porque perde os sinais ((−4)/(−3) = 4/3), e que `arctan2` e `angle` acertam.
- **Gráficos** no plano complexo: z₁, a potência z₁² e a raiz √z₁.
- Duas células do original davam erro e foram corrigidas: uma chamada com sintaxe inválida (`COMPLEXphase(z, 'deg')`) e
  uma que chamava uma função inexistente (`myMagnitude`).

### 3.2 Desafio 1 — módulo e fase sem funções prontas

O enunciado diz "ñ funções prontas". A primeira solução usava `np.arctan2`, `np.angle` e `np.sqrt`, o que não cumpria o
desafio; foi refeita com **só operadores** (`+ - * / **`) e comparações:

- **módulo** por Pitágoras, com a raiz como operador: `(a**2 + b**2) ** 0.5`;
- **arctan** pela série de Taylor (u − u³/3 + u⁵/5 − …), com duas reduções para convergir rápido: o inverso para
  |u| > 1 e três aplicações do meio ângulo;
- **π calculado**, pela fórmula de Machin: π = 16·arctan(1/5) − 4·arctan(1/239) → 3,141592653589794;
- **arctan2 próprio**, que decide o quadrante pelos sinais de a e b.

**Conferência:** 100 mil complexos aleatórios, em todos os quadrantes e em escalas de 10⁻⁶ a 10⁶. Erro máximo de
2,2 × 10⁻¹⁶ no módulo e 1,3 × 10⁻¹⁵ rad na fase — o limite da precisão do computador. Também foi conferido com `grep`
que nenhuma função pronta aparece no código.

### 3.3 Desafio 2 — antecipar o gráfico de jʲ

- **Antecipação:** j = e^(jπ/2), então jʲ = e^(j·j·π/2) = e^(−π/2) ≈ 0,2079 — um número **real**, sobre o eixo real.
- **Conferência:** a previsão feita com a fase do desafio 1 dá 0,20787957635076…, igual ao que o Python calcula.
- **Extensão:** jʲ tem **infinitos valores**, e^(−(π/2 + 2π·k)), todos reais e positivos; o Python devolve o de k = 0.

### 3.4 Extensões no notebook

- **Raízes n-ésimas** (`myRoots`): a raiz quadrada de 3 + 4j tem duas respostas, 2 + j e −2 − j; gráficos das raízes para
  n = 2, 3 e 6, que formam polígonos regulares, cada uma conferida (elevada a n volta a z₁).
- **Sinais periódicos e não periódicos:** cos(2π·n/10) tem período 10 (conferido por código); cos(n) nunca se repete,
  porque 2π não é um número inteiro de amostras.

### 3.5 Scripts Python (o professor pediu o código em Python)

| arquivo | o que faz |
|---|---|
| `le05_desafio1_modulo_e_fase.py` | o desafio 1 em Python puro, com a tabela dos quadrantes e a conferência dos 100 mil casos |
| `le05_desafio2_j_elevado_a_j.py` | o desafio 2: previsão com as funções do desafio 1, os infinitos valores e dois gráficos |

---

## 4. Lab 6 — A DFT

Notebook: `le06_DFT/le06_01_DFT-four-versions.ipynb` (movido para a pasta do curso).

### 4.1 As quatro versões da DFT e da IDFT

| versão | como calcula | custo |
|---|---|---|
| `signal` | a fórmula do slide, com dois laços | N² |
| `basis` | produto interno do sinal com cada vetor da base de Fourier | N² |
| `matrix` | multiplicação matriz × vetor, **X** = **W**·**x** | N² (e N² de memória) |
| `fft` | Cooley-Tukey radix-2: divide em amostras pares e ímpares, recursivamente | N·log₂N |

A inversa (IDFT) foi feita nas quatro versões; a da FFT usa o atalho IDFT{X} = (1/N)·conj(DFT{conj(X)}).

**Conferência com 1024 amostras do som de um trem (`train.wav`):**

- as quatro versões dão o mesmo resultado que `np.fft.fft` (diferença máxima de 10⁻¹¹);
- as quatro inversas devolvem o sinal original (erro de 10⁻¹³);
- tempos medidos: `signal` 0,6 s, `basis` 42 ms, `matrix` 29 ms, `fft` 8 ms.

O original tinha nomes de versão que não batiam (as chamadas usavam `'v1'`, `'v2'`, `'v3'` e as funções esperavam
`'signal'`, `'basis'`, `'matrix'`) e caminhos de pasta de outra máquina (`/home/kuntur/...`, `../../notebooks/sounds/`);
os dois foram corrigidos.

### 4.2 Aprofundamentos

- **Base ortogonal:** **W**·**W**ᴴ = N·**I**, conferido com N = 16. É por isso que a versão `basis` funciona e que a
  inversa é **W**ᴴ/N.
- **Teorema de Parseval:** a energia do trem é 30,264588 no tempo e na frequência.
- **Custo N² × N·log N:** gráfico do tempo de cada versão para N de 16 a 1024. A teoria prevê 102× menos operações
  para N = 1024; medido, a v1 ficou 73× mais lenta que a FFT.
- **N que não é potência de 2:** a FFT radix-2 recusa, e o *zero-padding* (completar com zeros) resolve.
- **Espectro do trem:** tons em 704, 888 e 1176 Hz, e um mais fraco em 2120 Hz (resolução de 8 Hz por bin).
- **Só a metade do espectro basta:** o sinal foi reconstruído a partir de 513 dos 1024 coeficientes, usando a
  simetria X[N−k] = conj(X[k]), com erro de 3 × 10⁻¹⁶.
- **DFT dos sinais básicos**, com cada previsão conferida por código: impulso → espectro plano; degrau → X[0] = 32 e
  zeros nos k pares; exponencial → igual à soma geométrica fechada; senoide de período 8 → picos só em k = 8 e 56;
  ruído → média de |X|² ≈ 64.

### 4.3 O slide "v1 – Signal notation"

A partir de uma foto do slide projetado em aula (fórmulas de análise e síntese):

- **no notebook:** o exemplo à mão x = [1, 2, 3, 4] → X = [10, −2+2j, −2, −2−2j], calculado numa tabela e conferido; e
  o som inteiro do trem (1,57 s) reconstruído pela v1, em 13 blocos, com os players do original e do reconstruído;
- **em script:** `le06_v1_signal_notation.py`, as duas fórmulas em Python puro, com o mesmo exemplo e o som.

### 4.4 Fazer o som funcionar

- **No Jupyter**, o `play()` usa o player do navegador: funciona sem mudança.
- **Nos scripts**, fora do Jupyter, não há esse player, e o ambiente Python não tem biblioteca de áudio. A solução foi
  tocar pelo player do sistema: o primeiro disponível entre `pw-play`, `paplay`, `aplay` e `ffplay` (nesta máquina, o
  `pw-play`). Se nenhum existir, o script avisa em vez de ficar calado.
- **Conferência real:** enquanto os scripts tocavam, a saída do alto-falante foi gravada e as frequências medidas.
  Exemplo do script das duas frequências: o 1º trecho gravado tinha 900 Hz, o 2º 1200 Hz, o 3º os dois.

### 4.5 Tarefa de aula: um sinal com 900 Hz e 1200 Hz

- Sinal: x = sen(2π·900·t) + sen(2π·1200·t).
- Parâmetros: fs = 9600 Hz e N = 1024 (potência de 2, para as quatro versões funcionarem). A resolução é
  Δf = fs/N = 9,375 Hz, e as frequências caem **exatamente** nos bins 96 e 128 — sem vazamento espectral.
- Resultado: dois picos de altura 512 (= A·N/2) em 900 e 1200 Hz; fora deles, tudo zero (10⁻¹¹).
- Gráfico em três painéis (as duas senoides, a soma no tempo, o espectro) e três players de som.
- Em script: `le06_duas_frequencias.py` (fs = 8000, N = 800, Δf = 10 Hz).

**Variações testadas**, para responder se o professor mudar a tarefa:

| caso | resultado |
|---|---|
| fs = 8000, N = 1024 (resolução que não fecha) | **vazamento espectral**: picos em 898 e 1203 Hz, 22 bins acesos em vez de 2 |
| fs = 2000 (abaixo de 2 × 1200) | **aliasing**: o 1200 Hz aparece em 800 Hz |
| 900 + 1000 Hz com N = 40 | resolução de 200 Hz: os dois picos se misturam |
| 800 + 2400 Hz, fs = 9600, N = 2048 (teste feito em aula) | o 2400 Hz cai no bin 512, exato; o 800 Hz cai em 170,67 e vaza. Com fs = 8192 os dois ficam limpos (bins 200 e 600) |

### 4.6 Tarefa de aula: remover um som (violão + guitarra → só o violão)

Pedido: um dos dois sons é indesejado — uma gravação pegou um **violão** e uma **guitarra** — e tem de sair, usando a
DFT, deixando o outro puro.

| instrumento | frequência | como é gerado | papel |
|---|---|---|---|
| violão | 900 Hz | `np.sin` | fica |
| guitarra | 1200 Hz | primitiva `osc` (`SIGNALgenerate`) | sai |

**Método, em três passos:**

1. **análise:** DFT da mistura → dois picos, guitarra no bin 1200, violão no 900 (fs = 8192, N = 8192, resolução de 1 Hz);
2. **remoção:** zerar o bin da guitarra **e o espelho dele**, N − k;
3. **síntese:** IDFT de volta ao tempo.

**Resultado:** a saída é igual ao violão original (erro de 6 × 10⁻¹³), e o espectro da saída tem só o pico do violão.

**Por que zerar dois bins:** um seno real é a soma de duas setas girando em sentidos opostos,
sen(ωn) = (e^(jωn) − e^(−jωn)) / 2j, e a DFT mostra uma em k e a outra em N − k. O notebook demonstra o erro de esquecer
o espelho: a saída fica complexa e a guitarra continua com **metade** da amplitude (0,50).

O notebook traz ainda a função `apagar_frequencia(x, fs, f, largura)`, que remove uma faixa de frequências (para
quando a frequência não cai num bin exato) e serve para remover o violão em vez da guitarra.

Em script: `le06_remover_guitarra.py`, com a DFT v1 do slide em blocos de 800 amostras. Conferido pelo alto-falante: a
mistura tocou 900 + 1200 Hz e a saída, só 900 Hz.

---

## 5. Lab 4 — Tom digital e Karplus-Strong: o que foi corrigido

Ao preparar a explicação do lab 4, a conferência dos notebooks encontrou sete pontos, todos corrigidos e reexecutados:

| # | problema | correção |
|---|---|---|
| 1 | o desafio `SIGNALtone` pedia 330 Hz e o código usava 220 Hz | agora usa 330 Hz |
| 2 | `KS_3` era redefinido no meio do notebook com outra fórmula (o Karplus-Strong de 1983, com média de duas amostras), e as células seguintes usavam essa versão sem aviso | `KS_3` ficou com a fórmula do slide, y[n] = x[n] + α·y[n−M]; a versão com média virou `KS_media`, numa seção própria que toca as duas para comparar |
| 3 | as duas células que deveriam mostrar "nota aguda decai mais rápido" eram idênticas | agora M = 50 × M = 25, com gráfico dos envelopes: após 1 s sobra 0,04 × 0,0016 da amplitude |
| 4 | o texto dizia que o baixo (D2) soava mais tempo e que cada nota tinha um ganho, mas o código não fazia isso | `ks_acorde` com ganho e α por nota: D2 com ganho 1,5 e α = 0,998 |
| 5 | comentário e seção final falando de outro projeto de software, sem relação com a disciplina | removidos |
| 6 | a resposta do "teste final" falava em "filtro comb", mas o `KS_1` só repete | reescrita: são duas notas, 160 e 200 Hz (uma terça maior), conferidas no espectro |
| 7 | a afinação das notas agudas sai aproximada (M precisa ser inteiro) | é limitação do algoritmo; foi **medida** numa tabela em cents: D2 −0,5, A4 +17, C5 −24, G5 +35 |

Também: `KS_1` cortava o resultado em `N+1` amostras e agora devolve exatamente N.

---

## 6. Textos de estudo

Escritos para estudar e para explicar ao professor. Os três de laboratório têm a ideia central, a explicação passo a
passo com os números medidos, perguntas prováveis com respostas curtas e um roteiro de 3 minutos; o das tarefas de aula
tem o código para digitar na hora e uma fala de 1 minuto para cada parte.

| arquivo | conteúdo |
|---|---|
| `LE04_EXPLICACAO.md` | tom digital (f = fs/P), FFT como prova, harmônicos e timbre, Karplus-Strong de KS_1 à versão compensada, acordes, teste final, as correções da seção 5 |
| `LE05_EXPLICACAO.md` | formas cartesiana e polar, o erro do `arctan`, os dois desafios explicados, potência e raízes, jʲ, periodicidade |
| `LE06_DFT_EXPLICACAO.md` | as fórmulas lidas em palavras, as quatro versões com o porquê, como ler o espectro, sinais básicos, o exemplo de duas frequências |
| `LE06_TAREFA_DUAS_FREQUENCIAS.md` | preparação para as tarefas de aula: código curto para digitar na hora, explicação linha por linha, variações, fala de 1 minuto — parte 1 (900 + 1200 Hz) e parte 2 (remover a guitarra) |

**Problema encontrado nos textos:** eles foram escritos com fórmulas em LaTeX (`$...$`). O editor usado para abri-los
não entende LaTeX: mostrava os comandos crus e, ao salvar, colocou barras de escape dentro das fórmulas (`$f\_s$`),
quebrando-as de vez — além de apagar separadores de tabela e marcações de código. Os quatro textos foram reescritos com
as fórmulas em caracteres comuns, que aparecem certo em qualquer lugar. Pelo mesmo motivo, a célula de explicação das
duas frequências no notebook do le06 foi reescrita (as fórmulas sumiam ao copiar o texto).

---

## 7. Como foi conferido

- **Notebooks executados de ponta a ponta** (com `jupyter nbconvert --execute`) depois de cada mudança, sem erro — a
  única exceção é a célula de teste `print(xmag)`, acrescentada em aula, que dá `NameError` (o nome certo é `mag`).
- **Resultados comparados com o numpy** (`np.fft.fft`) e com fórmulas fechadas, sempre por código (`np.allclose`).
- **Som verificado no alto-falante:** a saída de áudio foi gravada enquanto os scripts tocavam, e a frequência de cada
  trecho gravado foi medida.
- **Gráficos abertos e olhados**, não só gerados — o que pegou, por exemplo, rótulos sobrepostos nos picos.
- **Edições feitas em aula respeitadas:** antes de cada mudança nos notebooks, as alterações feitas no JupyterLab foram
  comparadas com a última versão salva, para não desfazer nada.

---

## 8. Commits

Todos na branch `main` do `sentinela`, sem push.

| commit | o que entrou |
|---|---|
| `0c1465e` | le05 e le06 completos e executados, nas pastas do curso |
| `83603f0` | desafios do le05 (notebook e scripts), aprofundamentos do le06, slide v1, som, 900 + 1200 Hz, primeiros textos de estudo |
| `41e4320` | alterações que já estavam pendentes antes desta sessão (notebooks do le03 e do le04, notebook da aula de 02/10), num commit separado |
| `aad539c` | as sete correções do le04, explicações dos labs 4 e 5, teste 800 + 2400 Hz feito em aula |
| `cb74ace` | remover um som com a DFT (notebook e script), textos de estudo sem LaTeX |

---

## 9. Mapa dos arquivos

```
assets/labs/
├── LE04_EXPLICACAO.md
├── LE05_EXPLICACAO.md
├── LE06_DFT_EXPLICACAO.md
├── LE06_TAREFA_DUAS_FREQUENCIAS.md
├── RELATORIO_DO_TRABALHO_09-10-2026.md        ← este arquivo
├── le04_karplus-strong/
│   ├── le04_01_signal-reconstruction.ipynb     (corrigido)
│   └── le04_karplus-strong.ipynb               (corrigido)
├── le05_complex-exponentials/
│   ├── le05_complex-numbers.ipynb
│   ├── le05_desafio1_modulo_e_fase.py
│   └── le05_desafio2_j_elevado_a_j.py
└── le06_DFT/
    ├── le06_01_DFT-four-versions.ipynb
    ├── le06_v1_signal_notation.py
    ├── le06_duas_frequencias.py
    └── le06_remover_guitarra.py
```

**Para rodar os scripts**, entre na pasta de cada um (alguns importam outros da mesma pasta):

```
cd assets/labs/le06_DFT
python le06_remover_guitarra.py            # com som
python le06_remover_guitarra.py --sem-som  # só gráficos e conferências
```

---

## 10. Pendências

- **Recarregar os notebooks no JupyterLab** (File → Reload Notebook from Disk) antes de salvar: vários foram alterados
  no disco com a aba aberta, e salvar a aba antiga desfaz as mudanças.
- **Trocar `print(xmag)` por `print(mag)`** na célula de teste do le06.
- **Fechar a aba antiga de `assets/labs/le05_complex-numbers.ipynb`** sem salvar: é a cópia removida, e salvar a faz
  voltar.
- Nada foi enviado ao GitHub (sem push).
