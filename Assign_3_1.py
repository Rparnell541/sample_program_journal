# For calculating pay based on pay rate and hours worked.
hrs = input('Enter Hours:')
rate = input('Enter Rate:')
h = float(hrs)
r = float(rate)
if h<=40 :
    pay = h*r
    print(pay)
else :
    pay = 420+(h-40)*15.75
    print(pay)
