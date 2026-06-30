# Ques. Suggest a activity based on the weather (e.g, Sunny-Go for a walk, Rainy-Read a book, Snowy-Build a snowman)

weather = "Sunny"

if weather == "Sunny":
    activiy = "Go for a walk"
elif weather == "Rainy":
    activiy = "Read a book"
elif weather == "Snowy":
    activiy = "Build a snowman"
print(activiy)

# Ques. Customize a coffee order: "Small", "Medium", or "Large" with an operation for "Extra shot" of 
#      express

order_size = "Medium "
extra_shot = bool

if extra_shot:
    coffee = order_size + "coffee with  an extra shot"
else:
    coffee = order_size + "coffee"
print("Order: ", coffee)



password = "SecurePass"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("Your password strenth is: ", strength)



#Ques. Leap year checker

year = 2023

if (year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0):
    print(year," is a leap year")