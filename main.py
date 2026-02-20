import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

player_start_x = SCREEN_WIDTH / 2
player_start_y = SCREEN_HEIGHT / 2


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(player_start_x, player_start_y)
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
