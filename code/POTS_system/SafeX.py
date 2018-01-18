class safex:

    def __int__(self, vol, b, s, l, ch, mt, mc, ps, vs, maxspd):
        self.announcing_vol = vol
        self.vis_brightness = b
        self.haptic_strg = s
        self.length = l
        self.concrete_hardness = ch
        self.marking_txt = mt
        self.marking_color = mc
        self.ped_spd = ps
        self.vehicle_spd = vs
        self.max_speed = maxspd

    def Visual_stop(self):
        return None

    def Visual_go_walk(self):
        return None

    def Audible_stop(self):
        return None

    def Audible_go_walk(self):
        return None

    def Haptic_stop(self):
        return None

    def Haptic_go_walk(self):
        return None

    def Caution(self):
        return None

    def Detect_car(self):
        return None

    def Detect_pedestrian(self):
        return None

    def Vehicle_drive(self):
        return None

    def Vehicle_stop(self):
        return None

    def Ped_walk(self):
        return None

    def Ped_stop(self):
        return None

    def Bike_move(self):
        return None

    def Bike_stop(self):
        return None

    def Track_interact(self):
        return None

    
