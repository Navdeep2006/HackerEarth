l = int(input())
n =int(input())
for x in range(n):
    list = [int (x) for x in input().split()] #list comprehesion for input
    w = list[0] #getting out the values from list made in above line
    h = list [1]
    if w < l or h < l:
        print("UPLOAD ANOTHER")
    elif w != h:
        print("CROP IT")
    else:
        print("ACCEPTED")

