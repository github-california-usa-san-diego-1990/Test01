#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan-Desktop
#
# Created:     19/10/2016
# Copyright:   (c) Yan-Desktop 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def E_001():
    l=[]
    for i in range(2000,3201):
        if (i % 7 == 0) and (i % 5 != 0):
            l.append(str(i))
    print ','.join(l)
    print len(l)

def E_002():
    n = 8
    s = []

    for i in range(0,n+1):
        if i==0:
            s.append(str(1))
        else:
            s.append(str(i*int(s[-1])))
    print ','.join(s)

def E_002B(n):
    if n==0:
        return 1
    return n*E_002B(n-1)

def E_002A():
    n=8
    k=E_002B(n)
    print k

def main():
    E_002A()

if __name__ == '__main__':
    main()
