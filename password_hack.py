import os

attemps=0
loop=True
ans=""
password=input("Enter the password (at least 8 characters): ")
ans_list=[""]*len(password)

keys="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[]{}`~;:'\"<>,.?/"

while(loop):
    if(ans==password):
        loop=False
        print(f"Your password is: {ans}")
        print(f"Attemps: {attemps}")
        break
    for i in range(0,len(password),1):
        for j in range(0,len(keys)-1,1):
            print(f"Analysing the password {ans}")
            os.system('cls')
            attemps+=1
            if(password[i]==keys[j]):
                ans_list[i]=keys[j]
                break
            ans="".join(ans_list)