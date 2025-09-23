def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def powi(a, n):
    """Potência inteira: a^n. Exige n inteiro."""
    if not isinstance(n, int):
        raise TypeError("n must be int")
    return a ** n
