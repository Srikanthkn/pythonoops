def fact(n):
  f=1
  sum=0
  for i in range(1,n+1):
      f=f*i
      sum+=f
  print(sum)
  return sum
n=int(input())
fact(n)
print(sum)
