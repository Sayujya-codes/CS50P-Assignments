'''
x = int(input("Enter x "))
y = str(input("Enter operator "))
z = int(input("Enter z "))
'''

x,y,z = input("Enter the values: ").split()
x = int(x)
z = int(z)

if y == "+":
    print(f"{x+z:.1f}")
elif y == "-":
    print(f"{x-z:.1f}")
elif y =="*":
    print(f"{x*z:.1f}")
elif y =="/":
    if z == 0:
        print("invalid")
    else:
       print(f"{x/z:.1f}")
else:
    print("Invalid operator")

