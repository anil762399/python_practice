"""
while loop repeatedly executes a block of code as long as a specified condition remains True
"""
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

name = "python"
current = 0
while current < len(name):
    print(name[current], current)
    current += 1
print("===================================")
name = "python"
current = len(name)-1
while current >= 0:
    print(name[current], current)
    current -= 1


# while-else
start = 0
while start < 5:
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
    start += 1
else:
    print("No Negative values Entered")