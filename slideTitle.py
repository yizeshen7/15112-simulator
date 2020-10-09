import pygame
import objShapes
import objFrame
import objDisplay


# initalize the display module
pygame.init()
window = pygame.display.set_mode((1280, 720))


# objects on the canvas
text1 = objShapes.Text(window, '15-112 Simulator', 72, [105,105,105], [140,170], 0)
button1 = objShapes.Button(window, 'New Game', 40, [105,105,105], [910,405], 0)
button2 = objShapes.Button(window, 'Options', 40, [105,105,105], [964,455], 0)
button3 = objShapes.Button(window, 'Quit', 40, [105,105,105], [1015,505], 0)


# objects into lists
buttons = [button1, button2, button3]
texts = [text1]


# main Loop
def draw():
    run = True
    while (run == True):
        # overlay the screen with a nice white background
        # pygame.draw.rect(window, [255,255,255], [0,0,1280,720])
        window.fill([255,255,255])

        # handles every single text in the given list
        for text in texts:
            text.draw()

        # handles every single button in the given list
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
                if (event.key == pygame.K_a):
                    objDisplay.Display.renderDisplay('selection')

        # side tools
        objShapes.SideTools.printCoordinate(window)

        # update the canvas (flip)
        pygame.display.update()

    # when run is no longer true, quit pygame
    pygame.quit()
