import pygame

# Dimensions et couleurs
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 60
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)
LIGHT_GRAY = (80, 80, 80)
RED = (200, 30, 30)
WHITE = (255, 255, 255)


def init_screen():
    """Initialisee la fenêtre de jeu."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mon jeu de stratégie")
    return screen


def display_menu(screen):
    """Affiche l'écran d'accueil avec un bouton PLAY."""
    screen.fill(DARK_GRAY)

    # Affichage du titre
    font = pygame.font.Font(None, 74)
    title_text = font.render("NINJA STRATEGY", True, RED)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

    # Bouton PLAY
    play_button_rect = pygame.Rect(WIDTH // 2 - 100, 300, 200, 60)
    pygame.draw.rect(screen, LIGHT_GRAY, play_button_rect)
    font = pygame.font.Font(None, 50)
    play_text = font.render("PLAY", True, BLACK)
    screen.blit(play_text, (play_button_rect.x + play_button_rect.width // 2 - play_text.get_width() // 2,
                            play_button_rect.y + play_button_rect.height // 2 - play_text.get_height() // 2))

    pygame.display.flip()
    return play_button_rect


def handle_menu_events(screen):
    """les événements sur l'écran d'accueil."""
    play_button_rect = display_menu(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    return  # Retourner au jeu principal


def draw_grid(screen):
    """Affiche la grille."""
    screen.fill(BLACK)
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LIGHT_GRAY, rect, 1)


def draw_units(screen, player_units, enemy_units):
    """Dessiner les unités sur le terrain."""
    for unit in player_units + enemy_units:
        unit.draw(screen)
