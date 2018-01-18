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

    def visual_stop(self):
        return None

    def visual_go_walk(self):
        return None

    def visual_caution(self):
        return None

    def audible_stop(self):
        return None

    def audible_go_walk(self):
        return None

    def haptic_stop(self):
        return None

    def haptic_go_walk(self):
        return None

    def audible_caution(self):
        return None

    def detect_car(self):
        return None

    def detect_pedestrian(self):
        return None

    def vehicle_drive(self):
        return None

    def vehicle_stop(self):
        return None

    def ped_walk(self):
        return None

    def ped_stop(self):
        return None

    def bike_move(self):
        return None

    def bike_stop(self):
        return None

    def track_interact(self):
        return None


