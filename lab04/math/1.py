import math
def degree_to_radian(n):
    rad = n*(math.pi/180)
    return rad
print("Output radian: ", degree_to_radian(int(input("Input degree: "))))