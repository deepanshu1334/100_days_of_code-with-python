#1
'''n=int(input("enter the number"))
r1=range(1,n,2)
for e in r1:
    print(e,end=" ")

print(r1[0])
print(r1[3])
print(r1.index(2))'''

#2
'''str="deepanshu kumar chaudhry"
print(str[0],str[2],str[6])
for e in str:
    print(str," ")
print()'''

# tuple
'''t1=(2,3,5,6)
print(t1)
print()
for e in t1:
    print(e,end=" ")
print()
print(t1[0])
print()
for r in t1:
    print(r)
print()
print(t1.count(2))
print(t1.index(3))

t1=(3,"True","Deepanshu","""kumar""",3.451,34.22)
print(t1,end=" ")
print()
for e in t1:
    print(e,end=" ")

print()'''

#1

'''l1=["Rter","e",34,532,23,53,"3a1f34",3443,34]
print(l1[0],l1[1],l1[3]) 
print()
for e in l1:
    if(type(e)==int):
        print(e,end=" ")
print()
l1.append("deepanshu,kumar")
print(l1)
print()
#print(l1.sort())
l1.clear()
print(l1)'''

#4

'''s=(input("enter the number"))
t=[int(e) for e in s.split(",") ]
print(t)'''

#5
from posixpath import split


'''s1="deepanshu kumar chaudhary hello"
print(s1.split(" "))
print()
print("".join(s1))
print()

print(max(s1))
print(min(s1))
print()

#how to input from user in the list

'''#p#rint("Enter the number you want  to seprated by comma")
'''t=[int(e) for e in input().split(",")]
print(t)'''

#how to take input from user in a list
'''print("enter the number seprated by comma")
t=[eval(e) for e in input().split(",")]
print(t)
print()'''

#4
l1=[]
l1.append(3)
l1.append("deepanshu")
l1.insert(3,"deepanshu kumar::")
print(l1)
print()
l1.reverse()
print(l1)
print()
l1[::1]
print(l1)
#l1.sort()
#print(l1)