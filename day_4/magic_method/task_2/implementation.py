class MathClock:

    def __init__(self):
        self.time = '00:00'
        self.mins = 0
        self.hours = 0

    def __add__(self, other):
        self.mins += other
        self.hours = (self.hours + self.mins // 60) % 24
        self.mins = self.mins % 60

    def __sub__(self, other):
        hours_to_add, mins_to_add = divmod(self.mins - other, 60)
        self.mins = mins_to_add
        self.hours = (self.hours + hours_to_add) % 24

    def __mul__(self, other):
        self.hours = (self.hours + other) % 24

    def __truediv__(self, other):
        self.hours = self.hours - other
        if self.hours < 0:
            self.hours = (24 + self.hours) % 24

    def get_time(self):
        str_minutes = str(self.mins).zfill(2)
        str_hours = str(self.hours).zfill(2)
        return str_hours + ":" + str_minutes




