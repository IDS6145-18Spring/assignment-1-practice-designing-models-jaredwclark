class Announcing_sys():

    def __init__(self):
        self.vol = 1.0

    def Audible_stop(self):
        Announcing_sys.sound = "STOP"
        return None

    def Audible_go_walk(self):
        Announcing_sys.sound = "WALK"
        return None
    def Audible_caution(self):
        Announcing_sys.sound = "WARNING"