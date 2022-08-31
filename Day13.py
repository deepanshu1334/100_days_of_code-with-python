#hashaablity

'''x=5 #all immutable object are hashable
print(type(x))
print(hash(x))
y=4.5
print(type(y))
#l1=[2,43,4,5,2] #list hashaable nahi hai ,so error aage
#print(hash(l1))

del y
z=4.5
print(hash(z))
id(z)'''


#string 

#how to create str object
s1="mysirg"
s2='mysirg'
s3="""mysirg"""
print(s1)
print(s1[0],s1[1],s1[2],end=" ")
print()
print(s2[0],s2,end=" ")
print()
print(s1[-1],s1[5])
print()
print(s3,s3[0])
print()
print("Teacher's Day")
print()
print("\"Teachers's Day\"")
print()

#accessing str object
for e in s1:
    print(e)
print()

i=0
while i<len(s1):#len function length return karega
    print(s1[i])
    i+=1
print()    

#range object bhi sequence hai 
'''r=range(10)
print(r[0])
print(range(5))
print(r[3])
print()'''

s1="deepanshu kumar"
print(s1)
print(len(s1))
print();
print(max(s1)) #ye unicode ka base pa decide hoga ki konsa elemnt bada hai
print()
print(min(s1)) #space ka unicode sabse kaam hai isme
print()
#print(sum(s1)) #int aur char ko kaise add karenge

s1="Mysirg Education Service"
print(min(s1)) #space ka unicode sabse kam hoga
print()
print(max(s1))#sabse jyada unicode y ka hoga
print()
#print(sum) #sum ek aur function jisme aap str type ki value ka sum nahi karva sakte
print()

#

s1="1234" #double quotes ma humne jo bhi likh diya woh str type ka data
#print(int(s1)) #s1 ko int ma convert kar diya par ye ek single value hai
print()
#print(sum(int)) #sum function iterable type ka data leta hai toh ye error dega
print(s1)

#using conditional expression
#cond expression ek result return karega use sum ma add karwa lenge
#print(sum[int(e) for e in s1]) #e main one by one elemnt aage aur use int ma convert karva lange


s1="1234"
print(sum([int(e) for e in s1]))

s2="1a2b3c4"
print(sum([int(e) for e in s2 if ord(e)>=49 and ord(e)<=57]))
#jiska unicode 49 se 57 ka bich main hai woh print hoga

#methods in str
s1="Mysirg education list"
print(sorted(s1)) #sorted funct always list return karke dega
print()
print(s1.index("e"))
print()
print(s1.index(" "))
print()
print(s1.count("e"))
print()
print(s1.count(" "))
print()
print(s1.count("educ"))
print()
print(s1.startswith("my"))
print()
print(s1.startswith("list"))
print()
print(s1.endswith("list"))
print()
print(s1.endswith(" "))
print()

s3='1a1b234'
print(s3.isdigit())
print()
print(s3.isdigit())
print()
print(s3.isalnum())
print()
print()

s1="{},welcome"
print(s1.format("deepanshu"))
print()
s2="{},{},deepansji"
print(s2.format("deepan","kumar"))
print()
a=5
b=3.5
s5="value of a is {} and b is {}"
print(s5.format(a,b))
print()

a=1
s3="deepanshu is {} in the class hai no {}"
print(s3.format("topper",a))
print()

#split funtion
#split func always return list of str value
s1="deepanshu kumar champion"
print(s1.split(" "))
print()

s2="your name is deepanshu kumar"
print(s2.split(" "))

#how to take input from user in a list

'''print("enter numbers seprated by comma")
l1=[int(e) for e in input().split(',')]
print(l1)'''

#join funt 
s1="deepanshu kumar champion"
print(s1.split(" "))
print()

print(" ".join(s1)) #space ka basis pa join hoga

#slicing operator

s1="deepanshu kumar"
print(s1[1:10:1]) #10 exclusive)
print()
print(s1[14:5:-1]) #string ko reverse karrane ke liye useful hai

print(s1[::-1]) #string poori reverse ho jayegi

#list ko reverse bhi karwa sakte hoon
l1=[2,3,4,5,3,4]
print(l1[0:4:1])
print(l1[::-1]) #by default beg value last hogu aur end value begging hogi aur step -1


#
n=input