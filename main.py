import tkinter as tk
import os
import time
import shutil as sh

def flap(event):

    canvas.move(flappy, 0, -75)
    root.update()


def main():
   

    '''Main function which creates our root window'''

    '''Constant for Heigh of screen'''
    HEIGHT = 700
    '''Constant for Width of screen'''
    WIDTH = 800


    # Main window plus config settings
    global root
    root = tk.Tk()
    root.geometry(f'{HEIGHT}x{WIDTH}')
    root.resizable(width=False, height=False)
    root.title("Flappy Bird")

    # Canvas object that will contain our lines and rectangles used for the game
    global canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()



    # Rectangle that will server as our player
    global flappy
    flappy = canvas.create_rectangle(50, 350, 100, 400, fill='purple')
    root.bind('<space>', flap)

    
    while True:

        # Moves our rectangle down at a constant, smooth rate
        canvas.move(flappy, 0, 1.5) 
        root.update()
        time.sleep(.01)

        # The moment we hit the ground, we break out, as we have lost
        if not canvas.coords(flappy)[1] <= 600:
            break;

    # Mainloop of our tk window
    root.mainloop()

if __name__ == "__main__":
    main()
