'''Reversetwistwed primes'''
def reverse(n:int) ->bool:
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev==n

def isprime(n: int) ->bool:
    c_n,i=0,1
    while i<=n:
        if n%i==0:
            c_n+=1
        i+=1
    return c_n==2

def istwisted(n : int) ->bool:
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    c_rev,i=0,1
    while i<=rev:
        if rev%i==0:
            c_rev+=1
        i+=1
    return c_rev==2

def twistedprimes(a:list[int]) ->list[int]:
    new_list = []
    for x in a:
        if istwisted(x):
            new_list.append(x)
    return new_list



n=int(input())
a=list(map(int,input().split()))
res=twistedprimes(a)
print(*res)