import pygame 


WIDTH = 550
background_color = (251,247,245)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption("Soduko")
    win.fill(background_color)

    for i in range(0,10):
        pygame.draw.line(win, (0,0,0), (50 + 50 *i, 50), (50 + 50*i ,500), 2)
        pygame.draw.line(win, (0,0,0), (), (), 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
