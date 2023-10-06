import pygame
import time
import random
import asyncio

# import tensorflow as tf
# # import tflearn
# from tflearn.layers.core import input_data, dropout, fully_connected
# from tflearn.layers.estimator import regression
# from statistics import mean, median
# from collections import Counter
# import numpy as np

# define tensors


from config.window import Window
from config.images import Images

pygame.init()

# create screen
window_width = 800
window_height = 600
window = Window("PySnake", window_width, window_height).create_window()

# COLORS
RED = (213, 50, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIENNA = (160, 82, 45)

background = Images().background
background = Images().scale(background, window_width, window_height)
game_over_background = Images().game_over
game_over_background = Images().scale(game_over_background, window_width, window_height)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("Pong-Game", 30)
score_font = pygame.font.SysFont("Pong-Game", 35)

def increase_speed(speed, score):
    if score % 4 == 0 and score != 0:
        speed += 1
    return speed

def high_scores(score):
    with open("high_scores.txt", "r") as f:
        high_scores = f.read()
    if int(score) > int(high_scores):
        with open("high_scores.txt", "w") as f:
            f.write(str(score))
    with open("high_scores.txt", "r") as f:
        high_scores = f.read()
    return high_scores

def high_score_board(score):
    high_score = high_scores(score)
    value = score_font.render("High Score: " + str(high_score), True, BLACK)
    window.blit(value, [0, 30])

def score_board(score):
    value = score_font.render("Score: " + str(score), True, BLACK)
    window.blit(value, [0, 0])

def snake(snake_size, snake_list):
    for s in snake_list:
        pygame.draw.rect(
            window,
            SIENNA,
            [
                s[0],
                s[1],
                snake_size,
                snake_size,
            ],
        )

def message(msg, color):
    message = font_style.render(msg, True, color)
    window.blit(message, [window_width/4, window_height/4])

def game_loop():
    game_over = False
    game_close = False
    
    x1 = window_width / 2
    y1 = window_height / 2 
    
    x1_change = 0
    y1_change = 0

    snake_size = 20
    snake_speed = 10

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, window_width - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, window_height - snake_size) / snake_size) * snake_size

    food = Images().food
    food = pygame.transform.scale(food, (snake_size, snake_size))

    while not game_over:
        
        while game_close == True:
            window.blit(game_over_background, (0, 0))
            message("You lost!    Q: Quit C: Play Again", RED)
            score_board(snake_length - 1)
            high_score_board(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size
                    
        # check if snake is out of bounds
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # fill screen
        window.blit(background, (0, 0))
        
        # draw food
        window.blit(food, (food_x, food_y))

        # draw snake
        snake_head = pygame.draw.rect(window, WHITE, [x1, y1, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        for s in snake_list[:-1]:
            if s == snake_head:
                game_close = True

        snake(snake_size, snake_list)

        # update score
        score = snake_length -1 
        score_board(score)


        # update screen
        pygame.display.update()

        # check if snake ate food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / snake_size) * snake_size 
            food_y = round(random.randrange(0, window_height - snake_size) / snake_size) * snake_size
            snake_length += 1

            # increase speed every 5 points
            snake_speed = increase_speed(snake_speed, score)

        # set fps
        clock.tick(snake_speed)
    

    pygame.quit()

    quit()

game_loop()