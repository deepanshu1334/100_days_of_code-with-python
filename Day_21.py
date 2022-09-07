#1

'''l1=[3,4,5,3,64,2,3]
it=iter(l1) #iter func jo hai wo iterator return karega jo pahle elemetn ko point karega
print(it)
print()
print(next(it))#next funct jo hai woh woh elemtent return karega
print()
print(next(it)) #next aab agle elemnt ko point karega
print()
print(next(it))
print()
print(next(it))
print()'''


#2

'''t1=(3,4,5,6,7,8,8,6)
it=iter(t1) #iter return karega iterable object jo pahle elemt ko point karega
while True:
    print(next(it),end=" ") #ek samay aisa aage jab sare elemtn access ho chuke honge aur koi elemtny access ka liya nahi bacha hoga toh stop iteratione error aage
'''

#3

'''t1=(2,4,5,6,7,7,5)
it=iter(t1)
while True:
    try:
        print(next(it),end=" ")
    except StopIteration:
        pass     

print("last line of the program")'''

#4 generator function 
# 

def f1():
    yield 10 #yeild matlab produce hona yeild ko read karte hii pause aagee
    yield 20
    yield 30

it=f1()
print(next(it))
print()
print(next(it))
print()
print(next(it))

#5

def f1():
    yield 10 #yeild matlab produce hona yeild ko read karte hii pause aagee
    print("one")  
    yield 20
    print("two")
    yield 30
    print("three")

it=f1()
print(next(it))
print()
print(next(it))
print()
print(next(it))
#print(next(it))

#6

def f1():
    yield 10 #yeild matlab produce hona yeild ko read karte hii pause aagee
    print("one")  
    yield 20
    print("two")
    yield 30
    print("three")

'''it=f1()
print(next(it))
print()
print(next(it))
print()
print(next(it))
#print(next(it))'''

for e in f1():
    print(e)

#8

def f1():
    yield 10 #yeild matlab produce hona yeild ko read karte hii pause aagee
    print("one")  
    yield 20
    print("two")
    yield 30
    print("three")

it=f1()
a=next(it)
print("the value of a is",a)
b=next(it)
print("the value of b is ",b)
c=next(it)
print("the value of c is",c)


#9

'''def ev(n):
    x=2
    while n:
        yield x #x generrate kar rahe jhhai 
        x+=2
        n-=1

for r in ev(int(input())):
    print(r)'''


#10

