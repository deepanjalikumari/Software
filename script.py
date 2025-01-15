# Module docstring
# This script calculates the area of square, rectangle, circle, and triangle.
import math
def area_of_square(side):
    """Calculating the area of a square."""
    return side * side
def area_of_rectangle(length, width):
    """Calculating the area of a rectangle."""
    return length * width
def area_of_circle(radius):
    """Calculating the area of a circle."""
    return math.pi * radius**2
def area_of_triangle(base, height):
    """Calculating the area of a triangle."""
    return 0.5 * base * height
def main():
    """Select shape and calculate area."""
    print("Select shape:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")
    while True:
        choice = input("\nEnter shape (1-4): ")
        if choice == "1":
            side = float(input("Input side of square: "))
            area = area_of_square(side)
            print(f"Area of the square: {area:.2f}")
        elif choice == "2":
            length = float(input("Input length of rectangle: "))
            width = float(input("Input width of the rectangle: "))
            area = area_of_rectangle(length, width)
            print(f"Area of the rectangle: {area:.2f}")
        elif choice == "3":
            radius = float(input("Input radius of circle: "))
            area = area_of_circle(radius)
            print(f"Area of the circle: {area:.2f}")
        elif choice == "4":
            base = float(input("Input base of triangle: "))
            height = float(input("Input height of triangle: "))
            area = area_of_triangle(base, height)
            print(f"Area of the triangle: {area:.2f}")
        elif choice == "5":
            print("Exit!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
