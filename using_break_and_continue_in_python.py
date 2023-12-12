# using break and continue in a loop

# in a range
for x in range(101):
    if x % 2 == 0:
        continue # continue with the next iteration of the loop
    print(x)
    
for x in range(101):
    if x == 50:
        break # break out of the loop
    print(x)

# in a list
flower = ['rose' , 'tulip' , 'daisy' , 'sumflower' , 'lily']
for x in flower:
    if x == 'daisy':
        continue
    print(x)
    
flower = ['rose' , 'tulip' , 'daisy' , 'sumflower' , 'lily']
for x in flower:
    if x == 'daisy':
        break
    print(x)
