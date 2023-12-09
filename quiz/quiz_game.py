import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220,20,60)  # Red background color

# Set screen dimensions and title
screen_width, screen_height = 500, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chinese Characters Game")

# Specify the path to the Chinese font file (NotoSansSC-Regular.ttf)
font_path = "static/NotoSansSC-Regular.ttf"
font_size = 80
font = pygame.font.Font(font_path, font_size)

# Initialize Chinese characters question
seed = 0
chinese_characters = ["塨", "禧", "沷", "材", "恭", "喜", "发", "财", "囍", "运", "發", "財"]
answer =  ["恭", "喜", "发", "财"]
pronunciation = "コーシーファアツァイ"
question_text = pygame.font.Font(font_path, 16).render("「お金がたまりますように」の中国語はなんでしょう？", True, BLACK)
random.shuffle(chinese_characters)
success_image = pygame.image.load("static/facai.jpg")
success_image_rect = success_image.get_rect()
success_image_rect.x = 25
success_image_rect.y = 100
text_lines = ["旧正月は、『恭喜發財』と言って挨拶します。", 
                "これは、元々『お金がたまりますように　とか　一攫千金』",
                "のような意味がありましたが、"
                "今は旧正月の挨拶として使います。",
                "恭喜 → おめでとう！ 發財 → お金が儲かりますように！",
                "簡体字は「恭喜发财」と書きます。"]

# Set the distance between characters
char_distance = 10

# Initialize grid positions
grid_positions = []
for i in range(3):
    for j in range(4):
        x = j * (font_size + char_distance) + 110
        y = i * (font_size + char_distance) + 200
        grid_positions.append((x, y))

# Initialize the candidate area
candidate_characters = []
candidate_positions = []
for i in range(4):
    candidate_positions.append((i*(font_size+20)+100, 600))

finish_flag = False
intro_flag = True
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
                intro_flag = True
                text_success = None

                # seed = random.randint(0, 1)
                seed = seed + 1 if seed < 1 else 0
                if seed == 0:
                    chinese_characters = ["塨", "禧", "沷", "材", "恭", "喜", "发", "财", "囍", "运", "發", "財"]
                    answer =  ["恭", "喜", "发", "财"]
                    pronunciation = "コーシーファアツァイ"
                    question_text = pygame.font.Font(font_path, 16).render("「お金がたまりますように」を表する挨拶はなんでしょう？", True, BLACK)
                    random.shuffle(chinese_characters)
                    success_image = pygame.image.load("static/facai.jpg")
                    success_image_rect = success_image.get_rect()
                    success_image_rect.x = 25
                    success_image_rect.y = 100
                    text_lines = ["旧正月は、『恭喜發財』と言って挨拶します。", 
                        "これは、元々『お金がたまりますように　とか　一攫千金』",
                        "のような意味がありましたが、"
                        "今は旧正月の挨拶として使います。",
                        "恭喜 → おめでとう！ 發財 → お金が儲かりますように！",
                        "簡体字は「恭喜发财」と書きます。"]

                elif seed == 1:
                    chinese_characters = ["万", "事", "如", "意", "方", "倳", "夷", "姑", "萬", "噫", "女", "癔"]
                    answer =  ["万", "事", "如", "意"]
                    pronunciation = "ばんじにょい"
                    question_text = pygame.font.Font(font_path, 12).render("「全て何もかもが思い通りになりますように」を表する挨拶はなんでしょう？", True, BLACK)
                    random.shuffle(chinese_characters)
                    success_image = pygame.image.load("static/ruyi.gif")
                    success_image_rect = success_image.get_rect()
                    success_image_rect.x = 50
                    success_image_rect.y = 100
                    text_lines = ["万事如意は、中国では正月などお祝いをする時に使われています", 
                        "『全て何もかもが思い通りになりますように』の意味です",
                        "全てのことを表す「万事」と",
                        "思い通りにうまく事が進むことを表す「如意」",
                        "を組み合わせてできた言葉になります。",
                        "簡体字は「万事如意」と書きます。"]

            elif intro_flag:
                x, y = event.pos
                if button_rect.collidepoint(x, y):
                    intro_flag = False
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
                        if candidate_characters == answer:
                            finish_flag = True
                            text_success = pygame.font.Font(font_path, 24).render(f"正解です！", True, BLACK)
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
        if chinese_characters[i] in candidate_characters:
            pygame.draw.rect(screen, WHITE,
                (grid_positions[i][0] - font_size*0.5, grid_positions[i][1] - font_size*0.45, font_size, font_size))
            text = font.render(chinese_characters[i], True, WHITE)
        else:
            # Draw the red background
            pygame.draw.rect(screen, RED,
                            (grid_positions[i][0] - font_size*0.5, grid_positions[i][1] - font_size*0.45, font_size*1.04, font_size*1.04), border_radius=10)
            # Display the Chinese character
            text = font.render(chinese_characters[i], True, BLACK)
        text_rect = text.get_rect(center=grid_positions[i])
        screen.blit(text, text_rect)

    question_title = pygame.font.Font(font_path, 28).render("正しい漢字を選べよう", True, BLACK)
    screen.blit(question_title, (20, 40))
    screen.blit(question_text, (25, 100))

    if text_success:
        screen.fill(WHITE)
        screen.blit(text_success, (50, 50))
        screen.blit(success_image, success_image_rect)
    
    for i in range(len(candidate_positions)):
        
        candidate_text = candidate_characters[i] if len(candidate_characters) > i else ""
        # Draw the red background
        if candidate_text:
            pygame.draw.rect(screen, RED,
            (candidate_positions[i][0] - font_size*0.5, candidate_positions[i][1] - font_size*0.45, font_size, font_size), border_radius=10)
        else:
            pygame.draw.rect(screen, WHITE, 
                             (candidate_positions[i][0] - font_size*0.5, candidate_positions[i][1] - font_size*0.45, font_size*1.04, font_size*1.04))
        text = font.render(candidate_text, True, BLACK)
        text_rect = text.get_rect(center=candidate_positions[i])
        screen.blit(text, text_rect)

    if intro_flag:
        # Clear the screen
        screen.fill(WHITE)
        
        screen.blit(
            pygame.font.Font(font_path, 38).render(''.join(answer), True, BLACK), (20, 80)
        )
        screen.blit(
            pygame.font.Font(font_path, 14).render(pronunciation, True, BLACK), (25, 60)
        )
        for i, line in enumerate(text_lines):
            screen.blit(
                pygame.font.Font(font_path, 16).render(line, True, BLACK), (20, 200+30*i)
            )

        button_width, button_height = 200, 50
        button_position = (150, 500)
        button_radius = 10
        button_text = "問題にGO"

        pygame.draw.rect(screen, RED, (button_position[0], button_position[1], button_width, button_height), border_radius=button_radius)
        button_surface = pygame.font.Font(font_path, 24).render(button_text, True, WHITE)
        button_rect = button_surface.get_rect(center=(button_position[0] + button_width // 2, button_position[1] + button_height // 2))

        screen.blit(button_surface, button_rect)

    # Update the screen
    pygame.display.flip()
