'''
Created on Aug 14, 2018
@author: Burkhard A. Meier
'''


import tkinter as tk
from PIL import Image, ImageTk
import turtle
import math


# define screen size
SCREEN_WIDTH = 1100         # adjust sizes to fit your screen
SCREEN_HEIGHT = 700

GAME_AREA_START_X = -((SCREEN_WIDTH // 2) -50)
GAME_AREA_START_Y = -((SCREEN_HEIGHT // 2) -50)

BORDER_WIDTH = SCREEN_WIDTH -100
BORDER_HEIGHT = SCREEN_HEIGHT -100

FINISH_LINE = 0, -232           # Turtle: tuple coords defining the finish line 
SCORE = 0                       # keep track of score between our two classes


class GameArea(turtle.RawTurtle):               # inherent/extend RawTurtle
    def __init__(self, tk_canvas):
        super().__init__(tk_canvas)             # initialize the super class (RawTurtle)
        self.tk_canvas = tk_canvas
        self.hideturtle()                       # hide the RawTurtle
        screen = self.getscreen()         
        screen.bgcolor('gray')
        screen.tracer(2)                        # delay drawing by two frames
        self.draw_game_area()
        self.draw_race_track()
        self.draw_score()
        self.add_score()
        self.draw_finish_line()
        self.draw_finish_label()
        screen.update()                         # update the screen

    def draw_score(self):
        score_pen = turtle.RawTurtle(self.tk_canvas)
        score_pen.setundobuffer(None) 
        score_pen.hideturtle()
        score_pen.speed(0)   
        score_pen.color('white')
        score_pen.penup() 
        score_pen.setpos(-100, 0) 
        score_string = "Score: "
        score_pen.write(score_string, align='left', font=('Arial', 24, 'bold'))        # turtle write method and font tuple
        
    def add_score(self):
        self.score_pen = turtle.RawTurtle(self.tk_canvas)
        self.score_pen.setundobuffer(None) 
        self.score_pen.hideturtle()
        self.score_pen.speed(0)   
        self.score_pen.color('orange')
        self.score_pen.penup() 
        self.score_pen.setpos(20, 0) 
        self.score_pen.write(SCORE, align='left', font=('Arial', 24, 'bold'))       # use global SCORE variable      

    def draw_game_area(self):
        area_turtle = turtle.RawTurtle(self.tk_canvas)
        area_turtle.setundobuffer(None)                             # no undo buffer to speed up the drawing
        area_turtle.hideturtle()
        area_turtle.speed(0)                                        # 0 is the fastest
        area_turtle.color('black', 'green')                         # pencolor, fillcolor
        area_turtle.penup()                                         # don't draw while moving into position
        area_turtle.setpos(GAME_AREA_START_X, GAME_AREA_START_Y)    # left bottom
        area_turtle.pendown()                                       # now start drawing
        area_turtle.pensize(4)
        
        area_turtle.begin_fill()                    # start filling in the game area
        for _border in range(2):
            area_turtle.fd(BORDER_WIDTH)
            area_turtle.lt(90)
            area_turtle.fd(BORDER_HEIGHT)
            area_turtle.lt(90)
        area_turtle.end_fill()

        
    def draw_race_track(self):
        race_track_pen = turtle.RawTurtle(self.tk_canvas)
        race_track_pen.setundobuffer(None)                             
        race_track_pen.hideturtle()
        race_track_pen.speed(0)                                                             
        race_track_pen.pensize(3)
        
        # --------------------------------------------------------------------------------
        race_track_pen.penup()                                         
        race_track_pen.setpos(GAME_AREA_START_X + 70,           # outer line of race track
                              GAME_AREA_START_Y + 20)                  
        race_track_pen.pendown()                                       
        
        race_track_pen.color('white', 'black')  
        race_track_pen.begin_fill()                    
        for _track in range(2):
            race_track_pen.forward(BORDER_WIDTH - 140)
            race_track_pen.circle(50, 90)
            race_track_pen.forward(BORDER_HEIGHT - 140)
            race_track_pen.circle(50, 90)
        race_track_pen.end_fill()  
        
        # --------------------------------------------------------------------------------  
        race_track_pen.penup()
        race_track_pen.setpos(GAME_AREA_START_X + 70 + 40,          # inner line of race track
                              GAME_AREA_START_Y + 20 + 40)                          
        race_track_pen.pendown()                                       

        race_track_pen.color('white', 'green')                  
        race_track_pen.begin_fill() 
        for _track in range(2):
            race_track_pen.forward(BORDER_WIDTH - 220)
            race_track_pen.circle(50, 90)
            race_track_pen.forward(BORDER_HEIGHT - 220)
            race_track_pen.circle(50, 90)                
        race_track_pen.end_fill()

        # --------------------------------------------------------------------------------
        race_track_pen.penup()                                         
        race_track_pen.setpos(GAME_AREA_START_X + 70 + 18,           # center line of race track
                              GAME_AREA_START_Y + 20 + 20)                  

        race_track_pen.color('white')  
                  
        for _track in range(2):
            for _center_line in range((BORDER_WIDTH - 160) // 40):
                race_track_pen.pendown()
                race_track_pen.forward(20)
                race_track_pen.up()
                race_track_pen.forward(20)
                             
            race_track_pen.pendown()    
            race_track_pen.circle(20, 45)
            race_track_pen.up()
            race_track_pen.forward(15)
            race_track_pen.pendown()
            race_track_pen.circle(20, 45)
            race_track_pen.up()
            race_track_pen.forward(20)

            for _center_line in range((BORDER_HEIGHT - 140) // 40):
                race_track_pen.pendown()
                race_track_pen.forward(20)
                race_track_pen.up()
                race_track_pen.forward(20)

            race_track_pen.pendown()    
            race_track_pen.circle(20, 45)
            race_track_pen.up()
            race_track_pen.forward(10)
            race_track_pen.pendown()
            race_track_pen.circle(20, 45)
            race_track_pen.up()
            race_track_pen.forward(20)

        # --------------------------------------------------------------------------------
        race_track_pen.penup()                                         
        race_track_pen.setpos(GAME_AREA_START_X + 70,           # color outer line of race track
                              GAME_AREA_START_Y + 20)                  
        race_track_pen.pendown()                                       
                 
        race_track_pen.pensize(6)
        for _track in range(2):
            race_track_pen.pendown()
            for _red_line in range((BORDER_WIDTH - 140) // 30):
                race_track_pen.color('red') 
                race_track_pen.forward(15)
                race_track_pen.color('white') 
                race_track_pen.forward(15)            
            
#             race_track_pen.up()
            race_track_pen.color('red')             # color curves red
            race_track_pen.forward(20)              # adjustment          
            race_track_pen.circle(50, 90)
            
            race_track_pen.pendown()
            for _red_line in range((BORDER_HEIGHT - 140) // 30):
                race_track_pen.color('red') 
                race_track_pen.forward(15)
                race_track_pen.color('white') 
                race_track_pen.forward(15)            
            
            race_track_pen.back(11)                 # adjustment
#             race_track_pen.up()
            race_track_pen.color('red')             # color curves red
            race_track_pen.forward(20)                   
            race_track_pen.circle(50, 90)
 
        # --------------------------------------------------------------------------------
        race_track_pen.penup()                                         
        race_track_pen.setpos(GAME_AREA_START_X + 70 + 40,           # color inner line of race track
                              GAME_AREA_START_Y + 20 + 40)                  
        race_track_pen.pendown()                                       
        
        race_track_pen.pensize(6)
        for _track in range(2):
            race_track_pen.pendown()
            for _red_line in range((BORDER_WIDTH - 220) // 30):
                race_track_pen.color('red') 
                race_track_pen.forward(15)
                race_track_pen.color('white') 
                race_track_pen.forward(15)            

            race_track_pen.color('red')
            race_track_pen.circle(50, 90)
            
            race_track_pen.pendown()
            for _red_line in range((BORDER_HEIGHT - 220) // 30):
                race_track_pen.color('red') 
                race_track_pen.forward(15)
                race_track_pen.color('white') 
                race_track_pen.forward(15)            
            
            race_track_pen.color('red')
            race_track_pen.forward(20)             
            race_track_pen.circle(50, 90)    
    
    
    def draw_finish_line(self):
        finish_line_pen = turtle.RawTurtle(self.tk_canvas)
        finish_line_pen.setundobuffer(None) 
        finish_line_pen.hideturtle()
        finish_line_pen.speed(0)
        finish_line_pen.penup() 
        
        finish_line_pen.setpos(FINISH_LINE)  
        finish_line_pen.pensize(18)
        finish_line_pen.setheading(270)
        for _line in range(4):
            finish_line_pen.down()
            finish_line_pen.color('black')
            finish_line_pen.forward(6)
            finish_line_pen.color("white")
            finish_line_pen.forward(6)

    def draw_finish_label(self):
        finish_label_pen = turtle.RawTurtle(self.tk_canvas)
        finish_label_pen.setundobuffer(None) 
        finish_label_pen.hideturtle()
        finish_label_pen.speed(0)   
        finish_label_pen.color('white')
        finish_label_pen.penup() 
        finish_label_pen.setpos(-50, -220) 
        finish_label_string = "Finish Line"
        finish_label_pen.write(finish_label_string, align='left', font=('Arial', 14, 'bold'))        
     
 
        

class CanvasAndCar():
    def __init__(self, win):
        self.canvas = tk.Canvas(win, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)      # create a tkinter canvas
        self.canvas.pack()                                                          # use the pack() manager
        
    def after_turtle_game_area_creation(self):
        self.car_pos_x = -360            # position car closer to the racing track 
        self.car_pos_y = 260             # turtle screen coords are 0,0 in center  
  
        self.img_file = 'car.png'                               # our .png image file located in the same folder as this .py file     
        self.angle = -90      
                 
        win.bind('<Key-Left>', self.turn_left)                  # bind arrow keys to methods
        win.bind('<Key-Right>', self.turn_right)
        win.bind('<Key-Up>', self.drive_forward)
        win.bind('<Key-Down>', self.drive_backward)
        
        self.place_car()                                        # call the method to position the car

    def place_car(self):
        global SCORE
        image = Image.open(self.img_file)                                           # open the image
        self.car_image = ImageTk.PhotoImage(image.rotate(self.angle))               # pass the image into PhotoImage. Use self.car_image or image might not show
        self.car_canvas = self.canvas.create_image(self.car_pos_x, self.car_pos_y,
                                                   image=self.car_image)         

        if 250 <= int(self.car_pos_y) <= 280:
#             print(self.car_pos_x, self.car_pos_y)
            if -8 <= int(self.car_pos_x) <= 0:
                print('car crossed the finish line!')
                game_area.score_pen.clear()
                SCORE += 1000                       # use global SCORE variable   
                game_area.add_score()
                
                
    def turn_left(self, _event):
        self.angle += 10
        self.place_car()
        
    def turn_right(self, _event):
        self.angle -= 10
        self.place_car()
        
    def drive_forward(self, _event): 
        # turn angle into radians, get cosine, multiply by 10, then decrement car y position
        self.car_pos_y -= math.cos(math.radians(self.angle)) * 10   
        self.car_pos_x -= math.sin(math.radians(self.angle)) * 10 
        self.place_car()
        
    def drive_backward(self, _event):
        self.car_pos_y += math.cos(math.radians(self.angle)) * 10
        self.car_pos_x += math.sin(math.radians(self.angle)) * 10 
        self.place_car()
 
        
if __name__ == '__main__':
    win = tk.Tk()
    win.title("Car Game")                           # create a tkinter window
    car_game = CanvasAndCar(win)                    # create CanvasAndCar and save class instance in variable or image might not show
    game_area = GameArea(car_game.canvas)           # create class instance, pass in canvas
    car_game.after_turtle_game_area_creation()
    win.mainloop()                                  # start the tkinter main gui event loop







