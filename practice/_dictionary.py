"""
 dictionary -> {}, mutable, unordered, unique
--> cannot use mutable data types as key in dictionary
--> keys can be any data types
--> duplicates are not allowed
"""
x={"name":"anil"}
print(x)

# adding value by using key
x["age"]=20
print(x)
print("=======================")

# accessing value by using key
value=x["name"]
print(value)
print(x["name"])
print("=======================")

# get method
value1=x.get("town","key not in dictionary") 
print(value1)
print("=======================")

# update
x["name"]="gayathri"
print(x)
print("=======================")

# in 
print("name" in x)
print("=======================")

# pop
#value=x.pop("age")  #----> it will return popped value 20
#print(value)
x.pop("age")        #-----> it will return {'name': 'gayathri'}
print(x)
print("=======================")

#iterate
y={"name":"gayathri","age":20}
for key in y.keys():
    print(key)
print("=======================")

for value in y.values():
    print(value)

# llist of tuples and lists into dictionary

list_of_tuples = ("a", 1), ("b", 2)
my_dict = dict(list_of_tuples)  # Output: {"a": 1, "b": 2}
print(my_dict)

temp1 = [("name1", "nick"), ("course1", "python")] # list of tuples
temp2 = [["course2", "python"]] # list of lists
temp3 = [{"name3", "nick"}, {"course3", "python"}] # working, but not suggestable
print(dict(temp1))
print(dict(temp2))
print(dict(temp3))
