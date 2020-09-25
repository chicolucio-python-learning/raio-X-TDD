def calc(a, b):
    return a + b


# quando é True, não há retorno visível
assert 3 == calc(1, 2)

# quando é False, mostra AssertionError
assert 4 == calc(1, 2)
