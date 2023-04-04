import pygame
import time
import random

pygame.init()

# Set up display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up clock
clock = pygame.time.Clock()

# Load images
car_img = pygame.image.load('images/car.png')
car_width = 73

# Define functions
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: ' + str(count), True, black)
    game_display.blit(text, (0, 0))

def things(thing_x, thing_y, thing_w, thing_h, color):
    pygame.draw.rect(game_display, color, [thing_x, thing_y, thing_w, thing_h])

def car(x, y):
    game_display.blit(car_img, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surface, text_rect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        game_display.fill(white)

        things(thing_start_x, thing_start_y, thing_width, thing_height, black)
        thing_start_y += thing_speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_start_y + thing_height:
            if x > thing_start_x and x < thing_start_x + thing_width or x + car_width > thing_start_x and x + car_width < thing_start_x + thing_width:
                crash()

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()

game_loop

