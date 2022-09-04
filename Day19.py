#1
'''def f1(a,b):
    print("a=",a,"b=",b)
print()

a=int(input("Enter the number"))
b=int(input("enter the number"))
f1(a,b)'''

#2

'''def f1(a,b,c):
    d=a+b+c
    return d
print()    
a=input("enter the name")
b=input("enter the name")
c=input("Enter the name")
print("the concatentaion is",f1(a,b,c))'''

#3

'''def f1(l1):
    print(sum(l1))
    print(max(l1))
    print(min(l1))
    print(sorted(l1))

l1=[2,3,34,5,4,5,6,7]
f1(l1)'''

#4

'''def f1(l1):
    print(l1)
    print(max(l1))
    l1.append(23)
    print(l1)
    l1.insert(2,34)
    print(l1)
    print()
    print(sorted(l1))
    print(l1.count(3))
    l1.clear()
    print(l1)



l1=list(range(1,10,1))
f1(l1)
print(l1)'''

#5
'''def f1(*t):
    d=sum(t)/len(t)
    return d

print("avg is ",f1(2),3,4,5)
print("Avg is ",f1(3,4,56,12,3,4,5))
print("avg is",f1(2,3,4,11,3,4,2))
#print("Avg is ",f1("Acd","fer","defg","frie"))'''


#6

'''def f1(a1):
    print(a1)
    print(a1[0],a1[7])
    print()
    print(sorted(a1))
    print()
    print(max(a1))
    print(min(a1))



f1("deepanshu")    '''

#7

'''def f1(a,b,c):
    d=a+b+c
    print(d)
print()

f1("deepanshu kumar","shivani kumari","seema")'''

#8

'''def f1(r1):
    for e in r1:
        print(e)
print()

f1(range(2,10,2))
f1(range(2,10,2))
f1(range(2,10,2))
f1([2,4,5,2,1,])'''

#9

'''def f1(l1):
    print(l1)
print()

f1([2,4,5,1,3,2,])'''

#10
#passing tuple into a function

'''def f1(t1):
    print(t1)
    print(t1[0])
print()

f1((2,3,4,5,6,5))'''

#11 passing into dict into a d1

'''def f1(d1):
    print(d1)
print()

f1({2,3,4,11,2,2,1,3,4})'''

#12

'''def f1(s1):
    print(s1)
    for e in s1:
        print(e)
        print(sorted(s1))
        print(s1[0])
        print(s1[1])
        print(s1[2])
print()

f1("mysirg")'''

#13

'''def f1(r1):
    for e in r1:
        print(e,end=" ")
print()

f1(range(1,11,1))'''

#14

'''def f1(n):
    i=1
    while i<=n:
        print(i)
        i+=1
print()
m=int(input("enter the number"))
f1(m)        '''

#15

'''def f1(d1):
    for e in d1:
        print(e)
print()

d1={2,3,4,23,3,4,"mysirg",1,3,1,3}
f1(d1)'''


#16
def f1(d1):
    for e in d1:
        print(e)

d1={1:"deepanshu",2:"hello",3:"durgesg",4:"broken has meaning"}
f1(d1)
print()

#17



