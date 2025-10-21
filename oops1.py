#How to initiate a class

class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        #print(id(self))
        #print("started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE" 
        #print("attributes or data have been initiated")

    def travel(self,destination):
        print("this travel function was called manually")
        print(f"Employee is now travelling to {destination}")



#create an obj/instance of the class
sam = employee()
sam.name = "Sam sharma"
#print(id(sam))
print(sam.name)
#print(sam.salary)

#calling a method
#sam.travel("Mumbai")
