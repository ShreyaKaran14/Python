#  Write the above solution in a function which takes take numbers and return the bigger number .

def bigger(a,b,c):
    if (a>b) and (a>c):
        print(a, " is the bigger number" )
    elif ( b>c)  and (b>a):
        print(b, "is the bigger number")
    else:
        print(c,"is the bigger number")

x = int(input("Enter the first number:"))
y = int(input("ENter the second number:"))
z = int(input("Enter the third number:"))
bigger(x,y,z)