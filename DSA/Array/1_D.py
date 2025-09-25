# arr = [10,20,30,40]

# print(arr[2])
# print(arr[0])

# # usig loop in Array....
# for i in range(len(arr)):
#     print(arr[i])
    
# insert element in the array....
print("how many element to store inside the aarry,",end="")
num = input()
arr=[]
print("\n enter ",num,"elemnt:",end="")
num = int(num)
for i in range(num):
    element = input()
    arr.append(element)
print("\n The array element are")
for i in range(num):
    print(arr[i],end="")