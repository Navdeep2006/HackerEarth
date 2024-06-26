n=int(input())
a=[int(x)for x in input().split()]
c=a[n-1]%10
if c==0:
    print('Yes')
else:
    print('No')