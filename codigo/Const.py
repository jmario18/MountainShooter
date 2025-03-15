
import pygame

#C
COLOR_ORANGE= (255,128,0)
COLOR_WHITE=(255,255,255)
COLOR_YELLOW=(255,255,128)


#E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

EVENT_ENEMY = pygame.USEREVENT +1


#M
MENU_OPTION=('NEW GAME 1 PLAYER','NEW GAME 2 PLAYERS - COOPERATIVE', 'NEW GAME 2 PLAYERS - COMPETITIVE','SCOREBOARD', 'EXIT')


#P
PLAYER_KEY_UP= {
    'Player1': pygame.K_w,
    'Player2': pygame.K_UP
}
PLAYER_KEY_DOWN= {
    'Player1': pygame.K_s,
    'Player2': pygame.K_DOWN
}
PLAYER_KEY_RIGHT= {
    'Player1': pygame.K_d,
    'Player2': pygame.K_RIGHT
}
PLAYER_KEY_LEFT= {
    'Player1': pygame.K_a,
    'Player2': pygame.K_LEFT
}
PLAYER_KEY_SHOOT= {
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_RETURN
}



#SIZES
WIDTH = 576
HEIGHT = 324


