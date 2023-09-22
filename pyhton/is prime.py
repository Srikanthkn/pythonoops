def isprime(n:int) ->bool:

      while n>0:
        r=n%10
        count=0
        for i in range(1,n):
            if r%i==0:
             count+=1
        return count==2


def istwisted(n:int) ->bool:
def twistedprimes(a:list[int])->list[int]:
    new_list=[]
    for x in a:
        if istwisted(x):
            new_list.append(x)
    return new_list

n=int(input())
a=list(map(int,input().split()))
res=twistedprimes(a)
print(*res)