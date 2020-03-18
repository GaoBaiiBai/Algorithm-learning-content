list1=[]
def chaifen(num):
    global list1
    if num<=0:
        print(list1)
    for num1 in range(1,num+1):
        list1.append(num1)
        chaifen(num-num1)
        list1.pop()
if __name__ == '__main__':
    num = 7
    chaifen(7)
