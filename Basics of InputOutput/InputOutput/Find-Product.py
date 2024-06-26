n=int(input())
a=[int(x)for x in input().split()]
s=1
for b in a:
    s=(s*b)%(10*9+7)
print (s)