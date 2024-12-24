num=int(input("input any number:"))
x=False
if num==0 or num==1:
    print("the number is not prime")
elif num>1:
    for  i  in range(2,num):
        if num%i==0:
          x=True
          break

if x:
      print("The number is not a prime number")
else :
    print("The given number is a prime number")



