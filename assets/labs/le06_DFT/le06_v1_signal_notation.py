#!/usr/bin/env python
# coding: utf-8
"""
le06 — DFT, v1: notação "Signal" (slide da aula).

Fórmula de análise — sinal de N pontos no domínio da frequência:

                N-1
    X[k]   =    Σ   x[n] e^(-j 2π n k / N),      k = 0, 1, ..., N-1
               n=0

Fórmula de síntese — sinal de N pontos no domínio do "tempo":

             1  N-1
    x[n]  =  -  Σ   X[k] e^(+j 2π n k / N),      n = 0, 1, ..., N-1
             N k=0

A v1 traduz cada fórmula ao pé da letra: um laço externo percorre o índice do
resultado (k na análise, n na síntese) e um laço interno faz o somatório.
São N x N termos, por isso o custo é O(N^2).

As duas funções usam só Python puro (listas e cmath.exp). O numpy entra apenas
para ler o som e para conferir o resultado contra np.fft.

Som: o train.wav inteiro (12880 amostras, 1,57 s) passa pela análise e pela
síntese da v1 em blocos de 1024 amostras, e o script toca o original e o
reconstruído pelo player do sistema (pw-play, paplay, aplay ou ffplay — o
primeiro que existir). Fora do Jupyter não há IPython.display.Audio, e o .venv
não tem biblioteca de áudio Python; o player do sistema não precisa de nenhuma.

Uso:
    python le06_v1_signal_notation.py            # gráficos + som
    python le06_v1_signal_notation.py --sem-som  # só gráficos e conferências
"""

import cmath
import os
import shutil
import subprocess
import sys
import tempfile
import time
import wave

import matplotlib.pyplot as plt
import numpy as np


def dft_v1(x):
    """Fórmula de análise: X[k] = Σ_n x[n] e^(-j 2π n k / N)."""
    N = len(x)
    X = []
    for k in range(N):                 # k = 0, 1, ..., N-1
        soma = 0j
        for n in range(N):             # Σ de n = 0 até N-1
            soma += x[n] * cmath.exp(-2j * cmath.pi * n * k / N)
        X.append(soma)
    return X


def idft_v1(X):
    """Fórmula de síntese: x[n] = (1/N) Σ_k X[k] e^(+j 2π n k / N)."""
    N = len(X)
    x = []
    for n in range(N):                 # n = 0, 1, ..., N-1
        soma = 0j
        for k in range(N):             # Σ de k = 0 até N-1
            soma += X[k] * cmath.exp(2j * cmath.pi * n * k / N)
        x.append(soma / N)
    return x


def ler_wav(caminho):
    """Lê um WAV de 16 bits mono como floats (mesma escala do audioread da lib)."""
    with wave.open(caminho) as arquivo:
        fs = arquivo.getframerate()
        dados = arquivo.readframes(arquivo.getnframes())
    return np.frombuffer(dados, dtype='int16').astype(float) / 65535, fs


def salvar_wav(caminho, x, fs):
    """Grava x como WAV mono de 16 bits, normalizado para pico 0,9."""
    x = np.asarray(x, dtype=float)
    pico = np.max(np.abs(x))
    amostras = np.round(0.9 * 32767 * x / pico).astype('<i2') if pico > 0 else np.zeros(len(x), '<i2')
    with wave.open(caminho, 'wb') as arquivo:
        arquivo.setnchannels(1)
        arquivo.setsampwidth(2)
        arquivo.setframerate(int(fs))
        arquivo.writeframes(amostras.tobytes())


PLAYERS = [
    ['pw-play'],                                    # PipeWire
    ['paplay'],                                     # PulseAudio
    ['aplay', '-q'],                                # ALSA
    ['ffplay', '-nodisp', '-autoexit', '-loglevel', 'error'],
]


def tocar(x, fs, rotulo):
    """Toca x pelo primeiro player do sistema disponível. Devolve True se tocou."""
    player = next((cmd for cmd in PLAYERS if shutil.which(cmd[0])), None)
    if player is None:
        print(f"  [som] nenhum player encontrado ({', '.join(c[0] for c in PLAYERS)}); "
              f"não foi possível tocar '{rotulo}'")
        return False
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, 'som.wav')
        salvar_wav(caminho, x, fs)
        print(f"  [som] tocando {rotulo} ({len(x) / fs:.2f} s) com {player[0]}...")
        resultado = subprocess.run(player + [caminho], capture_output=True, text=True)
    if resultado.returncode != 0:
        print(f"  [som] {player[0]} falhou (código {resultado.returncode}): {resultado.stderr.strip()}")
        return False
    return True


def sintetizar_em_blocos(x, tamanho=1024):
    """Análise + síntese v1 bloco a bloco; o último bloco usa o tamanho que sobrar."""
    reconstruido = []
    total = (len(x) + tamanho - 1) // tamanho
    for i, inicio in enumerate(range(0, len(x), tamanho), start=1):
        bloco = x[inicio:inicio + tamanho]
        reconstruido += [v.real for v in idft_v1(dft_v1(bloco))]
        print(f"\r  bloco {i}/{total}", end='', flush=True)
    print()
    return reconstruido


def arredonda(z):
    """Complexo legível: tira o ruído de arredondamento (1e-16) e o -0."""
    re, im = round(z.real, 10) + 0.0, round(z.imag, 10) + 0.0
    return complex(re, im)


if __name__ == '__main__':
    # ── 1. Exemplo à mão: x = [1, 2, 3, 4], N = 4 ───────────────────────────
    # Com N = 4, e^(-j 2π n k / 4) = (-j)^(nk), que só vale 1, -j, -1 ou j:
    #   X[0] = 1 + 2 + 3 + 4                    = 10
    #   X[1] = 1 + 2(-j) + 3(-1) + 4(j)         = -2 + 2j
    #   X[2] = 1 + 2(-1) + 3(1)  + 4(-1)        = -2
    #   X[3] = 1 + 2(j)  + 3(-1) + 4(-j)        = -2 - 2j
    x = [1, 2, 3, 4]
    X = dft_v1(x)
    print("Exemplo à mão, x =", x)
    print("  análise  X[k] =", [arredonda(v) for v in X])
    print("  esperado      = [(10+0j), (-2+2j), (-2+0j), (-2-2j)]")
    print("  síntese  x[n] =", [arredonda(v) for v in idft_v1(X)])

    # ── 2. Aplicação: os primeiros 1024 pontos do train.wav ─────────────────
    pasta_sons = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sounds')
    sinal, fs = ler_wav(os.path.join(pasta_sons, 'train.wav'))
    y = [float(v) for v in sinal[:1024]]  # float do Python: o laço fica ~4x mais rápido
    N = len(y)

    t0 = time.perf_counter()
    Y = dft_v1(y)
    t_analise = time.perf_counter() - t0

    t0 = time.perf_counter()
    y_rec = idft_v1(Y)
    t_sintese = time.perf_counter() - t0

    print(f"\ntrain.wav: N = {N}, fs = {fs} Hz")
    print(f"  análise : {t_analise:.2f} s  ({N}x{N} = {N * N:,} termos)".replace(',', '.'))
    print(f"  síntese : {t_sintese:.2f} s")
    print(f"  análise  = np.fft.fft ?  {np.allclose(Y, np.fft.fft(y))}  "
          f"(erro máx {np.max(np.abs(np.array(Y) - np.fft.fft(y))):.1e})")
    print(f"  síntese  devolve x[n] ? {np.allclose(y_rec, y)}  "
          f"(erro máx {np.max(np.abs(np.array(y_rec) - np.array(y))):.1e})")
    print(f"  parte imaginária da síntese: máx {max(abs(v.imag) for v in y_rec):.1e} "
          f"(x[n] é real; o resto é arredondamento)")

    # ── 3. Som: o train.wav inteiro, analisado e sintetizado pela v1 ───────
    print(f"\nSom: train.wav inteiro ({len(sinal)} amostras, {len(sinal) / fs:.2f} s) "
          f"pela v1, em blocos de 1024")
    t0 = time.perf_counter()
    som_rec = sintetizar_em_blocos([float(v) for v in sinal])
    print(f"  {time.perf_counter() - t0:.1f} s; reconstruído = original ? "
          f"{np.allclose(som_rec, sinal)} (erro máx {np.max(np.abs(np.array(som_rec) - sinal)):.1e})")

    if '--sem-som' not in sys.argv:
        tocar(sinal, fs, 'o original')
        time.sleep(0.5)
        tocar(som_rec, fs, 'o reconstruído pela síntese v1')

    # ── 4. Gráficos ─────────────────────────────────────────────────────────
    mag = np.abs(Y)
    f = np.arange(N // 2 + 1) * fs / N    # metade do espectro: 0 a fs/2

    fig, ax = plt.subplots(3, 1, figsize=(9, 8))
    ax[0].plot(y, 'r')
    ax[0].set_title('x[n] — 1024 amostras do train.wav')
    ax[0].set_xlabel('n')
    ax[1].plot(f, mag[:N // 2 + 1], 'r')
    ax[1].set_title('|X[k]| — análise (metade do espectro)')
    ax[1].set_xlabel('f = k fs / N (Hz)')
    ax[2].plot(y, 'r', label='original')
    ax[2].plot(np.real(y_rec), 'k--', linewidth=0.8, label='síntese')
    ax[2].set_title('x[n] reconstruído pela fórmula de síntese')
    ax[2].set_xlabel('n')
    ax[2].legend()
    for a in ax:
        a.grid(True)
    fig.tight_layout()
    plt.show()
