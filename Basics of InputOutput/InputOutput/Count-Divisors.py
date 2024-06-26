n=[int(x)for x in input().split()]
i=n[0]
c=n[2]
s=0
while i <= n[1]:
    if i%c==0:
        s+=1
    i+=1
print(s)