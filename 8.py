class a:
    k=10
class b(a):
    l=20
class c(b):
    m=30
    print("Welcome to python")
i=c()
print("The k value is:",i.k)
print("The l value is:",i.l)
print("The m value is:",i.m)
