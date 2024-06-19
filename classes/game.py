import pygame
from .bird import Bird
from .pipe import Pipe

class Game:
    def __init__(self, background, bird_image, pipe_image, font, screen, screen_width, screen_height, gravity, bird_jump, pipe_speed, pipe_gap, spawn_pipe_event):
        self.background = background
        self.bird_image = bird_image
        self.pipe_image = pipe_image
        self.font = font
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.gravity = gravity
        self.bird_jump = bird_jump
        self.pipe_speed = pipe_speed
        self.pipe_gap = pipe_gap
        self.spawn_pipe_event = spawn_pipe_event

        self.bird = Bird(self.bird_image)
        self.pipes = []
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.started = False
        pygame.time.set_timer(self.spawn_pipe_event, 1500)
    
    def start(self):
        self.bird = Bird(self.bird_image)
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.started = True
    
    def update(self):
        if not self.started:
            return
        if self.game_over:
            return

        self.bird.update(self.gravity)
        if self.bird.rect.top <= 0 or self.bird.rect.bottom >= self.screen_height:
            self.game_over = True

        for pipe in self.pipes:
            pipe.update(self.pipe_speed)
            if pipe.is_off_screen():
                self.pipes.remove(pipe)
            if pipe.has_collided_with(self.bird):
                self.game_over = True
            if pipe.top_rect.right < self.bird.rect.left and not pipe.passed:
                self.score += 10
                pipe.passed = True

        if self.game_over:
            self.high_score = max(self.score, self.high_score)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if not self.started:
            self.draw_start_screen()
        else:
            self.bird.draw(self.screen)
            for pipe in self.pipes:
                pipe.draw(self.screen)
            self.draw_score()
            if self.game_over:
                self.draw_game_over_screen()

    def draw_start_screen(self):
        start_text = self.font.render('Press SPACE to Start', True, (255, 255, 255))
        self.screen.blit(start_text, (self.screen_width // 2 - start_text.get_width() // 2, self.screen_height // 2 - start_text.get_height() // 2))

    def draw_game_over_screen(self):
        game_over_text = self.font.render('Game Over', True, (255, 255, 255))
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        high_score_text = self.font.render(f'High Score: {self.high_score}', True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, self.screen_height // 2 - game_over_text.get_height() // 2 - 30))
        self.screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, self.screen_height // 2 - score_text.get_height() // 2))
        self.screen.blit(high_score_text, (self.screen_width // 2 - high_score_text.get_width() // 2, self.screen_height // 2 - high_score_text.get_height() // 2 + 30))

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def spawn_pipe(self):
        if self.started and not self.game_over:
            self.pipes.append(Pipe(self.pipe_image, self.screen_width, self.pipe_gap, self.screen_height))
