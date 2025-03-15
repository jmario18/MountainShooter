
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from codigo.Const import WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, COLOR_YELLOW

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() #carregando imagem bg
        self.rect = self.surf.get_rect(left=0, top=0) #retangulo no topo esquedo da tela

    def run(self):
        running = True
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while running:
            self.screen.blit(source=self.surf, dest=self.rect) #pegando imagem do surf, colocando no retangulo
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIDTH/2),70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIDTH/2),110))

            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIDTH/2),200+25*i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIDTH/2),200+25*i))

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #SETA BAIXO
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:# SETA CIMA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION)-1
                    if event.key == pygame.K_RETURN:# ENTER
                        return MENU_OPTION[menu_option]
            pygame.display.flip()
        quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)