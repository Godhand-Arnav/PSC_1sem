list=[42,466,4567,877,567,453,56744,536879]
def number_of_evenorodd(num):
 a=0
 b=0
 for i in list:
    if i%2==0:
        a=a+1
    else :
        b=b+1
 print("number of even",a)   
 print("number of odd",b)     
number_of_evenorodd(list)
    
