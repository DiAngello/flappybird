import pygame
from classes.bird import Bird
from classes.pipe import Pipe
from classes.game import Game

# Iniciando o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Carregando imagens
BACKGROUND = pygame.image.load('fundo.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
BIRD_IMAGE = pygame.image.load('cobra.png')
BIRD_IMAGE = pygame.transform.scale(BIRD_IMAGE, (50, 50)) 
PIPE_IMAGE = pygame.image.load('tubo.png')
PIPE_IMAGE = pygame.transform.scale(PIPE_IMAGE, (70, 500))  

# Constantes do jogo
GRAVITY = 0.5
BIRD_JUMP = -10
PIPE_SPEED = 3
PIPE_GAP = 230
SPAWN_PIPE_EVENT = pygame.USEREVENT

# Configurações do texto
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 24)

def main():
    clock = pygame.time.Clock()
    game = Game(BACKGROUND, BIRD_IMAGE, PIPE_IMAGE, FONT, screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITY, BIRD_JUMP, PIPE_SPEED, PIPE_GAP, SPAWN_PIPE_EVENT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game.started:
                        game.start()
                    elif game.game_over:
                        game.start()
                    else:
                        game.bird.jump()
            if event.type == SPAWN_PIPE_EVENT:
                game.spawn_pipe()

        game.update()
        game.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
