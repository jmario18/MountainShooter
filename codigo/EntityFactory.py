
import random
from codigo.Background import Background
from codigo.Const import WIDTH, HEIGHT
from codigo.Player import Player
from codigo.Enemy import Enemy

class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg =[]
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIDTH,0)))
                return list_bg
            
            case 'Player1':
                return Player('Player1', (10, HEIGHT/2))
            case 'Player2':
                return Player('Player2', (10, (HEIGHT/2) + 35))
            case 'Enemy1':
                return Enemy('Enemy1', ((WIDTH +10), random.randint(30,HEIGHT-30)))
            case 'Enemy2':
                return Enemy('Enemy2', ((WIDTH +10), random.randint(30,HEIGHT-30)))
