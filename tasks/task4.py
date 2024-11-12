""" 
TASK: Take email as an input from user, than can contain 
      lower, upper, numbers and domains like @gmail.com, @hotmail.com, @yahoo.com
    After separating the domain,
      print the domainless lowercase name and count the number of vowels in the email.

      Your code should work for all the mails, irrespective of the domain.
      NOTE: No invalid email should be taken

Sample Input1:
  NIck@gmail.com
Sample Output1:
  nick ---- 1

Sample Input2:
  coDEwala@yahoo.com
Sample Output2:
  codewala ---- 4

Sample Input3:
  SteeveRogers123@hotmail.com
Sample Output3:
  steeverogers123 ---- 5

"""

email=input("Enter email:")
#index=email.find("@")
name=email[:email.find("@")]
#print(name)
lower=name.lower()
#print(lower)
vowels="aeiou"
count=0
for i in lower:
    if i in vowels:
        count+=1
print(f"{lower}----{count}")