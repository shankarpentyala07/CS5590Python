class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.__pay = pay #Private variable
    def fullname(self):
        return self.first+' '+self.last
    def employeepay(self):
        print(self.fullname(),"Pay is",self.__pay)
class Developer(Employee):  #single inheritance
    def __init__(self,first,last,pay,proglang):
        Employee.__init__(self,first,last,pay)
        self.proglang=proglang
    def getdevname(self):
        return self.first+' '+self.last
    def getproglang(self):
        return self.proglang


class Manager():
    def __init__(self,mfname,mlname,msalary,bu):
        self.mfname=mfname
        self.mlname=mlname
        self.msalary=msalary
        self.bu=bu
    def managername(self):
        return self.mfname +' '+self.mlname


    def getbu(self):
        return self.bu
class Client():
    def __init__(self,clientname):
        self.clientname= clientname
    def getclientname(self):
        return self.clientname



class Team(Developer,Manager,Client): #Multiple inheritance
    def __init__(self,dfname,dlname,dsalary,dproglang,mfname,mlname,msalary,mbu,clientname):
            Manager.__init__(self,mfname,mlname,msalary,mbu) #instance of manager class
            Client.__init__(self, clientname)  #instance of client class
            Developer.__init__(self,dfname,dlname,dsalary,dproglang) #instance of developer class


print('Welcome to software team building system')
print('Please enter developer details')
dfname=input('please enter developer1 first name')
dlname=input('please enter developer1 last name')
dsalary=input('please enter developer1 salary')
dproglang=input('please enter developer1 proglang')
mfname=input('Please enter the  manager first name')
mlname=input('Please enter the manager last name')
msalary=input('Please enter manager salary')
mbu=input('please enter manager business unit')
clientname=input('please enter client name')
Team1=Team(dfname,dlname,dsalary,dproglang,mfname,mlname,msalary,mbu,clientname)#instance of team class

print('------Team details are-------------')
print('------Client Details are-----------')
print('Client name is',Team1.getclientname())
print('------Manager Details are----------')
print('Manager name is ',Team1.managername())
print('Manager Business Unit is',Team1.getbu())
print('------Developer Details are---------')
print('Developer Name is',Team1.getdevname())
print('Developer programming language is',Team1.getproglang())
print('-----------------Bye,Have a nice day-------------------')




