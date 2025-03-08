from tkinter import *
import random

GAME_WIDTH = 576
GAME_HEIGHT = 576
SPEED = 50
SPACE_SIZE = 12
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    pass

class Food:
    def __init__(self, canvas):
        self.canvas = canvas

        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE


        self.coordinates = [x,y]

        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class App:
    def __init__(self, master=NONE):
        
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("576x720")

        self.tela_inicial()

    def tela_inicial(self):


        #Título
        self.widget1 = Frame(self.master)
        self.widget1.pack()
        self.titulo = Label(self.widget1, text= "Snake Game 1.0")
        self.titulo["font"] = ["Arial", "12", "italic", "bold"]
        self.titulo.pack()

    

        #Botão jogar e sair
        self.btnPlay = Button(self.widget1, text="Play", width=5)
        self.btnPlay["font"] = ["Calibri", "10"]
        self.btnPlay["command"] = self.iniciar_game
        # self.btnPlay.bind("<Button-1>", self.mudarTexto)

        self.btnExit = Button(self.widget1, text="Exit", width=5)
        self.btnExit["font"] = ["Calibri", "10"]
        self.btnExit["command"] = self.widget1.quit
        # self.exit.config(bg= "red")
        
        self.btnPlay.pack(side= LEFT)
        self.btnExit.pack(side= RIGHT)




    def iniciar_game(self):
        self.widget1.destroy()

        self.score = 0
        direction = 'down'
        
        self.label = Label(self.master, text= "Score:{}".format(self.score), font=('consolas', 40))
        self.label.pack()

        self.canvas = Canvas(self.master, bg= BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_HEIGHT)
        self.canvas.pack()

       

        # window_width = self.widget1.winfo_width()
        # window_height = self.widget1.winfo_height()
        # screen_width = self.widget1.winfo_screenwidth()
        # screen_height = self.widget1.winfo_screenheight()

        # x = int((screen_width/2) - (window_width/2))
        # y = int((screen_height/2) - (window_height/2))


        # self.snake = Snake()
        self.food= Food(self.canvas)





app = Tk()
App(app)





app.mainloop()

