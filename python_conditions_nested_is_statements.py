# nested if statements
# if statements can be nested inside other if statements
# this is called nesting

# check if a number is even and greater than 10

num = int(input("enter a number : "))
if num % 2 == 0:
    if num > 10:
        print("number is even and greater than 10 ")
    else:
        print("number is even but not greater than 10")
else:
    print("number is odd")
        
