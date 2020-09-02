# defining the function
def c(i, k):
    # initializing the count as 0
    count = 0

    for h in i:
        # counting the number of occurrences of a word in list k
        if h == k:
            count += 1
    # prints the word and its count
    print(k, count)


# selecting  wordcount.txt file in read mode
P = open("/Users/My Pc/Desktop/wordcount.txt", 'r')
# reading the lines from the file and storing it in a string 'j'
j = P.read()
# converting it into a list 'i'
i = j.split()
print(i)

# an empty list to check repetitions of the word
dup = []
# travelling through the list with 'k'
for k in i:
    # to avoid duplicate items in the output
    if k not in dup:
        dup.append(k)
        # calling the function 'c'
        c(i, k)
