# type conversions
""" 
 we can convert any data type into str and but, we can not convert string into all 
"""

num = (20)
print(type(num))

# int -> str
num = 3 #int
num = str(3) #str
print("int->str", num, type(num))


# int -> float
num = 3#int
num = float(3) #str
print("int->float", num, type(num))

num = 123.456
num = int(num)
print("float->int", num, type(num))


num = "12345"
num = int(num)
print("str->int", num, type(num))

num = "143.8"
num = float(num)
print("str->float", num, type(num))

num = "999.0"
num = float(num)
num = int(num)
print("str->int", num, type(num))

# non-zeroes or non-empty -------> True
# zeroes or empty -------> False
name = "anil"

name = bool(name)
print("str->bool", name, type(name)) 

print("================")
# composite type conversions
list1 = [1, 2, 3]
print(tuple(list1)) # ------> list into tuple
print(set(list1))   # ------> list into set
list2=[('x',1),('y',2)] # -----> list into dict
print(dict(list2))

print("=================")

my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # ---->tuple into list
print(my_list)

my_set = set(my_tuple)    # -----> tuple into set
print(my_list)

my_tuple = (('a', 1), ('b', 2))  # tuple into dict
my_dict = dict(my_tuple)
print(my_dict)
