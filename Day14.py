from re import split


s1="deepanshu"
s2="deepanshpu kumar {} and {} and {}"
print(s2.format("is","the","champion"))

#2
s1="Deepanshu kumar"
print(s1[::-1]) #isse poore string reverse ho jaege

#3

'''print("enter the number seprated by comma");
l1=[int(e) for e in input().split(",")]
print(l1)
print()'''

#4
#how to take input from user in a list
'''print("enter the number seprated by comma")
[print(e) for e in input()]
print()'''
#print(l1)

#2
'''print("Enter the number seprated by comma")
l1=[(int(e) for e in input().split(","))]
print(l1)'''

#4
s1="deepanshu kumar chaudhry"
print(s1.split(" "))
print("".join(s1))
print();

#5
s1="Deepanshu"
s2="1234"
print(s1[::-1])
print()
print()
print(sum([int(e) for e in s2.split(",")]))
#print(sum(l2))
#print(sum(l2))

#6
