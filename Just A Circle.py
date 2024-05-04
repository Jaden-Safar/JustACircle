import pygame
import sys
import math

# Change the "Path\To\Your.ico to what ever you like"
img = pygame.image.load(r'Path\To\your.ico')
pygame.display.set_icon(img)

pygame.display.set_caption("Just A Circle")

pygame.init()
width, height = 144, 144
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

White = (255, 255, 200)
Blue = (0, 208, 241)

center = (width // 2, height // 2)
radius = 50
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(White)

    x = center[0] + int(radius * math.cos(angle))
    y = center[1] + int(radius * math.sin(angle))

    pygame.draw.circle(screen, Blue, (x, y), 10)
    pygame.display.flip()
    angle += 0.1
    clock.tick(60)

pygame.quit()
sys.exit()
