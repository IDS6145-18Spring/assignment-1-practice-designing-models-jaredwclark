class crosswalk():

    def __init__(self, s, ch, mt, mc):
        self.state = 0 #Haptic feedback on or off
        self.haptic_strg = s
        self.concrete_hardness = ch
        self.marking_txt = mt
        self.marking_color = mc




    def Haptic_stop(self):
        crosswalk.state = 1
        return None

    def Haptic_go_walk(self):
        crosswalk.state = 0
        return None