##Part A — Intermediate Problems
##Problem 1: Valid Marks
marks=int(input("enter the marks:"))
if 0<=marks<=100:
    print("valid marks")
else:
    print("Invalid marks")


# Problem 2: Positive Integer


num=int(input("enter the num:"))
if num>=0:
    print("accepted number")
else:
    print("not accepted")  
#Problem 3: Age Validation


age=int(input("enter the age:"))
if 0<age<=120:
    print("valid age")
else:
    print("invalid age")  


#Problem 4: Menu Choice

print("1. View profile")
print("2. Edit profile")
print("3. Settings")
print("4. Exit")
menu=int(input("enter the menu:"))
match menu:
    case 1:
        print("valid input")
    case 2:
        print("valid input")
    case 3:
        print("valid input")
    case 4:
        print("valid input")
    case _:
        print("invalid input") 

##problem 5: Password Length

password = ""

while len(password.strip()) < 8:
    password = input("Enter a password (at least 8 characters): ")
    
    if len(password.strip()) < 8:
        print("Password is too short. It must contain at least 8 characters.")

print("Success! Your password has been accepted.")


# #Problem 6: Temperature Range
tem=float(input("enter the temprechure:"))
if -20<=tem<=45:
    print("valid temprecture")
else:
    print("invalid temprecture")


# # Problem 7: Withdrawal Validation 
balance = 5000.0
print(f"Current Balance: ₹{balance}")
while True:
    withdrawal = float(input("Enter withdrawal amount (₹): "))
    if withdrawal <= 0:
        print("Invalid amount. Withdrawal must be greater than zero.")
    elif withdrawal > balance:
        print("Insufficient funds. Withdrawal amount cannot exceed your balance.")
    else:
        break
balance -= withdrawal
print(f"Withdrawal successful! Remaining balance: ₹{balance}")


##Problem 8: Username Validation
while True:
    username = input("Enter a username: ")
    trimmed_username = username.strip()
    if len(trimmed_username) >= 5 and " " not in trimmed_username:
        print("Username accepted!")
        print("Accepted username:", username)
        break
    else:
        print("Invalid username. Please make sure it is at least 5 characters long (excluding outer spaces) and contains no spaces inside.")


##Problem 9: Divisible Number
num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("accepted number")
else:
    print("not accepted number")  


# # Problem 10: Limited PIN Attempts
secret_pin = "2468"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    
    if entered_pin == secret_pin:
        print("PIN accepted! Access granted.")
        break
    else:
      attempts -= 1
      if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.")
else:
            print("Access denied. All attempts failed.")


##Problem 11: Number Within a Range
num=int(input("enter the number:"))
if 10<=num<=50 and num%2==0:
    print("even")
else:
    print("odd")  


##Problem 12: Deposit Validation
balance = 2000.0
print(f"Current Balance: ₹{balance:.2f}")
while True:
    deposit = float(input("Enter deposit amount: "))
    
    if deposit > 0:
        balance += deposit
        print(f"Deposit successful! New Balance: ₹{balance:.2f}")
        break
    else:
        print("Invalid amount. Please enter a positive value greater than zero.")


#art B — Challenging Problems


##Problem 13: Integer Between 1 and 100
num=int(input("enter the number:"))
if 0<=num<=100:
    print("valid number")
else:
    print("Invalid number") 


# problem 14: Marks and Result
marks=int(input("enter marks:"))
if marks>75:
    print("Distinction")
elif 60<marks<=75:
    print("First Class")
elif 35<=marks<=60:
    print("pass")
else:
    print("fail")  


