import random   #hum random naam ka module import kar rahe hai,matalab random naam ki koi python file bani hogi(.py)file usse hum variable aur funct import kar raha hain
n=random.randrange(1,10,2)  #begg value 1 hai aur end value 10 hai aur step value 1 hai
print(n)  #rand range kuch random no generate karta hai, 1 se 10 ka bich aur woh increment honge by step size
guess=int(input("enter the number"))
while n!=guess:
    if guess<n:
        print("no is too low")
        guess=int(input("enter the number"))
    elif guess>n:
        print("Too high")
        guess=int(input("enter the number"))
    else:
        break
print("guess no is right")


