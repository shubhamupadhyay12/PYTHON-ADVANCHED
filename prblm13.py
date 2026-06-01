# . Override the __len__() method on vector of problem 12 to display the dimension of the 
# vector. 

class vector:
    def __init__(self,list):
        self.list = list
        

    
    def __len__(self):
        return len(self.list)
    
#implementation 

v1 = vector([1,2,3])
print(len(v1))
