import turtle

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    
    # Main branch
    t.forward(branch_length)
    t.right(45)

    # Right branch
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
    t.left(90)

    # Left branch
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
    t.right(45)
    t.backward(branch_length)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)
    level = int(input("Enter the recursion level: "))
    draw_pythagoras_tree(t, 100, level)
    window.mainloop()

if __name__ == "__main__":
    main()

