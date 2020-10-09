import pygame
import objShapes
import objFrame
import objDisplay


# initalize the display module
pygame.init()
window = pygame.display.set_mode((1280, 720))


#items
text1 = objShapes.Text(window, 'Where to...', 36, [105,105,105], [110,100], 0)
button1 = objShapes.Button(window, 'Lecture', 30, [105,105,105], [220,170], 0)
button2 = objShapes.Button(window, 'Recitation', 30, [105,105,105], [210,240], 0)
button3 = objShapes.Button(window, 'GHC', 30, [105,105,105], [230,310], 0)
button4 = objShapes.Button(window, 'iNoodle', 30, [105,105,105], [460,170], 0)
button5 = objShapes.Button(window, 'Dorm', 30, [105,105,105], [470,240], 0)
button6 = objShapes.Button(window, 'La Prima', 30, [105,105,105], [450,310], 0)
button7 = objShapes.Button(window, 'The Cut', 30, [105,105,105], [700,170], 0)
button8 = objShapes.Button(window, 'Entropy', 30, [105,105,105], [700,240], 0)
button9 = objShapes.Button(window, 'pHolder', 30, [105,105,105], [700, 310], 0)
button10 = objShapes.Button(window, 'Final', 30, [105,105,105], [470,110], 0)


# items into lists
texts = [text1]

buttons = [button1, button2, button3, button4, button5, button6, button7,
            button8, button9, button10]

def draw():
    run = True
    while (run == True):
        # overlay the screen with a nice white background
        # pygame.draw.rect(window, [255,255,255], [0,0,1280,720])
        window.fill([255,255,255])

        # drawFrame
        objFrame.draw()

        #draw items in lists
        for text in texts:
            text.draw()

        for button in buttons:
            # remember that we have to draw them first to get the border
            button.draw()
            # constnatly check mouse hover over any buttons to change color
            if button.border.collidepoint(pygame.mouse.get_pos()):
                button.hovered = True
            else: 
                button.hovered = False

        # checking for events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_b):
                    objDisplay.Display.renderDisplay('title')

        # side tools
        objShapes.SideTools.printCoordinate(window)

        # update the canvas (flip)
        pygame.display.update()

    # when run is no longer true, quit pygame
    pygame.quit()