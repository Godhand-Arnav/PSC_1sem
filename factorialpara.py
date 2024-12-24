def factorial(a):
    fac=1

    for i in range(1,a+1):
        fac=i*fac
        i=i+1
    return fac
print(factorial(int(input("enter a number:"))))    
# #using while loop
# def fact(n)
#     i=1
#     b=1
#     while(i<=n):
#         b=i*b
#         i+=1
#     return b
# print(fact(int(input("enter a number:")))) 
