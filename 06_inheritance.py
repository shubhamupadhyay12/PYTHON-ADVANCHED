class employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee {self.name} and the salary is {self.salary} ")
        
# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary} ")
    
#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good at {self.language} language")
 
 
class programmer(employee):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language")
 
    
          
a = employee()      
b = programmer()
print(a.company,b.company)