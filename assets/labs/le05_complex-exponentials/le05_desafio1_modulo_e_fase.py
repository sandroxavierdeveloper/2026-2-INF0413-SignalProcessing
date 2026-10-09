#!/usr/bin/env python
# coding: utf-8
"""
le05 — Desafio 1: módulo e fase de um número complexo SEM funções prontas.

Enunciado (le05_complex-numbers.ipynb):
    "Crie funções customizadas para calcular o módulo e fase de um complexo.
     Obs: ñ funções prontas!"

Só são usados operadores (+ - * / **), comparações e laços. Nada de abs, sqrt,
atan, atan2, angle — nem a constante pi, que é calculada aqui mesmo.

Ideia:
  1. Módulo — Pitágoras: |z| = (a^2 + b^2)^(1/2).
  2. arctan — série de Taylor  arctan(u) = u - u^3/3 + u^5/5 - ...
     Ela só converge rápido para |u| pequeno, então antes reduzimos u:
       - se |u| > 1:  arctan(u) = ±pi/2 - arctan(1/u)
       - meio ângulo: arctan(u) = 2 arctan( u / (1 + sqrt(1 + u^2)) )
  3. pi — fórmula de Machin: pi = 16 arctan(1/5) - 4 arctan(1/239).
  4. Fase — arctan2 próprio: decide o quadrante pelos sinais de a e de b
     separadamente. O arctan(b/a) sozinho erra no 2º e no 3º quadrantes,
     porque (-4)/(-3) = 4/3.

Uso:
    python le05_desafio1_modulo_e_fase.py
"""


def serie_arctan(u, tol=1e-17):
    """arctan(u) pela série de Taylor (para |u| pequeno)."""
    total = 0.0
    termo = u        # u^(2m+1) com o sinal alternado
    m = 1            # denominador ímpar: 1, 3, 5, ...
    while (termo / m if termo > 0 else -termo / m) > tol:
        total += termo / m
        termo *= -u * u
        m += 2
    return total


# pi pela fórmula de Machin, usando só a série acima
PI = 16 * serie_arctan(1 / 5) - 4 * serie_arctan(1 / 239)


def meu_arctan(u):
    """arctan(u) para qualquer u real, em (-pi/2, pi/2)."""
    if u > 1:
        return PI / 2 - meu_arctan(1 / u)
    if u < -1:
        return -PI / 2 - meu_arctan(1 / u)
    for _ in range(3):                 # 3 meios-ângulos: |u| <= 1 vira |u| <= 0.1
        u = u / (1 + (1 + u * u) ** 0.5)
    return 8 * serie_arctan(u)         # desfaz os meios-ângulos: 2^3 = 8


def meu_arctan2(b, a):
    """Ângulo do ponto (a, b) em (-pi, pi], decidindo o quadrante pelos sinais."""
    if a > 0:
        return meu_arctan(b / a)               # quadrantes 1 e 4
    if a < 0:
        if b >= 0:
            return meu_arctan(b / a) + PI      # quadrante 2
        return meu_arctan(b / a) - PI          # quadrante 3
    if b > 0:
        return PI / 2                          # semieixo imaginário positivo
    if b < 0:
        return -PI / 2                         # semieixo imaginário negativo
    return 0.0                                 # z = 0: fase indefinida, convenção 0


def myMagnitude(z):
    """Módulo de z = a + bj."""
    return (z.real ** 2 + z.imag ** 2) ** 0.5


def myPhase(z, degUnits=False):
    """Fase de z = a + bj, em radianos (ou graus, com degUnits=True)."""
    phi = meu_arctan2(z.imag, z.real)
    if degUnits:
        phi = phi * 180 / PI
    return phi


if __name__ == '__main__':
    # A conferência usa o cmath da biblioteca padrão — só para comparar,
    # as funções acima não dependem dele.
    import cmath
    import random

    print(f"PI calculado = {PI!r}")
    print(f"cmath.pi     = {cmath.pi!r}\n")

    print(f"{'z':>9} | {'|z|':>7} {'fase':>10} | {'arctan(b/a)':>11} | {'cmath':>18}")
    for z in [3 + 4j, -3 + 4j, -3 - 4j, 3 - 4j, 1j, -1j, -1 + 0j, 0j]:
        ingenuo = meu_arctan(z.imag / z.real) * 180 / PI if z.real != 0 else float('nan')
        print(f"{z!s:>9} | {myMagnitude(z):7.4f} {myPhase(z, True):9.4f}° | "
              f"{ingenuo:10.4f}° | {abs(z):7.4f} {cmath.phase(z) * 180 / cmath.pi:9.4f}°")

    # Conferência em massa: complexos aleatórios em todos os quadrantes e escalas
    random.seed(0)
    erro_mag = erro_fase = 0.0
    for _ in range(100_000):
        z = complex(random.gauss(0, 1), random.gauss(0, 1)) * 10 ** random.uniform(-6, 6)
        erro_mag = max(erro_mag, abs(myMagnitude(z) - abs(z)) / abs(z))
        erro_fase = max(erro_fase, abs(myPhase(z) - cmath.phase(z)))
    print(f"\n100 mil complexos aleatórios:")
    print(f"  erro relativo máximo do módulo: {erro_mag:.1e}")
    print(f"  erro absoluto máximo da fase  : {erro_fase:.1e} rad")
