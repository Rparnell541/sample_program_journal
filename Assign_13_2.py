import urllib.request as ur
import json


url = input("Enter location: ")
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
obj = json.loads(data)

sum = 0
total = 0

for comment in obj["comments"]:
    sum += int(comment["count"])
    total += 1

print('Count:', total)
print('Sum:', sum)