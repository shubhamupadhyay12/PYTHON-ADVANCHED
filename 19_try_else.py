try:
    a = int(input("Hey, Enter the number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("i am inside else") #runs oly when the try runs completely