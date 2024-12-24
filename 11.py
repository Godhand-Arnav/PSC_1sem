m1=int(input("Enter marks in russiann:"))
m2=int(input("Enter marks in necular mechanics:"))
m3=int(input("Enter marks in maths:"))
to=m1+m2+m3
print("total marks=",to)
per=(to)/3
print("percentage scored:",per)
if(per<35):
    print("you have failed")
else:
    print("you have passed")    
    print("you will get a moblie")
    if per>50:
        print("your will get a laptop")
        if per>76:
            print("your will get a bike")
            if per>90:
                    print("your will get a car")


        

