# class myclass:
#     x = 5
# p1 = myclass()
# print(p1.x)



# class vicky:
#     a = 10
# q1 = vicky()
# print(q1.a)


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = person("john",23)

# print(p1.name)
# print(p1.age)


# class student:
#     def __init__(self,name,age,roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
# s1 = student("vikcy",21,2)
# print(s1.name,s1.age,s1.roll_no)


# class sviet:
#     def __init__(self,Branch,subject,teacher):
#         self.Branch = Branch
#         self.subject = subject
#         self.teacher = teacher
# s1 = sviet("B-tech","Maths","Rupinder")
# print(s1.Branch)
# print(s1.teacher)
# print(s1.subject)

# __str__()....
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}, age:{self.age}"
# p1 = person("vicky",36)
# print(p1)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfun(self):
#         print("Hello my name is " + self.name)
        
# p1 = Person("vicky", 21)
# p1.myfun()

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
x = Person("vicky","kumar")
x.printname()