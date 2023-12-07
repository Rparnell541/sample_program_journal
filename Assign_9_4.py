# For opening a txt file, finding certain lines, counting the words,
# then finding which "word" happens the most and how many times.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith('From:'): continue
    words = line.split()
    if len(words) > 1:
        second = words[1]
        counts[second] = counts.get(second, 0) + 1

bigcount = None
bigemail = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = word
        bigcount = count

print(bigemail, bigcount)
