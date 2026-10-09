#!/usr/bin/env python
# coding: utf-8
"""
le06 — Remover um som com a DFT: violão + guitarra → só o violão.

Tarefa de aula: dois sinais oscilatórios tocam juntos (um deles gerado com a
primitiva 'osc'); supõe-se que um é um som indesejado. Exemplo: a gravação pegou
um violão e uma guitarra, e se quer só o violão. Com a DFT, a guitarra é
removida e a saída fica com o violão puro.

    violão   :  900 Hz  (np.sin direto)          -> fica
    guitarra : 1200 Hz  (SIGNALgenerate 'osc')   -> sai

Como:
    1. análise  — DFT da mistura;
    2. remover  — zerar o bin da guitarra E o espelho dele (k e N - k);
    3. síntese  — IDFT de volta ao tempo.

Zerar só o bin k não basta: um seno real é a soma de duas setas girando em
sentidos opostos, sen(ωn) = (e^(jωn) - e^(-jωn)) / 2j, e a segunda aparece no
bin N - k. Esquecida, a guitarra continua com metade da amplitude.

A DFT é a v1 do slide (le06_v1_signal_notation.py), O(N²). Para processar 1 s
de som com ela em poucos segundos, o sinal é tratado em blocos de N = 800
amostras com fs = 8000 Hz: Δf = fs/N = 10 Hz, o violão cai no bin 90 e a
guitarra no 120, e cada bloco contém um número inteiro de ciclos das duas
(90 e 120), então os blocos se emendam sem descontinuidade.

Uso:
    python le06_remover_guitarra.py            # gráficos + som
    python le06_remover_guitarra.py --sem-som  # só gráficos e conferências
"""

import os
import sys
import time

import matplotlib.pyplot as plt
import numpy as np

from le06_v1_signal_notation import dft_v1, idft_v1, tocar

# Biblioteca do curso (assets/lib), para a primitiva 'osc'
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lib.mySignalProcessingLib import SIGNALgenerate  # noqa: E402

fs = 8000                       # Hz (> 2 x 1200: Nyquist ok)
N = 800                         # tamanho do bloco da DFT -> Δf = 10 Hz
f_violao, f_guitarra = 900, 1200

# ── 1. Os dois sons e a mistura (1 s) ───────────────────────────────────────
n = np.arange(fs)
violao = np.sin(2 * np.pi * f_violao * n / fs)
guitarra, _ = SIGNALgenerate(fs, 'osc', period=fs / f_guitarra)
mistura = violao + guitarra

# ── 2. Remover a guitarra, bloco a bloco ───────────────────────────────────
k_guitarra = round(f_guitarra / (fs / N))          # 1200 / 10 = bin 120


def remover(bloco, k):
    """DFT v1 do bloco, zera os bins k e N - k, IDFT v1 de volta."""
    X = dft_v1([float(v) for v in bloco])
    X[k] = 0                     # frequência positiva
    X[len(X) - k] = 0            # espelho (frequência negativa)
    return [v.real for v in idft_v1(X)]


t0 = time.perf_counter()
saida = np.concatenate([remover(mistura[i:i + N], k_guitarra) for i in range(0, len(mistura), N)])
print(f"fs = {fs} Hz, blocos de N = {N} (Δf = {fs / N:.0f} Hz), {len(mistura) // N} blocos "
      f"em {time.perf_counter() - t0:.1f} s")
print(f"bins zerados em cada bloco: k = {k_guitarra} ({f_guitarra} Hz) e k = {N - k_guitarra} (espelho)")
print(f"saída = violão puro?  {np.allclose(saida, violao)}  "
      f"(erro máx {np.max(np.abs(saida - violao)):.1e})")

# ── 3. Gráficos: um bloco antes e depois ────────────────────────────────────
meio = N // 2 + 1
f = np.arange(meio) * fs / N
mag_antes = np.abs(dft_v1([float(v) for v in mistura[:N]]))[:meio]
mag_depois = np.abs(dft_v1([float(v) for v in saida[:N]]))[:meio]
zoom = n < fs * 0.01                                # 10 ms

fig, ax = plt.subplots(2, 2, figsize=(12, 7))
ax[0, 0].plot(n[zoom] / fs * 1e3, mistura[zoom], 'r')
ax[0, 0].set_title('Entrada: violão + guitarra misturados')
ax[0, 1].stem(f, mag_antes, linefmt='r-', markerfmt=' ', basefmt=' ')
ax[0, 1].set_title('Entrada na frequência: dois picos (DFT v1)')
ax[1, 0].plot(n[zoom] / fs * 1e3, saida[zoom], 'b', label='saída')
ax[1, 0].plot(n[zoom] / fs * 1e3, violao[zoom], 'k:', label='violão original')
ax[1, 0].set_title('Saída: igual ao violão original')
ax[1, 0].legend(loc='upper right')
ax[1, 1].stem(f, mag_depois, linefmt='b-', markerfmt=' ', basefmt=' ')
ax[1, 1].set_title('Saída na frequência: a guitarra sumiu')
nomes = {f_violao: 'violão', f_guitarra: 'guitarra'}
for i, (mag, cor) in enumerate([(mag_antes, 'r'), (mag_depois, 'b')]):
    for kk in np.flatnonzero(mag > 0.5 * mag.max()):
        ax[i, 1].annotate(f'{nomes[int(f[kk])]}\n{f[kk]:.0f} Hz', (f[kk], mag[kk]),
                          textcoords='offset points', xytext=(6, -10), ha='left', va='top', color=cor)
for a in ax[:, 0]:
    a.set_xlabel('t (ms)')
for a in ax[:, 1]:
    a.set_xlabel('f (Hz)')
    a.set_xlim([0, 2000])
    a.set_ylim([0, 1.2 * mag_antes.max()])
for a in ax.ravel():
    a.grid(True)
fig.tight_layout()

# ── 4. Som: a mistura e depois só o violão ──────────────────────────────────
if '--sem-som' not in sys.argv:
    print()
    tocar(mistura, fs, 'a mistura (violão + guitarra)')
    time.sleep(0.3)
    tocar(saida, fs, 'a saída (só o violão)')

plt.show()
