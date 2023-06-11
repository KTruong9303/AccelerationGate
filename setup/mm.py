import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Define circle properties
circle1_radius = 50
circle1_color = (255, 0, 0)
circle1_pos = (200, 300)

circle2_radius = 30
circle2_color = (0, 0, 255)
circle2_pos = (400, 300)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the circles
    pygame.draw.circle(screen, circle1_color, circle1_pos, circle1_radius)
    pygame.draw.circle(screen, circle2_color, circle2_pos, circle2_radius)

    # Check for collision
    distance = math.sqrt((circle2_pos[0] - circle1_pos[0]) ** 2 + (circle2_pos[1] - circle1_pos[1]) ** 2)
    if distance <= circle1_radius + circle2_radius:
        collision_text = "Collision!"
        collision_color = (0, 255, 0)
    else:
        collision_text = "No collision"
        collision_color = (255, 0, 0)

    # Draw collision text
    font = pygame.font.Font(None, 36)
    text = font.render(collision_text, True, collision_color)
    text_rect = text.get_rect(center=(screen_width // 2, 50))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
