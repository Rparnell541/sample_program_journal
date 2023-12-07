# Prompts user to enter file name, opens file and reads each line, counts how many times
# "X_Sample_Word" appears, then calculates the average of the numerical values found for each line.
fname = input("Enter file name: ")
fh = open(fname)

count = 0
aver = 0

for line in fh:
    if line.startswith("X_Sample_Word"):
        count = count + 1
        total = float(line[line.find(':')+1:])
        aver = aver + total
print('Average sample words:', aver/count)
