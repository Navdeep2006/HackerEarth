n=int(input()) #no of test cases
for i in range (n):# for each test case
    li=list(input())# getting number in list to itterate each
    check=[6,2,5,5,4,5,6,3,7,6]# value of match for each number(number=index)
    total=0#for finding total matches
    for i in li:
        total+=check[int(i)]#add index of check for the each number in list [index=number]
    od=7#only 7 can be made by 3 matches
    ev=1#only 1 can be mader by 2 matches
    ans=0# for final output
    while(total>0):#till total get 0
        if total%2!=0:
            ans=7# after -3 the number will became even
            total-=3
        else:
            ans=ans*10+ev # adding a new digit to it each time (7->71->711)
            total-=2
    print(ans)
#make formula no need for last loop
