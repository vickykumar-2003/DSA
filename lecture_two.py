# STRING AND CONDITIONAL STATEMENTS..... String is data type that store a sequence of characters.
# CHAPTER - 2... 
 
 
 # Adding a string is called Concatenation.....
# str1 = "vicky"
# str2 = "kumar"
# print(str1 + str2)


# Lenth of string......

# str1 = "vicky"
# len1 = len(str1)
# print(len1)

# str2 = "kumar"
# len2 = len(str2)
# print(len2)
# final_str = str1 + " " + str2
# print(len(final_str))


# Indexing ......... it strat always (0) OR index means position of string......

# str = "PYTHON LANGUAGE"
# ch = str[12]
# print(ch)


# Slicing....it means dived the string is called Slicing.......

# str = "vicky kumar"
# print(str[1:4])  #it Return (ick) kyuki start 1 index or 4 but 4 se hmesa 1 km hota hai

# str = "SVIET"
# print(str[1:2])

# str = "My Book"
# print(str[0:1])

# str = "Happy"
# print(str[0:3]) 

# str = "Apna college"
# print(str[:4]) #[0:4] it start 0 to 4
# print(str[5:]) #[5:len(str)] it start 5 to end


# slicing Negative Index......

# str = "Apple"
# print(str[-4:-1])

# str = "Elephant"
# print(str[-7:-2]) # lepha


# String Functionn.....

# str.endswith("er")

# str.capitalize()

# str.replace(old,new) 

# str.find(word)

# str = "I am studying python from apna college" #  cheak last value hai ya nhi so give True or False
# print(str.endswith("college"))

# str = "vicky"
# print(str.capitalize()) # char ko capital krna

# str = "I am stdying python from apan college"
# print(str.replace("a","o")) # replece Old value in New value..

# str = "zebra zack zero"
# print(str.replace("z","h")) # return hebra, hack, hero  replace the old value in new value

# str = "i am studying python from apna college"
# print(str.find("o")) # give the index number (o is 18th index), example we find another word so (is give the -1)


# str = "i am studying python from apna college"
# print(str.count("a")) # basically is count the a how much time in this sentance...


# Lets Practice.......

# WAP to input user's first name & print its lenght....
# name  =input("enter your name:")
# print("length of your name is",len(name))

# WAP to find the occurrence of '$' in a sting......
# str = "hi, $Iam the $ symbol $99.99"
# print(str.count("$"))


# Conditional Statements.........
# if-elif-else(SYNTAX)

# if(conditon):
#     Statement1
# elif(condition):
#     Statement2
# else:
#     StatementN

# age = 24

# if(age >= 18):
#     print("can vote")
#     print("can drive")


# light = "pink"

# if(light == "red"): # if ka mtlb hai ki condition True huaa to 
#     print("stop")
# elif(light == "green"):
#     print("go") # 4 space is important in python is called indentation
# elif(light == "yellow"):
#     print("look")
# else: # else ka mtlb sari condition false ho to ye kam kregi
#     print("light is broken")


# Grade students based on marks.....
# marks = int(input("enter student marks:"))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#    grade = "C"
# else:
#     grade = "D"
    
# print("grade of the student ->",grade)


# # nesting it means if ke andr if....
# age = 95
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")


# Let's Practice....

# WAP to cheak if a number enterd by the user is odd or even.......
# num = int(input("enter the number:"))

# if(num %2 == 0):
#     print("number is even:")
# else:
#     print("number is odd:")


# WAP to find the greatest of 3 number entered by the user....
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))

# if(a >= b and a >= c):
#     print("first number is largest", a)
# elif(b >= c):
#     print("second number is largest", b)
# else:
#     print("third is largest", c)


# WAP to cheak if a number is a multiple of 5 or not.....
# x = int(input("enter number:"))

# if(x %5 == 0):
#     print("multiple of 5")
# else:
#     print("not a multiple")


