user_dict={}
users = ["bobby1","bobby2","bobby3","bobby1","bobby22","bobby3","bobby4","bobby2","bobby3","bobby3"]
# for user in users:
#     user_dict[user] = user_dict.get(user,0)+1
for user in users:
    user_dict.setdefault(user,0)
    user_dict[user] +=1
print(user_dict)
from  collections import defaultdict

# list为默认值的类型
# default_dict=defaultdict(list)
# default_dict["bobby"]  =1

default_dict =defaultdict(int)
for user in users:
    default_dict[user]+=1
print(default_dict)

def get_default():
    return {
        "name":"",
        "nums":0
    }
default_dict1 = defaultdict(get_default)
print(default_dict1["group"])


