import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)


import pygame
from testinho import Testinho
from asteroid import Asteroid
import random
from shot import Shot

# inicializando o Pygame e criando Janela
pygame.init()

display = pygame.display.set_mode([840, 480]) # tamanho do "canvas"
pygame.display.set_caption("Meu Primeiro Jogo") # altera nome da janela


# Objects
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()
#background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/fundo.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

testinho = Testinho(objectGroup)

# music

pygame.mixer.music.load("data/fundo.mp3")
pygame.mixer.music.play(-1)

#sound
shoot = pygame.mixer.Sound("data/laser.mp3")

gameLoop = True
gameover = False
timer = 20
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shoot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = testinho.rect.center




        #Update and draw
        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.5:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup)
                    print("new Asteroid")


            collisions = pygame.sprite.spritecollide(testinho, asteroidGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print("GAME OVER!")
                gameover = True
                bg.image = pygame.image.load("data/fundo_game_over.jpg")


            hits = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

        display.fill([46, 46, 46])  # preenchendo com cor(RGB)
        objectGroup.draw(display)

        pygame.display.update()# fica atualizando o display



