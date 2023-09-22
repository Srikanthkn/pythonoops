def fact(n:int) ->int:
    fact = 1
    sum = 0
    while n > 0:
        n = n % 10
        sum += fact
        n //= 10
    return fact == sum == n
  print(fact)

n=int(input())
a=list(map(int,input().split()))
fact(n)
print(fact)