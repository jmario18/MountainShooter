import pygame
from codigo.Const import HEIGHT, WIDTH
from codigo.Menu import Menu

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        

    pygame.init()
    def run(self):
        running = True
        
        clock = pygame.time.Clock()

        while running:
            menu = Menu(self.screen)

            menu.run()

            pass
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:  #Verificando quando clica no X para fechar
#                    running = False
#                    pygame.quit()
#            pygame.display.flip() # Atualizando tela
#
#            clock.tick(60) #60 FPS
        quit()
    