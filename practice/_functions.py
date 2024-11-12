""" 
functions
  -return functions
  -not return functions
  -parameterized functions
  	-positional
    -keyword
    -default
    -*args
    -**kwargs(variable keyword arguments)
    -passing parameter by unpacking

--> To re-use the code
--> syntax: 
	def functionName(parameters):
		pass
--> function will get execute, only when it's called
--> if control finds return in function, it will get out of that entire function
"""
# non-return function & parameterized function
def welcome(name, bank):
    print(f"Hello {name}, Happy {bank} Banking")

welcome("Nick", "Paypal")
welcome("Rasool", "Hdfc")
welcome("Akash", "CANARA")
welcome("Anil", "ICICI")

print("-----------------------------------")

# return function & parameterized function
def welcome(name, bank):
   return f"Hello {name}, Happy {bank} Banking"

print(welcome("Dhanjay", "Paypal"))
print(welcome("Mouneesh", "Hdfc"))
print(welcome("Swaroop", "CANARA"))
print(welcome("Varma", "ICICI"))

print("-----------------------------------")

# non-parametrized function & return function
def oneToFive():
  for i in range(1, 6):
    print(i)
  return "done"

print(oneToFive())

print("-----------------------------------")

# non-parametrized function & non-return function
def oneToFive():
  for i in range(1, 6):
    print(i)

oneToFive() 

print("-----------------------------------")

# *args
def numbers(a, *args):
    print(f"Numbers are {a}, {args}")

print(numbers(10, 20, 30, 40))
numbers(30, 40)

# **kwargs(variable keyword arguments)

"""
ORDER:
   positional, Default
  	    *args, **kwargs
"""

def details(**kwargs):
    print(kwargs)

details(age=15, name="gayathri", brother="vidhya")

print("--------------------------------------------")

def details(a, **kwargs):
    print(kwargs)

details(100, age=15, name="latha", brother="maaz") 

print("--------------------------------------------")

def details(a, *args, **kwargs):
    print(a, args, kwargs)

details(100, 200, 300, 400, city="newJersey", age=15, name="asma", brother="rayyan") 

# passing parameters by unpacking
clrs = ("red", "blue", "green")

def colors(c1, c2, c3):
    print(f"Colors are {c1}, {c2}, {c3}")

colors(clrs[0], clrs[1], clrs[2])
colors(clrs[0], clrs[2], clrs[1])
colors(*clrs)

# Examples
def details(a, b, name, age, city="ong"):
    print(a, b, name, age, city)
details(10, 20, age=123, name="steeve")

print("============================")

# examples
def addition(*args):
    print(sum(args))
addition(10, 20, 30, 40)
addition(10, 20)
addition(10, 20, 30, 40, 50)

print("============================")

def addition(n1, n2, *remaining):
    return n1 + n2 + sum(remaining)
addition(10, 20, 30, 40, 50, 60)