arrays = []
list1=[]
def quanpailie(data_list):
    global arrays
    if data_list == []:
        list1.append(arrays[:])
        return
    for data in data_list:
        arrays.append(data)
        next_data = data_list[:]
        next_data.remove(data)
        quanpailie(next_data)
        arrays.pop()
    return list1
# class A(object):
#     arrays = []
#     def quanpailie(data_list):
#         global arrays
#         if data_list == []:
#             print(arrays)
#             return
#         for data in data_list:
#             arrays.append(data)
#             next_data = data_list[:]
#             next_data.remove(data)
#             A.quanpailie(next_data)
#             arrays.pop()
if __name__ == '__main__':
    data_list = [1, 2, 3]
    print(quanpailie(data_list))