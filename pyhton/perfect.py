def isperfect(n: int) ->bool:
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        return sum
def perfects(a:list[int]) ->int:
    new_list = []
    for x in a:
        new_list.append(isperfect(x))
    return new_list

n=int(input())
a=list(map(int,input().split()))
res=perfects(a)
print(*res)