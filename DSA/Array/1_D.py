# arr = [10,20,30,40]

# print(arr[2])
# print(arr[0])

# # usig loop in Array....
# for i in range(len(arr)):
#     print(arr[i])
    
# # insert,remove element in the 1-D array....
# arr = [10,20,30,40,50]

# print("Element at index 2:",arr[2]) # 30

# for i in arr:
#     print(i,end=" ") # 10.20,30,40,50


# arr.append(60)
# print("\n After append:",arr)# 10,20,30,40,50,60


# arr.remove(30) # 10,20,40,50,60
# print("Afetr remove:",arr)

# 1-D Array using array module.....
import array as arr 

#integer element
number = arr.array('i',[10,20,30,40,50]) # i ka mtlb h integr type

# Access element
print("element at index 1:",number[1])

# Add element
number.append(60)
print("After append:",number)

# Remove element
number.remove(30)
print("After remove:",number)









