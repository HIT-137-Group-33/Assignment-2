import turtle

# Recursive function to draw one edge with inward indentation
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.right(60)    # inward indentation
        draw_edge(length, depth - 1)
        turtle.left(120)
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)

# Function to draw the polygon with recursive edges
def draw_pattern(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)

# Main program
def main():
    # User inputs
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    turtle.speed(0)       # Fastest drawing
    turtle.hideturtle()

    # Move turtle to starting position so it's centered
    turtle.penup()
    turtle.goto(-length/2, length/3)
    turtle.pendown()

    draw_pattern(sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
