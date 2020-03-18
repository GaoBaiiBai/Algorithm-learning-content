import  math
x = str(math.sqrt((3**4+5+6**7)/8))
print(x.format(""))

list1=["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", \
      "综合", "综合", "师范", "理工", "综合", "理工", "综合", "综合", \
      "综合", "综合", "综合", "理工", "理工", "理工", "理工", "师范", \
      "综合", "农林", "理工", "综合", "理工", "理工", "理工", "综合", \
      "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
word = {}
for i in list1:
    word[i] = word.get(i,0)+1
print(word)
dict1= {'综合': 20, '理工': 13, '师范': 2, '农林': 2, '民族': 1, '军事': 1}
print(dict1.get("综合")+1)

for s in "HelloWorld":
    if s=="W":
        continue
    print(s,end="")
print("")
print(set(list1))

list4=[5,48,45,5,4,5,15,1,56,5,4,54,8,4,5,45,4]
for i in range(len(list4)):
    for j in range(len(list4)-1):
        if list4[j] >list4[j+1]:
            list4[j],list4[j+1] = list4[j+1],list4[j]
print(list4)