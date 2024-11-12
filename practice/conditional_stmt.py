# if
age = 18
if age >= 18:
    print("You are an adult.")  

# else
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.") 

#elif
age = 21
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.") 

# nested if-else
age = 20
if age >= 18:
    if age < 21:
        print("You are an adult, but not eligible to drink in the US.")
    else:
        print("You are an adult and eligible to drink.")
else:
    print("You are a minor.")



