"""
Mutable,
Ordered,
Allows Duplicates,
Heterogeneous Elements 
"""
my_list = [1, 2, 3, "Python", True,3]
print (type(my_list))
print(my_list)

#index
print(my_list[3])
print(my_list.index(3))
print(my_list.index(3,3)) # Finding 3, starting the search from index 3

# slicing
anil=[1,2,'anil','gayathri']
print(anil[0:3])  #--------> [1, 2, 'anil']
print(anil[0:])   #--------> [1, 2, 'anil', 'gayathri']
print(anil[-3:])  #--------> [2, 'anil', 'gayathri']

# in, not in 
x=[1,2,3,4,5]
print(1 in x)
print(10 in x)
y=['anil','gayathri','akash']
print('srividhya' not in y)
print('anil' not in y) 

# len function
x=[]
print(len(x))

my_list = [10, 20, 30, 40, 50]
list_length = len(my_list)
print(list_length) 

# count function
my_list = [1, 2, 3, 4, 2, 2, 5]
count_2 = my_list.count(2)
print(count_2)  
count_5 = my_list.count(5)
print(count_5)  

# modify  ----> By using index value we can replace new element with existed element
my_list = [10, 20, 30, 40]
my_list[-1] = 25 
my_list[3]=25 
print(my_list) 

# append -----> we can add elements at the end of list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#anil=my_list.append(4) 
#print(anil)

#print(my_list.append(4))

my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)

x=[]
x.append(4**2)
print(x) 


# extend ------> we can add multiple values at the end 
a=[1,2,'anil','gayathri',True]
a.extend('sri')
a.extend((2,4))
a.extend({21,27})
#a.extend(1)  ? error coming
print(a)
a.extend([2,'sri'])
print(a)  

# INSERT  -----> we can insert an element at specified index
# syntax : list.insert(index, element)

b=[1,2,'anil','akash']
b.insert(2,10.5)
b.insert(-1,'rajesh')
b.insert(len(b),'maaz')
print(b)
#print(type(b[3]))
b.insert(1,[2,3])
print(b)
print("=============")
b.insert(-20,2)
b.insert(20,2)
print(b)  

# POP -----> we can remove an element at specific index or at last 
# syntax : list.pop([index])

c=[1,2,3,4,5]
c.pop() # ----> it will remove last element
print(c)
c.pop(2) # ---> by using index
print(c)
#print(c.pop())  ? o/p--> 5
c.pop(1)
print(c) # ---> error : index outoff range """

# REMOVE ---> removes first occurenced element 
e=[1,2,3,4,5,7,4,4]
e.remove(5)
print(e)

friends=['gayathri','rajesh','balaji','akash']
for names in friends[:]:
    if names=='rajesh':
        friends.remove(names)
print(friends)

# concatenate
list1=[1,2,3,4,45]
another_list=['anil','loki']
conc=list1+another_list
print(conc)

# reverse 
reverse=list[::-1]
print(reverse)

# min and max
print(max(list1))
print(min(list1))

# sort
names=['zxy','anil','Anil','Zck','1']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# sorted
numbers=[[1,2,3],[3,455,6]]
sorted_names = sorted(numbers, reverse=True)
print(sorted_names)


# nested 
nested=[[1,2,3],[3,455,6]]
nested1=nested[1][2]
print(nested1)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Iterating over each sublist and then each element within the sublist
for sublist in nested_list:
    for element in sublist:
        print(element, end=' ')  # Output ----> 1 2 3 4 5 6 7 8 9

#unpacking
numbers2 = [1, 2, 3]
a, b, c = numbers2
print(a)   
print(b)   
print(c)   
# using * 
number2 = [1, 2, 3, 4, 5]
a, *rest = numbers2      # First element goes to 'a', the rest go to 'rest'
print(a)    
print(rest)   

# using * in middle
numbers3= [1, 2, 3, 4, 5, 6]
a, b, *middle, c = numbers3
print(a)       
print(b)       
print(middle)  
print(c) 

# nested list
data = [1, [2, 3], 4]
a, (b, c), d = data
print(a)   
print(b)   
print(c)   
print(d)   

# no need 
numbers4 = [1, 2, 3, 4]
a, _, _, d = numbers4
print(a) 
print(d)  

bio = ["1001", "steeve", "brooklyn"]
_id, *rest = bio
print(f"Remaining elements after unpacking bio: {rest}")

# list conversion
name = ("CodeWala",)
print(f"List created from tuple: {list(name)}\n")









