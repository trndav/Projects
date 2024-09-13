
# import pygame
# import sys
# import math
# import random

# # Initialize pygame
# pygame.init()

# # Game Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# FPS = 60

# # Bubble Properties
# POPULATION_INCREMENT = 0.9
# GROWTH_RATE = 1.5
# ATTACK_RATE = 1.2
# BASE_ATTACK = 3
# INITIAL_RADIUS = 40
# SIZE_INCREASE_PERCENTAGE = 0.1  # 10%
# POPULATION_THRESHOLD = 20
# MAX_POPULATION = 101
# NEUTRAL_POPULATION = 10
# NUM_NEUTRAL_BUBBLES = 2

# # Setup the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Bubbles")

# # Bubble Class
# # Bubble Class
# class Bubble:
#     def __init__(self, x, y, color, population=10, growth_rate=POPULATION_INCREMENT, is_neutral=False, is_player=False):
#         self.x = x
#         self.y = y
#         self.population = population
#         self.growth_rate = growth_rate
#         self.attack_rate = BASE_ATTACK
#         self.radius = INITIAL_RADIUS
#         self.color = color
#         self.is_neutral = is_neutral
#         self.is_player = is_player  # Track if this is the player bubble
#         self.growth_paused = False
#         self.growth_level = 0  # Track the number of times 'Grow' has been clicked

#         # Only player bubble has buttons
#         if self.is_player:
#             self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
#             self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

#     def draw(self, screen):
#         if self.population > 0:
#             pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius))
#             population_text = font.render(str(int(self.population)), True, BLACK)
#             screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))

#             # Only the player bubble shows the buttons
#             if self.is_player:
#                 pygame.draw.rect(screen, WHITE, self.grow_button)
#                 pygame.draw.rect(screen, WHITE, self.attack_button)
#                 pygame.draw.rect(screen, BLACK, self.grow_button, 2)
#                 pygame.draw.rect(screen, BLACK, self.attack_button, 2)
#                 screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
#                 screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

#     def update(self):
#         if self.population > 0 and not self.is_neutral and not self.growth_paused:
#             # Growth rate depends on growth level
#             self.population += (self.growth_rate * (1 + self.growth_level)) / FPS
#             self.adjust_size()

#     def adjust_size(self):
#         if self.population <= MAX_POPULATION:
#             size_increase_factor = 1 + SIZE_INCREASE_PERCENTAGE * (self.population // POPULATION_THRESHOLD - 1)
#             self.radius = INITIAL_RADIUS * size_increase_factor

#     def grow(self):
#         if not self.is_neutral and self.population > 10:
#             cost = 10 + (self.population - 10) * 0.5  # Calculate the cost: 10 + 50% of remaining population            
#             if self.population >= cost:  # Ensure the player has enough population to pay the cost
#                 self.population -= cost  # Deduct the cost from population
#                 self.growth_level += 1  # Increase growth level
#                 self.growth_rate = 1 + (self.growth_level * 0.2)  # Growth rate increases with each level
#             else:
#                 print("Not enough population to grow!")

#     def attack_boost(self):
#         if not self.is_neutral:
#             self.attack_rate = BASE_ATTACK * ATTACK_RATE

#     def fight(self, other_bubble):
#         if self.population > 0 and other_bubble.population > 0:
#             self.population -= other_bubble.attack_rate / FPS
#             other_bubble.population -= self.attack_rate / FPS

#             if self.population < 0:
#                 self.population = 0
#             if other_bubble.population < 0:
#                 other_bubble.population = 0

#         if self.is_neutral and self.population <= 0:
#             self.become_owned(other_bubble)

#         if other_bubble.is_neutral and other_bubble.population <= 0:
#             other_bubble.become_owned(self)

#     def become_owned(self, owner_bubble):
#         self.is_neutral = False
#         self.color = owner_bubble.color
#         self.population = 10
#         # Only assign buttons if the owner is the player
#         if owner_bubble.is_player:
#             self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
#             self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

#         connections_to_remove = []
#         for conn in connections:
#             if self in conn:
#                 connections_to_remove.append(conn)

#         for conn in connections_to_remove:
#             connections.remove(conn)


# # Initialize Font
# font = pygame.font.SysFont(None, 24)
# grow_text = font.render('Grow', True, BLACK)
# attack_text = font.render('Attack', True, BLACK)

# # Generate random position for neutral bubbles ensuring no overlap
# def generate_random_position(existing_bubbles, radius):
#     while True:
#         x = random.randint(radius, WIDTH - radius)
#         y = random.randint(radius, HEIGHT - radius)
#         new_bubble = Bubble(x, y, GREY, NEUTRAL_POPULATION, 0, True)

#         # Check for overlap with existing bubbles
#         overlap = False
#         for bubble in existing_bubbles:
#             distance = math.hypot(new_bubble.x - bubble.x, new_bubble.y - bubble.y)
#             if distance < new_bubble.radius + bubble.radius + 10:  # Ensure some distance
#                 overlap = True
#                 break

#         if not overlap:
#             return x, y

# # Initialize bubbles with different colors and positions
# def reset_game():
#     global player_bubble, enemy_bubble, neutral_bubbles, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start, dragging, drag_start, drag_end
#     player_bubble = Bubble(200, 300, (0, 128, 255), is_player=True)  # Blue bubble with buttons
#     enemy_bubble = Bubble(600, 300, (255, 0, 0))  # Red bubble without buttons

#     neutral_bubbles = []
#     for _ in range(NUM_NEUTRAL_BUBBLES):
#         x, y = generate_random_position([player_bubble, enemy_bubble] + neutral_bubbles, INITIAL_RADIUS)
#         neutral_bubble = Bubble(x, y, GREY, NEUTRAL_POPULATION, 0, True)
#         neutral_bubbles.append(neutral_bubble)

#     selected_bubble = None
#     connections = []
#     game_over = False
#     winner_text = None
#     play_again_button = None
#     drawing_line = False
#     line_start = None
#     dragging = False
#     drag_start = None
#     drag_end = None

# reset_game()

# # Function to check if two lines intersect
# def lines_intersect(p1, p2, p3, p4):
#     def ccw(A, B, C):
#         return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
#     return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# # Check if the player's drag intersects with a connection line
# def check_drag_intersection(drag_start, drag_end, conn_start, conn_end):
#     return lines_intersect(drag_start, drag_end, conn_start, conn_end)

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
#                 # Check if a bubble is clicked (player or enemy)
#                 bubbles = [player_bubble, enemy_bubble] + neutral_bubbles
#                 for bubble in bubbles:
#                     if bubble.radius > math.hypot(mouse_x - bubble.x, mouse_y - bubble.y):
#                         if not selected_bubble:
#                             selected_bubble = bubble
#                             drawing_line = True
#                             line_start = bubble
#                         elif selected_bubble and selected_bubble != bubble:
#                             connections.append((selected_bubble, bubble))
#                             selected_bubble = None
#                             drawing_line = False
#                             line_start = None
#                         break  # Stop checking other bubbles after the first hit

#                 # Handle button clicks for player and enemy bubbles
#                 if player_bubble.is_player:
#                     if player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                         player_bubble.grow()
#                     elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                         player_bubble.attack_boost()

#         elif event.type == pygame.MOUSEBUTTONUP:
#             dragging = False
#             drag_end = pygame.mouse.get_pos()

#             # Check for line-breaking intersections
#             broken_connections = []
#             for conn in connections:
#                 bubble1, bubble2 = conn[0], conn[1]
#                 conn_start = (bubble1.x, bubble1.y)
#                 conn_end = (bubble2.x, bubble2.y)
#                 if check_drag_intersection(drag_start, drag_end, conn_start, conn_end):
#                     broken_connections.append(conn)
            
#             # Remove the broken connections
#             for conn in broken_connections:
#                 connections.remove(conn)

#             # Reset drag positions
#             drag_start = None
#             drag_end = None

#         elif event.type == pygame.MOUSEMOTION and dragging:
#             drag_end = pygame.mouse.get_pos()

#     # Update bubble populations
#     if not game_over:
#         player_bubble.update()
#         enemy_bubble.update()
#         for neutral in neutral_bubbles:
#             neutral.update()

#     # Handle fighting between connected bubbles
#     for conn in connections:
#         bubble1, bubble2 = conn[0], conn[1]
#         bubble1.fight(bubble2)

#     # Check if the game is over
#     if player_bubble.population <= 0 or enemy_bubble.population <= 0:
#         game_over = True
#         winner = player_bubble if player_bubble.population > 0 else enemy_bubble
#         winner.growth_paused = True  # Stop the growth of the winning bubble
#         if player_bubble.population <= 0:
#             player_bubble.population = 0  # Hide the defeated bubble
#         if enemy_bubble.population <= 0:
#             enemy_bubble.population = 0  # Hide the defeated bubble

#     # Draw bubbles and connections
#     if not game_over:
#         player_bubble.draw(screen)
#         enemy_bubble.draw(screen)
#         for neutral in neutral_bubbles:
#             neutral.draw(screen)

#         # Draw connection lines
#         for conn in connections:
#             bubble1 = conn[0]
#             bubble2 = conn[1]
#             pygame.draw.line(screen, BLACK, (bubble1.x, bubble1.y), (bubble2.x, bubble2.y), 2)
        
#         # Draw line being dragged
#         if drawing_line and line_start:
#             mouse_pos = pygame.mouse.get_pos()
#             pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), mouse_pos, 2)
    
#     # Display winner and play again button if game is over
#     if game_over:
#         # Draw the winner bubble
#         winner.draw(screen)
#         winner_text = font.render("Winner!", True, BLACK)
#         screen.blit(winner_text, (winner.x + winner.radius + 10, winner.y - winner.radius // 2))
        
#         play_again_text = font.render("Play Again", True, BLACK)
#         play_again_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 40, 100, 30)
#         pygame.draw.rect(screen, WHITE, play_again_button)
#         pygame.draw.rect(screen, BLACK, play_again_button, 2)
#         screen.blit(play_again_text, (play_again_button.x + 10, play_again_button.y + 5))
    
#     # Update the display
#     pygame.display.flip()
#     clock.tick(FPS)

# # Quit the game
# pygame.quit()
# sys.exit()


# import pygame
# import sys
# import math
# import random

# # Initialize pygame
# pygame.init()

# # Game Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# FPS = 60

# # Bubble Properties
# POPULATION_INCREMENT = 0.9
# GROWTH_RATE = 1.5
# ATTACK_RATE = 1.2
# BASE_ATTACK = 3
# INITIAL_RADIUS = 40
# SIZE_INCREASE_PERCENTAGE = 0.1  # 10%
# POPULATION_THRESHOLD = 20
# MAX_POPULATION = 101
# NEUTRAL_POPULATION = 10
# NUM_NEUTRAL_BUBBLES = 2

# # Setup the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Bubbles")

# # Bubble Class
# class Bubble:
#     def __init__(self, x, y, color, population=10, growth_rate=POPULATION_INCREMENT, is_neutral=False, is_player=False):
#         self.x = x
#         self.y = y
#         self.population = population
#         self.growth_rate = growth_rate
#         self.attack_rate = BASE_ATTACK
#         self.radius = INITIAL_RADIUS
#         self.color = color
#         self.is_neutral = is_neutral
#         self.is_player = is_player  # Track if this is the player bubble
#         self.growth_paused = False
#         self.growth_level = 0  # Track the number of times 'Grow' has been clicked

#         # Only player bubble has buttons
#         if self.is_player:
#             self.grow_button = pygame.Rect(self.x - 60, self.y + 50, 60, 30)
#             self.attack_button = pygame.Rect(self.x + 5, self.y + 50, 60, 30)

#     def draw(self, screen):
#         if self.population > 0:
#             pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius))
#             population_text = font.render(str(int(self.population)), True, BLACK)
#             screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))

#             # Only the player bubble shows the buttons
#             if self.is_player:
#                 pygame.draw.rect(screen, WHITE, self.grow_button)
#                 pygame.draw.rect(screen, WHITE, self.attack_button)
#                 pygame.draw.rect(screen, BLACK, self.grow_button, 2)
#                 pygame.draw.rect(screen, BLACK, self.attack_button, 2)
#                 screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
#                 screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

#     def update(self):
#         if self.population > 0 and not self.is_neutral and not self.growth_paused:
#             # Growth rate depends on growth level
#             self.population += (self.growth_rate * (1 + self.growth_level)) / FPS
#             self.adjust_size()

#     def adjust_size(self):
#         if self.population <= MAX_POPULATION:
#             size_increase_factor = 1 + SIZE_INCREASE_PERCENTAGE * (self.population // POPULATION_THRESHOLD - 1)
#             self.radius = INITIAL_RADIUS * size_increase_factor

#     def grow(self):
#         if not self.is_neutral and self.population > 10:
#             cost = 10 + (self.population - 10) * 0.5  # Calculate the cost: 10 + 50% of remaining population            
#             if self.population >= cost:  # Ensure the player has enough population to pay the cost
#                 self.population -= cost  # Deduct the cost from population
#                 self.growth_level += 1  # Increase growth level
#                 self.growth_rate = 1 + (self.growth_level * 0.2)  # Growth rate increases with each level
#             else:
#                 print("Not enough population to grow!")

#     def attack_boost(self):
#         if not self.is_neutral:
#             self.attack_rate = BASE_ATTACK * ATTACK_RATE

#     def fight(self, other_bubble):
#         if self.population > 0 and other_bubble.population > 0:
#             self.population -= other_bubble.attack_rate / FPS
#             other_bubble.population -= self.attack_rate / FPS

#             if self.population < 0:
#                 self.population = 0
#             if other_bubble.population < 0:
#                 other_bubble.population = 0

#         if self.is_neutral and self.population <= 0:
#             self.become_owned(other_bubble)

#         if other_bubble.is_neutral and other_bubble.population <= 0:
#             other_bubble.become_owned(self)

#     def become_owned(self, owner_bubble):
#         self.is_neutral = False
#         self.color = owner_bubble.color
#         self.population = 10

#         # Inherit the growth rate and growth level of the owner bubble
#         self.growth_rate = owner_bubble.growth_rate
#         self.growth_level = owner_bubble.growth_level
#         self.growth_paused = owner_bubble.growth_paused  # Inherit whether growth is paused

#         # Only assign buttons if the owner is the player
#         if owner_bubble.is_player:
#             self.is_player = False  # Conquered bubble is player-controlled but doesn't get buttons

#         connections_to_remove = []
#         for conn in connections:
#             if self in conn:
#                 connections_to_remove.append(conn)

#         for conn in connections_to_remove:
#             connections.remove(conn)


# # Initialize Font
# font = pygame.font.SysFont(None, 24)
# grow_text = font.render('Grow', True, BLACK)
# attack_text = font.render('Attack', True, BLACK)

# # Generate random position for neutral bubbles ensuring no overlap
# def generate_random_position(existing_bubbles, radius):
#     while True:
#         x = random.randint(radius, WIDTH - radius)
#         y = random.randint(radius, HEIGHT - radius)
#         new_bubble = Bubble(x, y, GREY, NEUTRAL_POPULATION, 0, True)

#         # Check for overlap with existing bubbles
#         overlap = False
#         for bubble in existing_bubbles:
#             distance = math.hypot(new_bubble.x - bubble.x, new_bubble.y - bubble.y)
#             if distance < new_bubble.radius + bubble.radius + 10:  # Ensure some distance
#                 overlap = True
#                 break

#         if not overlap:
#             return x, y

# # Initialize bubbles with different colors and positions
# def reset_game():
#     global player_bubble, enemy_bubble, neutral_bubbles, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start, dragging, drag_start, drag_end
#     player_bubble = Bubble(200, 300, (0, 128, 255), is_player=True)  # Blue bubble with buttons
#     enemy_bubble = Bubble(600, 300, (255, 0, 0))  # Red bubble without buttons

#     neutral_bubbles = []
#     for _ in range(NUM_NEUTRAL_BUBBLES):
#         x, y = generate_random_position([player_bubble, enemy_bubble] + neutral_bubbles, INITIAL_RADIUS)
#         neutral_bubble = Bubble(x, y, GREY, NEUTRAL_POPULATION, 0, True)
#         neutral_bubbles.append(neutral_bubble)

#     selected_bubble = None
#     connections = []
#     game_over = False
#     winner_text = None
#     play_again_button = None
#     drawing_line = False
#     line_start = None
#     dragging = False
#     drag_start = None
#     drag_end = None

# reset_game()

# # Function to check if two lines intersect
# def lines_intersect(p1, p2, p3, p4):
#     def ccw(A, B, C):
#         return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
#     return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# # Check if the player's drag intersects with a connection line
# def check_drag_intersection(drag_start, drag_end, conn_start, conn_end):
#     return lines_intersect(drag_start, drag_end, conn_start, conn_end)

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
#                 # Check if a bubble is clicked (player or enemy)
#                 bubbles = [player_bubble, enemy_bubble] + neutral_bubbles
#                 for bubble in bubbles:
#                     if bubble.radius > math.hypot(mouse_x - bubble.x, mouse_y - bubble.y):
#                         if not selected_bubble:
#                             selected_bubble = bubble
#                             drawing_line = True
#                             line_start = bubble
#                         elif selected_bubble and selected_bubble != bubble:
#                             connections.append((selected_bubble, bubble))
#                             selected_bubble = None
#                             drawing_line = False
#                             line_start = None
#                         break  # Stop checking other bubbles after the first hit

#                 # Handle button clicks for player and enemy bubbles
#                 if player_bubble.is_player:
#                     if player_bubble.grow_button.collidepoint(mouse_x, mouse_y):
#                         player_bubble.grow()
#                     elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y):
#                         player_bubble.attack_boost()

#         elif event.type == pygame.MOUSEBUTTONUP:
#             dragging = False
#             drag_end = pygame.mouse.get_pos()

#             # Check for line-breaking intersections
#             broken_connections = []
#             for conn in connections:
#                 bubble1, bubble2 = conn[0], conn[1]
#                 conn_start = (bubble1.x, bubble1.y)
#                 conn_end = (bubble2.x, bubble2.y)
#                 if check_drag_intersection(drag_start, drag_end, conn_start, conn_end):
#                     broken_connections.append(conn)
            
#             # Remove the broken connections
#             for conn in broken_connections:
#                 connections.remove(conn)

#             # Reset drag positions
#             drag_start = None
#             drag_end = None

#         elif event.type == pygame.MOUSEMOTION and dragging:
#             drag_end = pygame.mouse.get_pos()

#     # Update bubble populations
#     if not game_over:
#         player_bubble.update()
#         enemy_bubble.update()
#         for neutral in neutral_bubbles:
#             neutral.update()

#     # Handle fighting between connected bubbles
#     for conn in connections:
#         bubble1, bubble2 = conn[0], conn[1]
#         bubble1.fight(bubble2)

#     # Check if the game is over
#     if player_bubble.population <= 0 or enemy_bubble.population <= 0:
#         game_over = True
#         winner = player_bubble if player_bubble.population > 0 else enemy_bubble
#         winner.growth_paused = True  # Stop the growth of the winning bubble
#         if player_bubble.population <= 0:
#             player_bubble.population = 0  # Hide the defeated bubble
#         if enemy_bubble.population <= 0:
#             enemy_bubble.population = 0  # Hide the defeated bubble

#     # Draw bubbles and connections
#     if not game_over:
#         player_bubble.draw(screen)
#         enemy_bubble.draw(screen)
#         for neutral in neutral_bubbles:
#             neutral.draw(screen)

#         # Draw connection lines
#         for conn in connections:
#             bubble1 = conn[0]
#             bubble2 = conn[1]
#             pygame.draw.line(screen, BLACK, (bubble1.x, bubble1.y), (bubble2.x, bubble2.y), 2)
        
#         # Draw line being dragged
#         if drawing_line and line_start:
#             mouse_pos = pygame.mouse.get_pos()
#             pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), mouse_pos, 2)
    
#     # Display winner and play again button if game is over
#     if game_over:
#         # Draw the winner bubble
#         winner.draw(screen)
#         winner_text = font.render("Winner!", True, BLACK)
#         screen.blit(winner_text, (winner.x + winner.radius + 10, winner.y - winner.radius // 2))
        
#         play_again_text = font.render("Play Again", True, BLACK)
#         play_again_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 40, 100, 30)
#         pygame.draw.rect(screen, WHITE, play_again_button)
#         pygame.draw.rect(screen, BLACK, play_again_button, 2)
#         screen.blit(play_again_text, (play_again_button.x + 10, play_again_button.y + 5))
    
#     # Update the display
#     pygame.display.flip()
#     clock.tick(FPS)

# # Quit the game
# pygame.quit()
# sys.exit()



import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
FPS = 60

# Bubble Properties
POPULATION_INCREMENT = 0.9
GROWTH_RATE = 1.5
ATTACK_RATE = 1.2
BASE_ATTACK = 3
INITIAL_RADIUS = 40
SIZE_INCREASE_PERCENTAGE = 0.1  # 10%
POPULATION_THRESHOLD = 20
MAX_POPULATION = 101
NEUTRAL_POPULATION = 10
NUM_NEUTRAL_BUBBLES = 2

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubbles")

# Screen split percentages
GAME_AREA_HEIGHT_PERCENT = 0.9  # 90% of the screen for gameplay
UI_AREA_HEIGHT_PERCENT = 0.1    # 10% of the screen for UI (buttons)

# New dimensions for the game area and the UI area
GAME_AREA_HEIGHT = int(HEIGHT * GAME_AREA_HEIGHT_PERCENT)
UI_AREA_HEIGHT = int(HEIGHT * UI_AREA_HEIGHT_PERCENT)

# Bubble Class
class Bubble:
    def __init__(self, x, y, color, population=10, growth_rate=POPULATION_INCREMENT, is_neutral=False, is_player=False):
        self.x = x
        self.y = y
        self.population = population
        self.growth_rate = growth_rate
        self.attack_rate = BASE_ATTACK
        self.radius = INITIAL_RADIUS
        self.color = color
        self.is_neutral = is_neutral
        self.is_player = is_player  # Track if this is the player bubble
        self.growth_paused = False
        self.growth_level = 0  # Track the number of times 'Grow' has been clicked

        # Only player bubble has buttons, placed in the UI area (bottom 10%)
        if self.is_player:
            self.grow_button = pygame.Rect(WIDTH // 2 - 70, GAME_AREA_HEIGHT + 10, 60, 30)
            self.attack_button = pygame.Rect(WIDTH // 2 + 10, GAME_AREA_HEIGHT + 10, 60, 30)

    def draw(self, screen):
        if self.population > 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius))
            population_text = font.render(str(int(self.population)), True, BLACK)
            screen.blit(population_text, (self.x - population_text.get_width() // 2, self.y - population_text.get_height() // 2))

            # Only the player bubble shows the buttons
            if self.is_player:
                pygame.draw.rect(screen, WHITE, self.grow_button)
                pygame.draw.rect(screen, WHITE, self.attack_button)
                pygame.draw.rect(screen, BLACK, self.grow_button, 2)
                pygame.draw.rect(screen, BLACK, self.attack_button, 2)
                screen.blit(grow_text, (self.grow_button.x + 5, self.grow_button.y + 5))
                screen.blit(attack_text, (self.attack_button.x + 5, self.attack_button.y + 5))

    def update(self):
        if self.population > 0 and not self.is_neutral and not self.growth_paused:
            # Growth rate depends on growth level
            self.population += (self.growth_rate * (1 + self.growth_level)) / FPS
            self.adjust_size()

    def adjust_size(self):
        if self.population <= MAX_POPULATION:
            size_increase_factor = 1 + SIZE_INCREASE_PERCENTAGE * (self.population // POPULATION_THRESHOLD - 1)
            self.radius = INITIAL_RADIUS * size_increase_factor

    def grow(self):
        if not self.is_neutral and self.population > 10:
            cost = 10 + (self.population - 10) * 0.5  # Calculate the cost: 10 + 50% of remaining population            
            if self.population >= cost:  # Ensure the player has enough population to pay the cost
                self.population -= cost  # Deduct the cost from population
                self.growth_level += 1  # Increase growth level
                self.growth_rate = 1 + (self.growth_level * 0.2)  # Growth rate increases with each level
            else:
                print("Not enough population to grow!")

    def attack_boost(self):
        if not self.is_neutral:
            self.attack_rate = BASE_ATTACK * ATTACK_RATE

    def fight(self, other_bubble):
        if self.population > 0 and other_bubble.population > 0:
            self.population -= other_bubble.attack_rate / FPS
            other_bubble.population -= self.attack_rate / FPS

            if self.population < 0:
                self.population = 0
            if other_bubble.population < 0:
                other_bubble.population = 0

        if self.is_neutral and self.population <= 0:
            self.become_owned(other_bubble)

        if other_bubble.is_neutral and other_bubble.population <= 0:
            other_bubble.become_owned(self)

    def become_owned(self, owner_bubble):
        self.is_neutral = False
        self.color = owner_bubble.color
        self.population = 10

        # Inherit the growth rate and growth level of the owner bubble
        self.growth_rate = owner_bubble.growth_rate
        self.growth_level = owner_bubble.growth_level
        self.growth_paused = owner_bubble.growth_paused  # Inherit whether growth is paused

        # Only assign buttons if the owner is the player
        if owner_bubble.is_player:
            self.is_player = False  # Conquered bubble is player-controlled but doesn't get buttons

        connections_to_remove = []
        for conn in connections:
            if self in conn:
                connections_to_remove.append(conn)

        for conn in connections_to_remove:
            connections.remove(conn)


# Initialize Font
font = pygame.font.SysFont(None, 24)
grow_text = font.render('Grow', True, BLACK)
attack_text = font.render('Attack', True, BLACK)

# Generate random position for neutral bubbles ensuring no overlap
def generate_random_position(existing_bubbles, radius):
    while True:
        x = random.randint(radius, WIDTH - radius)
        # Restrict Y-coordinate to be within the top 90% of the screen
        max_y = int(HEIGHT * 0.9) - radius  # Top 90% of the screen minus the bubble radius
        y = random.randint(radius, max_y)
        new_bubble = Bubble(x, y, GREY, NEUTRAL_POPULATION, 0, True)

        # Check for overlap with existing bubbles
        overlap = False
        for bubble in existing_bubbles:
            distance = math.hypot(new_bubble.x - bubble.x, new_bubble.y - bubble.y)
            if distance < new_bubble.radius + bubble.radius + 10:  # Ensure some distance
                overlap = True
                break

        if not overlap:
            return x, y

# Initialize bubbles with different colors and positions
def reset_game():
    global player_bubble, enemy_bubble, neutral_bubbles, selected_bubble, connections, game_over, winner_text, play_again_button, drawing_line, line_start, dragging, drag_start, drag_end
    player_bubble = Bubble(200, 300, (0, 128, 255), is_player=True)  # Blue bubble with buttons
    enemy_bubble = Bubble(600, 300, (255, 0, 0))  # Red bubble without buttons

    neutral_bubbles = []
    for _ in range(NUM_NEUTRAL_BUBBLES):
        x, y = generate_random_position([player_bubble, enemy_bubble] + neutral_bubbles, INITIAL_RADIUS)
        neutral_bubble = Bubble(x, y, GREY, NEUTRAL_POPULATION, 0, True)
        neutral_bubbles.append(neutral_bubble)

    selected_bubble = None
    connections = []
    game_over = False
    winner_text = None
    play_again_button = None
    drawing_line = False
    line_start = None
    dragging = False
    drag_start = None
    drag_end = None

reset_game()

# Function to check if two lines intersect
def lines_intersect(p1, p2, p3, p4):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# Check if the player's drag intersects with a connection line
def check_drag_intersection(drag_start, drag_end, conn_start, conn_end):
    return lines_intersect(drag_start, drag_end, conn_start, conn_end)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    # Fill the game area (top 90%)
    screen.fill(WHITE, pygame.Rect(0, 0, WIDTH, GAME_AREA_HEIGHT))

    # Fill the UI area (bottom 10%) for buttons
    pygame.draw.rect(screen, GREY, pygame.Rect(0, GAME_AREA_HEIGHT, WIDTH, UI_AREA_HEIGHT))

    
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
                # Check if a bubble is clicked (player or enemy)
                bubbles = [player_bubble, enemy_bubble] + neutral_bubbles
                for bubble in bubbles:
                    if bubble.radius > math.hypot(mouse_x - bubble.x, mouse_y - bubble.y):
                        if not selected_bubble:
                            selected_bubble = bubble
                            drawing_line = True
                            line_start = bubble
                        elif selected_bubble and selected_bubble != bubble:
                            connections.append((selected_bubble, bubble))
                            selected_bubble = None
                            drawing_line = False
                            line_start = None
                        break  # Stop checking other bubbles after the first hit

                # Handle button clicks for player bubbles (buttons are now in the UI area)
                if player_bubble.is_player:
                    if player_bubble.grow_button.collidepoint(mouse_x, mouse_y) and mouse_y > GAME_AREA_HEIGHT:
                        player_bubble.grow()
                    elif player_bubble.attack_button.collidepoint(mouse_x, mouse_y) and mouse_y > GAME_AREA_HEIGHT:
                        player_bubble.attack_boost()

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            drag_end = pygame.mouse.get_pos()

            # Check for line-breaking intersections
            broken_connections = []
            for conn in connections:
                bubble1, bubble2 = conn[0], conn[1]
                conn_start = (bubble1.x, bubble1.y)
                conn_end = (bubble2.x, bubble2.y)
                if check_drag_intersection(drag_start, drag_end, conn_start, conn_end):
                    broken_connections.append(conn)
            
            # Remove the broken connections
            for conn in broken_connections:
                connections.remove(conn)

            # Reset drag positions
            drag_start = None
            drag_end = None

        elif event.type == pygame.MOUSEMOTION and dragging:
            drag_end = pygame.mouse.get_pos()

    # Update bubble populations
    if not game_over:
        player_bubble.update()
        enemy_bubble.update()
        for neutral in neutral_bubbles:
            neutral.update()

    # Handle fighting between connected bubbles
    for conn in connections:
        bubble1, bubble2 = conn[0], conn[1]
        bubble1.fight(bubble2)

    # Check if the game is over
    if player_bubble.population <= 0 or enemy_bubble.population <= 0:
        game_over = True
        winner = player_bubble if player_bubble.population > 0 else enemy_bubble
        winner.growth_paused = True  # Stop the growth of the winning bubble
        if player_bubble.population <= 0:
            player_bubble.population = 0  # Hide the defeated bubble
        if enemy_bubble.population <= 0:
            enemy_bubble.population = 0  # Hide the defeated bubble

    # Draw bubbles and connections
    if not game_over:
        player_bubble.draw(screen)
        enemy_bubble.draw(screen)
        for neutral in neutral_bubbles:
            neutral.draw(screen)

        # Draw connection lines
        for conn in connections:
            bubble1 = conn[0]
            bubble2 = conn[1]
            pygame.draw.line(screen, BLACK, (bubble1.x, bubble1.y), (bubble2.x, bubble2.y), 2)
        
        # Draw line being dragged
        if drawing_line and line_start:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, BLACK, (line_start.x, line_start.y), mouse_pos, 2)
    
    # Display winner and play again button if game is over
    if game_over:
        # Draw the winner bubble
        winner.draw(screen)
        winner_text = font.render("Winner!", True, BLACK)
        screen.blit(winner_text, (winner.x + winner.radius + 10, winner.y - winner.radius // 2))
        
        play_again_text = font.render("Play Again", True, BLACK)
        play_again_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 40, 100, 30)
        pygame.draw.rect(screen, WHITE, play_again_button)
        pygame.draw.rect(screen, BLACK, play_again_button, 2)
        screen.blit(play_again_text, (play_again_button.x + 10, play_again_button.y + 5))
    
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
