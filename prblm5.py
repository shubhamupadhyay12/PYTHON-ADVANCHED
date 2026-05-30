# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


from random import randint

class train:
    
    def __init__(self,trainno):
        self.trainno = trainno
        
        
    def book(self, fro , to):
        print(f"Ticket is booked in {self.trainno} from {fro} to {to} ")
        
    
    def getstatus(self):
        print(f"Ticket no: {self.trainno}  is running on time")
    
    def getfare(self , fro , to):
        print(f"Ticket fare in {self.trainno} from {fro} to {to} is {randint(222,555)} ")

t = train(12399,2)     
t.book("rampur", "mau")
t.getstatus()
t.getfare("rampur", "mau")
