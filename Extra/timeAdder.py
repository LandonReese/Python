a1, a2 = 28, 41
b1, b2 = 43, 6
c1, c2 = 36, 38
d1, d2 = 25, 20
e1, e2 = 24, 00

def adder(number1, number2):
    while(number2 > 60):
        number2 -= 60
        number1 += 1
    
    print("Time: ", number1, ":", number2)
    return number1, number2

oneTotal = a1 + b1 + c1 #+ d1 + e1
twoTotal = a2 + b2 + c2 #+ d2 + e2

totalMinutes, seconds = adder(oneTotal, twoTotal)
hours, minutes = adder(0, totalMinutes)

print(hours, ":", minutes, ":", seconds)