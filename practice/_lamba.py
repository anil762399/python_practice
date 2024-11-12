# lambda  -> anonymous function
def wish(name):
    return f"Hey {name}, Happy Coding"
print(wish("stefan"))
print(wish("damon"))

wishing = lambda name:f"Hey {name}, Happy Coding"
print(wishing("stefan"))
print(wishing("damon"))


def addition(n1, n2):
    return n1 + n2
print(addition(10, 20))

addition = lambda n1, n2: n1 + n2
print(addition(10, 20))