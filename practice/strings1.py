# string formatting 

name = "anil"
age = 20
greeting = f"Hello! {name}, You are {age} years old."
#print(greeting)

greeting = "Hello, {} You are {} years old".format(name, age)
#print(greeting)

greeting = "Hello, %s You are %d years old" % (name, age)
print(greeting)

print("==================================")


