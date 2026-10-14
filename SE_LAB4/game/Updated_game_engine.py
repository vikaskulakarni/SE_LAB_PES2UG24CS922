import random
import pygame
from game.text_box import TextBox


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # NEW: Game state for maximum attempts and GAME_OVER
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 7
        self.game_won = False
        self.game_over = False

        # NEW: Dynamic range
        self.low_bound = 1
        self.high_bound = 100

        # NEW: Guess history
        # Each entry is: (guess, result)
        self.guess_history = []

        # Feedback
        self.feedback_msg = "Enter a number between 1 and 100"
        self.feedback_color = (220, 220, 220)

        # Input and button
        self.input_box = TextBox(width // 2 - 150, 125, 120, 48)
        self.submit_btn = pygame.Rect(width // 2 + 5, 125, 100, 48)

        # Fonts
        self.font_title = pygame.font.SysFont(None, 38)
        self.font_medium = pygame.font.SysFont(None, 25)
        self.font_small = pygame.font.SysFont(None, 21)
        self.font_btn = pygame.font.SysFont(None, 24)

    def submit_guess(self):
        # NEW: Block guesses after WIN or GAME_OVER
        if self.game_won or self.game_over:
            return

        # NEW - TASK 1: Validate empty input before int()
        if not self.input_box.text.strip():
            self.feedback_msg = "Please enter a valid number first!"
            self.feedback_color = (255, 210, 80)
            return

        # Convert input only after validation
        guess = int(self.input_box.text)

        # NEW: Validate the general game range
        if guess < 1 or guess > 100:
            self.feedback_msg = "Please enter a number between 1 and 100."
            self.feedback_color = (255, 210, 80)
            return

        # Count only valid guesses
        self.attempts += 1
        self.input_box.clear()

        # NEW - TASK 2: Dynamic range
        if guess < self.secret_number:
            self.low_bound = max(self.low_bound, guess + 1)

            self.feedback_msg = f"TOO LOW! (Guess was {guess})"
            self.feedback_color = (80, 160, 240)

            # NEW - TASK 3: Store guess history
            self.guess_history.append((guess, "TOO LOW"))

        elif guess > self.secret_number:
            self.high_bound = min(self.high_bound, guess - 1)

            self.feedback_msg = f"TOO HIGH! (Guess was {guess})"
            self.feedback_color = (240, 100, 80)

            # NEW - TASK 3: Store guess history
            self.guess_history.append((guess, "TOO HIGH"))

        else:
            self.feedback_msg = f"CORRECT! Found in {self.attempts} attempts."
            self.feedback_color = (80, 220, 90)

            # NEW - TASK 3: Record correct guess
            self.guess_history.append((guess, "CORRECT"))
            self.game_won = True
            return

        # NEW - TASK 4: Maximum attempts / GAME_OVER
        if self.attempts >= self.max_attempts:
            self.game_over = True
            self.feedback_msg = f"GAME OVER! The number was {self.secret_number}."
            self.feedback_color = (255, 90, 90)

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_won = False
        self.game_over = False

        # NEW: Reset dynamic range
        self.low_bound = 1
        self.high_bound = 100

        # NEW: Reset history
        self.guess_history = []

        self.feedback_msg = "Enter a number between 1 and 100"
        self.feedback_color = (220, 220, 220)
        self.input_box.clear()

    def handle_event(self, event):
        # NEW: Disable input after game ends
        if not self.game_won and not self.game_over:
            self.input_box.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.submit_guess()

            # NEW - TASK 4: Restart after WIN or GAME_OVER
            elif event.key == pygame.K_r and (
                self.game_won or self.game_over
            ):
                self.reset()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.submit_btn.collidepoint(event.pos):
                self.submit_guess()

    def update(self):
        pass

    def render(self, screen):
        screen.fill((30, 34, 42))

        title_surf = self.font_title.render(
            "Number Guessing Arena", True, (245, 245, 245)
        )
        screen.blit(
            title_surf,
            (self.width // 2 - title_surf.get_width() // 2, 20)
        )

        # NEW: Attempts display includes maximum
        attempts_surf = self.font_medium.render(
            f"Attempts: {self.attempts} / {self.max_attempts}",
            True, (180, 185, 195)
        )
        screen.blit(
            attempts_surf,
            (self.width // 2 - attempts_surf.get_width() // 2, 65)
        )

        # NEW - TASK 2: Display dynamic range
        range_surf = self.font_medium.render(
            f"Current Possible Range: {self.low_bound} - {self.high_bound}",
            True, (120, 210, 180)
        )
        screen.blit(
            range_surf,
            (self.width // 2 - range_surf.get_width() // 2, 92)
        )

        # Hide input after WIN/GAME_OVER
        if not self.game_won and not self.game_over:
            self.input_box.render(screen)

            pygame.draw.rect(
                screen, (50, 150, 80), self.submit_btn, border_radius=6
            )
            pygame.draw.rect(
                screen, (220, 220, 220), self.submit_btn,
                width=2, border_radius=6
            )

            btn_text = self.font_btn.render("SUBMIT", True, (255, 255, 255))
            screen.blit(
                btn_text,
                (
                    self.submit_btn.centerx - btn_text.get_width() // 2,
                    self.submit_btn.centery - btn_text.get_height() // 2
                )
            )

        feedback_surf = self.font_medium.render(
            self.feedback_msg, True, self.feedback_color
        )
        screen.blit(
            feedback_surf,
            (self.width // 2 - feedback_surf.get_width() // 2, 185)
        )

        # NEW - TASK 3: Display last five guesses
        history_title = self.font_small.render(
            "Last 5 Guesses:", True, (220, 220, 220)
        )
        screen.blit(history_title, (35, 225))

        recent_history = self.guess_history[-5:]

        for index, (guess, result) in enumerate(recent_history):
            if result == "TOO LOW":
                symbol = "↓"
                color = (80, 160, 240)
            elif result == "TOO HIGH":
                symbol = "↑"
                color = (240, 100, 80)
            else:
                symbol = "✓"
                color = (80, 220, 90)

            history_text = self.font_small.render(
                f"{guess}  {symbol}  {result}", True, color
            )
            screen.blit(history_text, (45, 250 + index * 22))

        # WIN state
        if self.game_won:
            restart_surf = self.font_medium.render(
                "You Win! Press [R] to Start a New Game",
                True, (255, 220, 80)
            )
            screen.blit(
                restart_surf,
                (self.width // 2 - restart_surf.get_width() // 2, 350)
            )

        # NEW - TASK 4: GAME_OVER state
        elif self.game_over:
            game_over_surf = self.font_medium.render(
                f"GAME OVER! Secret Number: {self.secret_number}",
                True, (255, 90, 90)
            )
            screen.blit(
                game_over_surf,
                (self.width // 2 - game_over_surf.get_width() // 2, 330)
            )

            restart_surf = self.font_small.render(
                "Press [R] to try again",
                True, (255, 220, 80)
            )
            screen.blit(
                restart_surf,
                (self.width // 2 - restart_surf.get_width() // 2, 355)
            )
