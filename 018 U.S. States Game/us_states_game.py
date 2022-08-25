"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""

import turtle
import pandas as pd
from coord_selector import get_gif_size

SAVE_CSV = 'states_to_learn.csv'

window = turtle.Screen()
window.title('U.S. States Game')
image = 'blank_states_img.gif'
size = get_gif_size(image)
window.setup(size[0], size[1])
window.addshape(image)
turtle.shape(image)
window.tracer(0)

data = pd.read_csv('50_states.csv')
state_lst = []

while True:
    window.update()

    if (answer := window.textinput(title=f'{len(state_lst)}/50 Guess the State',
                                   prompt='What\'s another state\'s name?')) is None:
        pd.DataFrame([state for state in data.state if state not in state_lst],
                     columns=['states_to_learn']).to_csv(SAVE_CSV)
        quit()

    for state in data.state:
        if state in answer.title() and state not in state_lst:
            state_lst.append(state)
            state_turtle = turtle.Turtle()
            state_turtle.ht()
            state_turtle.pu()
            state = data[data.state == answer.title()]
            state_turtle.setpos(int((data.loc[data.state == answer.title(), 'x'])),
                                int((data.loc[data.state == answer.title(), 'y'])))
            state_turtle.write(f'{answer.title()}', align='center', font=('Arial', 6, 'bold'))

        if len(state_lst) >= 50:
            break
        if answer.lower() in ('e', 'exit', 'q', 'quit', 's', 'stop'):
            pd.DataFrame([state for state in data.state if state not in state_lst],
                         columns=['states_to_learn']).to_csv(SAVE_CSV)
            window.bye()
            quit()
    else:
        continue
    break

pd.DataFrame([state for state in data.state if state not in state_lst], columns=['states_to_learn']).to_csv(SAVE_CSV)

window.mainloop()

