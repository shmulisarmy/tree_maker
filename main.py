import turtle, threading, time

def draw_branch(branch_size, main_turtle, angle, depth = 0):
    main_turtle.left(angle)
    main_turtle.forward(branch_size)
    if depth >= max_depth:
        main_turtle.fillcolor('green')
        main_turtle.begin_fill()
        main_turtle.circle(max(branch_sizes//20 - depth, 1))
        main_turtle.end_fill()
        return
    for i in range(-40, 41, 40):
        # if i == 0: continue
        branching_trutle = turtle.Turtle()
        branching_trutle.speed(0)
        branching_trutle.hideturtle     ()
        branching_trutle.penup()
        branching_trutle.goto(main_turtle.pos())
        branching_trutle.pendown()
        branching_trutle.setheading(main_turtle.heading())
        draw_branch(branch_size*(2/3), branching_trutle, i, depth + 1)

screen = turtle.Screen()

player = turtle.Turtle()

branch_sizes = 100

player.goto(0, -branch_sizes)

player.speed(0)

player.hideturtle()

max_depth = 5

draw_branch(branch_sizes, player, 90)

time.sleep(1)