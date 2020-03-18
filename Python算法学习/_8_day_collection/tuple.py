from collections import *
from collections.abc import *
# tuple是个不可变的对象
# name_tuple
# 元祖的拆包用法
name,age,height=("高永奇",15,175)
age,sd = ([1,2,58,2],[7,8,9,5,2,3])
print(name,age,height)
for i,q in zip(age,sd):
    print(i)
    print(q)
    print("----")
name, *other=("高永奇",15,175)
print(name)
print(other)
'''
# 元组中大部分都是不可变的对象 immutable 
# 性能优化：指出元素全部为immutable的tuple会作为常量在编译时确定，
# 因此产生了如此显著的速度差异
我们学习了list又学tuple的原因是因为,tuple在定下定值的时候因为list里的值不一定是定值
而当编译的过程中为定值的时候就可以更快的运行

list、set和dictionary 都是可改变的，比如可以通过list.append()，set.remove()，dict['key'] = value对其进行修改，所以它们都是不可哈希的；
而tuple和string是不可变的，只可以做复制或者切片等操作，所以它们就是可哈希的。
'''



