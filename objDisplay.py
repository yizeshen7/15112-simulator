import pygame
import slideTitle
import slideSelection


class Display(object):

    @staticmethod
    # this function takes in a given name and render the display based on
    #    the name provided, for swtiching scene purposes
    def renderDisplay(slide):
        if slide == "title":
            slideTitle.draw()
        
        elif slide == 'selection':
            slideSelection.draw()
