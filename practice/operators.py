""" 
operators
  Arithematic ---> +, -, *, /, //, %, **
  Short hand assignment ---> +=, -=, *=, /=, //=, %=, **=
  Relational ---> <=, >=, ==, !=
  Logical    ----> and, or
  MemberShip ----> in, not in
  Identity   ----> is, is not (based on id)
"""

#short hand assignment
num = 35
num += 5 # num = num + 5
print(num)
num *= 5 # num = num * 5
print(num)
num /= 5 # num = num / 5
print(num)

#Relational 
anil=20
gayathri=21
print(anil == gayathri)
print(anil <= gayathri)
print(anil >= gayathri)
print(anil != gayathri)

#membership
anil='gorrilla'
print('g' in 'gorrilla')  # or print('k' in 'kondamuchhu') , print('g' in 'kondamuchhu')
print('x' not in 'gorrilla')

# identity operators
a = -6
b = -4
# object pooling range (-6, +256)
print(b==a)
print(a is b)
print( b is not a)

print(id(a))
print(id(b))