import random
from tkinter.font import Font
import pygame
from codigo.Entity import Entity
from codigo.EntityFactory import EntityFactory
from codigo.Const import COLOR_WHITE, HEIGHT, MENU_OPTION, EVENT_ENEMY
from pygame import Surface, Rect

class Level:

    def __init__(self, screen, name, mode):
        self.screen = screen
        self.name = name
        self.timeout = 20000 #20 segundos
        self.game_mode = mode #1  ou 2 jogadores
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY,  2000)

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        print('Level Run')
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(60) #60fps
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'fps {clock.get_fps() :0f}', COLOR_WHITE, (10, HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10,HEIGHT - 20))
            pygame.display.flip()
        quit()
    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)

       
