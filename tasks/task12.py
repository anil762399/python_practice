""" 
Recursion Tasks:
  create a function that can generate 20 to 5 in reverse order
  create a function that will asks for user input 5 times and print after each input
"""
# task1
def reverse(n):
    if n <= 5:
        return  
    print(n)
    reverse(n - 1)  
reverse(20)

# task2

def _name(entered_name):
    for i in range(6):
        name=input(f"enter name {i}:")
        print(name)
_name("name")

def _input(count):
    if count > 5:
        return
    user_name = input(f"Enter input {count}: ")
    print(f"You entered: {user_name}")
    _input(count + 1)
count = 1  
_input(count) 


