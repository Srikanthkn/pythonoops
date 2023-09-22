def fact(n:int) ->int:
    temp = n
    sum = 0
    def fact(r):
        if r == 0 or r == 1:
            return 1
        else:
            return r * fact(r - 1)

    while n > 0:
        r = n % 10
        sum = sum + fact(r)
        n = n // 10
    if sum == temp :
        print(sum,end=' ')

def isspecial(n:int) ->bool:
    for x in a:
       if fact(x):
         sum==fact
    return sum

def specialnumbers(a:list[int]) ->list[int]:
    new_list = []
    for x in a:
        new_list.append(isspecial(x))
    return new_list

n=int(input())
a=list(map(int,input().split()))
res=specialnumbers(a)
print(*res)