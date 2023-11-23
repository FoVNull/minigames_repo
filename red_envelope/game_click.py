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

target_image = pygame.image.load("img/sad_pocket_popup.png")
target_image_rect = target_image.get_rect()

# Game variables
cursor_width = 3
cursor_height = 30
cursor_color = (205, 92, 92)
target_width = 50
target_height = 20
target_color = (144, 238, 144)
bar_width = width
bar_height = 20
bar_color = (255, 144, 0)
cursor_speed = 6  # Speed at which the cursor moves

# Initial position of the cursor
cursor_x = width // 2 - cursor_width // 2
cursor_y = height * 0.9

# Initial position of the target
target_x = random.randint(200, width - target_width * 2)
target_y = cursor_y
bar_x = 0
bar_y = cursor_y
bar_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)  # draw bar directly

target_rect = pygame.Rect(target_x, target_y, target_width, target_height)
cursor_rect = pygame.Rect(cursor_x, cursor_y, cursor_width, cursor_height)

# Game variables
success_count = 0
success_limit = 3
cursor_movable = True  # Whether the cursor is allowed to move
cursor_direction = 1  # 1 represents moving to the right, -1 represents moving to the left
font = pygame.font.Font(None, 36)  # Font settings

text_fail = None

# Game loop
while True:
    # Clear the screen
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Check if the player clicked the window after a failure
            if success_count < success_limit and cursor_movable:
                if target_rect.colliderect(cursor_rect):
                    success_count += 1
                    if success_count >= success_limit:
                        # After success 3 times, display a popup and exit the game
                        target_image = pygame.image.load("img/pocket.png")
                        target_image_rect = target_image.get_rect()
                        target_image_rect.x = target_x - target_image_rect.width // 2
                        target_image_rect.y = target_y - target_image_rect.height * 1.1
                        screen.blit(target_image, target_image_rect)
                        text = font.render("Success!", True, black)
                        screen.blit(text, (10, 10))
                        pygame.display.flip()
                        pygame.time.wait(3000)  # Close the window after 2 seconds
                        pygame.quit()
                        sys.exit()
                    else:
                        # Reset the position of the target for the next round
                        target_width -= 12
                        cursor_speed += 6
                        target_x = random.randint(target_image_rect.width, width - target_image_rect.width)
                else:
                    target_width = 50
                    cursor_speed = 6
                    success_count = 0
                    cursor_movable = False  # Prevent the cursor from moving
                    text_fail = font.render("Game Over! Click to restart.", True, black)
            else:
                text_fail = None
                cursor_movable = True

    # Move the cursor continuously when allowed
    if cursor_movable:
        cursor_x += cursor_speed * cursor_direction

    # Change direction if hitting the edges
    if cursor_x < 0 or cursor_x > width - cursor_width:
        cursor_direction *= -1
    
    # Update target position
    target_rect = pygame.Rect(target_x, target_y, target_width, target_height)
    target_image_rect.x = target_x - target_image_rect.width // 2
    target_image_rect.y = target_y - target_image_rect.height * 1.1

    # Update cursor position
    cursor_rect = pygame.Rect(cursor_x, cursor_y, cursor_width, cursor_height)
    cursor_image_rect.x = cursor_x - cursor_image_rect.width // 2
    cursor_image_rect.y = cursor_y - cursor_image_rect.height * 1.7

    # Draw the cursor and target
    pygame.draw.rect(screen, bar_color, bar_rect)
    pygame.draw.rect(screen, target_color, target_rect)
    screen.blit(target_image, target_image_rect)
    pygame.draw.rect(screen, cursor_color, cursor_rect)
    screen.blit(cursor_image, cursor_image_rect)

    if text_fail:
        screen.blit(text_fail, (50, 50))
    else:
        progress_text = font.render(f"stage {success_count+1} / 3", True, black)
        screen.blit(progress_text, (50, 50))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
