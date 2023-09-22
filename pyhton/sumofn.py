def sumofdigits(n:int) ->int:
    sum=0
    while n>0:
        r=n%10
        count=0
        for i in range(1,r+1):
            if r%i==0:
                count+=1
        if count==2:
            sum+=r
        n=n//10
    return sum


def fun(a: list[int]) ->list[int]:
    n_lst=[]
    for x in a:
        n_ldef amstrongnumbers(a: list[int]) ->list[int]:
    n_lst=[]
    for x in a:
        if isamstrong(x):
            n_lst.append(x)
    return n_lst
n=int(input())
a=list(map(int,input().split()))
res=amstrongnumbers(a)
print(*res)

    return n_lst
n=int(input())
a=list(map(int,input().split()))
res=fun(a)
print(*res)