class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.__pay = pay #Private variable
    def fullname(self):
        return self.first+' '+self.last
    def employeepay(self):
        print(self.fullname(),"Pay is",self.__pay)
Employee1 = Employee('Yugi','Lee',7000) #Employee class instance
print('Employee full name is',Employee1.fullname())
Employee1.employeepay()