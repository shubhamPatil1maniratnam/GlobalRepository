class student :
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name