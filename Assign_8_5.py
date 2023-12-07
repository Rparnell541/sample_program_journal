#For opening a file and counting how many lines start with a certain word.
fname = input("Enter file name: ")
count = 0
fh = open(fname)

for line in fh :
    if line.startswith('From:') :
        count += 1
        email = line.split()[1]
        print(email)
print("There were", count, "lines in the file with From as the first word")
