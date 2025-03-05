import random
class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"The trainNum {self.trainNo},The From {fro},To The destination {to}")

    def getstatus(self):
        print(f"The train No: {self.trainNo} is running on this time ")

    def getfare(self,fro,to):
        print(f"The Train In Fare {self.trainNo},from {fro} to {to},{random.randint(12,5555)}")



t = train(1334)
t.book("Dhaka",'Jamalpur')
t.getstatus()
t.getfare("Dhaka","Gazipur")

