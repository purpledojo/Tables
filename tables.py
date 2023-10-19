num = input("Give a number")
till = input("Until")
for t in range(1,int(till)+1):
    ans = int(t) * int(num)
    print(num, "x" , t , "=" , ans)