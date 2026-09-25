"""
mySignalProcessingLib.py — Biblioteca de Processamento de Sinais Discretos
Stub de compatibilidade para os notebooks do curso INF0413.

Exporta: SIGNALgenerate, SIGNALdelay, SIGNALplot, figureFormat
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio, display
import os, sys

# ─────────────────────────────────────────────
# SIGNALgenerate
# ─────────────────────────────────────────────
def SIGNALgenerate(N=100, signal='delta', params=None, amplitude=1.0, phase=0.0, period=10.0):
    """
    Gera sinais discretos fundamentais.
    signal: 'delta', 'step', 'exp', 'osc', 'random'
    params: dict com parâmetros do sinal OU string 'uniform' para ruído uniforme
    amplitude, phase, period: aliases convenientes para uso em notebooks.
    """
    n = np.arange(N)
    if signal in ('delta', 'impulse'):
        k = params.get('k', 0) if isinstance(params, dict) else 0
        x = np.where(n == k, amplitude, 0)
    elif signal in ('step', 'degrau'):
        k = params.get('k', 0) if isinstance(params, dict) else 0
        x = amplitude * np.where(n >= k, 1, 0)
    elif signal in ('exp', 'exponential'):
        a = params.get('a', 0.5) if isinstance(params, dict) else 0.5
        k = params.get('k', 0) if isinstance(params, dict) else 0
        x = amplitude * (a**n) * np.where(n >= k, 1, 0)
    elif signal in ('osc', 'sinusoid', 'sine'):
        P   = params.get('P', period) if isinstance(params, dict) else period
        phi = params.get('phi', phase) if isinstance(params, dict) else phase
        w0  = 2 * np.pi / P
        x   = amplitude * np.sin(w0 * n + phi)
    elif signal == 'random':
        if params == 'uniform':
            x = amplitude * np.random.uniform(-1, 1, N)
        else:
            x = amplitude * np.random.randn(N)
    else:
        x = np.zeros(N)
    return np.array(x), n

# ─────────────────────────────────────────────
# SIGNALdelay
# ─────────────────────────────────────────────
def SIGNALdelay(x, k):
    """Atrasa (k>0) ou adianta (k<0) um sinal discreto por k amostras."""
    result = np.zeros_like(x)
    if k > 0:
        result[k:] = x[:-k]
    elif k < 0:
        result[:k] = x[-k:]
    else:
        result = x.copy()
    return result

# ─────────────────────────────────────────────
# SIGNALplot
# ─────────────────────────────────────────────
def SIGNALplot(x, n=None, title='Sinal Discreto x[n]', color='r', xlim=None,
               xlabel='n (amostras)', max_stem=2000):
    """Plota um sinal discreto como stem plot.

    xlim    : [xmin, xmax] opcional, recorte do eixo horizontal.
    max_stem: acima desse número de amostras visíveis, usa linha (plot) em vez de stem.
    """
    x = np.asarray(x)
    n = np.arange(len(x)) if n is None else np.asarray(n)
    visible = len(x) if xlim is None else int(np.count_nonzero((n >= xlim[0]) & (n <= xlim[1])))
    fig, ax = plt.subplots(figsize=(10, 4))
    if visible <= max_stem:
        ax.stem(n, x, linefmt=f'{color}-', markerfmt=f'{color}o', basefmt=' ')
    else:
        ax.plot(n, x, color=color)
    if xlim is not None:
        ax.set_xlim(xlim)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    plt.show()

# ─────────────────────────────────────────────
# figureFormat — compatibilidade com myPlotLib
# ─────────────────────────────────────────────
def figureFormat(ax, fig=None, tight=False):
    """Formata uma figura de forma padronizada."""
    if hasattr(ax, '__len__'):
        for a in ax:
            a.grid(True)
    else:
        ax.grid(True)
    if tight and fig is not None:
        fig.tight_layout()
