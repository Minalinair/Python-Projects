str=input("Enter a string of your choice:")
l=len(str)
count=0
for i in range(l):
    for j in range(i+1,l):
        if str[i]==str[j]:
            count+=1
if count>=1:
    print("The string is not unique")
else:
    print("The string is unique")
