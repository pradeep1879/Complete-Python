# Classfiy a person's age group: Child(<13), Teenager(13-19), Adults(19-60), Senior(60+)

userAge = 61

if userAge < 13:
    print("Child")
elif userAge < 20:
    print("Teenager")
elif userAge < 61:
    print("Adult")
else:
    print("Senior")


# Que: Movie ticket are price based on age: $12 for adults(18 and over), $8 for children. 
#      Everyone gets a $2 discount on Wednesday.


age = 18
day = "Wednesday"

# if age < 18:
#     print("Your ticket price is $8")
# if day == "Wednesday":
#     print("Today you will get $2 discount")
# elif day != "Wednesday":
#     print("No discount today")    
# else:
#     print("Your tickent price is $12")



price = 12 if age >= 18 else 8
print(price)

if day == "Monday":
    #price -= 2
    price = price - 2

print("Ticket price for you is $",price)



# Que: Assign a letter grade based on the student's score: A(91-100), B(81-90), C(71-80), D(61-70)

score = 122

if score > 100:
    print("Wrong input")
    exit()

if score > 90:
    print('A')
elif score > 80:
    print('B')
elif score > 70:
    print('C')
elif score > 60:
    print('D')
else:
    print('F')




# Ques.Determine if a fruit is ripe, overripe ,or unripe based on its color.(e.g,Banana:green-unripe, 
# Yellow-Ripe, Brown-overripe)


fruit = "Banana"
color = "Green"

if fruit == "Banana":
    if color == "Green":
        print("unripe")
    elif color == "Yellow":
        print("ripe")
    elif color == "Brown":
        print("overipe")














