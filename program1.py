#create a program to compare three numbers and find a bigger number

a= int(input("Enter the first number"))
b= int(input("Enter the secon number"))
c= int(input("Enter the third number"))
if (a>b)and(a>c):
    print(a)
elif (b>c)and(b>a):
    print(b)
else:
    print(c)