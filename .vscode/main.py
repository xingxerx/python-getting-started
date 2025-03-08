import pygame
from physics import GameObject
from collision import check_collision, resolve_collision

# Initialize Pygame
pygame.init()

# Window dimensions and creation
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Simulation")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Instantiate some game objects using your GameObject class from physics.py
player_ship = GameObject("Player Ship", 1000, (0, 0, 0), (0, 0, 0), (100, 100, 0))
enemy_ship = GameObject("Enemy Ship", 500, (0, 0, 0), (0, 0, 0), (150, 150, 0))

# Main simulation loop
running = True
while running:
    clock.tick(60)  # Limit to 60 FPS

    # Process events (like quitting the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update object properties
    player_ship.position += player_ship.velocity
    player_ship.velocity += player_ship.acceleration

    enemy_ship.position += enemy_ship.velocity
    enemy_ship.velocity += enemy_ship.acceleration

    # Check for collision between the player_ship and enemy_ship
    if check_collision(player_ship, enemy_ship):
        print("Collision detected between Player Ship and Enemy Ship!")
        resolve_collision(player_ship, enemy_ship)

    # Clear the screen with a black color
    window.fill((0, 0, 0))

    # Render our objects as circles for simplicity
    pygame.draw.circle(window, (0, 255, 0), (int(player_ship.position.x), int(player_ship.position.y)), player_ship.collision_radius)
    pygame.draw.circle(window, (255, 0, 0), (int(enemy_ship.position.x), int(enemy_ship.position.y)), enemy_ship.collision_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
