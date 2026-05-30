#Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. Does this change the class attribute?



class Demo:
    a = 4
    
o = Demo()
print(o.a) #pritn the class attribute bcz instance attribute is not presnt
o.a=0 #instance attribute is set
print(o.a) #print the instace attribute bcz instance attribute is presnt
print(Demo.a) #print the class attribute