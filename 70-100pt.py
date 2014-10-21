##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
#house outline
rectangle1 = drawpad.create_rectangle(300,400,500,600,fill='red')
#roof
line1 = drawpad.create_line(300,400,400,300)
line2 = drawpad.create_line(500,400,400,300)
#door
rectangle2 = drawpad.create_rectangle(400,540,450,600)
#windows
rectangle3 = drawpad.create_rectangle(340,480,400,520,fill='green')
rectangle4 = drawpad.create_rectangle(410,480,450,520,fill='yellow')
#doorknob
oval1 = drawpad.create_oval(410,560,420,570,fill='blue')
#chimney
rectangle5 = drawpad.create_rectangle(481,400,501,300,fill='purple')
#grass
line3 = drawpad.create_line(0,600,299,600,fill='green')
line4 = drawpad.create_line(0,599,299,599,fill='green')
line5 = drawpad.create_line(501,600,800,600,fill='green')
line6 = drawpad.create_line(501,599,800,599,fill='green')
root.mainloop()
