class pedestrian():

    def __init__(self, ps):
        self.ped_spd = ps

    def ped_walk(self):
        self.ped_spd = 1.0
        return None

    def ped_stop(self):
        pedestrian.speed = 0.0
        return None