import tkinter as tk
from tkinter import *

class Player:
    def __init__(self, x, y, canvas):
        self.posx = x
        self.posy = y
        self.size = 20
        self.canvas = canvas
        self.player = self.canvas.create_oval(self.posx, self.posy, self.posx + 20, self.posy + 20, fill="black")
        self.gravity_speed = 0  
        self.jump_speed = -5   
        self.jumping = False     

    def update(self):
        if self.jumping:
            self.jump()
        else:
            self.apply_gravity()

    def jump(self):
        self.canvas.move(self.player, 0, self.jump_speed)
        self.jump_speed += 0.5  
        if(self.jump_speed ==0):
            self.jump_speed = -5
            self.jumping = False
            self.gravity_speed = 0

   
        if self.posy >= 200:  
            self.posy = 200
            self.jumping = False
            self.jump_speed = -5

    def apply_gravity(self):
        self.canvas.move(self.player, 0, self.gravity_speed)
        self.gravity_speed += 0.5  

      
        if self.posy >= 0:  
            self.posy = 0
           

window = tk.Tk()
window.geometry("700x500")
canvas = tk.Canvas(window, bg="white", height="500", width="700")
canvas.pack()

player1 = Player(200, 200, canvas)

def keyPressed(event):
    key = event.keysym
 
    if key == 'space':
       
        player1.jumping = True
        player1.jump()




def update_player():
    player1.update() 
    window.after(50, update_player)  


update_player()
window.bind("<KeyPress>", keyPressed)

window.mainloop()