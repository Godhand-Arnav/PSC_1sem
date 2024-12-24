# def index():
#     n=0
#     list=[2,25,55,45,75,95,100]
#     for i in list:
#         if i==45:
#             return n
#         else:
#             n+=1
# print(index())        
list=[2,25,55,45,75,95,100]       
def findindex(list1,elem):
    for i in range(0,len(list)):
        if list[i]==elem:
            print(i)
            return
    print("element not found")
findindex(list,45)