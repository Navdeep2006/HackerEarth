n=int(input())# inputing number of test cases
for i in range (n):# loop for total test cases
    price=[int(x)for x in input().split()]# input price as list
    n2=int(input())# inputing total number test cases in each test case (n2)
    var=[0,0]# varible for storing total problem solved
    for j in range(n2):#for storing and counting total problem solved till n2
        prob=[int(x)for x in input().split()]#inputing in list 
        var[0]+=prob[0]#increasing value ar varriable
        var[1]+=prob[1]
    print(min(var)*max(price)+max(var)*min(price))# getting least price

