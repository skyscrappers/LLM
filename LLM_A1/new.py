print('''-----MENU------
1). Right-angled
2). Isoceles triangle
3). Kite
4). Half Kite 
5). "X"''')
n = int(input("Enter the number of pattern you want to print:"))
if n==1:
    n = int(input("enter number:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
if n==2:
    n = int(input("enter number:"))
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print(j+1,"",end="")
        print()
if n==3:
    n = int(input("Enter number:"))
    for i in range(1,n+1):
        print(" "*(n-i), end='')
        for j in range(1,i*2):
            print(j, end='')
        print()
    for i in range(n-1,0,-1):
        print(' '*(n-i), end='')
        for j in range(1,i*2):
            print(j, end='')
        print()
if n==4:
    n = int(input("Enter number:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        print()
    for i in range(n,0,-1):
        for j in range(1,i):
            print(j, end=' ')
        print()
if n==5:
    n = int(input("Enter number:"))
    for i in range(n,0,-1):
        print(' '*(n-i), end='')
        for j in range(1,i*2):
            print(j, end='')
        print()
    for i in range(1,n+1):
        print(" "*(n-i), end='')
        for j in range(1,i*2):
            print(j, end='')
        print()