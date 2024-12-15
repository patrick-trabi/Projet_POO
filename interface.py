import pygame
import random

CELL_SIZE = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TREE_COLOR = (34, 139, 34)
WALL_COLOR = (139, 69, 19)

class Interface:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.grid_width = width // CELL_SIZE
        self.grid_height = height // CELL_SIZE
        self.obstacles = self.generate_obstacles()

        # Backgrounds pour l'accueil et la sélection
        self.background_home = pygame.image.load("main.jpg").convert()
        self.background_home = pygame.transform.scale(self.background_home, (width, height))
        self.background_selection = pygame.image.load("selection.jpg").convert()
        self.background_selection = pygame.transform.scale(self.background_selection, (width, height))

        # Terrain du jeu
        self.background = pygame.image.load("field.jpg").convert()

    def generate_obstacles(self):
        obstacles = []
        for _ in range(20):
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            obstacles.append((x, y, random.choice(["tree", "wall"])))
        return obstacles

    def draw_grid(self):
        self.screen.blit(self.background, (0, 0))
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_obstacles(self):
        for x, y, obstacle_type in self.obstacles:
            color = TREE_COLOR if obstacle_type == "tree" else WALL_COLOR
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

    def draw_units(self, player_units, enemy_units):
        for unit in player_units + enemy_units:
            unit.draw(self.screen)

    def show_home_screen(self):
        """Affiche l'écran d'accueil avec un bouton 'Play'."""
        font = pygame.font.Font(None, 72)
        play_button = pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 100)
        running = True

        while running:
            self.screen.blit(self.background_home, (0, 0))  # Affiche le background de l'accueil
            text = font.render("Play", True, BLACK)
            pygame.draw.rect(self.screen, WHITE, play_button, border_radius=10)
            self.screen.blit(text, (play_button.x + 50, play_button.y + 25))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        running = False

    def show_unit_selection(self):
        """Affiche un écran de sélection d'unités."""
        font = pygame.font.Font(None, 36)
        unit_names = ["Ninja", "Samurai", "Archer"]
        unit_rects = [
            pygame.Rect(self.width // 4 - 50, self.height // 2 - 50, 100, 100),
            pygame.Rect(self.width // 2 - 50, self.height // 2 - 50, 100, 100),
            pygame.Rect(3 * self.width // 4 - 50, self.height // 2 - 50, 100, 100)
        ]

        selected_units = []
        running = True

        while running:
            self.screen.blit(self.background_selection, (0, 0))  # Affiche le background de la sélection
            for idx, rect in enumerate(unit_rects):
                pygame.draw.rect(self.screen, WHITE, rect, border_radius=10)
                text = font.render(unit_names[idx], True, BLACK)
                pygame.draw.rect(self.screen, (255, 255, 255), rect)
                self.screen.blit(text, (rect.x + 15, rect.y + 35))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for idx, rect in enumerate(unit_rects):
                        if rect.collidepoint(event.pos) and len(selected_units) < 2:
                            selected_units.append(unit_names[idx])
                            print(f"Vous avez sélectionné : {unit_names[idx]}")
                            if len(selected_units) == 2:
                                running = False

        return selected_units

    def draw_skills(self, unit):
        if not unit.skills:
            return

        font = pygame.font.Font(None, 24)
        skill_text = "Skills: "
        for idx, skill in enumerate(unit.skills):
            skill_text += f"{idx + 1} - {skill.name}  "

        skill_surface = font.render(skill_text, True, (255, 255, 255))
        self.screen.blit(skill_surface, (10, self.height - 30))

    def flip_display(self, player_units, enemy_units):
        self.draw_grid()
        self.draw_obstacles()
        self.draw_units(player_units, enemy_units)
        selected_unit = next((unit for unit in player_units if unit.is_selected), None)
        if selected_unit:
            self.draw_skills(selected_unit)
        pygame.display.flip()
