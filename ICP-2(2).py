# initializing the counter
i = 0
# getting input from the user
j = int(input("enter the digit"))
# breaks the loop when j==0
while j !=0:
    # checking if j is even 
    if j % 2 == 0:
        
        j = j / 2
        # incrementing the counter
        i = i + 1
    # if 'if condition' is false then j should be an odd number
    else:
        # decrementing the number by one to make it even
        j=j-1
        i=i+1

print(i)

