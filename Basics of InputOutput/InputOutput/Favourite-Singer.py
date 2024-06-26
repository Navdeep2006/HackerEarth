n=int(input())
arr=[int(x) for x in input().split()]#taking input as array
dic={}# making dictonary for knowing the occurence of each element
for i in arr:# putting elements in arr with their number of occurence's
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
maxi=0
for i,j in dic.items():#find the maximum occuence value
    if j>maxi:
        maxi=j
count=0
for i,j in dic.items():#checking how many time maximum occurence is present
    if j==maxi:
        count+=1
print(count)