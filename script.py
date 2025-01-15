import math

def area_of_square(side):
  return side*side

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    return math.pi * radius**2

def area_of_triangle(base, height):
    return 0.5 * base * height

def main():
    print("select shape:")
    print("1.square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    while True:
        choice = input("\nEnter shape (1-4): ")
        
        if choice=="1":
            side = float(input("input side of square: "))
            area = area_of_square(side)
            print(f"area of the square: {area:.2f}")

        elif choice == "2":
            length = float(input("input length of rectangle: "))
            width = float(input("width of the rectangle: "))
            area = area_of_rectangle(length, width)
            print(f"area of the rectangle: {area:.2f}")

        elif choice == "3":
            radius = float(input("input radius of circle: "))
            area = area_of_circle(radius)
            print(f"area of the circle: {area:.2f}")

        elif choice == "4":
            base = float(input("input base of triangle: "))
            height = float(input("input height of triangle: "))
            area = area_of_triangle(base, height)
            print(f"area of the triangle: {area:.2f}")

        elif choice == "5":
            print("exit!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
