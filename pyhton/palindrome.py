def ispalindrome(n : int) -> bool:
    temp=n
    rev=0
    while n>0:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev==temp


def palindrome(a: list[int]) ->list[int]:
    n_lst=[]
    for x in a:
        n_lst.append(ispalindrome(x))
    return n_lst


n=int(input())
a=list(map(int,input().split()))
res=palindrome(a)
print(*res)