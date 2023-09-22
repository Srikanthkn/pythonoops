n=int(input())
p=1
for i in range(1,n+1):
    p=i+2
    for j in range(1,n+1):
        p=j-1
        print(p,end=' ')
        p+=1
    print()

"""j= 1 2 3 4 5
--------------
1=1 | 1 2 3 4 5
  2 | 1 2 3 4 5
  3 | 1 2 3 4 5
  4 | 1 2 3 4 5
  5 | 1 2 3 4 5"""
