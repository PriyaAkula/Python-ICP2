# initialising two lists
# for input
p = []
# for output
k = []

n = int(input(" Enter height in feet "))
# adding the input items to the list 'P'
for i in range(0, n):
    j = float(input())
    p.append(j)
    # converting feet to cm , 1feet=30.48 cm
    c = float(j*30.48)
    # to get only one decimal place using strings
    m = str(c)[:-2]
    # appending the resultant value to the output list'k'
 
    k.append(m)

print(p)
print(k)


