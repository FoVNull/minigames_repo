import pygame
import sys
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# Initialize Pygame
pygame.init()

# Game settings
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Example")

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)

# load image
cursor_image = pygame.image.load("img/envelope-small.png")
cursor_image_rect = cursor_image.get_rect()

target_image = pygame.image.load("img/sad_pocket.png")
target_image_rect = target_image.get_rect()

# Game variables
cursor_width = 3
cursor_height = 30
cursor_color = (205,92,92)
target_width = 50
target_height = 20
target_color = (144,238,144)
bar_width = width
bar_height = 20
bar_color = (255,144,0)
auto_move_speed = 6
time_limit = 5  # Time limit in seconds
font = pygame.font.Font(None, 36)  # Font settings

# Initial position of the cursor
cursor_x = width
cursor_y = height*0.9

# Initial position of the target
target_x = random.randint(200, width - target_width*2)
target_y = cursor_y
bar_x = 0
bar_y = cursor_y
bar_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height) # draw bar directly

# Game variables
success_count = 0
success_limit = 3
space_pressed = False  # Record whether the space key is pressed
cursor_movable = True  # Whether the cursor is allowed to move

# Distance to move when the space key is pressed
space_move_distance = 50

# Game loop
start_time = pygame.time.get_ticks() // 1000  # Get the start time of the game in seconds
while True:
    # Clear the screen
    screen.fill(white)

    # Calculate game time
    current_time = pygame.time.get_ticks() // 1000
    elapsed_time = current_time - start_time
    remaining_time = max(0, time_limit - elapsed_time)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space_pressed = True
        elif event.type == MOUSEBUTTONDOWN:
            # Check if the player clicked the window after a failure
            cursor_movable = True  # Allow the cursor to move
            if success_count < success_limit and remaining_time == 0:
                # Reset the game state
                success_count = 0
                target_x = random.randint(0, width - target_width)
                start_time = pygame.time.get_ticks() // 1000  # Reset the start time of the game
            else:
                space_pressed = True

    # Automatically move the cursor backward
    if cursor_movable:
        cursor_x -= auto_move_speed

    # Handle the space key
    if space_pressed and cursor_movable:
        cursor_x += space_move_distance
        space_pressed = False

    # Boundary check
    if cursor_x < 0:
        cursor_x = 0
    elif cursor_x > width - cursor_width:
        cursor_x = width - cursor_width

    # Update target position
    target_rect = pygame.Rect(target_x, target_y, target_width, target_height)
    target_image_rect.x = target_x - target_image_rect.width // 2
    target_image_rect.y = target_y - target_image_rect.height*1.1

    # Update cursor position
    cursor_rect = pygame.Rect(cursor_x, cursor_y, cursor_width, cursor_height)
    cursor_image_rect.x = cursor_x - cursor_image_rect.width // 2
    cursor_image_rect.y = cursor_y - cursor_image_rect.height*1.7

    if remaining_time == 0:
        if cursor_rect.colliderect(target_rect):
            success_count += 1
            if success_count >= success_limit:
                # After success 3 times, display a popup and exit the game
                target_image = pygame.image.load("img/pocket.png")
                target_image_rect = target_image.get_rect()
                target_image_rect.x = target_x - target_image_rect.width // 2
                target_image_rect.y = target_y - target_image_rect.height*1.1
                screen.blit(target_image, target_image_rect)
                text = font.render("Success!", True, black)
                screen.blit(text, (10, 10))
                pygame.display.flip()
                pygame.time.wait(10000)  # Close the window after 2 seconds
                pygame.quit()
                sys.exit()
            else:
                # Reset the position of the target
                target_x = random.randint(200, width - target_width)
                start_time = pygame.time.get_ticks() // 1000  # Reset the start time of the game
        else:
            text_fail = font.render("Game Over! Click to restart.", True, black)
            cursor_movable = False  # Prevent the cursor from moving
            screen.blit(text_fail, (50, 50))

    # Draw the cursor and target
    pygame.draw.rect(screen, bar_color, bar_rect)
    pygame.draw.rect(screen, target_color, target_rect)
    screen.blit(target_image, target_image_rect)
    pygame.draw.rect(screen, cursor_color, cursor_rect)
    screen.blit(cursor_image, cursor_image_rect)

    # Display the countdown
    text = font.render(f"Countdown: {remaining_time} seconds", True, black)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
