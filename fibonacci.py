num=int(input("enter a number :"))
def fibo(number):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,number-1):
            c = a + b
            print(c)
            a = b
            b = c
 
fibo(num)