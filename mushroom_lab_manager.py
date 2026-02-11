class GrowRooms:
    def __init__(self, room, temperature, rh):
        self.room = room
        self.temperature = temperature
        self.rh = rh

    def update_temp(self, new_temp):
        self.temperature = new_temp

    def __repr__(self):
        return f"{self.room} at {self.temperature}°C"


class Laboratory:
    def __init__(self, lab_name):
        self.lab_name = lab_name
        self.rooms = []

# to be continued.........
