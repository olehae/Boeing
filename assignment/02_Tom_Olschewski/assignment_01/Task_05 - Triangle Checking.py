while True:
    x = int(input("Input the first side : "))
    y = int(input("Input the second side : "))
    z = int(input("Input the third side : "))

    if x > y + z or y > x + z or z > x+y:
        print("Your input is invalid, please try again \n")

    else:
        break

if x == y == z:
    print("\nThe triangle is equilateral since all sides have the same lenght!")

elif x == y or y == z or x == z:
    print("\nThe triangle is isosceles since exactly two sides have the same lenght!")

else:
    print("\nThe triangle is scalene since all the sides have different lenghts!")