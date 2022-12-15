''' Program 1:
In second year computer engineering class, group A students play cricket, group B students play badminton and goupr C students play football.
Write a python program using functions to compute following:
    a) List of students who play both cricket and badminton
    b) List of students who play either cricket aur badminton but not both
    c) Number of students who play neither cricket nor badminton
    d) Number of students who play cricket and football but not badminton.
(Note: While realizing the group duplicate entries should be avoided,do not use SET built-in functions)
'''


def duplicate(d):
    lis=[]
    for i in d:
        if i not in lis:
            lis.append(i)
    return lis

def intersection(lis1,lis2):
    lis3=[]
    for i in lis1:
        if i in lis2:
            lis3.append(i)
    return lis3


def union(lis1,lis2):
    lis3=lis1.copy()

    for i in lis2:
        if i not in lis1:
            lis3.append(i)
    return lis3

def difference(lis1,lis2):
    lis3=[]
    for i in lis1:
        if i not in lis2:
            lis3.append(i)
    return lis3


def sym_diff(lis1,lis2):
    lis3=[]
    d1=difference(lis1,lis2)
    d2=difference(lis2,lis1)

    lis3 = union(d1,d2)

    return lis3

def CnB(lis1,lis2):
    lis3=intersection(lis1,lis2)
    print("\n\n List of students that play both cricket and badminton : ", lis3)
    return len(lis3)

def eCeB(lis1,lis2):
    lis3=sym_diff(lis1,lis2)
    print("\n\n List of the students that either play cricket or badminton but not both : ",lis3)
    return len(lis3)


def nCnB(lis1,lis2,lis3):
    lis4=difference(lis1,union(lis2,lis3))
    print("\n\n Number of student that play neither cricket nor badminton : ",lis4)
    return len(lis4)

def CBnF(lis1,lis2,lis3):
    lis4=difference(lis1,intersection(lis2,lis3))
    print("\n\n Number of students that play cricket and football but not badminton : ",lis4)
    return len(lis4)

students = int(input("Enter the number of students in the class : "))
print("Enter the names of the students")
lis=[]
for i in range (students):
    name=input()
    lis.append(name)
print("List of student in class : ",lis)

# Creating an empty list for Cricket

grpA=int(input("Enter the number of students that play cricket : "))
lis1=[]
for i in range(grpA):
    name=input()
    lis1.append(name)
print("List of students that play cricket : ",lis1)

# Creating an empty list for Badminton

grpB=int(input("Enter the number of students that play badminton : "))
lis2=[]
for i in range(grpB):
    name=input()
    lis2.append(name)
print("List of students that play badminton : ",lis2)

# Creating an empty list for Football

grpC=int(input("Enter the number of students that play football : "))
lis3=[]
for i in range(grpC):
    name=input()
    lis3.append(name)
print("List of students that play football : ",lis3)


flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", CnB(lis1,lis2))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both : ", eCeB(lis1, lis2))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", nCnB(lis,lis1,lis2))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CBnF(lis1,lis2,lis3))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==5:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("\n\nDo you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")