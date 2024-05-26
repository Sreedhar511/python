units=input("Enter the Units:")
cost=0
if(int(units)<100):
    cost=units*2
    print("The Cost is:",cost)
elif(int(units)>100 and int(units)<150):
    cost=int(units)*3
    print("The Cost is:",cost)
elif(int(units)>150 and int(units)<200):
    cost=int(units)*4
    print("The Cost is:",cost)
elif(int(units)>200 and int(units)<250):
    cost=int(units)*5
    print("The Cost is:",cost)
else:
    cost=int(units)*10
    print("The Cost is:",cost)

