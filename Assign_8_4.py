# For opening a file and making a list of all the words used in the file.
fname = input("Enter file name: ")
word_list = []
with open(fname, 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word not in word_list:
                word_list.append(word)
word_list.sort()
print(word_list)
