n = int(input("Enter the value: "))
for i in range(1,n+1):
    print(" "*(2*n-i+3),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+3):
    print(" "*(2*n-i+1),end="")
    for j in range(-1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+5):
    print(" "*(2*n-i+1),end="")
    for j in range(-2,i+1):
        print("*",end=" ")
    print()

for i in range(1,n+3):
    print(" "*((2*n)),end="")
    print("| "*5)

    print()
