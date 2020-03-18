'''
f(n)=f(n-1)+f(n-3)
'''
def tuzi(n):
    if n ==1:
        return 2
    if n ==2:
        return 2
    if n ==3:
        return 4
    return tuzi(n-1)+tuzi(n-3)
if __name__ == '__main__':
    print(tuzi(4))
