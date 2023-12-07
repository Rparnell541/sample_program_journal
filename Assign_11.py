# Reads file, extracts all numerical values using regular expression, sums and prints totals.
import re

with open('sample.txt', 'r') as f:
    content = f.read()
numbs = re.findall(r'\d+', content)
total = sum(map(int, numbs))
print('Total:', total)
