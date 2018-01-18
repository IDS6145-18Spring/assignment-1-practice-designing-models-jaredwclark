class Crosswalk():

    def __init__(self):
        self.state = 0 #Haptic feedback on or off

    def Haptic_stop(self):
        Crosswalk.state = 1
        return None

    def Haptic_go_walk(self):
        Crosswalk.state = 0
        return None