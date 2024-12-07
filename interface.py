import pygame

# Dimensions et couleurs
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 60
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)
LIGHT_GRAY = (80, 80, 80)
RED = (200, 30, 30)
WHITE = (255, 255, 255)

class Game_interface:
    #Classe responsable de l'affichage de la grille, des unités

    def __init__(self, screen):
        self.screen = screen

    def draw_grid(self):
        #Affiche la grille
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, DARK_GRAY, rect, 1)

    def draw_units(self, player_units, enemy_units):
        #Dessine les unités du joueur et des ennemis
        for unit in player_units + enemy_units:
            unit.draw(self.screen)

    def draw_dynamic_grid(self, accessible_cells):
        """Dessine les cases accessibles."""
        for x, y in accessible_cells:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, BLUE_PALE, rect)

    def display_menu(self):
        #Affiche le menu principal avec un bouton PLAY.
        self.screen.fill(DARK_GRAY)

        # Affichage du titre
        font = pygame.font.Font(None, 74)
        title_text = font.render("NINJA STRATEGY", True, RED)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Bouton PLAY
        play_button_rect = pygame.Rect(WIDTH // 2 - 100, 300, 200, 60)
        pygame.draw.rect(self.screen, LIGHT_GRAY, play_button_rect)
        font = pygame.font.Font(None, 50)
        play_text = font.render("PLAY", True, BLACK)
        self.screen.blit(
            play_text,
            (
                play_button_rect.x + play_button_rect.width // 2 - play_text.get_width() // 2,
                play_button_rect.y + play_button_rect.height // 2 - play_text.get_height() // 2,
            ),
        )

        pygame.display.flip()
        return play_button_rect
