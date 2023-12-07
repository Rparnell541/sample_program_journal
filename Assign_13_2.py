# It prompts the user to enter a location (URL), retrieves data from the specified URL,
# It prints the URL and the number of characters retrieved, the retrieved data, assumed to be in JSON format, 
# is loaded into a Python object, It iterates over the "comments" in the JSON object, extracts the "count" from each comment, 
# converts it to an integer, and accumulates the sum, it increments the total count for each comment, 
# finally, it prints the total count and the sum of counts.
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
