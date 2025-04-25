
from codigo.Entity import Entity
from codigo.Const import ENTITY_SPEED

class PlayerShot(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name,position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]