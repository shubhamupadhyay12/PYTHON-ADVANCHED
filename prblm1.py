#create a class programmer for stroing info of few programmers working at microsoft


class programmer:
    company = "Microsoft"
    def __init__(self , name ,salary , pincode):
        self.name = name 
        self.salary = salary 
        self.pincode = pincode
        
        
p = programmer("Shubham",120000,275101)
print(p.name,p.salary,p.pincode,p.company)

g = programmer("Garv",120000,275105)
print(g.name,g.salary,g.pincode,g.company)
