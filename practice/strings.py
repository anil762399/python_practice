# STRINGS ARE IMMUTABLE

a = """
  strings \
- Representation (single, double, triple) 
"""
print(a)
print(a.strip())

'''a = "
strings \
- Representation (single, double, triple) 
" '''

g = "gayathri"
b = '1234567'
c =  """chandu"""
d = '''dharani'''

#indexing

print(f"Positive index: {b[2]}")
print(f"Negative index: {b[-4]}")

# quote character and \ in string
print('python\'s')
print('python\\\'s')

# multi line string(using \)
sentence = 'This \
is python \
prime batch'
print(sentence)

# multi line string(using """)
anil=""" 
he is a brother \
of gayathri
"""
print(anil)

# concatination
x="anil is brother of "
y="gayathri"
relation=x + y
print(relation)
print(relation.capitalize() and y.capitalize())    # <------

# repeatation 
repeated_string = "he" * 3  
print(repeated_string)

# methods
string="hello world"
string=string.replace('hello', 'Hi')
print(string)

print(string.upper()) 
print(string.lower()) 
print(a.strip()) # -----> removes spaces 

# index vs find

sentence = "this is zkdgber ger grt zach salvatore"
# print(sentence.index("j"))
# print(sentence.rfind("z"))
print(sentence.find("j"))


sentence = "steewefrgkj@nrjkrhtgrejkrhrve@gmail.com"
print(sentence[sentence.rfind("@"):] == "@ gmail.com")

print(sentence.startswith("T")) 
print(sentence.endswith("@gmail.com"))

sentence = "1223"
print(sentence.isalnum())
print(sentence.isalpha())
print(sentence.isdigit())



# slicing
""" 
syntax --> var[start:stop:step]
syntax --> var[start:stop]
"""
sentence = "This is python code"
print(f"positive index--->{sentence[0:2:2]}")
print(f"positive index--->{sentence[0:]}")
print(f"positive index--->{sentence[:]}")
print(f"positive index--->{sentence[:4:2]}")


print(f"negative index ---->{sentence[-4::2]}")
print(f"negative index ---->{sentence[-1::-1]}")
print(f"negative index ---->{sentence[-11:5]}")
print(f"negative index ---->{sentence[::]}")
print(f"negative index ---->{sentence[:]}")








