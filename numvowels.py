vowles="aeiouAEIOU"
word=input("input a word:")
count=0
for i in word:
    if i in vowles:
        count+=1
print("number of vowles in ", word,"are",count)        