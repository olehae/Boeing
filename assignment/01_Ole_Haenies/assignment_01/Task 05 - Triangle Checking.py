while True:
    x = float(input("Length of first triangle side: "))
    y = float(input("Length of second triangle side: "))
    z = float(input("Length of third triangle side: "))

    if x >= y+z or y >= x+z or z >= x+y:
        print("Your input can´t be a triangle! Please choose valid side lengths:")

    else:
        break

if x == y or y == z or x == z:
    print("The triangle is isosceles", end = " ")
    if x == y == z:
        print("and also equilateral")
else:
    print("The triangle is scalene")