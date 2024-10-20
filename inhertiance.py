class person(object):
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
    def display(self):
        print(self.name)
        print(self.idno)
class employee(person):
    def __init__(self,name,idno,salary):
        self.salary=salary
        super().__init__(name,idno)
a=employee("virat kolhi",77777,1)
a.display()
    
        

