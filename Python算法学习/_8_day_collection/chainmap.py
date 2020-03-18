from collections import ChainMap
user_dict1={"a":"GaoBAiBai","b":'Honghuhu'}
user_dict2={"a":"GaoBAiBai111","b":'Honghuhu222'}
new_dict= ChainMap(user_dict1,user_dict2)
print(new_dict)
for key,value in new_dict.items():
    print(key, value)
#浅度复制
new_dict.maps[0]['a']='bobby'
print(new_dict)
new_dict.new_child()