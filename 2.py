#2 check rectangle or square
length=float(input("length:"))
breadth=float(input("breadth:"))
area=length*breadth
if(length==breadth):
              print(f"it is a square with area :{area}")
else:
    print(f"it is a rectangle with area :{area}")
