from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # instance method
    # can modify the state of a single instance
    def print_date(self):
        print('{0!s:.4} {1!s:.2} {2!s:.2}'.format(self.year, self.month, self.day))

    # class method
    # can only modify the state of the class that applies to all instances of the class
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

if __name__ == "__main__":
    data = { 
        'year' : 2020,
        'month' : 9,
        'day' : 7,
    }

    d1 = Date(**data)
    print(d1.year, d1.month, d1.day)
    d1.print_date()

    d2 = Date.today()
    d2.print_date()
