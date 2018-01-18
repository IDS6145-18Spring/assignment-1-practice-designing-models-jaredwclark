class display():

    def __init__(self, b):
        self.state = 1.0 #Displays instructions
        self.vis_brightness = b


    def Visual_stop(self):
        display.text = "STOP"
        return None

    def Visual_go_walk(self):
        display.text = "WALK"
        return None

    def Caution(self):
        display.text = "WARNING"
        return None