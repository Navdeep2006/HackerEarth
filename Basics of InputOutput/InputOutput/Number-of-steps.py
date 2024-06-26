n=int(input())
arr1=[int(x)for x in input().split()]
arr2=[int(x)for x in input().split()]
count=0#counting steps
i=0#for irritating the string
mini=min(arr1)#getting the minimum value of the array
while i<n:
    if arr1[i]>mini:#making all the other values in string equal to mini
        arr1[i]=arr1[i]-arr2[i]
        count+=1#counting steps
    elif arr1[i]<mini:#if any value get less then mini makin him new mini value
        mini=arr1[i]
        i=0#starting irritation from start again because mini is change
    elif arr1[i]<0:#ai-bi if ai>=bi so any value go in negative not possible condition
        count=-1
        break
    else:# going to next value at array
        i+=1
print(count)