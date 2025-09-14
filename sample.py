class Company:
    companyname = "IBM"
    def __init__(self,id,name,city):
        self.id = id
        self.name = name
        self.city = city

    def show(self):
        print("Company Name:",Company.companyname)
        print("ID:",self.id)
        print("Name:",self.name)
        print("City:",self.city)

    @staticmethod
    def add(x,y):
        return x+y

    @classmethod
    def companyname_change(cls):
        cls.companyname = "Infosys"

obj = Company(101,'Rahul','Pune')
obj.show()
Company.companyname_change()


obj.show()

result = obj.add(100,300)
print(result)
