a = int(input("enter a numebr: "))
b = int(input("enter second numebr: "))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero")
else:
    print(f"The division a/b is {a/b}")