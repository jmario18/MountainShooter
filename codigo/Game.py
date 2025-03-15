import pygame
from codigo.Const import HEIGHT, WIDTH, MENU_OPTION
from codigo.Menu import Menu
from codigo.Level import Level

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        

    pygame.init()
    def run(self):
        running = True
        
        

        while running:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level =  Level(self.screen, 'level1', menu_return)
                level_return = level.run()
            if menu_return == MENU_OPTION[1]:
                level = Level(self.screen, 'level1', menu_return)
                level_return = level.run()
            if menu_return == MENU_OPTION[2]:
                level = Level(self.screen, 'level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass

            
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:  #Verificando quando clica no X para fechar
#                    running = False
#                    pygame.quit()
#            pygame.display.flip() # Atualizando tela
#
#            clock.tick(60) #60 FPS
    