from collections import OrderedDict
user_dict = OrderedDict()
user_dict["a"]="158"
user_dict["b"]="482"
user_dict["c"]="482"
# dict的python2里是无序的python3下是有序的
print(user_dict.popitem())
print(user_dict)
user_dict.move_to_end("a")
print(user_dict)