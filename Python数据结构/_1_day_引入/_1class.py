import time
starttime = time.time()
num = 0
# for a in range(0,998):
#     for b in range(0,1000):
#         for c in range(0,1000):
#             if a+b+c == 1000 and a**2 +b**2==c**2:
#                 print("a{},b{},c{}".format(a,b,c))
#                 num +=1

for a in range(0,998):
    for b in range(0,1000):
        c = 1000-a-b
        if a**2 +b**2==c**2:
            print("a{},b{},c{}".format(a,b,c))
            num +=1
endtime = time.time()
finnaltime = endtime-starttime
print(finnaltime)
print(num)