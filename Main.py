import pygame
import slideTitle


# initalize the display module
pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("15-112 Simulator")


# main Loop
def main():
    run = True
    while (run == True):

        # display the title slide
        slideTitle.draw()

        # checking for events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

        # update the canvas (flip)
        pygame.display.update()

    # when run is no longer true, quit pygame
    pygame.quit()

# run the main function
main()
