def sumofdigits(n: int) ->int:
    sum=0
    while n>0:
        r=n%10
        sum+=r
        n=n//10
    return sum
def fun(a:list[int]) ->list[int]:
    new_list = []
    for x in a:
        new_list.append(sumofdigits(x))
    return new_list


n=int(input())
a=list(map(int,input().split()))
res=fun(a)
print(*res)