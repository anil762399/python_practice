

""" 
Checking Palindromes
You need to check if each word in a list of words is a palindrome.
if it is palindrome, make the word as key and value as True
else, make the word as key and value as False

Sample Input:
  words = ["radar", "apple", "level", "world"]
Sample Output:
  {"radar":True, "apple":False, "level":True, "world":False}
"""
words = ["radar", "apple", "level", "world"]
result = {}
for word in words:
    if word == word[::-1]:  
        result[word] = True  
    else:
        result[word] = False  
print(result)
