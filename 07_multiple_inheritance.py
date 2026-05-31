class employee:
    company = "ITC"
    name = "shubham"
    def show(self):
        print(f"The name of the employee {self.name} and the company is {self.company} ")
        
class coder:
    language = "python"
    def prinlanguages(self):
        print(f"out of all the laguages here is your language:{self.language} ")
        
        
 
 
class programmer(employee,coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and comapmy is {self.company} and he is good at {self.language} language")
 
    
          
a = employee()      
b = programmer()

b.show()
b.showlanguage()
b.prinlanguages()