import tkinter as tk
from tkinter import *
import random


class Player:
    def __init__(self, x, y, canvas):
        self.posx = x
        self.posy = y
        self.size = 20
        self.canvas = canvas
        self.first = False
        self.player = self.canvas.create_oval(self.posx, self.posy, self.posx + 20, self.posy + 20, fill="black")
        self.gravity_speed = 0  
        self.jump_speed = -10   
        self.jumping = False 
        self.die  = False  
        self.score = 0
        self.board = canvas.create_text(650, 50, text="0", fill="black", font=('Helvetica 15 bold'))
    def update(self,pipe,pipe2):
        if(self.first == True):
            if self.jumping:
                self.jump()
            else:
                self.apply_gravity()
            self.colidedWith(pipe,pipe2)
            self.point(pipe,pipe2)

    def jump(self):
        self.canvas.move(self.player, 0, self.jump_speed)
        self.posy += self.jump_speed
        self.jump_speed += 1  
        
        if(self.jump_speed ==0):
            self.jump_speed = -7
            self.jumping = False
            self.gravity_speed = 0
      
    def colidedWith(self,pipe,pipe2):
        if(((self.posx <= pipe.posx + 100 and self.posx >= pipe.posx) or(self.posx+20 <= pipe.posx + 100 and self.posx+20 >= pipe.posx))and 
           (((self.posy >=0 and self.posy <= pipe.num * 10) or (self.posy+20 >=0 and self.posy+20 <= pipe.num * 10)) or
           ((self.posy >= pipe.num * 10 + 100 and self.posy <= 500) or(self.posy + 20 >= pipe.num * 10 + 100 and self.posy + 20 <= 500)))):
            canvas.itemconfig(player1.player, fill='red')
            if(self.die == False):
                self.die = not self.die
                canvas.create_text(350, 250, text="YOU LOSE", fill="black", font=('Helvetica 15 bold'))

        elif(((self.posx <= pipe2.posx + 100 and self.posx >= pipe2.posx) or (self.posx + 20 <= pipe2.posx + 100 and self.posx +20 >= pipe2.posx))and 
           (((self.posy >= pipe2.num * 10 + 100 and self.posy <= 500) or(self.posy + 20 >= pipe2.num * 10 + 100 and self.posy + 20 <= 500))  or
           ((self.posy >=0 and self.posy <= pipe2.num * 10) or (self.posy+20 >=0 and self.posy+20 <= pipe2.num * 10)))):
            canvas.itemconfig(player1.player, fill='red')
            if(self.die == False):
                self.die = not self.die
                canvas.create_text(350, 250, text="YOU LOSE", fill="black", font=('Helvetica 15 bold'))
    def point(self,pipe,pipe2):
        if((self.posx > pipe.posx + 100) and pipe.first == True):
            pipe.first = False
            canvas.delete(self.board)
            self.score += 1
            self.board = canvas.create_text(650, 50, text=self.score, fill="black", font=('Helvetica 15 bold'))
        if((self.posx > pipe2.posx + 100) and pipe2.first == True):
            pipe2.first = False
            canvas.delete(self.board)
            self.score += 1
            self.board = canvas.create_text(650, 50, text=self.score, fill="black", font=('Helvetica 15 bold'))

      
        
    def apply_gravity(self):
        self.canvas.move(self.player, 0, self.gravity_speed)
        self.posy += self.gravity_speed
        self.gravity_speed += 2  
        

        if self.posy == 0:  
            self.posy = 0
        
    

class Pipe:
    def __init__(self, x, y, canvas):
        self.posx = x
        self.posy = y
        self.size = 20
        self.canvas = canvas
        self.num = random.randint(1, 35)
        self.pipe =  self.canvas.create_rectangle(self.posx, self.num * 10, self.posx + 100, 0,fill = "blue",width = 2)
        self.pipetwo =  self.canvas.create_rectangle(self.posx, 500, self.posx + 100, 100 +self.num * 10,  fill = "blue",width = 2)
        self.move_speed = -6 
        self.first = True
    def move_right(self, player):
        if(player.die == False and player.first == True):
            self.canvas.move(self.pipe, self.move_speed, 0)
            self.canvas.move(self.pipetwo, self.move_speed, 0)
            self.posx += self.move_speed
            if(self.posx+100 <= 0):
                canvas.delete(self.pipe)                              
                canvas.delete(self.pipetwo)

                self.posx = 700
                self.first = True
                self.num = random.randint(1, 35)
                self.pipe =  self.canvas.create_rectangle(self.posx, self.num * 10, self.posx + 100, 0, fill = "blue",width = 2)
                self.pipetwo =  self.canvas.create_rectangle(self.posx, 500, self.posx + 100, 100 +self.num * 10, fill = "blue",width = 2)
                canvas.lower(self.pipe)
                canvas.lower(self.pipetwo)
class ScrollingBackground:
    def __init__(self, canvas, image_path, width, height):
        self.canvas = canvas
        self.image = tk.PhotoImage(file="C:\python\FLAPPY\motor-ai-20240221151245_resized.jpg")
        self.image_width = width
        self.image_height = height
        self.bg_image1 = canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
      
        
        self.scroll_speed = 0  # Adjust the scroll speed as needed
       
        
    def update(self):
        canvas.lower(self.bg_image1)
       






window = tk.Tk()
window.geometry("700x500")
canvas = tk.Canvas(window, bg="white", height="500", width="700")
canvas.pack()

background = ScrollingBackground(canvas,"C:\python\FLAPPY\motor-ai-20240221151245_resized.jpg",700,500)
pipe = Pipe(700,250,canvas)
pipe2 = Pipe(350,250,canvas)
player1 = Player(200, 200, canvas)

def keyPressed(event):
    key = event.keysym
    player1.first = True
    if key == 'space' and player1.die == False:
        player1.jumping = True
        player1.jump_speed = -7 
        player1.jump()


def update_player():
    player1.update(pipe,pipe2) 
    pipe.move_right(player1)  
    pipe2.move_right(player1)
    background.update()
    window.after(50, update_player) 
 




update_player()

window.bind("<KeyPress>", keyPressed)

window.mainloop()
