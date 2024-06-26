n=int(input())
a=list(input()) #inputing string as list for easy changing of '.'
flag=1 #flag to check if there are two consecutive H (HH)
for i in range(n):# changing '.' to 'B'
    if a[i]=='.':
        a[i]='B'
for i in range (n-1):# checking if there is two consecutive H (HH)
    if a[i]=='H' and a[i+1]=='H':
        flag=0# changing flag if find any (HH)
        break
if not flag:
    print("NO")
else:
    print("YES")
    for i in range (n):# printing the list as string
        print(a[i],end='')