import pygame
pygame.mixer.init()

pygame.init()
screen = pygame.display.set_mode((800, 800))

songs = ["music/Bôa - Duvet.mp3", "music/Yung Lean - Ginseng Strip.mp3", "music/Radiohead - Creep.mp3", "music/Kiss - I Was Made For Loving You.mp3",]
current_music = 0
pygame.mixer.music.load(songs[current_music])
pygame.mixer.music.play()
background = pygame.image.load("music/back.jpg")
background_rect = background.get_rect()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()
pygame.quit()