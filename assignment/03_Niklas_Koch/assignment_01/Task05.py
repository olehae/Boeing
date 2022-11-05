print("I need 3 numbers for the sides of a triangle from you!")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if type(x) != int or type(y) != int or type(z) != int or x > y + z or y > x + z or z > x + y:
    print("Enter a valid Input!")
else:
    if x == y and x == z:
        print("The triangle is equilateral")
    if x == y and x != z and y != z or x != y and y == z and x != y or x != y and y != z and x == z:
        print("The triagle is isosceles")
    if x != y and y != z and x != z:
        print("The triangle is scalene")
