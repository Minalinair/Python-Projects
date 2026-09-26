n=int(input("Please enter the upper limit till which prime number is to be printed:"))
for num in range(2,n):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
print()







