# Import the pygame module

import pygame

# Intialize pygame module
# x = pygame.init()
# print(x)

import random

"""
init() initialize all imported pygame modules. No exceptions will be raised if a module fails, but
the total number if successful and failed inits will be returned as a tuple
"""
pygame.init()
# For music
pygame.mixer.init()

# Define Colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0 ,0)
dark_brown = (86, 1 ,0)
green = (25, 196, 13)

# To set the game display :
# gameWindow = pygame.display.set_mode((Width, Height))
gameWindow = pygame.display.set_mode((1000, 600))

# Background image work
backimg = pygame.image.load('bgimg.png')
backimg = pygame.transform.scale(backimg, (1000, 600)).convert_alpha()

# Create a game title
pygame.display.set_caption("Snack Survival")
pygame.display.update()

# Game specific Variables we required to create a game :
exit_game = False
game_Over = False

# Variables of Snack Head
head_x = 45
head_y = 45
head_size = 12

# Variable of times related
clock = pygame.time.Clock()
# Frames per second ( How many frames we get in 1 second )
fps = 60

# Variable of velocity
velocity_x = 0
velocity_y = 0
init_velocity = 5

# Variables to create a snack food
food_x = random.randint(20, 1000)
food_y = random.randint(20, 600)
food_radius = 9

# Variables of score
score = 0
font = pygame.font.SysFont('arialblack', 25)

# Saw your score on game screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snack(gameWindow, colour, snk_list, head_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, head_size, head_size])

# Variable of times related
clock = pygame.time.Clock()
# Frames per second ( How many frames we get in 1 second )
fps = 60

# Creating a game loop
# If game is not exit, handle the events

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((green))
        welcomebg = pygame.image.load('snack_icon.png')
        gameWindow.blit(welcomebg, (40, 20))
        text_screen("Snack Survival", white, 500, 120)
        text_screen("Created by : Datt Panchal", white, 430, 180)
        text_screen("Press Space Bar To Start !", white, 430, 290)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bg.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():

    # Game specific Variables we required to create a game :
    exit_game = False
    game_Over = False

    # Variables of Snack Head
    head_x = 45
    head_y = 45
    head_size = 12

    # Variable of velocity
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5

    # Variables to create a snack food
    food_x = random.randint(20, 800)
    food_y = random.randint(20, 500)

    # Variables of score
    score = 0

    # Snack length related variables
    snk_list = []
    snk_length = 1

    # High score
    with open('High_Score', "r") as f:
        hiscore = f.read()

    while not exit_game:

        if game_Over:
            with open('High_Score', "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(green)
            game_over_bg = pygame.image.load('game_over_icon.png')
            gameWindow.blit(game_over_bg, (270, 100))
            text_screen("Game Over !", white, 420, 350)
            text_screen("Pree Enter To Try Again", white, 340, 390)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                # Handles the arrow keys
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Cheat code
                    # if event.key == pygame.K_q:
                    #     score += 10

                    # For quit
                    if event.key == pygame.K_q:
                           exit_game = True


            # Select the windows or game display colour
            gameWindow.fill(white)
            gameWindow.blit(backimg, (0, 0))

            # Velocity Code
            head_x = head_x + velocity_x
            head_y = head_y + velocity_y

            if abs(head_x - food_x) < 14 and abs(head_y - food_y) < 14:
                eating_sound = pygame.mixer.Sound('beep.mp3')
                eating_sound.play()
                score += 2
                # print("Score : ", score)
                food_x = random.randint(50, 400)
                food_y = random.randint(50, 300)
                snk_length += 3

                if score > int(hiscore):
                    hiscore = score

            head = []
            head.append(head_x)
            head.append(head_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_Over = True
                pygame.mixer.music.load('game_over.wav')
                pygame.mixer.music.play()

            if head_x < 0 or head_x > 1000 or head_y < 0 or head_y > 600:
                game_Over = True
                pygame.mixer.music.load('game_over.wav')
                pygame.mixer.music.play()

                # print("Game Over")

            text_screen("Score : " + str(score) + "  High-Score : " + str(hiscore), white, 5, 5)
            text_screen("Press 'Q' For Quit This Game !", white, 610, 566)

            # Creat a snack head
            pygame.draw.rect(gameWindow, black, [head_x, head_y, head_size, head_size])

            # Create a snack food
            # pygame.draw.rect(gameWindow, red, [food_x, food_y, head_size, head_size])
            pygame.draw.circle(gameWindow, red, [food_x, food_y], food_radius )

            # plot_snk(gameWindow, colour, [x, y, size])
            plot_snack(gameWindow, black, snk_list, head_size)

        pygame.display.update()
        clock.tick(fps)

    # After run the loop or exit the game
    pygame.quit()
    quit()

welcome()
# gameloop()

