# use optional parameter to set text tilted?

import pygame
import objShapes
import objFrame
import objDisplay


# initalize the display module
pygame.init()
window = pygame.display.set_mode((1280, 720))


# items
# dorm outline
line1 = objShapes.Line(window, [105,105,105], [230,230], [746,230], 2)
line2 = objShapes.Line(window, [105,105,105], [80,380], [230,230], 2)
line3 = objShapes.Line(window, [105,105,105], [900,380], [746,230], 2)
line4 = objShapes.Line(window, [105,105,105], [230,80], [230,230], 2)
line5 = objShapes.Line(window, [105,105,105], [746,80], [746,230], 2)
# room items
text1 = objShapes.Text(window, 'dresser', 30, [105,105,105], [240,240], 0)
text2 = objShapes.Text(window, 'desk', 30, [105,105,105], [410,240], 0)
text3 = objShapes.Text(window, 'b', 30, [105,105,105], [550,240], 0)
text4 = objShapes.Text(window, 'e', 30, [105,105,105], [595,240], 0)
text5 = objShapes.Text(window, 'd', 30, [105,105,105], [640,240], 0)
text6 = objShapes.Text(window, 'dresser', 38, [105,105,105], [210,300], 0)
text7 = objShapes.Text(window, 'desk', 38, [105,105,105], [400,300], 0)
text8 = objShapes.Text(window, 'b', 38, [105,105,105], [550,300], 0)
text9 = objShapes.Text(window, 'e', 38, [105,105,105], [595,300], 0)
text10 = objShapes.Text(window, 'd', 38, [105,105,105], [645, 300], 0)
text11 = objShapes.Text(window, 'c', 28, [105,105,105], [203,110], 0)
text12 = objShapes.Text(window, 'l', 28, [105,105,105], [205,135], 0)
text13 = objShapes.Text(window, 'o', 28, [105,105,105], [203,155], 0)
text14 = objShapes.Text(window, 's', 28, [105,105,105], [203,172], 0)
text15 = objShapes.Text(window, 'e', 28, [105,105,105], [203,190], 0)
text16 = objShapes.Text(window, 't', 28, [105,105,105], [205,210], 0)
text17 = objShapes.Text(window, 'c', 28, [105,105,105], [120,180], 0)
text18 = objShapes.Text(window, 'l', 28, [105,105,105], [120,210], 0)
text19 = objShapes.Text(window, 'o', 28, [105,105,105], [120,230], 0)
text20 = objShapes.Text(window, 's', 28, [105,105,105], [120,250], 0)
text21 = objShapes.Text(window, 'e', 28, [105,105,105], [118,270], 0)
text22 = objShapes.Text(window, 't', 28, [105,105,105], [120,290], 0)
text23 = objShapes.Text(window, 'chair', 24, [105,105,105], [400,260], 0)
text24 = objShapes.Text(window, 'chair', 24, [105,105,105], [430,290], 0)
text25 = objShapes.Text(window, 'w', 28, [105,105,105], [770,110], 0)
text26 = objShapes.Text(window, 'i', 28, [105,105,105], [773,130], 0)
text27 = objShapes.Text(window, 'n', 28, [105,105,105], [770,150], 0)
text28 = objShapes.Text(window, 'd', 28, [105,105,105], [770,170], 0)
text29 = objShapes.Text(window, 'o', 28, [105,105,105], [770,190], 0)
text30 = objShapes.Text(window, 'w', 28, [105,105,105], [770,210], 0)
text31 = objShapes.Text(window, 'w', 28, [105,105,105], [840,160], 0)
text32 = objShapes.Text(window, 'i', 28, [105,105,105], [843,180], 0)
text33 = objShapes.Text(window, 'n', 28, [105,105,105], [840,200], 0)
text34 = objShapes.Text(window, 'd', 28, [105,105,105], [840,220], 0)
text35 = objShapes.Text(window, 'o', 28, [105,105,105], [840,240], 0)
text36 = objShapes.Text(window, 'w', 28, [105,105,105], [840,260], 0)
# room decor
text37 = objShapes.Text(window, 'orange', 12, [105,105,105], [700,290], 0)
text38 = objShapes.Text(window, 'cloth', 12, [105,105,105], [720,310], 0)
text39 = objShapes.Text(window, 'cloth', 12, [105,105,105], [670,280], 0)
text40 = objShapes.Text(window, 'cloth', 12, [105,105,105], [570,330], 0)
text41 = objShapes.Text(window, 'cloth', 12, [105,105,105], [220,240], 0)
text42 = objShapes.Text(window, 'cloth', 12, [105,105,105], [260,290], 0)
text43 = objShapes.Text(window, 'cloth', 12, [105,105,105], [330,330], 0)
text44 = objShapes.Text(window, 'cloth', 12, [105,105,105], [360,250], 0)
text45 = objShapes.Text(window, 'cloth', 12, [105,105,105], [400,290], 0)
text46 = objShapes.Text(window, 'cloth', 12, [105,105,105], [480,350], 0)
text47 = objShapes.Text(window, 'sock', 12, [105,105,105], [350,350], 0)
text48 = objShapes.Text(window, 'sock', 12, [105,105,105], [340,280], 0)
text49 = objShapes.Text(window, 'sock', 12, [105,105,105], [130,350], 0)
text50 = objShapes.Text(window, 'sock', 12, [105,105,105], [380,300], 0)
text51 = objShapes.Text(window, 'sock', 12, [105,105,105], [710,240], 0)
text52 = objShapes.Text(window, 'sock', 12, [105,105,105], [620,320], 0)
text53 = objShapes.Text(window, 'sock', 12, [105,105,105], [580,280], 0)
text54 = objShapes.Text(window, 'left', 12, [105,105,105], [480,240], 0)
text55 = objShapes.Text(window, 'left', 12, [105,105,105], [250,350], 0)
text56 = objShapes.Text(window, 'left', 12, [105,105,105], [500,290], 0)
text57 = objShapes.Text(window, 'left', 12, [105,105,105], [760,330], 0)
text58 = objShapes.Text(window, 'right', 12, [105,105,105], [180,290], 0)
text59 = objShapes.Text(window, 'right', 12, [105,105,105], [660,355], 0)
text60 = objShapes.Text(window, 'right', 12, [105,105,105], [630,280], 0)
text61 = objShapes.Text(window, 'right', 12, [105,105,105], [750,280], 0)
text62 = objShapes.Text(window, 'shoe', 12, [105,105,105], [480,250], 0)
text63 = objShapes.Text(window, 'shoe', 12, [105,105,105], [250,360], 0)
text64 = objShapes.Text(window, 'shoe', 12, [105,105,105], [500,300], 0)
text65 = objShapes.Text(window, 'shoe', 12, [105,105,105], [760,340], 0)
text66 = objShapes.Text(window, 'shoe', 12, [105,105,105], [180,300], 0)
text67 = objShapes.Text(window, 'shoe', 12, [105,105,105], [660,365], 0)
text68 = objShapes.Text(window, 'shoe', 12, [105,105,105], [630,290], 0)
text69 = objShapes.Text(window, 'shoe', 12, [105,105,105], [750,290], 0)

button1 = objShapes.Button(window, 'd', 38, [105,105,105], [165,180], 0)
button2 = objShapes.Button(window, 'o', 38, [105,105,105], [165,200], 0)
button3 = objShapes.Button(window, 'o', 38, [105,105,105], [165,220], 0)
button4 = objShapes.Button(window, 'r', 38, [105,105,105], [165,240], 0)
button5 = objShapes.Button(window, 'roommate', 22, [105,105,105], [560,230], 0)
# use optional parameter to set text tilted?
button6 = objShapes.Button(window, 'heater', 24, [105,105,105], [735,230], -45)
button7 = objShapes.Button(window, 'heater', 24, [105,105,105], [795,290], -45)


# items into lists
lines = [line1, line2, line3, line4, line5,]
texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10,
        text11, text12, text13, text14, text15, text16, text17, text18, text19,
        text20, text21, text22, text23, text24, text25, text26, text27, text28,
        text29, text30, text31, text32, text33, text34, text35, text36, text37,
        text38, text39, text40, text41, text42, text43, text44, text45, text46,
        text47, text48, text49, text50, text51, text52, text53, text54, text55,
        text56, text57, text58, text59, text60, text61, text62, text63, text64,
        text65, text66, text67, text68, text69]
buttons = [button1, button2, button3, button4, button5, button6, button7]

def draw():
    run = True
    while (run == True):
        # overlay the screen with a nice white background
        # pygame.draw.rect(window, [255,255,255], [0,0,1280,720])
        window.fill([255,255,255])

        # drawFrame
        objFrame.draw()

        #draw items in lists
        for line in lines:
            line.draw()

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

# testing only, delete after completion
draw()