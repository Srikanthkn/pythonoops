n=int(input())
temp=n
sum=0
def fact(r):
  if r==0 or r==1:
    return 1
  else:
    return r*fact(r-1)
while n>0:
    r=n%10
    sum=sum+fact(r)
    n=n//10
print(sum==temp)   
  
