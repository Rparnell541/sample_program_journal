fname = input("Enter file name: ")
fh = open(fname)

count = 0
aver = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        total = float(line[line.find(':')+1:])
        aver = aver + total
print('Average spam confidence:', aver/count)
