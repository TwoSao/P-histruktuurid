import math

try:
    a = float(input('Enter the side length of the square => '))
    S = a**2
    print("Square area:", S)
    P = 4 * a
    print("Square perimeter:", P)
    di = a * math.sqrt(2)
    print("Square diagonal:", round(di, 2))
except ValueError:
    print("Please enter a valid number.")

print()

try:
    b = float(input("Enter the first side length of the rectangle => "))
    c = float(input("Enter the second side length of the rectangle => "))
    S = b * c
    print("Rectangle area:", S)
    P = 2 * (b + c)
    print("Rectangle perimeter:", P)
    di = math.sqrt(b**2 + c**2)
    print("Rectangle diagonal:", round(di, 2))
except ValueError:
    print("Please enter a valid number.")

print()

try:
    r = float(input('Enter the radius of the circle => '))
    d = 2 * r
    print("Circle diameter:", d)
    S = math.pi * r**2
    print("Circle area:", round(S, 2))
    C = 2 * math.pi * r
    print("Circumference:", round(C, 2))
except ValueError:
    print("Please enter a valid number.")
