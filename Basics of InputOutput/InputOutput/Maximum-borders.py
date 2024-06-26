n=int(input())
for i in range(n):
    list=[int(x)for x in input().split()] # taking input
    m=0 # for defining maximum value for each line
    for j in range(list[0]):
        count=0 # for count the maximum "#"
        arr=input()
        for k in range (list[1]): # for irrtation on string
            if arr[k] == '#':
                count=count+1
        if count>m: # comparing the count with maximum
            m=count
    print(m)