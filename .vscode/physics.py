import pygame
class GameObject:
  def __init__(self, name, mass, velocity, acceleration, position):
    self.name = name
    self.mass = mass
    self.velocity = pygame.math.Vector3(velocity)
    self.acceleration = pygame.math.Vector3(acceleration)
    self.position = pygame.math.Vector3(position)
    self.collision_radius = 10  # default radius
# Example usage:
player_ship = GameObject("Player Ship", 1000, (0, 0, 0), (0, 0, 0), (100, 100, 0))
