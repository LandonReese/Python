def xyDiag(x1, y1, x2, y2):
    print("x1:", x1, "y1", y1, "x2:", x2, "y2", y2)
    x = (x1 - x2)
    y = (y1 - y2)
    print("x:", x, "y", y)
    
    tempx = x2
    tempy = y2
    
    for i in range(20):
        tempx -= x
        tempy -= y
        # print(tempx, x)
        # print(tempy, y)
        print(tempx, tempy)
    return

xyDiag(-50, -141, -49, -140)