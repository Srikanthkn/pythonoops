def countofdigits(n:int) ->int:
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
def isamstrong(n: list[int]) ->list[int]:
    temp=n
    count=0
    while n>0:
        n=n//10
        count+=1
    n=temp
    sum=0
    while n>0:
        r=n%10
        sum+=r**count
        n=n//10
    return sum==temp
def amstrongnumbers(a: list[int]) ->list[int]:
    n_lst=[]
    for x in a:
        if isamstrong(x):
            n_lst.append(x)
    return n_lst
n=int(input())
a=list(map(int,input().split()))
res=amstrongnumbers(a)
print(*res)