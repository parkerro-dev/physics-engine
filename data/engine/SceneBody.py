
class SceneBody():
    def __init__(self, body, active):
        self.body = body
        self.active = active

    def checkActivate(self):
        return self.active()

    def changeActiveState(self):
        self.active = not self.active

