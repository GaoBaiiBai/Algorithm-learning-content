from timeit import Timer
li1=[1,2]
li2=[23,5]

li = li1+li2
li = [i for i in range(10000)]
li = list(range(10000))
def test1():
    li = []
    for i in range(10000):
        li +=[i]
def test2():
    li =[]
    for i in range(10000):
        li.append(i)
def test3():
    li = [i for i in range(10000)]
def test4():
    li = list(range(10000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "seconds")
