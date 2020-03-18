from  collections import namedtuple
# tuple的编译比写class要快，并且相比于class更加占内存和复杂
user =namedtuple("user",["name","age","height","other"])
user1 = user(name='boddy',age=29,height=175,other=25)
print(user1.name,user1.age,user1.height)

user.other="高永奇"
user_tuple = ("bobby",29,15,58)
user_info =user(*user_tuple)
print(user.name,user.age,user.height)

def ask(*args,**target):
    pass
# 传递进来的是一个元祖
ask("bobby",18)
# 传递进来的是一个dict{"name":null,"age":null}
ask(name="bobby",age=18)
# 将数据转换成orderdict
user_info_dict= user._asdict()
