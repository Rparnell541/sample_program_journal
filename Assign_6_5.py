# Code for snipping a numerical value from sample text data, and then prints extracted number.
text = "X-Sample-Data:    123.4567"

ipos = text.find(':')
piece = text[ipos+1:]
value = float(piece)
print(value)
