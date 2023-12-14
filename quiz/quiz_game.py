import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220,20,60)  # Red background color
GRAY = (105,105,105)

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

# Initialize fail
show_fail_image = False
show_fail_image_timer = None
fail_image = pygame.image.load("static/fail.png")
fail_image_rect = success_image.get_rect()
fail_image_rect.x = 200
fail_image_rect.y = 450

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

                seed = random.randint(0, 3)
                # seed = seed + 1 if seed < 3 else 0
                if seed == 0:
                    chinese_characters = ["塨", "禧", "沷", "材", "恭", "喜", "发", "财", "囍", "运", "金", "祝"]
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
                    chinese_characters = ["万", "事", "如", "意", "方", "倳", "夷", "姑", "友", "噫", "女", "癔"]
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
                elif seed == 2:
                    chinese_characters = ["心", "想", "事", "成", "态", "相", "戍" , "堇", "咸", "怂", "感", "盛"]
                    answer =  ["心", "想", "事", "成"]
                    pronunciation = "しんそうじせい"
                    question_text = pygame.font.Font(font_path, 16).render("「願いがすべて叶いますように」を表する挨拶はなんでしょう？", True, BLACK)
                    random.shuffle(chinese_characters)
                    success_image = pygame.image.load("static/xinxiang.jpg")
                    success_image_rect = success_image.get_rect()
                    success_image_rect.x = 50
                    success_image_rect.y = 100
                    text_lines = ["中国では正月などお祝いをする時に使われています", 
                        "『心で願ったことが全てかなう』の意味です",
                        "万事如意（ばんじにょい）と一緒に使うことが多いです"
                        ]
                elif seed == 3:
                    chinese_characters = ["笼", "尤", "详", "样", "羊", "舌", "五", "韦", "龙", "年", "吉", "祥"]
                    answer =  ["龙", "年", "吉", "祥"]
                    pronunciation = "りゅうねんきちじょう"
                    question_text = pygame.font.Font(font_path, 16).render("「龍年で幸せになるように」を表する挨拶はなんでしょう？", True, BLACK)
                    random.shuffle(chinese_characters)
                    success_image = pygame.image.load("static/jixiang.gif")
                    success_image_rect = success_image.get_rect()
                    success_image_rect.x = 50
                    success_image_rect.y = 100
                    text_lines = ["「十二支+吉祥」 は旧正月の時によく使われています挨拶です", 
                        "2024年は日本では辰年ですが、中国では龍年と呼ばれます。",
                        "簡体字は「龙年吉祥」と書きます。"
                        ]

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
                            show_fail_image = True
                            show_fail_image_timer = pygame.time.get_ticks() + 1000

    # Clear the screen
    screen.fill(WHITE)

    # Display Chinese characters with red background
    for i in range(len(chinese_characters)):
        if chinese_characters[i] in candidate_characters:
            pygame.draw.rect(screen, WHITE,
                (grid_positions[i][0] - font_size*0.5, grid_positions[i][1] - font_size*0.45, font_size*1.04, font_size*1.04))
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
        if not finish_flag:
            pygame.draw.rect(screen, GRAY,
                (candidate_positions[i][0] - font_size*0.5, candidate_positions[i][1]+50, font_size*1.04, 5))
        candidate_text = candidate_characters[i] if len(candidate_characters) > i else ""
        # Draw the red background
        if candidate_text:
            pygame.draw.rect(screen, RED,
            (candidate_positions[i][0] - font_size*0.5, candidate_positions[i][1] - font_size*0.45, font_size*1.04, font_size*1.04), border_radius=10)
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
            pygame.font.Font(font_path, 38).render("中国新年の挨拶を学ぼう", True, BLACK), (15, 50)
        )
        if seed == 0 or seed == 3:
            screen.blit(
                pygame.font.Font(font_path, 12).render(pronunciation, True, BLACK), (35, 155)
            )
        else:
            screen.blit(
                pygame.font.Font(font_path, 12).render(pronunciation, True, BLACK), (50, 155)
            )
        screen.blit(
            pygame.font.Font(font_path, 28).render(''.join(answer), True, BLACK), (40, 170)
        )
        for i, line in enumerate(text_lines):
            screen.blit(
                pygame.font.Font(font_path, 16).render(line, True, BLACK), (20, 230+30*i)
            )
        
        if seed == 0:
            image_path = "static/facai" 
        elif seed == 1:
            image_path = "static/ruyi"
        elif seed == 2:
            image_path = "static/xinxiang"
        else:
            image_path = "static/jixiang"
        
        info_image = pygame.image.load(f"{image_path}1.jpg")
        info_image_rect = info_image.get_rect()
        info_image_rect.x = 55
        info_image_rect.y = 420 if seed < 2 else 350
        screen.blit(info_image, info_image_rect)

        info_image1 = pygame.image.load(f"{image_path}2.jpg")
        info_image_rect1 = info_image1.get_rect()
        info_image_rect1.x = 255
        info_image_rect1.y = 420 if seed < 2 else 350
        screen.blit(info_image1, info_image_rect1)

        button_width, button_height = 200, 50
        button_position = (150, 650)
        button_radius = 10
        button_text = "問題へGO"

        pygame.draw.rect(screen, RED, (button_position[0], button_position[1], button_width, button_height), border_radius=button_radius)
        button_surface = pygame.font.Font(font_path, 24).render(button_text, True, WHITE)
        button_rect = button_surface.get_rect(center=(button_position[0] + button_width // 2, button_position[1] + button_height // 2))

        screen.blit(button_surface, button_rect)
    
    if show_fail_image:
        screen.blit(fail_image, fail_image_rect)
        current_time = pygame.time.get_ticks()
        if current_time > show_fail_image_timer:
            show_fail_image = False

    # Update the screen
    pygame.display.flip()
