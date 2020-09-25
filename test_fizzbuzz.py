"""
Regras do FizzBuzz

1. Se a posição for múltipla de 3, retorne 'fizz'
2. Se a posição for múltipla de 5, retorne 'buzz'
3. Se a posição for múltipla de 3 e 5, retorne 'fizzbuzz'
4. Para qualquer outra posição, retorne  o próprio número.

Programe um robô que jogue FizzBuzz
"""


def robot(value):
    say = str(value)
    if value % 15 == 0:
        say = 'fizzbuzz'
    elif value % 3 == 0:
        say = 'fizz'
    elif value % 5 == 0:
        say = 'buzz'
    return say


if __name__ == "__main__":
    assert robot(1) == '1'
    assert robot(2) == '2'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
