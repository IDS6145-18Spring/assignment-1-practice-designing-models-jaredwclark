class display():

    def __init__(self, b):
        self.state = 1.0 #Displays instructions
        self.vis_brightness = b


    def visual_stop(self):
        display.text = "STOP"
        return None

    def visual_go_walk(self):
        display.text = "WALK"
        return None

    def visual_caution(self):
        display.text = "WARNING"
        return None