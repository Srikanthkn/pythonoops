def isprime(n:int) ->bool:
    count=0
    for i in  range(1,n+1):
        if n%i==0:
            count+=1
    return count==2
def primesres(a:list[int])->list[bool]:
    new_list=[]
    for x in a:
        new_list.append(isprime(x))
    return new_list

n=int(input())
a=list(map(int,input().split()))
res=primesres(a)
print(*res)