# For scanning through a txt file, finding certain lines, slicing what I need from each line,
# putting it in a dictionary, then counting how many things are in the dictionary and how many times it comes up.
name = input("Enter file:")
thand = open(name)
counts = dict()
hours = []
for line in thand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        hours.append(hour)

for hour in hours:
    if hour in counts:
        counts[hour] += 1
    else:
        counts[hour] = 1

for hour, count in sorted(counts.items()):
    print(hour, count)
