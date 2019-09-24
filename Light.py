#A traffic light by Jonathan Abramson
#jonathan.abramson@ibm.com
#Pretty and it works

from graphics import *

def main():
    win = GraphWin("Green Circle", 500, 500)
    black = Rectangle(Point(200,75),Point(300,425))
    black.draw(win)
    black.setFill("white")
    red = Circle(Point(250,125), 35)
    red.setFill("red")
    red.setOutline("black")
    red.draw(win)
    yellow = Circle(Point(250,250), 35)
    yellow.setFill("yellow")
    yellow.setOutline("black")
    yellow.draw(win)
    green = Circle(Point(250,375), 35)
    green.setFill("green")
    green.setOutline("black")
    green.draw(win)
    pole = Rectangle(Point(235,425),Point(265,500))
    pole.draw(win)
    pole.setFill("green")
    win.setBackground("black")    
    
    win.getMouse() # pause for click in window
    win.close()
    
main()
