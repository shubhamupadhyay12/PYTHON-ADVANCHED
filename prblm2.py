#write a class calculator capable of finding the sqr and cube and sqrrt of a number


class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"the square is = {self.n*self.n}")
        
    def cube(self):
        print(f"the cube is = {self.n**3}")
        
    def sqrt(self):
        print(f"the sqrt is = {self.n**1/2}")
        
        
a = calculator(4)
a.square()
a.cube()
a.sqrt()