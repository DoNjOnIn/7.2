import random

def print1(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print()

def minm(A,a):
    for i in range(len(A)):
        mnum=A[i][0]
        for j in range(len(A[i])):
            if A[i][j]<mnum:
                mnum=A[i][j]
            else:
                pass
        a.append(mnum)
    return a

def maxl(a):
    maxl=a[0]
    for i in range(len(a)):
        if a[i]>maxl:
            maxl=a[i]
        else:
            pass
    return maxl

def create(A,low,high):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = random.randint(low, high)


def main():
    M = int(input('К-сть рядків?='))
    N = int(input('К-сть стовпчиків?='))
    low = int(input('Low='))
    high = int(input('High='))
    a=[]
    A = [[0] * M for i in range(N)]
    create(A,low,high)
    print1(A)
    print('-------------')
    print('All min-'+str(minm(A,a)))
    print('Max of min='+str(maxl(a)))




if __name__=='__main__':
    main()