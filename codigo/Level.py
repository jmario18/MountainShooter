import pygame
from codigo.Entity import Entity
from codigo.EntityFactory import EntityFactory

class Level:

    def __init__(self, screen, name, mode):
        self.screen = screen
        self.name = name
        self.game_mode = mode #1  ou 2 jogadores
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        running = True
        while running:

            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
            
        quit()
