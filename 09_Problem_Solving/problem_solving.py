# que=1
# num=int(input("enter the number: "))
# if num>0:
#     print("Positive")
# elif num==0:
#     print("Zero")
# else:
#     print("Negative")    

# que=2 
# num=int(input("enter the number: "))
# if num>0 and num%2==0 :
#     print("positive Even")
# elif num<0 and num%2==0:
#     print("negative even")
# elif num>0 and num%2==1:
#     print("positive odd")
# elif num<0 and num%2==1:
#     print("negative odd")  
# else:
#     print("Zero") 
    
#que=3
# a=int(input("enter the value of a: "))
# b=int(input("enter the value of b: "))

# if a>b:
#     print(f"{a} is the largest number")
# elif b>a:
#     print(f"{b} is the largest number")
# else:
#     print("both are equal")         

#que=4

# a=int(input("enter the value of a: "))
# b=int(input("enter the value of b: "))
# c=int(input("enter the value of c: "))
# if a<=b and a<=c:
#     print(f"{a} is the Smallest number")
# elif b<=a and b<=c:
#     print(f"{b} is the Smallest number")
# elif c<=a and a<=b:
#     print(f"{c} is the Smallest number")
  
            
#que=5
# a=int(input("enter the value of a: "))
# b=int(input("enter the value of b: "))
# c=int(input("enter the value of c: "))
# if a>=b and a>=c:
#     print(f"{a} is the largest number")
# elif b>=a and b>=c:
#     print(f"{b} is the largest number")
# elif c>=a and c>=b:
#     print(f"{c} is the largest number")

#que=6
# num=int(input("enter the number:"))
# if num%5==0 and num%11==0:
#     print(f"{num} is Divisible by 5 and 11")
# elif num%5==0: 
#     print(f"{num} is Divisible by 5 ")
# elif num%11==0: 
#     print(f"{num} is Divisible by 11 ")    
# else:
#     print("Divisible by neither")

#que=7
# num=int(input("enter the number:"))
# if num%3==0 and num%7==0:
#     print(f"{num} is Divisible by 3 and 7")
# elif num%3==0: 
#     print(f"{num} is Divisible by 3 ")
# elif num%7==0: 
#     print(f"{num} is Divisible by 7 ")    
# else:
#     print("Divisible by neither")

#que=8
# marks=int(input("enter the marks: "))
# if marks<0 or marks>100:
#     print("Invalid marks")
# elif marks>=40:
#     print("Pass")
# else:
#     print("Fail")
    
#que=9
# marks=int(input("enter the marks: "))
# if marks<0 or marks>100:
#     print("Invalid marks")
# elif marks>=90:
#     print("A")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# elif marks>=60:
#     print("D")
# elif marks>=40:
#     print("E")
# else:
#     print("Fail")   

#que=10

# age=int(input("enter your age: "))
# if age<0 or age>120:
#     print("Invalid age")
# elif age<18:
#     print("Cannot vote")
# else:
#     print("Can vote") 

#que=11
# year=int(input("enter the year: "))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print(f"{year} Leap year") 
# else:
#     print(f"{year} not leep year")  

#que=12

# character=input("enter the value: ")
# if  'A' <= character <= 'Z':
#     print("Uppercase alphabet")
# elif 'a'<= character <= 'z':
#     print("Lowercase alphabet")    
# elif '0'<= character <= '9':
#     print("Digit")
# else:
#     print("Special character")

#que=13

#que=14

# cost_price=float(input("enter the cost price: "))
# selling_price=float(input("enter the selling price: "))


# if selling_price > cost_price:
#     print("profit")
# elif selling_price < cost_price:
#     print("loss")
# else:
#     print("No profit and no loss")
                
#que=15


# cost_price=float(input("enter the cost price: "))
# selling_price=float(input("enter the selling price: "))
# profit=selling_price > cost_price
# loss=selling_price < cost_price

# if profit :
#     profit_percentage= profit/cost_price*100
#     print("profit percentage is", profit_percentage,"%")
# elif loss :
#     loss_percentage= loss/cost_price*100
#     print("loss percentage is ", loss_percentage,"%")
# else:
#     print("No profit and no loss")

#que=16

# units=float(input(("enter youe electricity bill units:")))

# if units<=100:
#     print(f"total:{units*5}")
# elif units<=200:
#     first_hundred=100*5
#     next_hundred=(units-100)*7
#     print(f"taotal:",first_hundred+next_hundred)
# else :
#     first_hundred=100*5
#     next_hundred= 100*7 
#     remaing_units=(units-200)*10
#     print(f"taotal:",first_hundred+next_hundred+remaing_units)   
 


#que=18

# tem=float(input("enter the temperature: "))

# if tem < 0:
#     print("Freezing")
# elif 0<=tem<=15:
#     print("Very Cold") 
# elif 16<=tem<=25:
#     print("Cold")
# elif 26<=tem<=35:
#     print("Normal")
# else:
#     print("Hot")       
     
#que=19
# num=int(input("enter the number: "))

# if num < 0:
#     print(f"{num} is Negative ")
# elif 0<=num<=10:
#     print(f"{num} is between 0 and 10") 
# elif 11<=num<=50:
#     print(f"{num} is between 11 and 50")
# elif 51<=num<=100:
#     print(f"{num} is between 51 and 100")
# else:
#     print(f"{num} is above 100") 

#que=20

# lenth1=int(input("enter the triangle lenth1: "))
# lenth2=int(input("enter the triangle lenth2: "))
# lenth3=int(input("enter the triangle lenth3: "))

# if lenth1+ lenth2 > lenth3 and lenth1+ lenth3 > lenth2 and lenth2+ lenth3 > lenth1:
#     print("Valid triangle") 
# else:
#     print(" Invalid triangle")

#que=21

# lenth1=int(input("enter the triangle lenth1: "))
# lenth2=int(input("enter the triangle lenth2: "))
# lenth3=int(input("enter the triangle lenth3: "))

# if lenth1==lenth2 and lenth1==lenth3 and lenth2==lenth3:
#     print(" Equilateral(all three sides equal)")
# elif  lenth1==lenth2 or lenth1==lenth3 or lenth2==lenth3:   
#     print("Isosceles(exactly two sides equal)")
# else:
#     print("Scalene (all sides different)")    
                
#que=22

# Account_balance=float(input("enter your account balance="))
# Withdrawal_amount=float(input("enter the amount you want to withdrawal="))

# if Withdrawal_amount>0 and Withdrawal_amount%100==0 and Withdrawal_amount <= Account_balance and Account_balance - Withdrawal_amount >= 500:
#     print("Withdrawal successful") 
#     print("Remaining balancesful",Account_balance - Withdrawal_amount)
# else:
#     print("Withdrawal failed")     

#que=23

# Username=(input("enter youe Username ="))
# password=(input("enter the password = "))

# if Username == "" or password == "":
#     print("Login successful")
# else:
#     print("Wrong password") 

#que=24

# amount=float(input("enter the purchase amount="))


# if amount < 500:
#     print("discount:0%" )
#     print("discount amount: " ,amount*0)
#     if amount>1000:
#         print("discount:5%" )
#         print("discount amount: " ,amount*0.05)
#     elif amount>2000:
#         print("discount:10%" )
#         print("discount amount: " ,amount*0.10)
#     elif amount>5000:
#         print("discount:15%" )
#         print("discount amount: " ,amount*0.15)
# else:
#     print("discount:20%" )
#     print("discount amount: " ,amount*0.20)

#que=25


# total = 0
# passed = True
# marks=int(input("enter the marks="))

# total = total + marks

# percentage=total/5
# for i in range(5):


#     if marks < 35:
#         passed = False




# if passed:
#     if percentage >= 90:
#          garde="A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 50:
#         grade = "D"
#     else:
#         grade = "F"
# else:
#     grade = "F"

# print(total)
# print(percentage)
# print(garde)

# if passed:
#     print("PASS")
# else:
#     print( "FAIL")





    


 
                

   






