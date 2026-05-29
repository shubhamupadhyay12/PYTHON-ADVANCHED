class employee:
    language = "python" #this is class attribute
    salary = 99000
    
shubham = employee()
shubham.name = "Hadestheshubh" #this is instance attribute
print(shubham.name,shubham.salary,shubham.language)

garv = employee()
garv.name = "GodGarv" #this is instance attribute
print(garv.language,garv.salary,garv.name)

# here name is instance attribute and lang and salary 
# are class attributes as they directly belong to class