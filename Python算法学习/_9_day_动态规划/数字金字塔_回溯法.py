list2 = []
lenTa = 5
num=0
list3=[]
def Shuzi_jinziTa(list1,index =0):
    global num
    global list2
    global list3
    if num==lenTa:
        num-=1
        print(list2)
        list3.append(list2[::])
        return
    else:
        for i in range(index,index+2):
            try:
                list2.append(list1[num][i])
                num+=1
                Shuzi_jinziTa(list1,i)
                list2.pop()
            except:
                return "运行结束"
        num-=1
if __name__ == '__main__':
    list1 = [
                [13],
               [11,8],
             [12, 7, 26],
            [6, 14, 15, 8],
        [12, 17, 13, 24, 11]
    ]
    lenta = len(list1)
    print(Shuzi_jinziTa(list1))
    print(list3)
    num =0
    list4 =[]
    for i in list3:
        for q in i :
            num+=q
        list4.append(num)
        num=0
    for i in range(len(list4)):
        for j in range(len(list4)-1):
            if list4[j]>list4[j+1]:
                list4[j],list4[j+1]=list4[j+1],list4[j]
    print(list4)