class MethodDemo:
    a=0
    def read(self,name,age):
        self.name=name
        self.age=age
    def write(self):
        name="Sreedhar"
        age=19
        print("The Name is:",name+"\n"+"Age is:",age)
b=MethodDemo()
b.write()
