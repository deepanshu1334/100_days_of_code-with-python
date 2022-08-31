''' x=int(input("enter the number"))
y=int(input("enter the number"))
z=x+y #indentation error
print("the sum of two number is z",z)'''

'''n=int(input("enter the number"))
if n>0:#indetation 4 space apne aap aaga
    print("posotive")
if n<=0:
    print("no is non posotive")
print()'''

'''n=int(input("enter the number"))
if n>0:#syntax
    print("no is posotive")
    print("hello")
print("yo")#is line main error aage kyunki ye block main nahi hai
#gap aa sakte hai if else main
else:
    print("non posotive")
print()'''    

'''m=int(input("enter the number"))
if 90<m<=100:
    print("grade A")
elif 80<m<=90:#m dono se true hona chaiye ,realational operator alag tarah se kaam karta hai pyhon main
    print("grade B")
elif 70<m<=80:
    print("grade C")
elif 60<m<=70:
    print("grade d")    
elif 50<m<=60:
    print("grade E")
else:
    print("grade F")#ye ek block hai'''


'''#single line if else
print("posotive") if int(input("enter the number"))>0 else print("non posotive")'''     

'''#match is like switch 
#match is a soft keyword that work like a variable
x=int(input("enter the number"))
match=x
print(match)'''


'''x=int(input("enter the number"))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")'''


'''x=int(input("enter the number"))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case -4:
        print("nagative 4")
    case 1:
        print("onews")
    case 3:
        print("theressee") 
    case _:#jab sari condition fail hogi tab ye line chalegi
        print("default") '''    


#int ko eval ka sath replace kar ko 
#eval string as an argument lega , aur string ka data bataga ki ya int ,float,bool hai ya nahi


x=eval(input("enter the number"))
match x:
    case 1:
        print("one")
    case True:
        print("two")
    case 2.3:
        print("float")
    case -4:
        print("nagative 4")
    case 1:
        print("onews")
    case 3:
        print("theressee") 
    case _:#jab sari condition fail hogi tab ye line chalegi
        print("default")     