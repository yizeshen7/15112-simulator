import pygame


class Rectangle(object):
    def __init__(self, canvas, color, size):
        self.canvas = canvas
        self.color = color
        self.size = size   

    def draw(self):
        pygame.draw.rect(self.canvas, self.color, self.size)


class Circle(object):
    def __init__(self, canvas, color, center, radius):
        self.canvas = canvas
        self.color = color
        self.center = center
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.canvas, self.color, self.center, self.radius)


class Line(object):
    def __init__(self, canvas, color, startPos, endPos, width):
        self.canvas = canvas
        self.color = color
        self.startPos = startPos
        self.endPos = endPos
        self.width = width
    
    def draw(self):
        pygame.draw.line(self.canvas, self.color, 
                            self.startPos, self.endPos, self.width)


class Text(object):
    def __init__(self, canvas, text, size, color, position, rotateAngle):
        self.canvas = canvas
        self.text = text
        self.size = size
        self.color = color
        self.position = position
        self.rotateAngle = rotateAngle
        self.font = None
        self.image = None
        self.border = None
    
    def __repr__(self):
        return (self.text)
    
    def renderFont(self):
        self.font = pygame.font.SysFont('Times New Roman', self.size)
    
    def createImage(self):
        self.image = self.font.render(self.text, True, self.color)
        self.image = pygame.transform.rotate(self.image, self.rotateAngle)
        self.border = self.image.get_rect()
        self.border.topleft = self.position
    
    def draw(self):
        self.renderFont()
        self.createImage()
        self.canvas.blit(self.image, self.position)


# same as the text class, expect it changes color upon hover
class Button(Text):
    def __init__(self, canvas, text, size, color, position, rotateAngle):
        super().__init__(canvas, text, size, color, position, rotateAngle)
        self.hovered = False

    def checkHovered(self):
        if self.hovered == True:
            self.color = [0,0,0]
        else:
            self.color = [105,105,105]

    def draw(self):
        self.checkHovered()
        self.renderFont()
        self.createImage()
        self.canvas.blit(self.image, self.position)


# side tools for some quality of life improvement on development
#   thanks, says Sean
class SideTools(object):

    # this gets all fonts that's currently on your computer
    # https://pygame.readthedocs.io/en/latest/4_text/text.html
    @staticmethod
    def getSystemFontsInYourComputer():
        fonts = pygame.font.get_fonts()
        print(f'{len(fonts)} fonts in your computer!')
        for font in fonts:
            print(font)
    
    #this gets mouse position on canvas and print it on the buttom-right
    @staticmethod
    def printCoordinate(canvas):
        mouseX, mouseY = pygame.mouse.get_pos()
        font = pygame.font.SysFont('Times New Roman', 16)
        image = font.render(f'({mouseX}, {mouseY})', True, [105,105,105])
        canvas.blit(image, [1200,700])

