

import pygame, time
def main():
    pygame.init()
    size = width, height = 600, 400
    speed = [1, 1]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("test")

    ball = pygame.image.load("intro_ball.png")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                return

        time.sleep(.01)

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball,ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()