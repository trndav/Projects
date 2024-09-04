
# import pygame
# import sys
# import math

# # Initialize pygame
# pygame.init()

# # Game Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# FPS = 60

# # Bubble Properties
# POPULATION_INCREMENT = 1
# GROWTH_RATE = 1.5
# ATTACK_RATE = 1.2
# BASE_ATTACK = 3

# # Setup the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Bubbles")

# # Bubble Class
# class Bubble:
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.population = 10
#         self.growth_rate = POPULATION_INCREMENT
#         self.attack_rate = BASE_ATTACK
#         self.radius = 40
#         self.color = color
#         self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
#         self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

#     def draw(self, screen):
#         if self.population > 0:
#             pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#             population_text = font.render(str(int(self.population)), True, BLACK)
#             screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))
            
#             pygame.draw.rect(screen, WHITE, self.grow_button)
#             pygame.draw.rect(screen, WHITE, self.attack_button)
#             pygame.draw.rect(screen, BLACK, self.grow_button, 2)
#             pygame.draw.rect(screen, BLACK, self.attack_button, 2)
#             screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
#             screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

#     def update(self):
#         if self.population > 0:
#             self.population += self.growth_rate / FPS

#     def grow(self):
#         self.growth_rate = GROWTH_RATE

#     def attack_boost(self):
#         self.attack_rate = BASE_ATTACK * ATTACK_RATE

# # Initialize Font
# font = pygame.font.SysFont(None, 24)
# grow_text = font.render('Grow', True, BLACK)
# attack_text = font.render('Attack', True, BLACK)

# # Initialize bubbles with different colors
# def reset_game():
#     global player_bubble, enemy_bubble, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start
#     player_bubble = Bubble(200, 300, (0, 128, 255))  # Blue bubble
#     enemy_bubble = Bubble(600, 300, (255, 0, 0))     # Red bubble
#     selected_bubble = None
#     connections = []
#     game_over = False
#     winner_text = None
#     play_again_button = None
#     drawing_line = False  # Track whether a line is currently being drawn
#     line_start = None  # The starting bubble for the line

# reset_game()

# # Game Loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     screen.fill(WHITE)
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
            
#             if game_over and play_again_button and play_again_button.collidepoint(mouse_x, mouse_y):
#                 reset_game()
#             elif not game_over:
#                 # Check if a bubble is clicked
#                 if player_bubble.radius > math.hypot(mouse_x - player_bubble.x, mouse_y - player_bubble.y):
#                     if not selected_bubble:
#                         selected_bubble = player_bubble
#                         drawing_line = True
#                         line_start = player_bubble
#                     elif selected_bubble and selected_bubble != player_bubble:
#                         connections.append((selected_bubble, player_bubble))
#                         selected_bubble = None
#                         drawing_line = False
#                         line_start = None
#                 elif enemy_bubble.radius > math.hypot(mouse_x - enemy_bubble.x, mouse_y - enemy_bubble.y):
#                     if not selected_bubble:
#                         selected_bubble = enemy_bubble
#                         drawing_line = True
#                         line_start = enemy_bubble
#                     elif selected_bubble and selected_bubble != enemy_bubble:
#                         connections.append((selected_bubble, enemy_bubble))
#                         selected_bubble = None
#                         drawing_line = False
#                         line_start = None
#                 else:
#                     selected_bubble = None
#                     drawing_line = False  # Stop drawing the line if clicked outside
#                     line_start = None

#                 # Handle button clicks
#                 if player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                     player_bubble.grow()
#                 elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                     player_bubble.attack_boost()
#                 elif enemy_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                     enemy_bubble.grow()
#                 elif enemy_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                     enemy_bubble.attack_boost()
                
#     # Draw and update bubbles
#     if not game_over:
#         player_bubble.update()
#         enemy_bubble.update()
    
#     player_bubble.draw(screen)
#     enemy_bubble.draw(screen)
    
#     # Draw the line to the mouse cursor if a bubble is selected
#     if drawing_line and line_start:
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), (mouse_x, mouse_y), 2)

#     # Draw the permanent connecting lines and manage the fight
#     for conn in connections:
#         pygame.draw.line(screen, BLACK, (conn[0].x, conn[0].y), (conn[1].x, conn[1].y), 2)
#         conn[1].population -= conn[0].attack_rate / FPS
#         conn[0].population -= BASE_ATTACK / FPS
        
#         if conn[1].population <= 0:
#             conn[1].population = 0
#             game_over = True
#             winner_text = font.render("Winner!", True, BLACK)
#             play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)
#         elif conn[0].population <= 0:
#             conn[0].population = 0
#             game_over = True
#             winner_text = font.render("Winner!", True, BLACK)
#             play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)
    
#     # Display winner text and "Play Again" button if game over
#     if game_over:
#         if conn[1].population == 0 and conn[0].population > 0:
#             screen.blit(winner_text, (conn[0].x - winner_text.get_width() // 2, conn[0].y - 60))
#         elif conn[0].population == 0 and conn[1].population > 0:
#             screen.blit(winner_text, (conn[1].x - winner_text.get_width() // 2, conn[1].y - 60))
        
#         # Draw "Play Again" button
#         if play_again_button:
#             pygame.draw.rect(screen, BLACK, play_again_button)
#             play_again_text = font.render("Play Again", True, WHITE)
#             screen.blit(play_again_text, (play_again_button.x + (play_again_button.width - play_again_text.get_width()) // 2, play_again_button.y + (play_again_button.height - play_again_text.get_height()) // 2))

#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()
# sys.exit()


# import pygame
# import sys
# import math

# # Initialize pygame
# pygame.init()

# # Game Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# FPS = 60

# # Bubble Properties
# POPULATION_INCREMENT = 1
# GROWTH_RATE = 1.5
# ATTACK_RATE = 1.2
# BASE_ATTACK = 3

# # Setup the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Bubbles")

# # Bubble Class
# class Bubble:
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.population = 10
#         self.growth_rate = POPULATION_INCREMENT
#         self.attack_rate = BASE_ATTACK
#         self.radius = 40
#         self.color = color
#         self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
#         self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

#     def draw(self, screen):
#         if self.population > 0:
#             pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#             population_text = font.render(str(int(self.population)), True, BLACK)
#             screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))
            
#             pygame.draw.rect(screen, WHITE, self.grow_button)
#             pygame.draw.rect(screen, WHITE, self.attack_button)
#             pygame.draw.rect(screen, BLACK, self.grow_button, 2)
#             pygame.draw.rect(screen, BLACK, self.attack_button, 2)
#             screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
#             screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

#     def update(self):
#         if self.population > 0:
#             self.population += self.growth_rate / FPS

#     def grow(self):
#         self.growth_rate = GROWTH_RATE

#     def attack_boost(self):
#         self.attack_rate = BASE_ATTACK * ATTACK_RATE

# # Initialize Font
# font = pygame.font.SysFont(None, 24)
# grow_text = font.render('Grow', True, BLACK)
# attack_text = font.render('Attack', True, BLACK)

# # Initialize bubbles with different colors
# def reset_game():
#     global player_bubble, enemy_bubble, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start, dragging, drag_start, drag_end
#     player_bubble = Bubble(200, 300, (0, 128, 255))  # Blue bubble
#     enemy_bubble = Bubble(600, 300, (255, 0, 0))     # Red bubble
#     selected_bubble = None
#     connections = []
#     game_over = False
#     winner_text = None
#     play_again_button = None
#     drawing_line = False  # Track whether a line is currently being drawn
#     line_start = None  # The starting bubble for the line
#     dragging = False  # Track whether the player is dragging the mouse
#     drag_start = None  # The starting point of the drag
#     drag_end = None  # The end point of the drag

# reset_game()

# # Function to check if two lines intersect
# def lines_intersect(p1, p2, p3, p4):
#     def ccw(A, B, C):
#         return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
#     return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# # Game Loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     screen.fill(WHITE)
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             dragging = True
#             drag_start = (mouse_x, mouse_y)
            
#             if game_over and play_again_button and play_again_button.collidepoint(mouse_x, mouse_y):
#                 reset_game()
#             elif not game_over:
#                 # Check if a bubble is clicked
#                 if player_bubble.radius > math.hypot(mouse_x - player_bubble.x, mouse_y - player_bubble.y):
#                     if not selected_bubble:
#                         selected_bubble = player_bubble
#                         drawing_line = True
#                         line_start = player_bubble
#                     elif selected_bubble and selected_bubble != player_bubble:
#                         connections.append((selected_bubble, player_bubble))
#                         selected_bubble = None
#                         drawing_line = False
#                         line_start = None
#                 elif enemy_bubble.radius > math.hypot(mouse_x - enemy_bubble.x, mouse_y - enemy_bubble.y):
#                     if not selected_bubble:
#                         selected_bubble = enemy_bubble
#                         drawing_line = True
#                         line_start = enemy_bubble
#                     elif selected_bubble and selected_bubble != enemy_bubble:
#                         connections.append((selected_bubble, enemy_bubble))
#                         selected_bubble = None
#                         drawing_line = False
#                         line_start = None
#                 else:
#                     selected_bubble = None
#                     drawing_line = False  # Stop drawing the line if clicked outside
#                     line_start = None

#                 # Handle button clicks
#                 if player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                     player_bubble.grow()
#                 elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                     player_bubble.attack_boost()
#                 elif enemy_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                     enemy_bubble.grow()
#                 elif enemy_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                     enemy_bubble.attack_boost()
#         elif event.type == pygame.MOUSEBUTTONUP:
#             dragging = False
#             drag_end = pygame.mouse.get_pos()

#             # Check if drag path intersects any connection lines
#             if drag_start and drag_end:
#                 for conn in connections[:]:
#                     bubble1 = conn[0]
#                     bubble2 = conn[1]
#                     if lines_intersect(drag_start, drag_end, (bubble1.x, bubble1.y), (bubble2.x, bubble2.y)):
#                         connections.remove(conn)
#                         break
                
#     # Draw and update bubbles
#     if not game_over:
#         player_bubble.update()
#         enemy_bubble.update()
    
#     player_bubble.draw(screen)
#     enemy_bubble.draw(screen)
    
#     # Draw the line to the mouse cursor if a bubble is selected
#     if drawing_line and line_start:
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), (mouse_x, mouse_y), 2)

#     # Draw the permanent connecting lines and manage the fight
#     for conn in connections:
#         pygame.draw.line(screen, BLACK, (conn[0].x, conn[0].y), (conn[1].x, conn[1].y), 2)
#         conn[1].population -= conn[0].attack_rate / FPS
#         conn[0].population -= BASE_ATTACK / FPS
        
#         if conn[1].population <= 0:
#             conn[1].population = 0
#             game_over = True
#             winner_text = font.render("Winner!", True, BLACK)
#             play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)
#         elif conn[0].population <= 0:
#             conn[0].population = 0
#             game_over = True
#             winner_text = font.render("Winner!", True, BLACK)
#             play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)
    
#     # Display winner text and "Play Again" button if game over
#     if game_over:
#         if conn[1].population == 0 and conn[0].population > 0:
#             screen.blit(winner_text, (conn[0].x - winner_text.get_width() // 2, conn[0].y - winner_text.get_height() // 2))
#         elif conn[0].population == 0 and conn[1].population > 0:
#             screen.blit(winner_text, (conn[1].x - winner_text.get_width() // 2, conn[1].y - winner_text.get_height() // 2))
#         pygame.draw.rect(screen, WHITE, play_again_button)
#         pygame.draw.rect(screen, BLACK, play_again_button, 2)
       
#         play_again_text = font.render("Play Again", True, BLACK)
#         screen.blit(play_again_text, (play_again_button.x + 5, play_again_button.y + 5))
    
#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()
# sys.exit()


# import pygame
# import sys
# import math

# # Initialize pygame
# pygame.init()

# # Game Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# FPS = 60

# # Bubble Properties
# POPULATION_INCREMENT = 1
# GROWTH_RATE = 1.5
# ATTACK_RATE = 1.2
# BASE_ATTACK = 3

# # Setup the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Bubbles")

# # Bubble Class
# class Bubble:
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.population = 10
#         self.growth_rate = POPULATION_INCREMENT
#         self.attack_rate = BASE_ATTACK
#         self.radius = 40
#         self.color = color
#         self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
#         self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

#     def draw(self, screen):
#         if self.population > 0:
#             pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#             population_text = font.render(str(int(self.population)), True, BLACK)
#             screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))
            
#             pygame.draw.rect(screen, WHITE, self.grow_button)
#             pygame.draw.rect(screen, WHITE, self.attack_button)
#             pygame.draw.rect(screen, BLACK, self.grow_button, 2)
#             pygame.draw.rect(screen, BLACK, self.attack_button, 2)
#             screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
#             screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

#     def update(self):
#         if self.population > 0:
#             self.population += self.growth_rate / FPS

#     def grow(self):
#         self.growth_rate = GROWTH_RATE

#     def attack_boost(self):
#         self.attack_rate = BASE_ATTACK * ATTACK_RATE

# # Initialize Font
# font = pygame.font.SysFont(None, 24)
# grow_text = font.render('Grow', True, BLACK)
# attack_text = font.render('Attack', True, BLACK)

# # Initialize bubbles with different colors
# def reset_game():
#     global player_bubble, enemy_bubble, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start, dragging, drag_start, drag_end
#     player_bubble = Bubble(200, 300, (0, 128, 255))  # Blue bubble
#     enemy_bubble = Bubble(600, 300, (255, 0, 0))     # Red bubble
#     selected_bubble = None
#     connections = []
#     game_over = False
#     winner_text = None
#     play_again_button = None
#     drawing_line = False  # Track whether a line is currently being drawn
#     line_start = None  # The starting bubble for the line
#     dragging = False  # Track whether the player is dragging the mouse
#     drag_start = None  # The starting point of the drag
#     drag_end = None  # The end point of the drag

# reset_game()

# # Function to check if two lines intersect
# def lines_intersect(p1, p2, p3, p4):
#     def ccw(A, B, C):
#         return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
#     return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# # Game Loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     screen.fill(WHITE)
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             dragging = True
#             drag_start = (mouse_x, mouse_y)
            
#             if game_over and play_again_button and play_again_button.collidepoint(mouse_x, mouse_y):
#                 reset_game()
#             elif not game_over:
#                 # Check if a bubble is clicked
#                 if player_bubble.radius > math.hypot(mouse_x - player_bubble.x, mouse_y - player_bubble.y):
#                     if not selected_bubble:
#                         selected_bubble = player_bubble
#                         drawing_line = True
#                         line_start = player_bubble
#                     elif selected_bubble and selected_bubble != player_bubble:
#                         connections.append((selected_bubble, player_bubble))
#                         selected_bubble = None
#                         drawing_line = False
#                         line_start = None
#                 elif enemy_bubble.radius > math.hypot(mouse_x - enemy_bubble.x, mouse_y - enemy_bubble.y):
#                     if not selected_bubble:
#                         selected_bubble = enemy_bubble
#                         drawing_line = True
#                         line_start = enemy_bubble
#                     elif selected_bubble and selected_bubble != enemy_bubble:
#                         connections.append((selected_bubble, enemy_bubble))
#                         selected_bubble = None
#                         drawing_line = False
#                         line_start = None
#                 else:
#                     selected_bubble = None
#                     drawing_line = False  # Stop drawing the line if clicked outside
#                     line_start = None

#                 # Handle button clicks
#                 if player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                     player_bubble.grow()
#                 elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                     player_bubble.attack_boost()
#                 elif enemy_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                     enemy_bubble.grow()
#                 elif enemy_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                     enemy_bubble.attack_boost()
#         elif event.type == pygame.MOUSEBUTTONUP:
#             dragging = False
#             drag_end = pygame.mouse.get_pos()

#             # Check if drag path intersects any connection lines
#             if drag_start and drag_end:
#                 for conn in connections[:]:
#                     bubble1 = conn[0]
#                     bubble2 = conn[1]
#                     if lines_intersect(drag_start, drag_end, (bubble1.x, bubble1.y), (bubble2.x, bubble2.y)):
#                         connections.remove(conn)
#                         break
    
#     # Update bubbles if game is not over
#     if not game_over:
#         player_bubble.update()
#         enemy_bubble.update()

#     # Draw bubbles and connections if game is not over
#     if not game_over:
#         player_bubble.draw(screen)
#         enemy_bubble.draw(screen)

#         # Draw the line to the mouse cursor if a bubble is selected
#         if drawing_line and line_start:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), (mouse_x, mouse_y), 2)

#         # Draw the permanent connecting lines and manage the fight
#         for conn in connections:
#             pygame.draw.line(screen, BLACK, (conn[0].x, conn[0].y), (conn[1].x, conn[1].y), 2)
#             conn[1].population -= conn[0].attack_rate / FPS
#             conn[0].population -= BASE_ATTACK / FPS

#             # Check if a bubble has lost all population
#             if conn[1].population <= 0:
#                 conn[1].population = 0
#                 connections.clear()
#                 game_over = True
#                 winner_text = font.render("Winner!", True, BLACK)
#                 play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)
#             elif conn[0].population <= 0:
#                 conn[0].population = 0
#                 connections.clear()
#                 game_over = True
#                 winner_text = font.render("Winner!", True, BLACK)
#                 play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)

#     # Handle game over state
#     if game_over:
#         # Draw the winning bubble
#         if player_bubble.population > 0:
#             player_bubble.draw(screen)
#         elif enemy_bubble.population > 0:
#             enemy_bubble.draw(screen)

#         # Display winner text and "Play Again" button
#         if winner_text:
#             if player_bubble.population > 0:
#                 screen.blit(winner_text, (player_bubble.x - winner_text.get_width() // 2, player_bubble.y - 60))
#             elif enemy_bubble.population > 0:
#                 screen.blit(winner_text, (enemy_bubble.x - winner_text.get_width() // 2, enemy_bubble.y - 60))
        
#         if play_again_button:
#             pygame.draw.rect(screen, WHITE, play_again_button)
#             pygame.draw.rect(screen, BLACK, play_again_button, 2)
#             play_again_text = font.render("Play Again", True, BLACK)
#             screen.blit(play_again_text, (play_again_button.x + (play_again_button.width - play_again_text.get_width()) // 2, play_again_button.y + (play_again_button.height - play_again_text.get_height()) // 2))
    
#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()
# sys.exit()


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
INITIAL_RADIUS = 40
SIZE_INCREASE_PERCENTAGE = 0.1  # 10%
POPULATION_THRESHOLD = 20
MAX_POPULATION = 101

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
        self.radius = INITIAL_RADIUS
        self.color = color
        self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
        self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

    def draw(self, screen):
        if self.population > 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius))
            population_text = font.render(str(int(self.population)), True, BLACK)
            screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))
            
            pygame.draw.rect(screen, WHITE, self.grow_button)
            pygame.draw.rect(screen, WHITE, self.attack_button)
            pygame.draw.rect(screen, BLACK, self.grow_button, 2)
            pygame.draw.rect(screen, BLACK, self.attack_button, 2)
            screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
            screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

    def update(self):
        if self.population > 0:
            self.population += self.growth_rate / FPS
            self.adjust_size()

    def adjust_size(self):
        # Adjust the size based on population thresholds
        if self.population <= MAX_POPULATION:
            size_increase_factor = 1 + SIZE_INCREASE_PERCENTAGE * (self.population // POPULATION_THRESHOLD - 1)
            self.radius = INITIAL_RADIUS * size_increase_factor

    def grow(self):
        self.growth_rate = GROWTH_RATE

    def attack_boost(self):
        self.attack_rate = BASE_ATTACK * ATTACK_RATE

# Initialize Font
font = pygame.font.SysFont(None, 24)
grow_text = font.render('Grow', True, BLACK)
attack_text = font.render('Attack', True, BLACK)

# Initialize bubbles with different colors
def reset_game():
    global player_bubble, enemy_bubble, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start, dragging, drag_start, drag_end
    player_bubble = Bubble(200, 300, (0, 128, 255))  # Blue bubble
    enemy_bubble = Bubble(600, 300, (255, 0, 0))     # Red bubble
    selected_bubble = None
    connections = []
    game_over = False
    winner_text = None
    play_again_button = None
    drawing_line = False  # Track whether a line is currently being drawn
    line_start = None  # The starting bubble for the line
    dragging = False  # Track whether the player is dragging the mouse
    drag_start = None  # The starting point of the drag
    drag_end = None  # The end point of the drag

reset_game()

# Function to check if two lines intersect
def lines_intersect(p1, p2, p3, p4):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dragging = True
            drag_start = (mouse_x, mouse_y)
            
            if game_over and play_again_button and play_again_button.collidepoint(mouse_x, mouse_y):
                reset_game()
            elif not game_over:
                # Check if a bubble is clicked
                if player_bubble.radius > math.hypot(mouse_x - player_bubble.x, mouse_y - player_bubble.y):
                    if not selected_bubble:
                        selected_bubble = player_bubble
                        drawing_line = True
                        line_start = player_bubble
                    elif selected_bubble and selected_bubble != player_bubble:
                        connections.append((selected_bubble, player_bubble))
                        selected_bubble = None
                        drawing_line = False
                        line_start = None
                elif enemy_bubble.radius > math.hypot(mouse_x - enemy_bubble.x, mouse_y - enemy_bubble.y):
                    if not selected_bubble:
                        selected_bubble = enemy_bubble
                        drawing_line = True
                        line_start = enemy_bubble
                    elif selected_bubble and selected_bubble != enemy_bubble:
                        connections.append((selected_bubble, enemy_bubble))
                        selected_bubble = None
                        drawing_line = False
                        line_start = None
                else:
                    selected_bubble = None
                    drawing_line = False  # Stop drawing the line if clicked outside
                    line_start = None

                # Handle button clicks
                if player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
                    player_bubble.grow()
                elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
                    player_bubble.attack_boost()
                elif enemy_bubble.grow_button.collidepoint(mouse_x, mouse_y):
                    enemy_bubble.grow()
                elif enemy_bubble.attack_button.collidepoint(mouse_x, mouse_y):
                    enemy_bubble.attack_boost()
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            drag_end = pygame.mouse.get_pos()

            # Check if drag path intersects any connection lines
            if drag_start and drag_end:
                for conn in connections[:]:
                    bubble1 = conn[0]
                    bubble2 = conn[1]
                    if lines_intersect(drag_start, drag_end, (bubble1.x, bubble1.y), (bubble2.x, bubble2.y)):
                        connections.remove(conn)
                        break
    
    # Update bubbles if game is not over
    if not game_over:
        player_bubble.update()
        enemy_bubble.update()

    # Draw bubbles and connections if game is not over
    if not game_over:
        player_bubble.draw(screen)
        enemy_bubble.draw(screen)

        # Draw the line to the mouse cursor if a bubble is selected
        if drawing_line and line_start:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), (mouse_x, mouse_y), 2)

        # Draw the permanent connecting lines and manage the fight
        for conn in connections:
            pygame.draw.line(screen, BLACK, (conn[0].x, conn[0].y), (conn[1].x, conn[1].y), 2)
            conn[1].population -= conn[0].attack_rate / FPS
            conn[0].population -= BASE_ATTACK / FPS

            # Check if a bubble has lost all population
            if conn[1].population <= 0:
                conn[1].population = 0
                connections.clear()
                game_over = True
                winner_text = font.render("Winner!", True, BLACK)
                play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)
            elif conn[0].population <= 0:
                conn[0].population = 0
                connections.clear()
                game_over = True
                winner_text = font.render("Winner!", True, BLACK)
                play_again_button = pygame.Rect(WIDTH//2 - 50, 20, 100, 40)

    # Handle game over state
    if game_over:
        # Draw the winning bubble
        if player_bubble.population > 0:
            player_bubble.draw(screen)
        elif enemy_bubble.population > 0:
            enemy_bubble.draw(screen)

        # Display winner text and "Play Again" button
        screen.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2, HEIGHT//2 - 20))
        pygame.draw.rect(screen, WHITE, play_again_button)
        pygame.draw.rect(screen, BLACK, play_again_button, 2)
        play_again_text = font.render("Play Again", True, BLACK)
        screen.blit(play_again_text, (play_again_button.x + (play_again_button.width - play_again_text.get_width()) // 2, play_again_button.y + (play_again_button.height - play_again_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
