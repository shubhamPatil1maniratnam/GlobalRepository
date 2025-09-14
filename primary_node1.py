class A:
    def m17(self):
        print("in m1 from A")
class B(A):
    def m11(self):
        print("in m1 from B")
class C(A):
    def m15(self):
        print("in m1 from C")
class D(B,C):
    def m2(self):
        print("in m1 from D")

obj = D()
obj.m1()

result = obj.add(100,300)
print(result)
