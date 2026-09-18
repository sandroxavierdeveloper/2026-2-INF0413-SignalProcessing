# Biblioteca de plotagem customizada
import matplotlib.pyplot as plt

plt.style.use('default')

def figureFormat(ax, fig=None, tight=False):
    """Formata uma figura de forma padronizada."""
    if hasattr(ax, '__len__'):
        for a in ax:
            if hasattr(a, 'grid'):
                a.grid(True)
    else:
        if hasattr(ax, 'grid'):
            ax.grid(True)
            
    if tight and fig is not None:
        fig.tight_layout()
