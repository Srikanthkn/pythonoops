from toll import tollbooth
t1=tollbooth()
print('/n........tollbooth details.........')
print("if we want to add toll charges press 1")
print("if we want to skip toll charges press 2")
print("if we want to display toll balance 3")
options=int(input("enter the option here :"))

if options==1 or options==2:
    a = int(input("add amount for paying car: "))
    if a % 50 == 0:
        t1.payingcar(a)
    elif a == 0:
        t1.nopaying(a)
    else:
        print("enter valid amount")


elif options==3:
    t1.display()
else:
    print("Enter Valid option")










