class A:
    def show(self):
        print("This is A class")
class B:
    def show(self):
        print("This is B class")
class C(A,B):
    def show(self):
        super().show()
        super().show()
        print("This is C class")
s=C()
s.show()
