# using conditions in a loop

for x in range(10 , 20 , 3): # will print 10, 13, 16, 19
    print(x)
    
# printing out even numbers between 1 and 100

print("Even numbers between 1 and 100 are: ")
for x in range(1 , 100):
    if x % 2 == 0:
        print(x)

# printing out odd numbers between 1 and 100

print("Odd numbers between 1 and 100 are: ")
for x in range(1 , 100):
    if x % 2 == 1:
        print(x)
