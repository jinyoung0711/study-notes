# =====================================
# 🚀 TASK 1: Data types
# =====================================

# Subscripting
print("Hello"[0])

# String
print("123" + "345") # Concatenation

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# =====================================
# 🚀 TASK 2: Type Error, Checking and Conversion
# =====================================

# len("Hello")

# string type
print(type("Hello"))

# integer type
print(type(1234))

# float type
print(type(3.141592))

# boolean type
print(type(False))

# Convert data type string as integer
print(int("123") + int("456"))

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print("Number of letters in your name: " + str(length_of_name))

# =====================================
# 🚀 TASK 3: Mathematical Operations
# =====================================

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(4 ** 2)

# PEMDAS

# ()
# **
# * OR /
# + OR -

# =====================================
# 🚀 TASK 4: Number Manipulation
# =====================================

""" bmi = 84 / 1.65 ** 2

print(bmi)

print(int(bmi))

print(round(3.9))

print(round(bmi, 2))
 """
# Assign 

score = 0

# User scores a point

score += 1
print(score)

# f-strings
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

# 문자열 앞에 f 추가, 중괄호를 통해 변수 추가
print(f"Your score is = {score}, your height is {height}. YOur are winning is {is_winning}")

# =====================================
# 🚀 TASK 5: Tip Calculator Project
# =====================================

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total = bill*(1+tip/100)/people
print(f"Each person should pay: ${round(total, 2)}")
