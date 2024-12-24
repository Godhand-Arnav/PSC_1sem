num=int(input("Enter a number:"))      #num=100->num->isprime->number    therefore number becomes 100
def isprime(number):
    for i in range(2,number):
        if num % i==0:
            return False
    return True
print(isprime(num))    
