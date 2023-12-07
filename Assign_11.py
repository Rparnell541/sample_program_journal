import re

with open('regex_sum_data.txt', 'r') as f:
    content = f.read()
numbs = re.findall(r'\d+', content)
total = sum(map(int, numbs))
print('Total:', total)