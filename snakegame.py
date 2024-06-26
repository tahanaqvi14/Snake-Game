import pygame
import random
import os

pygame.mixer.init()
pygame.init()


# pygame.mixer.music.load('do-not-wake-the-snake-164474.mp3')
# medium-explosion-40472
#beep-08b

# Colors

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))


main=pygame.image.load('snake1.jpg')
main=pygame.transform.scale(main,(screen_width,screen_height)).convert_alpha()

game=pygame.image.load('snake2.jpg')
game=pygame.transform.scale(game,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption("SnakezzzGame")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def gameloop():
    # Game specific variables
    pygame.time.delay(500)
    pygame.mixer.music.load('do-not-wake-the-snake-164474.mp3')
    pygame.mixer.music.play()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    if not(os.path.exists('hiscore.txt')):
        with open("hiscore.txt", "w") as f:
            hiscore = f.read()

    with open("hiscore.txt", "r") as f:
            hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps=30
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(main, (0,0))
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('beep-08b.mp3')
                        pygame.mixer.music.play()
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

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

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                sound_effect = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
                sound_effect.play()

                # pygame.mixer.music.load('')
                # pygame.mixer.music.play()
                
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(game, (0,0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load('medium-explosion-40472.mp3')
                pygame.mixer.music.play()
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('medium-explosion-40472.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
    
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(main, (0,0))
        text_screen('Welcome to Snake Game',white,250,250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('beep-08b.mp3')
                    pygame.mixer.music.play()
                    gameloop()      
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
welcome()