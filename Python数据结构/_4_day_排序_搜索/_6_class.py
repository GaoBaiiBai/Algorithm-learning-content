def merge_sort(alist):
    n = len(alist)
    if n <=1:
        return alist
    mid = n//2
    # left采用归并排序后形成的有序的新的列表
    left =merge_sort(alist[:mid])
    right =merge_sort(alist[mid:])
    # 将两个子序列进行合并
    # merge(left,right)
    left_point,right_point =0,0
    result =[]
    while left_point<len(left) and right_point<len(right):
        if left[left_point]<right[right_point]:
            result.append(left[left_point])
            left_point+=1
        elif left[left_point]>=right[right_point]:
            result.append(right[right_point])
            right_point+=1
    result +=left[left_point:]
    result += right[right_point:]
    return result
if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(alist))