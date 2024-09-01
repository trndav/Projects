import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Bubble Properties
POPULATION_INCREMENT = 1
GROWTH_RATE = 1.5
ATTACK_RATE = 1.2
BASE_ATTACK = 3

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubbles")

# Bubble Class
class Bubble:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.population = 10
        self.growth_rate = POPULATION_INCREMENT
        self.attack_rate = BASE_ATTACK
        self.radius = 40
        self.color = color
        self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
        self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

    def draw(self, screen):
        if self.population > 0:  # Only draw if population is greater than 0
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            population_text = font.render(str(int(self.population)), True, BLACK)
            screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))
            
            # Draw buttons
            pygame.draw.rect(screen, WHITE, self.grow_button)
            pygame.draw.rect(screen, WHITE, self.attack_button)
            pygame.draw.rect(screen, BLACK, self.grow_button, 2)  # Add border to buttons
            pygame.draw.rect(screen, BLACK, self.attack_button, 2)  # Add border to buttons
            screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
            screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

    def update(self):
        if self.population > 0:  # Only update if population is greater than 0
            self.population += self.growth_rate / FPS

    def grow(self):
        self.growth_rate = GROWTH_RATE

    def attack_boost(self):
        self.attack_rate = BASE_ATTACK * ATTACK_RATE

# Initialize Font
font = pygame.font.SysFont(None, 24)
grow_text = font.render('Grow', True, BLACK)
attack_text = font.render('Attack', True, BLACK)

# Initialize bubbles with different colors
player_bubble = Bubble(200, 300, (0, 128, 255))  # Blue bubble
enemy_bubble = Bubble(600, 300, (255, 0, 0))     # Red bubble

# Game Loop
running = True
clock = pygame.time.Clock()
selected_bubble = None
attack_line = None
game_over = False
winner_text = None

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Select or connect bubbles
            if player_bubble.radius > math.hypot(mouse_x - player_bubble.x, mouse_y - player_bubble.y):
                selected_bubble = player_bubble
            elif selected_bubble and enemy_bubble.radius > math.hypot(mouse_x - enemy_bubble.x, mouse_y - enemy_bubble.y):
                attack_line = (selected_bubble, enemy_bubble)
            elif player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
                player_bubble.grow()
            elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
                player_bubble.attack_boost()
                
    # Draw and update bubbles
    if not game_over:
        player_bubble.update()
        enemy_bubble.update()
    
    player_bubble.draw(screen)
    enemy_bubble.draw(screen)
    
    # Handle attack
    if attack_line and not game_over:
        attacker, defender = attack_line
        defender.population -= attacker.attack_rate / FPS
        attacker.population -= BASE_ATTACK / FPS
        
        if defender.population <= 0:
            defender.population = 0
            game_over = True
            winner_text = font.render("Winner!", True, BLACK)
        elif attacker.population <= 0:
            attacker.population = 0
            game_over = True
            winner_text = font.render("Winner!", True, BLACK)
    
    # Display winner text if game over
    if game_over:
        if defender.population == 0 and attacker.population > 0:
            screen.blit(winner_text, (attacker.x - winner_text.get_width() // 2, attacker.y - 60))
            enemy_bubble.population = 0  # Remove losing bubble
        elif attacker.population == 0 and defender.population > 0:
            screen.blit(winner_text, (defender.x - winner_text.get_width() // 2, defender.y - 60))
            player_bubble.population = 0  # Remove losing bubble

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
