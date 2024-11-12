"""
convert the following functions into anonymous functions
"""
def homepage(name, bank):
    return f"Hey {name}, Happy {bank} Banking"

homepage = lambda name, bank: f"Hey {name}, Happy {bank} Banking"
print(homepage("anil","HDFC"))

def isNegative(num):
    return num<0
isNegative = lambda num: num < 0
print(isNegative(10))


def multiply(n1, n2, n3=1):
    return n1*n2*n3
multiply = lambda n1, n2, n3=1: n1 * n2 * n3
print(multiply(1,4))


def check(num):
    return num > 0 and num != 4
check = lambda num: num > 0 and num != 4
print(check(44))
