array=[65,85,95,20,14]
num = ""
for i in range(0, len(array)):
    num = num + str(array[i] % 10)
num1 = int(num)
print(num1)
if num1 % 10 == 0:
    print("Divisibility test done")
else:
    print("Divisibility test failed")





