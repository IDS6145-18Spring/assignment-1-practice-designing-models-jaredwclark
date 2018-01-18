class Display():

    def __init__(self):
        self.state = 1.0 #Displays instructions

    def Visual_stop(self):
        Display.text = "STOP"
        return None

    def Visual_go_walk(self):
        Display.text = "WALK"
        return None

    def Caution(self):
        Display.text = "WARNING"
        return None