'''
'''
info =[
    [3,8],
    [2,5],
    [5,12]
]
data=[]
max_select=[]
def search(depth,rest):
    global data
    if depth==3:
        max_select.append(data[0]*info[0][1]+data[1]*info[1][1]+data[2]*info[2][1])
        return
    else:
        #     1.不放
        # 设置现场
        data.append(0)
        search(depth+1,rest)
        data.pop()
         #     2.放
        if rest>=info[depth][0]:
            data.append(1)
            search(depth+1,rest-info[depth][0])
            data.pop()
if __name__ == '__main__':
    search(0,5)
    print(max(max_select))