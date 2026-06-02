
def main():
    try:
        a = int(input("Hey, Enter the number: "))
        print(a)
        return


    except Exception as e:
        print(e)
        return
    
    finally:  #run irrespectively
        print("Hey i am  inside the finally")

main()
