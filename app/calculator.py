def add(a, b):
    return a + b

def dev(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b