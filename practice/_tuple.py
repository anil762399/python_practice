# tuple (), ordered, immutable
# arr = ("code",1, 1, 2, 3)
# print(arr.count(1))
# print(arr)

data = [(1, "steeve", "nyk"), (2, "steeve", "nyk")]
steeve_cnt = 0
for bio in range(len(data)):
    if data[bio][1] == "steeve":
        steeve_cnt += 1
print(steeve_cnt)

data = [(1, "steeve", "nyk"), (2, "tony", "nyk")]
for user in range(len(data)):
    print(data[user][0]) # (1, 'steeve', 'nyk')

data = [
    (1, "steeve", "nyk", 100000), 
    (2, "tony", "nyk", 50000),
    (12, "bucky", "usa", 200),
    (10, "nat", "uk", 4000)
	]
data.sort(key=lambda x:x[2], reverse=True)
for user in range(len(data)):
    print(*data[user])

# unpacking
values = (1, 2, 3, 4, 5)
a, b, *rest = values
print(a)       
print(b)       
print(rest)    
