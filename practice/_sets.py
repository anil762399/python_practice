# Creating a set with curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Creating an empty set (must use `set()`; {} creates an empty dictionary)
empty_set = set()


# add
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# remove and discard
fruits.remove("banana")  # Removes 'banana'
fruits.discard("pear")   # Does nothing, as 'pear' is not in the set

#pop
fruits = {"apple", "banana", "cherry"}
popped_item = fruits.pop()
print(popped_item)  # Output: (random element, e.g., "apple")
print(fruits)       # Output: Remaining elements, e.g., {"banana", "cherry"}

# update 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}

#intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)  # Output: {3}

#difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)  # Output: {1, 2}

# isdisjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(set1.isdisjoint(set2))  # Output: True (no common elements)
print(set1.isdisjoint(set3))  # Output: False (3 is common)

# issubset
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True (set1 is a subset of set2)
print(set2.issubset(set1))  # Output: False (set2 has extra elements)

# issuperset
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True (set1 is a superset of set2)
print(set2.issuperset(set1))  # Output: False (set2 does not contain all elements of set1)

