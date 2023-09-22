n=int(input())
count=0
i=1                  #6  1<6     sum=1 
while i<=n:
    if n%i==0:
        count+=1
        print(count)
    i=i+1
if count==2:
    print("yes")
else:
    print("no")
