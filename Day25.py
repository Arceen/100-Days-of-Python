# Day 25 - working with csv and analysing data with pandas
import pandas
import csv
# file = pandas.read_csv('Day25_weather_data.csv', sep=",")
# print(file)
# with open("Day25_weather_data.csv") as f:
#     data = [i.strip() for i in f.readlines()]
# print(data)


# with open("Day25_weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
    
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

# file = pandas.read_csv('Day25_weather_data.csv', sep=",")
# print(file['temp'])


# States game
import turtle

df = pandas.read_csv('Day25_50_states.csv')
screen = turtle.Screen()
screen.title("States Game")
image = 'Day25_blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.listen()
writer = turtle.Turtle()
writer.hideturtle()
writer.pu()
guessed_states = []
state_count = 0
exit = False
while not exit and state_count<50:
    state = turtle.textinput(f"{state_count}/50 States Correct", "What's another state name?").title()
    if state == 'Exit':
        with open('Day25_missed_states.txt', 'w') as f:
            missed_states = df[~df.state.isin(guessed_states)].state.values
            for i in missed_states:
                f.write(i+'\n')
        # print(missed_states.state.values)    
        exit = True
        continue
        
    selected = df[df.state==state]
    # print(selected)
    # print(selected['x'].values[0])
    # guessed_states+=1
    if len(selected) == 1:
        state_count += 1
        guessed_states.append(state)
        writer.goto(int(selected.x), int(selected.y))
        writer.write(f'{selected["state"].values[0]}', move=True)
        
screen.exitonclick()






