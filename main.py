import tkinter as tk
from tkvideo import tkvideo

size = "1440x460"
x = 1
key = 0
right = 0
wrong = 0
i = 0


def exit_game(line):
    ex = tk.Tk()
    ex.geometry("1500x500")
    ex.configure(bg='black')
    tk.Label(ex, text=line, bg='black', foreground='white', anchor='center', font=("Arial", 25), pady=200).pack()
    ex.after(5000, lambda: exit(0))
    ex.mainloop()


# First window: START window
def start():
    start = tk.Tk()
    start.geometry(size)
    start.configure(bg='black')
    start.resizable(False, False)
    start.protocol("WM_DELETE_WINDOW", exit)

    title = "Welcome to\n Alice in wonderland"
    subtitle = "A text based adventure game based on the widely known\n children's novel by Lewis Carroll"
    tk.Label(start, text=title, bg='black', foreground='white', anchor='center', font=("Arial", 55), pady=50).pack()
    tk.Label(start, text=subtitle, bg='black', foreground='white', anchor='center', font=("Arial", 22)).pack()

    bstart = tk.Button(start, text='START', width=15, height=2, command=start.destroy)
    bstart.pack(pady=10)
    start.mainloop()
    win2()


# Second Window: Intro window
def win2():
    intro = tk.Tk()
    intro.title("WELCOME")
    intro.geometry(size)
    intro.configure(bg='black')
    intro.resizable(False, False)
    intro.protocol("WM_DELETE_WINDOW", exit)

    img = tk.PhotoImage(file="img.png")
    bg = tk.Label(intro, image=img, bd=0)
    bg.place(x=10, y=30)

    line = "Hey, Alice!!  \nYeah you.... \nYou are the main character of this story....\nLet's begin now, shall we?"
    tk.Label(intro, text=line, bg='black', foreground='white', anchor='center', font=("Arial", 20), pady=50).place(
        x=800, y=0)

    tk.Button(intro, text='YES', width=15, height=2, command=intro.destroy).place(x=1000, y=280)

    intro.mainloop()
    win3()


# Third Window: Chap 1
def win3():
    chap1 = tk.Tk()
    chap1.title("Down the rabbit hole")
    chap1.geometry(size)
    chap1.configure(bg='black')
    chap1.resizable(False, False)
    chap1.protocol("WM_DELETE_WINDOW", exit)

    img = tk.PhotoImage(file="tree.png")
    bg = tk.Label(chap1, image=img, bd=0)
    bg.place(x=0, y=5)

    line = "You are sitting on a tree,\nlistening to your sister read\nBored out of your mind.\nDistracting yourself " \
           "by making a tiara \nfor your lovely cat. "
    line1 = "And then, out of the corner or your eye, \nyou notice a rabbit, hurriedly running away.\nBut what is " \
            "weird is, he was running \non his TWO FEET! "
    line2 = "And moreover, \nHe kept glancing at his watch, \nover and over again...\nMumbling to himself about how " \
            "late he was\nWait... A WATCH??!!! "

    tk.Label(chap1, text=line, bg='black', foreground='white', anchor='center', font=("Arial", 16), pady=20).place(
        x=780, y=0)
    tk.Label(chap1, text=line1, bg='black', foreground='white', anchor='center', font=("Arial", 16)).place(
        x=750, y=150)
    tk.Label(chap1, text=line2, bg='black', foreground='white', anchor='center', font=("Arial", 16)).place(
        x=750, y=260)
    tk.Label(chap1, text="Are you Curious?", bg='black', foreground='white', anchor='center', font=("Arial", 25)).place(
        x=820, y=400)
    tk.Button(chap1, text='YES\nFollow Mr. Rabbit', command=chap1.destroy, font=("Arial", 15)).place(x=1220, y=150)
    tk.Button(chap1, text='NO\nContinue with the tiara', command=lambda: exit_game('You go back to making tiara for '
                                                                                   'your cat !'),
              font=("Arial", 15)).place(x=1200, y=220)

    chap1.mainloop()
    tran1()


# rabbit gif and tumbling gif
def tran1():
    mid1 = tk.Tk()
    mid1.geometry(size)
    mid1.title('Rabbit')
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='You follow him and enter the hole\nhe went into', bg='black', foreground='white',
             anchor='center', font=("Arial", 20), pady=5).place(x=500, y=0)
    label1 = tk.Label(mid1, bg='black', foreground='white', anchor='center')
    label1.place(x=500, y=80)
    vid = tkvideo("Rabbit and fall.mp4", label1, loop=1, size=(400, 300))
    vid.play()
    tk.Label(mid1, text='And AAAHHHHHHHHHHHHHH!!!!\nYou fall down the rabbit hole', bg='black', foreground='white',
             anchor='center', font=("Arial", 20), pady=5).place(x=500, y=380)
    mid1.after(11700, label1.destroy)
    # this will give an error, but the program will continue, if this is not there, it stops running, so don't remove

    mid1.after(12700, mid1.destroy)
    mid1.mainloop()
    win4()


# Fourth Window: Chapter 2
def win4():
    chap2 = tk.Tk()
    chap2.geometry(size)
    chap2.title("Pool of tears")
    chap2.resizable(False, False)
    chap2.protocol("WM_DELETE_WINDOW", exit)

    chap2.configure(bg='black')
    tk.Label(chap2, text='You see various shelves stacked with different things\nfloating lamps and frames and '
                         'mirrors and books\nand clocks and maps and \nfireplaces and rocking chairs?!\nand\n\nTA DUM '
                         'TSHHH !!\n\nyou are hanging upside down\nwatching Mr.Rabbit haste away', bg='black',
             foreground='white', anchor='center', font=("Arial", 20), pady=5).place(x=100, y=50)
    img = tk.PhotoImage(file="updown.png")
    bg = tk.Label(chap2, image=img, bd=0)
    bg.place(x=930, y=90)
    chap2.after(5000, chap2.destroy)
    chap2.mainloop()
    door()


# The choosing game
def door():
    global x, key
    mid1 = tk.Tk()
    mid1.geometry(size)
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='You follow him to come across a door\n You open it, and another door\nand door. And door. And '
                        'another door.\nAfter another door\neach getting smaller in size\nand hush\n you reach the '
                        'last one to finally enter a large room\nA room with walls of checkers\n\nAt the opposite end '
                        'of room, your hear a door shutting noise\n You run towards it and are met with a small '
                        'door\nSmall enough to only fit your cat through', bg='black',
             foreground='white', anchor='center',
             font=("Arial", 20)).place(x=550, y=15)
    im = tk.PhotoImage(file="doorroom.png")
    tk.Label(mid1, image=im, bd=0).place(x=90, y=90)
    mid1.after(10000, mid1.destroy)
    mid1.mainloop()

    mid2 = tk.Tk()
    mid2.geometry(size)
    mid2.configure(bg='black')
    mid2.resizable(False, False)
    mid2.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid2, text='You try twisting the knob when suddenly\nYou hear a wailing noise\nIt takes you a second to '
                        'realise that it was\nTHE DOOR\nIt asks "What can i do for you?"\nAnd you tell him that you are'
                        ' following a rabbit and\nask him to let you through\n\nHe shakes his head and says,\n"You are '
                        'simply too big. You are impassible". \nSuddenly, A table appears with a drink and a Label '
                        '"Drink me"\n also, with a cookie with a label\n"Eat me" ', bg='black',
             foreground='white', anchor='center',
             font=("Arial", 20)).place(x=25, y=15)
    im = tk.PhotoImage(file="doorknob.png")
    tk.Label(mid2, image=im, bd=0).place(x=950, y=100)
    mid2.after(10000, mid2.destroy)
    mid2.mainloop()

    chap2 = tk.Tk()
    chap2.geometry(size)
    chap2.title("Pool of tears")
    chap2.configure(bg='black')
    chap2.resizable(False, False)
    chap2.protocol("WM_DELETE_WINDOW", exit)

    img = tk.PhotoImage(file="key.png")
    tk.Button(chap2, image=img, bd=0, command=lambda: keyval()).place(x=10, y=10)
    tk.Label(chap2, text='So what do you want to do ?', bg='black', foreground='white', anchor='center',
             font=("Arial", 22)).place(x=200, y=10)
    tk.Button(chap2, text='Drink from the Bottle', bg='grey', width=50, height=2,
              command=lambda: her_size(0), font=("Arial", 20)).place(x=200, y=50)
    tk.Button(chap2, text='Eat the Cookie', bg='grey', width=50, height=2,
              command=lambda: her_size(2), font=("Arial", 20)).place(x=200, y=150)
    tk.Button(chap2, text='Try Entering', bg='grey', width=50, height=2,
              command=lambda: enter_door(), font=("Arial", 20)).place(x=200, y=250)

    def her_size(a):
        global x
        x = a
        if a == 0:
            tk.Label(chap2, text='          Oh my... You have become so tiny.        \n ', width=50, bg='black',
                     foreground='white', anchor='center', font=("Arial", 22)).place(x=250, y=370)
        if a == 2:
            tk.Label(chap2, text='Oh Goodness... You have become so huge. You start crying.\n'
                                 'Making a pool, rather a flood of tears ', bg='black', foreground='white',
                     anchor='center', font=("Arial", 22)).place(x=250, y=370)

    def keyval():
        global key
        if x == 0:
            tk.Label(chap2, text='           You are too small to reach        \n    ', bg='black', foreground='white',
                     width=50, anchor='center', font=("Arial", 22)).place(x=250, y=370)
        else:
            key = 1
            tk.Label(chap2, text='                               Got the key                      \n   ', bg='black',
                     foreground='white', anchor='center', width=50, font=("Arial", 22)).place(x=250, y=370)

    def enter_door():
        global key
        if key == 1 and x == 0:
            chap2.destroy()
        elif key == 0:
            tk.Label(chap2, text='                                 No key                      \n      ', bg='black',
                     foreground='white', width=50, anchor='center', font=("Arial", 22)).place(x=250, y=370)
        elif x == 1 or x == 2:
            tk.Label(chap2, text='Too big to pass. Cannot enter\n', bg='black', foreground='white', anchor='center',
                     font=("Arial", 22), width=50).place(x=250, y=370)

    chap2.mainloop()
    tran2()


# The race chapter, the one with dodo
def tran2():
    mid1 = tk.Tk()
    mid1.geometry(size)
    mid1.title('The Caucus Race and the Long tale')
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='You get through the room to end up \nin a flood that you have caused.\n'
                        'You see a Dodo floating on the water and call out for help\n'
                        'As you are almost drowning.\nJust then you see the dodo standing on a rock \nand other animals'
                        ' and birds \nrunning in circles around the rock.\nEvery now and then a wave engulfing them\n'
                        'You get washed onto the bank and inevitably into the race\nA race you understand to be the '
                        'race to get dry\nWhich is impossible to attain with everyone running in circles\nAnd the '
                        'waves periodically making them wet all over again.\nYou try to tell the dodo,\nbut he calls '
                        'Nonsense and keeps the race going', bg='black', foreground='white',
             anchor='center', font=("Arial", 19), pady=5).place(x=680, y=20)
    img = tk.PhotoImage(file="dodo.png")
    bg = tk.Label(mid1, image=img, bd=0)
    bg.place(x=30, y=50)
    mid1.after(17000, mid1.destroy)
    mid1.mainloop()

    mid2 = tk.Tk()
    mid2.geometry(size)
    mid2.title('The Caucus Race and the Long tale')
    mid2.configure(bg='black')
    mid2.resizable(False, False)

    tk.Label(mid2, text='Just then you see the rabbit in an upside down umbrella\ngetting washed up at the bank.\n'
                        'You call out to him, "Mr. Rabbit!!"\nAnd he just runs off, still hurrying and cursing \nabout '
                        'how late he was.\n\nYou ditch the race and follow the rabbit \ninto the dark forest '
                        'still calling out for him\n\n"Mr. Rabbit", you pause\n"Oh, Mr. Rabbit".',
             bg='black', foreground='white', anchor='center', font=("Arial", 20), pady=5).place(x=30, y=30)
    label1 = tk.Label(mid2, bg='black', foreground='white', anchor='center')
    label1.place(x=720, y=20)
    vid = tkvideo("dodo.mp4", label1, loop=1, size=(800, 400))
    vid.play()
    mid2.after(23000, mid2.destroy)
    mid2.mainloop()
    forest()


# Tweedledee Tweedledum
def forest():
    mid1 = tk.Tk()
    mid1.title('The Rabbit sends a Little bill')
    mid1.geometry(size)
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    # mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='You search for him behind the tree, the bushes\nYou crawl inside a log searching for him\n'
                        'Just as you exit the log, you turn around and\n"Oh my!", you get startled.\n\nYou come face to'
                        ' face with two same looking short, stout twins.\n"Tweedle Dee and Tweedle Dum", you read off '
                        'of their collars.\nYou greet them,"Well, it was nice to meet you both,\nbut I need to take'
                        ' your leave.\nI am following Mr. Rabbit, you see."\n\nYou try to leave but they stop you to '
                        'shake hands.\n\nYou try to leave again, but they stop you again.\n"We just started talking",'
                        ' they say,"You can\'t leave yet !\nThe visiting just started"', bg='black', foreground='white',
             anchor='center', font=("Arial", 18), pady=5).place(x=690, y=3)
    img = tk.PhotoImage(file="tweedle.png")
    bg = tk.Label(mid1, image=img, bd=0)
    bg.place(x=10, y=5)
    mid1.after(12000, mid1.destroy)
    mid1.mainloop()

    mid2 = tk.Tk()
    mid2.title('The Rabbit sends a Little bill')
    mid2.geometry(size)
    mid2.configure(bg='black')
    mid2.resizable(False, False)
    # mid2.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid2, text='"Would you like to play hide and seek?",they ask.\n"Or maybe Button, Button, Who\'s got the '
                        'button?\nIf you stay long enough we might have a battle!"\n "That\'s very kind of you! But I'
                        ' must leave.\n I am following the white Rabbit I\'m curious", you say.\n But they still try '
                        'to stop.\n"Curious?!\nthere was another someone who was curious...\nThe oysters towards the '
                        'walrus...\nAnd you know what happened?......",\nthey start with a story\n'
                        '\nIf you wanna leave, try escaping the game in the next 30 seconds ,\n before they catch up '
                        'with you\n or else you\'ll never get to leave!',
             bg='black', foreground='white', anchor='center', font=("Arial", 19), pady=3).place(x=70, y=15)
    img = tk.PhotoImage(file="deedum.png")
    bg = tk.Label(mid2, image=img, bd=0)
    bg.place(x=1000, y=70)

    mid2.after(13000, mid2.destroy)
    mid2.mainloop()

    import math
    import turtle

    window = turtle.Screen()
    window.bgcolor('black')
    window.title('Maze')
    window.setup(900, 700)

    turtle.register_shape("alice.gif")
    turtle.register_shape("treewall.gif")

    # Create Pen : whatever a turtle can do like move and shit
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape('treewall.gif')
            self.color('white')
            self.penup()
            self.speed(0)

    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape('alice.gif')
            self.color('blue')
            self.penup()
            self.speed(0)

        def go_up(self):
            move_to_x = player.xcor()
            move_to_y = player.ycor() + 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(self.xcor(), self.ycor() + 24)

        def go_down(self):
            move_to_x = player.xcor()
            move_to_y = player.ycor() - 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(self.xcor(), self.ycor() - 24)

        def go_left(self):
            move_to_x = player.xcor() - 24
            move_to_y = player.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(self.xcor() - 24, self.ycor())

        def go_right(self):
            move_to_x = player.xcor() + 24
            move_to_y = player.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(self.xcor() + 24, self.ycor())

        def is_collision(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 5:
                return True
            else:
                return False

    class Out(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('square')
            self.color('yellow')
            self.penup()
            self.speed(0)
            self.goto(x, y)

        def destroy(self):
            self.hideturtle()
            turtle.bye()
            house()

    levels = [""]
    level_1 = [
        " XXXXXXXXXXXXXXXXXXXXXXXXXX",
        " X    XX  XXX   XXXXX     O",
        " XXX          X      XX  XX",
        " X X X    XXX XXXXX  XX  X ",
        " X X XXX  X    X         X ",
        " X X   XXXXX  XX    XXXXXX ",
        " X XXX  X X  XXXXXX XXXX X ",
        " X   X XX X X    X       X ",
        " X  XX X  X X XXXX XX    X ",
        " X X   XX X X      XXXXX X ",
        " X XX   X X         XXXX X ",
        " X XXXX   XXXXX XX  XXXX X ",
        " X        X     XX       X ",
        " XXXXXX   XXX XXXXXXX    X ",
        " X                  X  X X ",
        " X XXXXX  XX  XXXXXXX  X X ",
        " X X   X  X   X  X     X X ",
        " X X      X   X  X  X   XX ",
        " X XXXXXXXX   X     X  X X ",
        " X          XXXXXXX XXXX X ",
        " XXXXXXX                 X ",
        " X       XXXXXX XXXXXXXXXX ",
        "XX  XXXXXXXXXXX XXXXXXXXXX ",
        "P                      XXX ",
        "XXXXXXXXXXXXXXXXXXXXXXXXXX "]

    levels.append(level_1)

    def setup_maze(level):
        for rows in range(len(level)):
            for columns in range(len(level[rows])):
                character = level[rows][columns]
                screen_column = -288 + (columns * 24)
                screen_row = 288 - (rows * 24)

                if character == 'X':
                    pen.goto(screen_column, screen_row)
                    pen.stamp()
                    walls.append((screen_column, screen_row))

                if character == 'P':
                    player.goto(screen_column, screen_row)

                if character == 'O':
                    outs.append(Out(screen_column, screen_row))

    pen = Pen()
    player = Player()

    outs = []

    walls = []

    setup_maze(levels[1])

    turtle.listen()
    turtle.onkey(player.go_up, 'Up')
    turtle.onkey(player.go_down, 'Down')
    turtle.onkey(player.go_left, 'Left')
    turtle.onkey(player.go_right, 'Right')

    window.tracer(0)

    temp = tk.Tk()
    temp.geometry("0x0")
    temp.overrideredirect(1)
    temp.configure(bg='black')
    temp.after(30000, turtle.bye)
    # temp.after(30001, lambda: exit_game('Oh no! They caught you...\nYou won\'t ever be able to escape them now'))
    temp.after(30002, temp.destroy)

    while True:
        for out in outs:
            if player.is_collision(out):
                out.destroy()
                outs.remove(out)
                temp.destroy()
                break

        window.update()
    temp.mainloop()


# Gloves game
def house():
    mid1 = tk.Tk()
    mid1.geometry(size)
    mid1.title('The Rabbit Sends a Little Bill')
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='Just as you exit the forest, you come across a house.\nYou wonder whose house it might be.  '
                        'Just then... \nThe rabbit opens the window and starts calling out\n"Marianne ! Marianne ! '
                        'Marianne !"\n"The rabbit !", You exclaim.\nJust when you are about to knock on the door,...\n'
                        'The rabbit rushes out... running out of the gate.\nYou call him out and he turns around...\n'
                        'And suddenly\n\nSTARTS SHOUTING !\n\n"Why, Marianne! What are you doing out HERE ??!"',
             bg='black', foreground='white', anchor='center', font=("Arial", 20), pady=5).place(x=630, y=10)
    img = tk.PhotoImage(file="house1.png")
    bg = tk.Label(mid1, image=img, bd=0)
    bg.place(x=30, y=30)
    mid1.after(12000, mid1.destroy)
    mid1.mainloop()

    mid2 = tk.Tk()
    mid2.geometry(size)
    mid2.configure(bg='black')
    mid2.resizable(False, False)
    mid2.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid2, text='"Marianne ?!!",\nWho is Marianne, you think to yourself...\nSuddenly he is making you rush '
                        'inside the house.\n"Don\'t just be standing there !! Go get my Gloves", he orders...\n'
                        '"I AM ALREADY LATE !"\n\n"But late for what? That\'s just what I-",\nHe cuts you off '
                        'midsentence... almost pushing you into the house\n\n"Goodness !",you think, \n"I '
                        'suppose I\'ll be taking orders from him now !"\n\n',
             bg='black', foreground='white', anchor='center', font=("Arial", 19)).place(x=75, y=30)
    im = tk.PhotoImage(file="house2.png")
    tk.Label(mid2, image=im, bd=0).place(x=900, y=30)
    mid2.after(10000, mid2.destroy)
    mid2.mainloop()

    tran3()


# Caterpillar and Flowers
def tran3():
    mid1 = tk.Tk()
    mid1.geometry(size)
    mid1.title('Advice from a Caterpillar')
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='Just as you bring the gloves out, he snatches it out of your hand\nAnd sprints down the road.'
                        '\nIt takes you about two seconds to realize he ran away\nAnd you follow him down the path as '
                        'well\nYou come across a beautiful forest of huge flowers\nYou enter, and see "Butterflies !"\n'
                        '"You mean Bread butterflies?"\n\n Huh?! who said that ?!\nYou turn around and see Nothing but '
                        'flowers\n\'Was it the flower?\',you think... But brush it off\nmumbling, "It\'s not possible"'
                        '\n"Oh, But it is ! " the rose bends forward to say\nAnd the tulips retort,"We Sing too !\n'
                        'And thus begins a musical of flowers just singing',
             bg='black', foreground='white', anchor='center', font=("Arial", 19), pady=5).place(x=620, y=10)
    img = tk.PhotoImage(file="flowers.png")
    bg = tk.Label(mid1, image=img, bd=0)
    bg.place(x=30, y=30)
    mid1.after(12000, mid1.destroy)
    mid1.mainloop()

    mid2 = tk.Tk()
    mid2.geometry(size)
    mid2.configure(bg='black')
    mid2.resizable(False, False)
    mid2.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid2, text='You slip out of the musical, and walk down the path to come across\nanother song just breezing'
                        ' through the wind.\n\nYou follow the voice\nonly to come face to face with a caterpillar\nwho '
                        'appears to be smoking puffs of smoke\nSurprisingly in the shapes of letters,\njust relaxing on'
                        ' a branch, singing by himself...\n\nYou go up to talk to him, but he keeps on smoking directly'
                        ' on your face\n\n Annoyed, you leave him be and continue\nYour journey to find Mr.Rabbit',
             bg='black', foreground='white', anchor='center', font=("Arial", 19)).place(x=75, y=15)
    im = tk.PhotoImage(file="caterpillar.png")
    tk.Label(mid2, image=im, bd=0).place(x=900, y=30)
    mid2.after(10000, mid2.destroy)
    mid2.mainloop()

    mid3 = tk.Tk()
    mid3.geometry(size)
    mid3.title('Advice from a Caterpillar')
    mid3.configure(bg='black')
    mid3.resizable(False, False)
    mid3.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid3, text='You come at a crossroad...\n confused where to go...\n Just then you hear someone else\n'
                        'Singing...Again\n\nYou follow the voice and meet a cheshire cat\n The creepiest one you have '
                        'ever see\nAnd after an elaborate singing chorus and confusing answers\n to your rather simple '
                        'Question,\'Where to go further?\'...\nHe finally points you towards the Mad Hatter.\nWho'
                        ' supposedly knows where the rabbit would go\n\nHe disappears but his grin remains behind to '
                        'float on its own in the air\n prompting you to remark that \nyou have often seen a cat without'
                        ' a grin...\n but never a grin without a cat.',
             bg='black', foreground='white', anchor='center', font=("Arial", 18), pady=5).place(x=620, y=5)
    img = tk.PhotoImage(file="cat.png")
    bg = tk.Label(mid3, image=img, bd=0)
    bg.place(x=30, y=30)
    mid3.after(9000, mid3.destroy)
    mid3.mainloop()

    win5()


# Mad Hatter
def win5():
    mid1 = tk.Tk()
    mid1.geometry(size)
    mid1.title('A Mad Tea-Party')
    mid1.configure(bg='black')
    mid1.resizable(False, False)
    mid1.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid1, text='You follow the cat\'s instructions and go to the Mad Hatter\'s house.\n You enter the house, '
                        'and stumble upon a table full of steaming hot teapots,\nthe steam barely letting you see '
                        'anything further\nYou squat and squint to see between the pots\n and what do you see?\nA hare '
                        'and the Hatter along with \na very tired looking Dormouse, having a Party...\npresumably, a '
                        'Birthday party\n you give a round of applause, just after their singing ends\nAnd they finally'
                        ' notice you...\n\n You all start talking... It\'s a Tea Party, you understand\nBut they barely'
                        ' let you put in a word.\nEvery time you start to say something\nThey "Move on"',
             bg='black', foreground='white', anchor='center', font=("Arial", 19), pady=5).place(x=580, y=10)
    img = tk.PhotoImage(file="madhat.png")
    bg = tk.Label(mid1, image=img, bd=0)
    bg.place(x=30, y=30)
    mid1.after(20000, mid1.destroy)
    mid1.mainloop()

    mid2 = tk.Tk()
    mid2.geometry(size)
    mid2.title('A Mad Tea-Party')
    mid2.configure(bg='black')
    mid2.resizable(False, False)
    mid2.protocol("WM_DELETE_WINDOW", exit)

    tk.Label(mid2, text='Just when you are annoyed and about to leave,\n Mr.Rabbit joins the party\nor rather tries to '
                        'rush through it, still late, you think\nThe hare and Hatter catch him though\n and through a '
                        'series of elaborate debacles,\nmanage to break and ruin Mr.Rabbit\'s watch rather '
                        'spectacularly...\n\n You along with Mr. Rabbit want to leave,\nBut for that... You\'ll have to'
                        ' answer at least 3\n out of the five riddles asked...\n\n Let\'s Dive into it',
             bg='black', foreground='white', anchor='center', font=("Arial", 20)).place(x=35, y=15)
    im = tk.PhotoImage(file="watch.png")
    tk.Label(mid2, image=im, bd=0).place(x=900, y=30)
    mid2.after(7000, mid2.destroy)
    mid2.mainloop()

    global i, right, wrong

    q1 = 'What has a face and two hands, but has no arms or legs?'
    a1 = 'a clock'
    q2 = 'What begins with T, ends with T, and has T in it?'
    a2 = 'a teapot'
    q3 = 'When is a door not a door?'
    a3 = 'when it is a jar'
    q4 = 'I go in hard. I come out soft. You blow me hard. What am I?'
    a4 = 'gum'
    q5 = 'I have keys but no locks. I have a space but no room. \nYou can enter, but you can’t go outside. What am I?'
    a5 = 'a keyboard'

    ques = [q1, q2, q3, q4, q5]
    ans = [a1, a2, a3, a4, a5]

    mid3 = tk.Tk()
    mid3.geometry(size)
    mid3.title('Advice from a Caterpillar')
    mid3.configure(bg='black')
    mid3.resizable(False, False)
    mid3.protocol("WM_DELETE_WINDOW", exit)

    que = tk.StringVar()
    answer = tk.StringVar()
    r, w = tk.StringVar(), tk.StringVar()
    r.set(str(right))
    w.set(str(wrong))

    que.set(ques[i])

    def check():
        global i, right, wrong
        ans1 = answer.get()
        ans1 = ans1.lower()
        if i < 5:
            if ans1 == ans[i]:
                right = right + 1
                r.set(str(right))
                tk.Label(mid3, text='You Got it right  ', bg='black', foreground='white', anchor='center',
                         font=("Arial", 16)).place(x=600, y=325)
            else:
                wrong = wrong + 1
                w.set(str(wrong))
                tk.Label(mid3, text='You Got it wrong', bg='black', foreground='white', anchor='center',
                         font=("Arial", 16)).place(x=600, y=325)
            i = i + 1
        if i == 5:
            if right >= 3:
                mid3.destroy()
                last()
            else:
                mid3.destroy()
        que.set(ques[i])
        answer.set('')

    tk.Button(mid3, text='Check', command=lambda: check()).place(x=650, y=300)
    tk.Label(mid3, text='Right Answers : ', bg='black', foreground='white', anchor='center',
             font=("Arial", 20)).place(x=1100, y=100)
    tk.Label(mid3, text='Right Answer : ', textvariable=r, bg='black', foreground='white', anchor='center',
             font=("Arial", 20)).place(x=1300, y=100)
    tk.Label(mid3, textvariable=que, bg='black', foreground='white', anchor='center', font=("Arial", 20)).place(x=350,
                                                                                                                y=50)
    tk.Entry(mid3, textvariable=answer, width=30, bg='grey', font=20,
             justify="center").place(x=520, y=160, height=60)
    mid3.mainloop()


# Meet the rabbit and win
def last():
    ex = tk.Tk()
    ex.geometry("1500x500")
    ex.configure(bg='black')
    tk.Label(ex, text='CONGRATULATIONS\nYou finally met Mr. rabbit\nYou won the game', bg='black', foreground='white',
             anchor='center', font=("Arial", 25), pady=200).pack()
    ex.after(5000, lambda: exit(0))
    ex.mainloop()


start()
