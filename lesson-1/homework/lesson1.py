def square_properties(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

side_of_square = 5
square_perimeter, square_area = square_properties(side_of_square)

print(f"Square with side {side_of_square}:")
print(f"Perimeter: {square_perimeter}")
print(f"Area: {square_area}")

import math

def circle_length(diameter):
    return math.pi * diameter

diameter_of_circle = 10
circle_circumference = circle_length(diameter_of_circle)

print(f"Circle with diameter {diameter_of_circle}:")
print(f"Circumference: {circle_circumference:.2f}")

def mean_of_two(a, b):
    return (a + b) / 2

a = 4
b = 7
mean = mean_of_two(a, b)

print(f"Mean of {a} and {b}: {mean}")

def sum_product_squares(a, b):
    sum_ab = a + b
    product_ab = a * b
    square_a = a ** 2
    square_b = b ** 2
    return sum_ab, product_ab, square_a, square_b

a = 4
b = 7
sum_ab, product_ab, square_a, square_b = sum_product_squares(a, b)

print(f"Sum: {sum_ab}, Product: {product_ab}, Square of {a}: {square_a}, Square of {b}: {square_b}")
