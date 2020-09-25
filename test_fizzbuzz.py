"""
Regras do FizzBuzz

1. Se a posição for múltipla de 3, retorne 'fizz'
2. Se a posição for múltipla de 5, retorne 'buzz'
3. Se a posição for múltipla de 3 e 5, retorne 'fizzbuzz'
4. Para qualquer outra posição, retorne  o próprio número.

Programe um robô que jogue FizzBuzz
"""


def multiple_of_3(value):
    return value % 3 == 0


def multiple_of_5(value):
    return value % 5 == 0


def multiple_of_3_and_5(value):
    return multiple_of_3(value) and multiple_of_5(value)


def robot(value):
    say = str(value)
    if multiple_of_3_and_5(value):
        say = 'fizzbuzz'
    elif multiple_of_3(value):
        say = 'fizz'
    elif multiple_of_5(value):
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
