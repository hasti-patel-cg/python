# str=input("enter the string :")
# n=len(str)
# falg=True
# for i in range(n):
#     if  str[i]=="o" :
#         falg=False
#         print("Found")
#         break

# if falg==True:
#     print("Not Found")    


# for i in range(1, 6):
#     if i == 4:
#         break

#     print(i)


# Que=1

# for i in range(1, 10):
#     if i == 6:
#         break

#     print(i)

# # que=2    

# numbers = [10, 20, 30, 40, 50]
# flag=True
# for i in numbers:
#     if i==30:
#         flag=False
#         print("found")
#         break
# if flag==True:
#     print("Not found")    


# # que=3

# num=int(input("Enter the number : "))

# while num != 0:
#     num = int(input("Enter a number: "))
#     if num==0:
#         break
     
# #que=4

# for i in range(1,100):
#     if i%17==0:
#         break
#     print(i)

    
# continue

# que=1
# for i in range(1,20):
#     if i%2==0:
#         continue
#     print(i)    


# que=2

# num = [10, -2, 30, -5, 40, -8]

# for i in num:
#     if i< 0:
#         continue
#     print(i)

# que=3
# for i in range(1,20):
#     if i%3==0:
#         continue
#     print(i)

# que=4
# numbers = [5, 12, 8, 21, 30, 7]

# for i in numbers:
#     if i<10:
#         continue
#     print(i)

# 35
# challenge=1

# while True:
#     num=int(input("enter the num :"))
#     if num<0:
#         continue
#     if num==0:
#         break
#     print(num)

# challenge=2

# numbers =[12, 5, -4, 18, 0, 25, 30]
# for i in  numbers:
#     if i<0:
#         continue
#     if i==0:
#         break
#     print(i)


# challenge=3

# numbers =[12, 5, -4, 18, 0, 25, 30]
# num=int(input("enter the number :"))
# for i in numbers:
    
#     if num in numbers:
#         print("found")
#         break
# else:
#     print("not found")




for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")
