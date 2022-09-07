#group angram using python

'''from collections import defaultdict

def group_angram(a):
    dfdict=defaultdict(list) #default dict module main list pass kari hai
    for i in a:
        sorted_a=" ".join(sorted(i))
        dfdict[sorted_a].append(i)
    return dfdict.values()

words=["eat","japan","bat","ate"]
print(group_angram(words))'''    

#2

'''def f1(r1):
    for e in r1:
        print(e)
        if 

print()

f1(range(1,11,1))'''

#3

'''def f1(r1):
    for e in r1:
        print(e)
print()

f1(11)
f1(11)
f1(11)'''

#4 find missing numebrer in python
'''def findno(n):
    number=set(n)
    length=len(n)
    output=[]
    for i in range(1,n[-1]):
        if i not in number:
            output.append(i)
    return output


listno=[1,2,3,4,5,5,6,7,8,9,10,11,14]
print(findno(listno))           '''  


