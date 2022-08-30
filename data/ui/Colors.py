class Colors:
    def __init__(self, dark = True):
        self.dark = dark
        self.ColorMode()

    def ColorMode(self):
        if self.dark:
            self.primary = (255, 255, 255)
            self.secondary = (155, 155, 155)
            self.darkSecondary = (105, 105, 105)
            self.bg = (30,30,30)
            self.darkBg= (20, 20, 20)
            self.antiPrimary = (0, 0, 0)
        else:
            self.primary = (0, 0, 0)
            self.secondary = (100, 100, 100)
            self.darkSecondary = (150, 150, 150)
            self.bg = (205, 205, 205)
            self.darkBg = (175, 175, 175)
            self.antiPrimary = (255, 255, 255)