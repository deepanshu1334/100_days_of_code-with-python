#

'''f=open("student.txt",mode="w")
f.write("hello how are you")
f.closed'''


#1

'''f=open("student.txt",mode="w")
f.write("hello how are you")
f.write("geeky shows are ")
f.close()
print("writing success")'''

#opening a file

'''f=open("student.txt","r")
print(f)'''

#

'''f=open("deep.txt")
print(f)'''

# 
'''f=open("student.txt","w")
print("f")
f.close()#yaha pa file ko close kar diya'''

#4

'''#foer write mode mode="w", 
#error age agar file waha pa present nahi hai 
f=open("student.txt",mode="r",encoding="utf-8")
print(f)#file object hai f
print(f.name) #name bataga ka file ka ya
print(f.mode) #file kis mode ma open hua ye batayge
print(f.readable())#kya file readable hai ya nahi 
print(f.writable()) #kya yr file writeable hai,agar nahi toh false retunr hoga
f.close()
print(f.closed) #kya aapaka file close hua ya nahi'''

#4

'''f=open("student.txt",mode="r+",encoding="utf-8")
print(f) #mode=a+, mode=w+, mode=rb for binary file,binary file for reading purpose
print(f.name) 
print(f.mode) #exclusive x , file majood nahi hona chahiye, aur ye nayi file banayge
print(f.readable()) 
print(f.writable()) 
f.close()
print(f.closed)'''


#5 chechk file exist or not
'''import imp
import os #os check karega ki file present hai ya nahi
print(os.path.isfile("student.txt")) #os bataga ki file majood hai ya nahi
'''
'''from genericpath import isfile
import os
if os.path.isfile("student.txt"): #agar ye file majood hai toh ho if statent chalegi
    f=open("student.txt")
    print("File opened")
    f.close()
else:
    print("file not found")    '''


#5 writinga data to a file

f=open("student.txt",mode="w")
n=f.write("bye to") #overwrite ho jayega file main
print(f.write("deepanshu kuamr"))
print(n)
f.close()

#4

'''f=open("student1.txt",mode="x") #x hamesha nayi file pa karega
print(f.write("deepanshu"))
f.close() #x ko hamesa nayi file chahiye,apna kaam karne ka liye
'''

#4
'''f=open("student1.txt",mode="a") #x hamesha nayi file pa karega
print(f.write("deepanshu kumar"))
f.close()'''#append se data lase ma add hoga 


#4

'''#mode w se ek nayi file ban jayegi agar file present nahi hai
f=open("student2.txt",mode="a") #mode a se append hoga
lst=["rahul\n","deepanshu\n","sumit\n","deepanshu kumar\n"]
f.writelines(lst) #writeline se group of string likh sakte ho app
f.close() #group of string ka data enter kar sakte hai file main
print("succees")'''

#5
#read ma file pahle se present honi chahiye
'''f=open("student.txt",mode="r")
data=f.read()
print(data)
f.close()
print("completed")'''

'''f1=open("student2.txt",mode="r")
r1=f1.read()
print(r1)
print("yre")'''

#6

'''f=open("student.txt",mode="r")
data2=f.readline() #readline data ko read karne ka liya 
data1=f.readline()
print(data1,end=" ")
print(data2,end=" ")
print("champion")'''

#6

#file pointer ki posotion bataga ftell() method 
#tell file pointer ki current posotion batega
#fseek file pointer ko move kara dega, file pointer ko move karta hai
#seek 2 se start karega file pointer koo 
f=open("student.txt",mode="r")
print(f.tell())
data1=f.read(5)
print(data1)

#overwrite matlab jo pahle se likha hai, usse hata ke kuch naya likhna


