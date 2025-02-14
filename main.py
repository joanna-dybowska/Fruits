import pygame
import Box2D  # The main Box2D module
from Box2D.b2 import world, polygonShape, dynamicBody

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Box2D world setup
GRAVITY = (0, -10)  # Gravity pointing downward
world = world(gravity=GRAVITY, doSleep=True)

# Create ground body
ground_body = world.CreateStaticBody(position=(0, 10), shapes=polygonShape(box=(50, 1)))

# Create a dynamic body (e.g., a player)
player_body = world.CreateDynamicBody(position=(10, 20))
player_box = player_body.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3)
#

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Step the physics world (60Hz)
    time_step = 1.0 / 60
    velocity_iters = 6
    position_iters = 2
    world.Step(time_step, velocity_iters, position_iters)

    # Draw Box2D objects
    for body in world.bodies:
        for fixture in body.fixtures:
            shape = fixture.shape
            vertices = [(body.transform * v) * 10 for v in shape.vertices]  # Scale to pixels
            vertices = [(int(v[0]), HEIGHT - int(v[1])) for v in vertices]  # Flip Y-axis
            pygame.draw.polygon(screen, (0, 255, 0), vertices)

    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
