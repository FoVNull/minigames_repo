import pygame
import sys
import random
import asyncio

async def main():
    # Initialize Pygame
    pygame.init()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (220,20,60)  # Red background color
    GREEN = (0,255,127)

    # Set screen dimensions and title
    screen_width, screen_height = 500, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Chinese Characters Game")

    # Specify the path to the Chinese font file (NotoSansSC-Regular.ttf)
    font_path = "NotoSansSC-Regular.ttf"
    font_size = 80
    font = pygame.font.Font(font_path, font_size)

    # Initialize Chinese characters list
    chinese_characters = ["塨", "禧", "沷", "材", "恭", "喜", "发", "财", "囍", "运", "發", "財"]
    random.shuffle(chinese_characters)

    # Set the distance between characters
    char_distance = 10

    # Initialize grid positions
    grid_positions = []
    for i in range(3):
        for j in range(4):
            x = j * (font_size + char_distance) + 110
            y = i * (font_size + char_distance) + 100
            grid_positions.append((x, y))

    # Initialize the candidate area
    candidate_characters = []
    candidate_positions = []
    for i in range(4):
        candidate_positions.append((i*(font_size+20)+100, 450))

    finish_flag = False
    text_success = None

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if finish_flag:
                    # Clear the candidate area
                    candidate_characters = []
                    finish_flag = False
                    text_success = None
                else:
                    # Get the mouse click position
                    x, y = event.pos

                    # Determine which Chinese character was clicked
                    for i in range(len(chinese_characters)):
                        text = font.render(chinese_characters[i], True, BLACK)
                        text_rect = text.get_rect(center=grid_positions[i])

                        if text_rect.collidepoint(x, y):
                            # Add the clicked Chinese character to the candidate area
                            candidate_characters.append(chinese_characters[i])

                            # Check if the candidate area is '恭喜发财' (Congratulations, you're successful!)
                            if candidate_characters == ["恭", "喜", "发", "财"]:
                                finish_flag = True
                                text_success = pygame.font.Font(font_path, 24).render("Success! Tap to restart.", True, BLACK)
                                continue
                            elif len(candidate_characters) == 4:
                                # Shuffle the Chinese characters for a new round
                                random.shuffle(chinese_characters)
                                # Clear the candidate area if it exceeds 4 characters
                                candidate_characters = []

        # Clear the screen
        screen.fill(WHITE)

        # Display Chinese characters with red background
        for i in range(len(chinese_characters)):
            # Draw the red background
            pygame.draw.rect(screen, RED,
                            (grid_positions[i][0] - font_size*0.5, grid_positions[i][1] - font_size*0.4, font_size, font_size))
            # Display the Chinese character
            text = font.render(chinese_characters[i], True, BLACK)
            text_rect = text.get_rect(center=grid_positions[i])
            screen.blit(text, text_rect)

        question_text = pygame.font.Font(font_path, 16).render("How to say 'Wish you be prosperous' in Chinese?", True, BLACK)
        screen.blit(question_text, (10, 20))

        if text_success:
            screen.fill(WHITE)
            screen.blit(text_success, (50, 50))
        
        for i in range(len(candidate_positions)):
            # Draw the red background
            pygame.draw.rect(screen, RED, (candidate_positions[i][0] - font_size*0.5, candidate_positions[i][1] - font_size*0.4, font_size, font_size))
            
            candidate_text = candidate_characters[i] if len(candidate_characters) > i else ""
            text = font.render(candidate_text, True, BLACK)
            text_rect = text.get_rect(center=candidate_positions[i])
            screen.blit(text, text_rect)


        # Update the screen
        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
