


'''x=int(input("enter the number"))
match=x
print(match)'''

'''x=int(input("enter the number"))
match x:
    case 1:
        print("monday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("default")'''                   

'''#menu driven program
a=int(input("enter the number"))
b=int(input("enter the number"))
n=int(input("enter the number"))
match n:
    case 1:
        c=a+b
        print("addition is",c)
    case 2:
        c=a-b
        print("subtraction is ",c)
    case 3:
        c=a*b
        print("multiplication is ",c)
    case 4:
        c=a/b
        print("divide is",c)
    case _: 
        print("default")'''  


#3
'''a=int(input("enter the value of a"))
b=int(input("enter the value of b is"))
c=int(input("enter the value of c is"))
n=int(input("enter the number"))    
match n:
    case 1:
        if a==b | a==c:
            print("length are equal")
        else:
            print("length are not equal")
    case 2:
        if a*a+b*b==c*c:
            print("triangle is right angle triangle")
        else:
            print("triangle is not a right triangle") 
    case 3:
        if a==b==c:
            print("triangle is right angle")
        else:
            print("triangle is not equilateral")
    case _:
        print("default")'''

'''#user age
age=int(input("enter the age of a person"))
x=int(input("enter the number"))
match x:
    case 1:
        if age<10:
            print("kid")
    case 2:
        if 10<=age<20:
            print("teen")
    case 3:
        if 20<=age<40:
            print("young man") 
    case 4:
        if 40<=age<60:
            print("experinced")
    case 5:
        if age>60:
            print("senior citizen")
    case _:
        print("invalid age")'''

'''#even number#
n=int(input("enter the number")) 
x=int(input("enter the number"))
match x:
    case 1:
        if n%2==0:
            print("saurabh shukla") 
    case 2:
        if 1-2*n<0:
            print("prateek jain")
    case 3:
        if 2*n+1>0:
            print("aditya chaudhry")
    case _:
        print("invalid number")'''

#multiword string in python

'''x=input("enter your name")
y=int(input("enter your name"))
match y:
    case 1:
        if x==" ":
            print("string is multiword",x)
        #else:
         #   print("error")
          #  print("string is a single string",x)
    case _:
        print("invalid string")'''

'''#no is posotive or not

x=int(input("enter the case"))
n=int(input("enter the number"))

match x:
    case 1:
        if n>0:
            print("posotive number")
        else:
            print("nagative")
    case 2:
        if n==0:
            print("no is zero")
    case 3:
        if n<0:
            print("nagative number")
    case _:
        print("invalid case")'''

 #identical string
 
'''f="abc"
r="deepanshu"
if 'f'=='r':
    print("string are same",f)
else:
    print("string are same")'''    

    