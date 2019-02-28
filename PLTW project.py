#Imports Tkinter and a time stopper
import tkinter
import time


#Makes a shortcut
root = tkinter.Tk()
#Sets up Variables
# 'Most recent' to know which radio button is 'on'
Material = tkinter.IntVar()
Type = tkinter.IntVar()
#Makes a canvas
canvas = tkinter.Canvas(root, height = 600, width = 600, bg='#FFFFFF')
canvas.grid(row=10,rowspan=999, column = 0, columnspan = 12)
#creates colors
red_intvar = tkinter.IntVar()
green_intvar = tkinter.IntVar()
blue_intvar = tkinter.IntVar()
startx , starty = 300, 300
for x in  range(10, 300, 40):
    y = x
    r = 30 #So all circles will have this radius
    

    
def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a string representing two hexadecimal digits
    '''

def wood():
    print
def iron():
    print
    
def steel():
    print

def Sailboat():
    canvas.delete("all")
    y = x # So that circles are along diagonal line y=x 
    r = 30 # All the circles will have this radius
    rectangle1 = canvas.create_rectangle(100, 100, 200, 200, fill="#850000", outline = "#850000") 
    circle1 = canvas.create_oval(100, 140, 500, 500, fill='#850000', outline = "#850000")


def Ironclad():
    canvas.delete("all")
    y = x # So that circles are along diagonal line y=x 
    r = 30 # All the circles will have this radius
    rectangle = canvas.create_rectangle(200, 50, 100, 150, fill="#ece9ec", outline='#ece9ec')
    circle = canvas.create_oval(100, 140, 500, 500, fill="#ece9ec", outline = "#ece9ec")

    
def Warship():    
    canvas.delete("all")
    y = x # So that circles are along diagonal line y=x 
    r = 30 # All the circles will have this radius
    rectangle2 = canvas.create_rectangle(100, 100, 200, 200, fill='#c3cbad', outline='#c3cbad')
    rectangle3 = canvas.create_rectangle(150, 150, 250, 200, fill='#c3cbad', outline='#c3cbad')
    circle2 = canvas.create_oval(100, 140, 500, 500, fill='#c3cbad', outline='#c3cbad')

#Makes buttons
Wood_Radio = tkinter.Radiobutton(root, text='Wood', variable=Material, value=1, command = wood)
Iron_Radio = tkinter.Radiobutton(root, text='Iron', variable=Material, value=2, command = iron)
Steel_Radio = tkinter.Radiobutton(root, text= 'Steel', variable = Material, value=3, command = steel)
Sailboat_Radio = tkinter.Radiobutton(root, text='Sailboat, "Caution may break upon use"', variable=Type, value=1, command = Sailboat)
Ironclad_Radio = tkinter.Radiobutton(root, text='Ironclad, meh', variable=Type, value=2, command = Ironclad)
Warship_Radio = tkinter.Radiobutton(root, text='Warship, "Boat Builder Destroyer"', variable=Type, value=3, command = Warship)


#Sets up positions for buttons
Wood_Radio.grid(row=0, column = 0, sticky=tkinter.W)
Iron_Radio.grid(row=0, column = 4, sticky=tkinter.W)
Steel_Radio.grid(row=0, column=8, sticky=tkinter.W)
Sailboat_Radio.grid(row=1, column=0, sticky=tkinter.W)
Ironclad_Radio.grid(row=1, column=4, sticky=tkinter.W)
Warship_Radio.grid(row=1, column=8, sticky=tkinter.W)


#Sets Radio Buttons to 1, so only one is activated when program started.
#Otherwise all butons would be "On"
Material.set(1) 
Type.set(1)


#Event loop, loops everything
root.mainloop()