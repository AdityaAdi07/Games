import turtle
import pandas

is_game= True
cross= turtle.Turtle()
data= pandas.read_csv('50_states.csv')
screen= turtle.Screen()
screen.title('U.S STATES')
screen.bgcolor('black')
crosshair= 'blank_states_img.gif'
screen.addshape(crosshair) #creating the shape req
turtle.shape(crosshair) #adding tht instead of tutrtle/square/rectangle


def check_state(ans_state):
    if ans_state in data['state'].values: # most imp here checking if answer value is in csv column of 'state'
        row= data[data['state']== ans_state] # going to tht row where ans_state cell is present
        x_cor= row['x'].values[0] # acessing the req ele frm abv row, [0] for taking 1st element
        y_cor= row['y'].values[0]
        return x_cor,y_cor




# def get_mouse_click_coord(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coord)
# not req coz already there
a=0
guessed_state=[]
missing_state=[]
while is_game:
    for sates in data['state']:
        if sates not in guessed_state:
            missing_state.append(sates)

    answer_state= screen.textinput(f'Guess the state {a}/50', "What is the name of the state?")
    if answer_state in data['state'].values:
        cross.penup()# always create new cross=turtle.Turtle() so it doesnt reset into new one so image moves
        cross.hideturtle()
        cross.goto(check_state(answer_state))
        cross.pendown()
        cross.write(f'{answer_state}')
        guessed_state.append(answer_state)
        a+=1
    elif answer_state== 'exit':
        is_game= False
        print(f'All guessed states are {guessed_state}')
        print(f'Remaing ones are {missing_state}')
    else:
        is_game= True


#screen.exitonclick(),  because here we dont want to exit on click
turtle.mainloop()