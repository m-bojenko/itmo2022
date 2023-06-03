class Time:
    """ класс, определяющий время """

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def show_time(self):
        time = ''
        for i in self.__dict__.values():
            for j in range(2-len(str(i))):
                time += '0'
            time += str(i) + ':'
        print(time[:-1])

    def __add__(self, other):
        temp = Time()
        temp.hours = self.hours + other.hours
        temp.minutes = self.minutes + other.minutes
        temp.seconds = self.seconds + other.seconds
        if temp.seconds >= 60:
            temp.seconds %= 60
            temp.minutes += 1
        if temp.minutes >= 60:
            temp.minutes %= 60
            temp.hours += 1
        if temp.hours >= 24:
            temp.hours %= 24
        return temp


t1 = Time(13, 31, 26)
t2 = Time(8, 53, 41)
t = t1 + t2
t.show_time()
