
class Settings:
    """A class to store all settings for Alien Invasion. """

    def __init__(self):
        """Initilaize the game static settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 230)


        # Ship Settings
        self.ship_speed = 4
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 13
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 45

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point vales increase
        self.score_scale = 1.5

        self.initialize_dynamic_setting()


    def initialize_dynamic_setting(self):
        """Initialize settings that change throughtout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Scoring
        self.alien_points = 50

        # Fleet direction of 1 represents right ; -1 represents left.
        self.fleet_direction = 1


    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
