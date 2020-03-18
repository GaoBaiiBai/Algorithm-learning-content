'''
    A B C
1 A->c
2 1->A->B   2->A->C  1->B->C
3 1->A->c   2->A->B  1->C->B     3->A->C    1->B->A    2->B->C    1->A->C
1 3 7 17
'''
def move(index,start,mid,end):
    if index ==1:
        print("{}-->{}".format(start,end))
        return
    else:
        move(index-1,start,end,mid)
        print("{}-->{}".format(start,end))
        move(index-1,mid,start,end)
if __name__ == '__main__':
    move(5,"A","B","C")