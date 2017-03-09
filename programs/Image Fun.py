#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brian
#
# Created:     04/12/2012
# Copyright:   (c) Brian 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from Graphics import *

def main():
    img = Image(Point(550,425), "halo3.gif") #Creating the image
    win = GraphWin("Python Project",1100,850) #setting up the window
    img.draw(win)

    row = 0
    column = 0

    win.getMouse()

    for row in range(1023):
        for column in range(767):
            r, g ,b = img.getPixel(row, column)
            pixelValue = int((r + b + g) / 3) #average of the r g b values
            img.setPixel(row, column, color_rgb(pixelValue, pixelValue, pixelValue)) #set all values to average of the 3 subpixels
            #this converts the image into grayscale

    win.getMouse()
    win.close()

main()
