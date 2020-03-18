dict1 = {}
list1=[
    ["洪汪琪","2"],["洪汪琪","3"],["洪汪琪","4"],["洪汪琪","5"],
    ["洪汪琪1","2"],["洪汪琪1","3"],["洪汪琪1","4"],["洪汪琪1","5"],
]
for i in list1:
    # print(i)
    # print(dict1.get(i[0],i[1]))
    dict1[i[0]] = dict1.get(i[0],i[1])+","+i[1]
print(dict1)
a =[1,2,3]
b = a
a.append(1)
print(b)