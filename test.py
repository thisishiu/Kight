import pygame

pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vị trí va chạm")



# Tải ảnh
player_image = pygame.image.load("assets\player\charactor_af_process\charactor.png").convert_alpha()
enemy_image = pygame.image.load("assets\player\charactor_af_process\charactor.png").convert_alpha()

# Vị trí ban đầu
player_pos = [300, 300]
enemy_pos = [400, 300]

# Tạo mask
player_mask = pygame.mask.from_surface(player_image)
enemy_mask = pygame.mask.from_surface(enemy_image)

# Vòng lặp game
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Tính offset giữa 2 mask
    offset = (enemy_pos[0] - player_pos[0], enemy_pos[1] - player_pos[1])
    collision_point = player_mask.overlap(enemy_mask, offset)

    # Vẽ màn hình
    screen.fill((100, 200, 100))
    screen.blit(player_image, player_pos)
    screen.blit(enemy_image, enemy_pos)

    # Nếu có va chạm, đánh dấu vị trí
    if collision_point:
        print(f"Va chạm tại pixel: {collision_point}")
        # Tọa độ thực trên màn hình
        collision_real = (player_pos[0] + collision_point[0], player_pos[1] + collision_point[1])
        pygame.draw.circle(screen, (255, 0, 0), collision_real, 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
