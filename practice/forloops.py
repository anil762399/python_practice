for steeve in range(0,10):
    print(steeve)

print("========================================")

name = ("steeverogers")
for anil in range(0,10):
    print(name)

print("===========================")

name = ("steeverogers")
for anil in range(0,len(name)):
    print(name[anil])

# tuple
name = ("steeverogers","anil","gayathri")  
for steeve in range(0,2):
    print(name)  #-------------> ("steeverogers","anil","gayathri")  
    print(name[steeve]) # -----> steeverogers, anil"""



""" 
take 5 inputs from user
after each input, print if input length is below or equal to 5, else print invalid  """

for num in range(2):
    name = input(f"Enter Input-{num} :")
    if len(name) <= 5:
        print(f"Output: {name}")
    else:
        print("invalid")
        #break

for i in range(2):
    data = int(input("Enter Number: "))
    if data <= 100:
        print("Valid Input")
    else:
        print("invalid")
else:
    print("Invalid")

# for-else
for i in range(5):
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
else:
    print("No Negative values Entered")
