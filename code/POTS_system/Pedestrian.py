class pedestrian():

    def __init__(self, ps):
        self.ped_spd = ps

    def Ped_walk(self):
        self.ped_spd = 1.0
        return None

    def Ped_stop(self):
        pedestrian.speed = 0.0
        return None