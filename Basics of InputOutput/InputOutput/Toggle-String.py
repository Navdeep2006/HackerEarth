n=input()
a=list(n)
for i in range (len(a)):
    if a[i]==a[i].upper():
        a[i]=a[i].lower()
    elif a[i]==a[i].lower():
        a[i]=a[i].upper()
for k in a:
    print(k,end='')