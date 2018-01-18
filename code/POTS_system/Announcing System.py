class Announcing_sys():

    def __init__(self, vol):
        self.announcing_vol = vol

    def audible_stop(self):
        Announcing_sys.sound = "STOP"
        return None

    def audible_go_walk(self):
        Announcing_sys.sound = "WALK"
        return None

    def audible_caution(self):
        Announcing_sys.sound = "WARNING"
        return None