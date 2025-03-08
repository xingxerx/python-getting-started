import pygame

def check_collision(obj1, obj2):
    """
    Check if two GameObjects are colliding.
    A collision is detected if the distance between their positions is 
    less than the sum of their collision radii.
    """
    # Calculate the distance vector between the two objects
    distance_vector = obj1.position - obj2.position
    # Get the actual distance
    distance = distance_vector.length()
    # Sum of the radii of both objects
    collision_threshold = obj1.collision_radius + obj2.collision_radius

    return distance < collision_threshold

# Optional: A function to resolve collision (e.g., a simple bounce)
def resolve_collision(obj1, obj2):
    """
    A simple collision response that swaps the velocities of the objects.
    This is just one possible way to handle collisions.
    """
    obj1.velocity, obj2.velocity = obj2.velocity, obj1.velocity
