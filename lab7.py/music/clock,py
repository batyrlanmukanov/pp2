import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((828, 836))
done = False
background = pygame.image.load("images/main-clock.png")
left = pygame.image.load("images/left-hand.png")
right = pygame.image.load("images/right-hand.png")

left = pygame.transform.rotate(left, 90)
left_rect = left.get_rect()
left_rect.center = (414, 418)

right = pygame.transform.rotate(right, 90)
right_rect = right.get_rect()
right_rect.center = (414, 418)

while not done:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    current_time = datetime.datetime.now().time()

    sec_angle = -(current_time.second * 6)
    min_angle = -((current_time.minute + current_time.second/60) * 6)

    n_left = pygame.transform.rotate(left, sec_angle)
    n_right = pygame.transform.rotate(right, min_angle)

    left_rect = n_left.get_rect(center=(414, 418)) 
    right_rect = n_right.get_rect(center=(414, 418))
    screen.blit(n_left, left_rect.topleft)
    screen.blit(n_right, right_rect.topleft)

    pygame.display.flip()
    pygame.time.Clock().tick(1)
pygame.quit()