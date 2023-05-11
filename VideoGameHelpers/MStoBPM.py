def MStoBPM(milliseconds):
    return 60000/milliseconds

print("0.2 Seconds, 200 ms")
x = 200
print(MStoBPM(x), "BPM")