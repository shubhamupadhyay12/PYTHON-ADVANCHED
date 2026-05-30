# Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "slf" or something and see the effects.\
    
    
    
    
from random import randint

class train:
    
    def __init__(slf,trainno):
        slf.trainno = trainno
        
        
    def book(slf, fro , to):
        print(f"Ticket is booked in {slf.trainno} from {fro} to {to} ")
        
    
    def getstatus(slf):
        print(f"Ticket no: {slf.trainno}  is running on time")
    
    def getfare(slf , fro , to):
        print(f"Ticket fare in {slf.trainno} from {fro} to {to} is {randint(222,555)} ")

t = train(12399)     
t.book("rampur", "mau")
t.getstatus()
t.getfare("rampur", "mau")