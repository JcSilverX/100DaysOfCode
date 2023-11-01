
"""
    add -> n1 + n2
"""
def add(n1, n2):
    return n1 + n2


"""
    subtract -> n1 - n2
"""
def subtract(n1, n2):
    return n1 - n2


"""
    multiply -> n1 * n2
"""
def multiply(n1, n2):
    return n1 * n2


"""
    divide -> n1 / n2
"""
def divide(n1, n2):
    return n1 / n2


opts = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
