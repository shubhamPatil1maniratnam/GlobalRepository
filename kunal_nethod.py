class student :
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print("name:", self.name)
        print("age:", self.age)
        print("gender:",self.gender)
    obj1 = student(kunal,25, male)
    print(show.obj1)