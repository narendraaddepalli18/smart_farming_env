class FarmEnv:
    def __init__(self):
        self.water = 50
        self.crop_health = 50
        self.done = False

    def reset(self):
        self.water = 50
        self.crop_health = 50
        self.done = False
        return self.state()

    def state(self):
        return {
            "water": self.water,
            "crop_health": self.crop_health
        }

    def step(self, action):
        reward = 0

        if action == "irrigate":
            self.water += 10
            reward = 0.2

        elif action == "fertilize":
            self.crop_health += 10
            reward = 0.3

        elif action == "harvest":
            if self.crop_health > 70:
                reward = 1.0
                self.done = True
            else:
                reward = -0.5

        else:
            reward = -0.1

        return self.state(), reward, self.done, {}