print("Enter triangle side lengths: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

valid_input = False
while not valid_input:
    if x+y > z and y+z > x and z+x > y:
        valid_input = True
    else:
        print("Wrong input. Please give a valid input: ")
        x = int(input("x: "))
        y = int(input("y: "))
        z = int(input("z: "))

if x == y == z:
    print("equilateral triangle")
elif x == y or y == z or z == x:
    print("isosceles triangle")
else:
    print("scalene triangle")
