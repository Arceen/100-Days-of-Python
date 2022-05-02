# Day 6 - Functions, while loops and karel the robot

# print('Hello')

# def my_function():
#     print("hello")
#     print("bye")

# my_function()

# Reeborg's World
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_opposite():
#     turn_left()
#     turn_left()
# def move_more(steps):
#     for i in range(steps):
#         move()
# def build_wall_more(length):
#     for i in range(length):
#         build_wall()
#         turn_left()
#         move()
#         turn_right()
# move_more(3)
# build_wall_more(4)

# def draw_square(length):
#     for _ in range(length):
#         move_more(length)
#         turn_left()

# draw_square(5)       

# Reeborg's world - Hurdle - 1, 2 & 3 -Solve
# def move_more_check_right():
#     while front_is_clear() and wall_on_right():
#         move()
# def jump_hurdle(length):
#     turn_left()
#     move_more_check_right()
#     turn_right()
#     move()
#     turn_right()
#     move_more_check_right()
#     turn_left()
# def race():
#     while not at_goal():
#         if front_is_clear():
#             move()
#         else:
#             jump_hurdle()

# race()

# Day 6 - Project - Reeborg's world - Maze

# def solve_maze():
#     while not at_goal():
#         if right_is_clear():
#             turn_right()
#             move()
#         elif front_is_clear():
#             move()
#         else:
#             turn_left()
            