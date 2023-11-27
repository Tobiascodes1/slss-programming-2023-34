# Functions Practice
# Author: Toby
# 24 November 2023


def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

def stars(num: int) -> int:
    stars = "*" * num
    return stars
print(stars(10))

def biggest_of_three(num1: float, num2: float, num3: float):
    biggest_of_three = max(num1,num2,num3)
    return biggest_of_three

print(biggest_of_three(10,10.0005,3))

def pyramid(num: int):
    pyramid = ""
    for i in range(num):
        layer = "*"*(i+1)
        pyramid += "\n" + layer
    return pyramid
print(pyramid(5))

def pyramid_mirror(num: int):
    mpyramid = ""
    for i in range(num):
        layer= " "*(num-i+1) + "*"*(i+1)
        mpyramid += "\n" + layer
    return mpyramid

print(pyramid_mirror(5))