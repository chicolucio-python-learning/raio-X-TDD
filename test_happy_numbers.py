"""
Como saber se um número é feliz ou triste?

Dado um número inteiro positivo:
1. Substitua o número pela soma dos quadrados de seus dígitos
2. Se o resultado for 1, encerre a rotina
3. Caso contrário, repita o processo indefinidamente
4. Os números que resultarem em 1, são felizes. Os demais, tristes.

Exemplo:

a) Número 7
7² = 49
4² + 9² = 97
9² + 7² = 130
1² + 3² + 0² = 10
1² + 0² = 1 ---> Feliz

b) Número 4
4² = 16
1² + 6² = 37
3² + 7² = 58
5² + 8² = 89
8² + 9² = 145
1² + 4² + 5² = 42
4² + 2² = 20
2² + 0² = 4 ---> Triste (voltou ao número original)
"""


def happy(number):
    total = 0
    n = str(number)
    while (total != 1) and (total != number):
        total = sum([int(i)**2 for i in n])
        n = str(total)
    return total == 1


assert happy(1)
assert happy(10)
assert happy(100)
assert happy(7)
assert not happy(4)
