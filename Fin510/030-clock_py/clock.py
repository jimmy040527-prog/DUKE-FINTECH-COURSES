class MyClock24:

    def __init__(self, hours, minutes, seconds):
        if hours < 0 or hours > 23:
            raise ValueError("hours must be between 0 and 23")

        if minutes < 0 or minutes > 59:
            raise ValueError("minutes must be between 0 and 59")

        if seconds < 0 or seconds > 59:
            raise ValueError("seconds must be between 0 and 59")
        
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @property
    def hours(self):
        return self._hours     

    @property
    def minutes(self):
        return self._minutes
        
    @property
    def seconds(self):
        return self._seconds
        
    def tick(self):
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minutes += 1
        if self._minutes == 60:
            self._minutes = 0
            self._hours += 1
        if self._hours == 24:
            self._hours = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self):
        return (f'{{"hours": {self.hours}, 'f'"minutes": {self.minutes}, 'f'"seconds": {self.seconds}}}')

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        return False

    def __ne__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return False
        return True

    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        else:
            if self.minutes > other.minutes:
                return True
            elif self.minutes < other.minutes:
                return False
            else:
                if self.seconds > other.seconds:
                    return True
                elif self.seconds < other.seconds:
                    return False
                else:
                    return True
        
    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        else:
            if self.minutes > other.minutes:
                return True
            elif self.minutes < other.minutes:
                return False
            else:
                if self.seconds > other.seconds:
                    return True
                elif self.seconds < other.seconds:
                    return False
                else:
                    return False               

    def __le__(self, other):
        if self.hours > other.hours:
            return False
        elif self.hours < other.hours:
            return True
        else:
            if self.minutes > other.minutes:
                return False
            elif self.minutes < other.minutes:
                return True
            else:
                if self.seconds > other.seconds:
                    return False
                elif self.seconds < other.seconds:
                    return True
                else:
                    return True       
        
    def __lt__(self, other):
        if self.hours > other.hours:
            return False
        elif self.hours < other.hours:
            return True
        else:
            if self.minutes > other.minutes:
                return False
            elif self.minutes < other.minutes:
                return True
            else:
                if self.seconds > other.seconds:
                    return False
                elif self.seconds < other.seconds:
                    return True
                else:
                    return False      

    def __add__(self, other):
        if isinstance(other, MyClock24):
            hours = self.hours + other.hours
            minutes = self.minutes + other.minutes
            seconds = self.seconds + other.seconds

            if seconds >= 60:
                seconds -= 60
                minutes += 1
            if minutes >= 60:
                minutes -= 60
                hours += 1
            if hours >= 24:
                hours -= 24
            return MyClock24(hours, minutes, seconds)
        elif isinstance(other, int):
            total = self.hours * 3600 + self.minutes * 60 + self.seconds
            total = (total + other) % 86400

            hours = total // 3600
            minutes = (total % 3600) // 60
            seconds = total % 60

            return MyClock24(hours, minutes, seconds)

    def __sub__(self, other):
        if isinstance(other, MyClock24):
            hours = self.hours - other.hours
            minutes = self.minutes - other.minutes
            seconds = self.seconds - other.seconds

            if seconds < 0:
                seconds += 60
                minutes -= 1
            if minutes < 0:
                minutes += 60
                hours -= 1
            if hours < 0:
                hours += 24     
            return MyClock24(hours, minutes, seconds)  
        elif isinstance(other, int):
            total = self.hours * 3600 + self.minutes * 60 + self.seconds
            total = (total - other) % 86400

            hours = total // 3600
            minutes = (total % 3600) // 60
            seconds = total % 60

            return MyClock24(hours, minutes, seconds)

        