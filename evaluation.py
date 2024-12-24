m1=int(input("enter marks obtained in maths:"))
m2=int(input("enter marks obtained in physics:"))
m3=int(input("enter marks obtained in chemistry:"))

avg=(m1+m2+m3)/3
print("your avarage is:",avg)
if (avg<35):
    print("you have failed")
else:
    print("you have passed")    