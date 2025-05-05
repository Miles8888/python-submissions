class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen resolution
        self.screen_width = 1200
        self.screen_height = 800
        # Background colour
        self.bg_color = (20, 20, 20)

        # Lives per run
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60, 10)
        self.bullets_allowed = 3

        # Alien speed
        self.fleet_drop_speed = 10

        # Wave speed scaling on round clear
        self.speedup_scale = 1.1
        # Point-per-kill scaling on round clear
        self.score_scale = 1.5

        self.difficulty_level = 'normal' 

        self.initialize_dynamic_settings()

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Set defaults in case difficulty_level is not set
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Lives per round, max active bullets, ship speed, bullet speed, alien speed, and alien points-per-kill. 
        # Three difficulty options
        if self.difficulty_level == 'normal':
            self.ship_limit = 3
            self.bullets_allowed = 10
            self.ship_speed = 1.0
            self.bullet_speed = 1.5
            self.alien_speed = 0.75
            self.alien_points = 50
        elif self.difficulty_level == 'hard':
            self.ship_limit = 3
            self.bullets_allowed = 5
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.5
            self.alien_points = 75
        elif self.difficulty_level == 'unfair':
            self.ship_limit = 4
            self.bullets_allowed = 5
            self.ship_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 3.0
            self.alien_points = 100

        # fleet_direction where 1 represents right and -1 represents left.
        self.fleet_direction = 1

    def set_difficulty(self, diff_setting):
        """Set the difficulty and re-initialize dynamic settings."""
        self.difficulty_level = diff_setting
        self.initialize_dynamic_settings()