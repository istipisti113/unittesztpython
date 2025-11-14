def sum(a: int, b: int):
    return a+b

def sub(a: int, b: int):
    return a-b

def mul(a: int, b: int):
    return a*b

def div(a: int, b: int):
    if not b==0:
        return a/b
    else:
        "Division by zero"