# Biblioteca de plotagem customizada
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')

def figureFormat(ax, fig=None, tight=False):
    """Formata uma figura de forma padronizada.

    ax pode ser um único Axes ou um array de Axes (1D ou 2D, como retornado por plt.subplots).
    """
    for a in np.atleast_1d(ax).ravel():
        if hasattr(a, 'grid'):
            a.grid(True)

    if tight and fig is not None:
        fig.tight_layout()
