class employee:
    language = "python" #this is class attribute
    salary = 99000
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("Good Morning")
        
        
shubham = employee()
# shubham.language = "javascript" #this is instance attribute
shubham.greet()
shubham.getinfo()
# employee.getinfo(shubham)
