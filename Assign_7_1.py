# Opens and reads file, removes white space, and then prints the file in uppercase.
fname = input("Enter file name: ")
fh = open(fname)

for lx in fh :
    ly = lx.rstrip()
    print(ly.upper())
