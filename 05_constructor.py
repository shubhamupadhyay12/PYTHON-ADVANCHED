class employee:
    language = "python" #this is class attribute
    salary = 99000
    
    def __init__(self , name , language , salary):  #dunder method which is automatcally called started with double underscore
        self.name = name
        self.language = language
        self.salary = salary
        print(f"I am creating an object ")
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod #function whihch doesnt require the object , called only when the object is created
    def greet():
        print("Good Morning")
        
        
shubham = employee("Shubham","javascript",130000)
# shubham.name = "shubham upadhyay"
print(shubham.name,shubham.language,shubham.salary)

# garv = employee()

