# # que=1

# Take a string containing letters, digits, spaces, and special characters.

# Using a for loop:

# Count uppercase letters.
# Count lowercase letters.
# Count digits.
# Count spaces.
# Count special characters.
# Print which category has the highest count.
# If two or more categories have the same highest count, print "Tie".

# char=input("enter the string :")
# count=0
# uppercsae = 0
# lowercase=0
# space = 0
# special = 0

# for scr in char:
#     if scr in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         uppercsae +=1 
#     elif scr in "abcdefghijklmnopqrstuvwxyz":
#         lowercase += 1
#     elif scr in "0123456789":
#         count +=1    
#     elif scr == " ": 
#         space += 1
#     else:
#         special += 1

# print("uppercase letters :",uppercsae)
# print("lowercase letters :",lowercase)
# print("digits : ",count)
# print("spaces :",space)
# print("special characters :",special)

# if uppercsae>lowercase and uppercsae>count and uppercsae>space and uppercsae>special:
#     print("highest count: uppercase")
# elif lowercase>uppercsae and lowercase>count and lowercase>space and lowercase>special:
#     print("highest count :lowercase")
# elif count>uppercsae and count>lowercase and count>space and count>special:
#     print("highest count :digits")
# elif space>uppercsae and space>lowercase and space>count and space>special:
#     print("highest count :spaces")
# elif special>uppercsae and special>lowercase and special>count and special>space:
#     print("highest count :special characters")  
# else:
#     print("Tie")          


#2 . Student Performance Analyzer
# Take marks of 10 students using a for loop.

# For each student:

# Print "Fail" if marks are below 35.
# Print "Pass" for 35–49.
# Print "Good" for 50–74.
# Print "Excellent" for 75–100.
# At the end, print the number of students in each category


# for marks in range(1,11):
#     marks=int(input("enter the marks : "))
#     if marks >= 75:
#         print("Excellent")
#     elif marks>=50:
#         print("Good")
#     elif marks>=35:
#         print("Pass")
#     else:
#         print("Fail")        


# 3. Word Score Calculator
# Take a sentence.

# For every word:

# Vowel = 2 points.
# Consonant = 1 point.
# Digit = 3 points.
# Special character = 4 points.
# Calculate the score of every word and print the word with the highest score.

# Do not use max()
   
vowel="aeiouAEIOU"
consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
digit="1234567890"
str=input("enter the string :").split()


