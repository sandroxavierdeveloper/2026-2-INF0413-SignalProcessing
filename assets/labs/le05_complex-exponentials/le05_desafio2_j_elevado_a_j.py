#!/usr/bin/env python
# coding: utf-8
"""
le05 — Desafio 2: antecipar o gráfico de z = j^j no plano complexo.

Enunciado (le05_complex-numbers.ipynb):
    "Curioso, não é? Desafio: Antecipar o gráfico do seguinte número no
     plano complexo:  z = 1j ** 1j"

Antecipação (antes de perguntar ao Python):
    Na forma polar, j = e^(j pi/2). Então

        j^j = (e^(j pi/2))^j = e^(j * j * pi/2) = e^(-pi/2) ≈ 0.2079

    Um número REAL e positivo: o ponto cai sobre o eixo Re{z}, com fase zero.

    Em geral z^w = e^(w ln z), com ln z = ln|z| + j fase(z). Como |j| = 1,
    ln j = j fase(j) e j^j = e^(-fase(j)). Basta a fase do Desafio 1.

Mais curioso ainda:
    a fase de j não é só pi/2, é pi/2 + 2 pi k para qualquer inteiro k.
    Então j^j tem infinitos valores, e^(-(pi/2 + 2 pi k)), todos reais e
    positivos. O Python devolve o ramo principal (k = 0).

Uso:
    python le05_desafio2_j_elevado_a_j.py
"""

import matplotlib.pyplot as plt

from le05_desafio1_modulo_e_fase import PI, myMagnitude, myPhase


def meu_exp(x, tol=1e-17):
    """e^x pela série de Taylor, sem funções prontas."""
    # e^x = (e^(x/2^m))^(2^m): reduz x para a série convergir rápido
    m = 0
    while (x if x > 0 else -x) > 0.5:
        x /= 2
        m += 1
    total, termo, n = 1.0, 1.0, 1
    while (termo if termo > 0 else -termo) > tol:
        termo *= x / n
        total += termo
        n += 1
    for _ in range(m):
        total *= total
    return total


# 1. Antecipação: j^j = e^(-fase(j)), só com as funções próprias
fase_j = myPhase(1j)
previsto = meu_exp(-fase_j)

# 2. O que o Python calcula
z = 1j ** 1j

print(f"fase(j)               = {fase_j!r}  (= pi/2)")
print(f"previsto e^(-fase(j)) = {previsto!r}")
print(f"Python  1j ** 1j      = {z!r}")
print(f"\nparte real = {z.real:.6f}, parte imaginária = {z.imag:.6f}")
print(f"módulo = {myMagnitude(z):.6f}, fase = {myPhase(z, True):.6f}°  -> real e positivo")

# 3. Os infinitos valores de j^j
print("\nTodos os valores de j^j = e^(-(pi/2 + 2 pi k)):")
ks = range(-2, 3)
valores = [meu_exp(-(PI / 2 + 2 * PI * k)) for k in ks]
for k, v in zip(ks, valores):
    print(f"  k = {k:+d}:  {v:.6e}" + ("   <- ramo principal (Python)" if k == 0 else ""))

# 4. Gráficos
fig, ax = plt.subplots(1, 2, figsize=(12, 5.5))

# 4a. j e j^j no plano complexo
ax[0].plot(0, 1, 'bo')
ax[0].arrow(0, 0, 0, 1, color='b', linestyle='--', length_includes_head=True,
            head_width=0.03, label='j')
ax[0].plot(z.real, z.imag, 'go')
ax[0].arrow(0, 0, z.real, z.imag, color='g', linestyle='--', length_includes_head=True,
            head_width=0.03, label=f'j^j = {z.real:.4f}')
ax[0].axhline(0, color='black', linewidth=1)
ax[0].axvline(0, color='black', linewidth=1)
ax[0].set_xlim([-1.1, 1.1])
ax[0].set_ylim([-1.1, 1.1])
ax[0].set_aspect('equal')
ax[0].set_xlabel('Re{z}')
ax[0].set_ylabel('Im{z}')
ax[0].set_title('j^j cai sobre o eixo real')
ax[0].grid(True)
ax[0].legend()

# 4b. Os valores de j^j para k = -2 ... 2, em escala log
ax[1].plot(valores, [0] * len(valores), 'go')
for k, v in zip(ks, valores):
    ax[1].annotate(f'k={k}', (v, 0), textcoords='offset points', xytext=(0, 8), ha='center')
ax[1].set_xscale('log')
ax[1].set_yticks([])
ax[1].set_xlabel('Re{z} (escala log)')
ax[1].set_title('Todos os valores de j^j: reais e positivos')
ax[1].grid(True)

fig.tight_layout()
plt.show()
