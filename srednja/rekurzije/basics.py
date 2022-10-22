import math


def basic_recursion_1(n):
    if n < 0:
        print(f"A: {n}")
        return
    else:
        print(f"B: {n}")
        basic_recursion_1(n - 1)
        print(f"C: {n}")


def basic_recursion_2(n):
    if n < 0:
        print(f"A: {n}")
        return
    else:
        if n % 2 == 0:
            print(f"B1: {n}")
            print(f"Broj {n} je paran.")
        else:
            print(f"B2: {n}")
            print(f"Broj {n} je neparan.")
        print(f"C: {n}")
        basic_recursion_2(n - 1)
        print(f"D: {n}")


def length_recursive(s):
    if s == "":
        return 0
    else:
        return 1 + length_recursive(s[1:])


def potention(a, b):
    # pretpostavka: a^b != 0^0
    if a == 0:
        return 0
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a * potention(a, b - 1)


def multisqrt(n):
    if n == 1:
        return math.sqrt(6)
    else:
        return math.sqrt(6 + multisqrt(n - 1))


def binary_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 10 * binary_recursive(n // 2) + n % 2


def n_letters(letter, content):
    if content == "":
        return 0
    else:
        if content[0] == letter:
            return 1 + n_letters(letter, content[1:])
        else:
            return 0 + n_letters(letter, content[1:])


def max_list(content):
    if len(content) == 0:
        return 0
    if len(content) == 1:
        return content[0]
    else:
        return max(content[0], max_list(content[1:]))


def euclid_recursive(n1, n2):
    bigger = max(n1, n2)
    smaller = min(n1, n2)
    modulo = bigger % smaller
    if modulo == 0:
        return smaller
    else:
        return euclid_recursive(smaller, modulo)


def suma(n):
    if n == 1:
        return 1
    else:
        return 1.0/n + suma(n-1)


print(suma(2))
