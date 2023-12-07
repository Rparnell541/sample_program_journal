# For calculating pay including overtime.
def computepay(hrs, rt):
    if hrs <= 40:
        pay = hrs*rt
    else:
        pay = (40*rt) + ((hrs - 40) * rt * 1.5)
    return pay

hrs = float(input("Enter Hours:"))
rt = float(input("Enter Rate:"))

pay = computepay(hrs, rt)
print("Pay", pay)
