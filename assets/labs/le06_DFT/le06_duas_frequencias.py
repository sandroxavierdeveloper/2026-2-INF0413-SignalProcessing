#!/usr/bin/env python
# coding: utf-8
"""
le06 — Sinal com duas frequências (900 Hz + 1200 Hz) e a DFT que as revela.

    x(t) = sin(2π·900·t) + sin(2π·1200·t)

amostrado em fs = 8000 Hz (acima de 2 x 1200 = 2400 Hz, Nyquist ok).

Por que N = 800 amostras na DFT:
    a resolução em frequência é Δf = fs / N = 8000 / 800 = 10 Hz, e as duas
    frequências caem EXATAMENTE em bins inteiros:
        k = f / Δf  ->  900 / 10 = 90   e   1200 / 10 = 120
    Cada senoide de amplitude A vira dois picos de altura A·N/2 = 400, em k e
    em N - k (o espelho da metade negativa). Se f não caísse num bin inteiro,
    a energia "vazaria" para os bins vizinhos (vazamento espectral).

A DFT é a v1 do slide (le06_v1_signal_notation.py), que também toca o som.

Uso:
    python le06_duas_frequencias.py            # gráficos + som
    python le06_duas_frequencias.py --sem-som  # só gráficos
"""

import sys
import time

import matplotlib.pyplot as plt
import numpy as np

from le06_v1_signal_notation import dft_v1, tocar

fs = 8000            # Hz
f1, f2 = 900, 1200   # Hz
duracao = 1.0        # s de som para ouvir
N = 800              # amostras analisadas pela DFT -> Δf = 10 Hz

# ── 1. O sinal ──────────────────────────────────────────────────────────────
t = np.arange(int(duracao * fs)) / fs
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.sin(2 * np.pi * f2 * t)
x = x1 + x2

# ── 2. A DFT (v1) das primeiras N amostras ──────────────────────────────────
X = dft_v1([float(v) for v in x[:N]])
mag = np.abs(X)
k = np.arange(N // 2 + 1)
f = k * fs / N                        # frequência de cada bin (Hz)

# As frequências presentes: bins da metade 0..fs/2 com pico acima de metade do máximo
meio = mag[:N // 2 + 1]
achadas = k[meio > 0.5 * meio.max()]

print(f"fs = {fs} Hz, N = {N}, resolução Δf = fs/N = {fs / N:.0f} Hz\n")
print("Frequências encontradas pela DFT:")
for kk in achadas:
    print(f"  k = {kk:3d}  ->  f = k·fs/N = {kk * fs / N:6.0f} Hz   |X[k]| = {meio[kk]:.1f}  "
          f"(amplitude = 2|X|/N = {2 * meio[kk] / N:.2f})")
outros = np.delete(meio, achadas)
print(f"\nmaior |X[k]| fora desses bins: {outros.max():.1e} (zero, a menos de arredondamento)")

# ── 3. Gráficos ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(3, 1, figsize=(10, 9))

zoom = t < 0.01                       # 10 ms: 9 ciclos de 900 Hz, 12 de 1200 Hz
ax[0].plot(t[zoom] * 1e3, x1[zoom], color='tab:blue', linewidth=1, label=f'{f1} Hz')
ax[0].plot(t[zoom] * 1e3, x2[zoom], color='tab:orange', linewidth=1, label=f'{f2} Hz')
ax[0].set_title('As duas senoides separadas (10 ms)')
ax[0].set_xlabel('t (ms)')
ax[0].legend(loc='upper right')

ax[1].plot(t[zoom] * 1e3, x[zoom], 'r')
ax[1].set_title(f'x(t) = sin(2π·{f1}t) + sin(2π·{f2}t) — no tempo as frequências se misturam')
ax[1].set_xlabel('t (ms)')

ax[2].stem(f, meio, basefmt=' ')
for kk in achadas:
    ax[2].annotate(f'{kk * fs / N:.0f} Hz\n(k = {kk})', (f[kk], meio[kk]),
                   textcoords='offset points', xytext=(0, 6), ha='center')
ax[2].set_xlim([0, fs / 2])
ax[2].set_ylim([0, 1.25 * meio.max()])
ax[2].set_title(f'|X[k]| — DFT v1, N = {N}: na frequência elas se separam')
ax[2].set_xlabel('f = k·fs/N (Hz)')

for a in ax:
    a.grid(True)
fig.tight_layout()

# ── 4. Som: cada frequência sozinha, depois as duas juntas ──────────────────
if '--sem-som' not in sys.argv:
    print()
    for sinal, rotulo in [(x1, f'{f1} Hz'), (x2, f'{f2} Hz'), (x, f'{f1} Hz + {f2} Hz')]:
        tocar(sinal, fs, rotulo)
        time.sleep(0.3)

plt.show()
