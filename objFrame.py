import pygame
import objShapes
window = pygame.display.set_mode((1280, 720))


# display canvas
Line1 = objShapes.Line(window, [105,105,105], [80,80], [900,80], 4)
Line2 = objShapes.Line(window, [105,105,105], [80,80], [80,380], 4)
Line3 = objShapes.Line(window, [105,105,105], [80,380], [900,380], 4)
Line4 = objShapes.Line(window, [105,105,105], [900,80], [900,380], 4)
# action canvas
Line5 = objShapes.Line(window, [105,105,105], [920,80], [1080,80], 4)
Line6 = objShapes.Line(window, [105,105,105], [920,80], [920,380], 4)
Line7 = objShapes.Line(window, [105,105,105], [920,380], [1080,380], 4)
Line8 = objShapes.Line(window, [105,105,105], [1080,80], [1080,380], 4)
# text canvas
Line9 = objShapes.Line(window, [105,105,105], [80,400], [1080,400], 4)
Line10 = objShapes.Line(window, [105,105,105], [80,400], [80,680], 4)
Line11 = objShapes.Line(window, [105,105,105], [80,680], [1080,680], 4)
Line12 = objShapes.Line(window, [105,105,105], [1080,400], [1080,680], 4)
# status canvas
Line13 = objShapes.Line(window, [105,105,105], [1100,80], [1170,80], 4)
Line14 = objShapes.Line(window, [105,105,105], [1100,680], [1170,680], 4)
Line15 = objShapes.Line(window, [105,105,105], [1100,80], [1100,680], 4)
Line16 = objShapes.Line(window, [105,105,105], [1170,80], [1170,680], 4)
# scroll indicator
Line17 = objShapes.Line(window, [105,105,105], [1055,420], (1055,660), 4)
Line18 = objShapes.Line(window, (255,255,255), [1055,440], (1055,490), 4)
# item blocks
rect1 = objShapes.Rectangle(window, [105,105,105], [1113,120,45,45])
rect2 = objShapes.Rectangle(window, [105,105,105], [1113,240,45,45])
rect3 = objShapes.Rectangle(window, [105,105,105], [1113,360,45,45])
rect4 = objShapes.Rectangle(window, [105,105,105], [1113,480,45,45])
rect5 = objShapes.Rectangle(window, [105,105,105], [1113,600,45,45])

frames = [Line1, Line2, Line3, Line4, Line3, Line5, Line6, Line7, Line8, 
            Line9, Line10, Line11, Line12, Line13, Line14, Line15, Line16, 
            Line17, Line18, rect1, rect2, rect3, rect4, rect5]


def draw():
    for frame in frames:
        frame.draw()
