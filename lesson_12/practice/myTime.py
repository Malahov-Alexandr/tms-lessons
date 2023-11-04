class MyTime:

    def __init__(self, seconds: float):
        self.second = seconds

    @property
    def hours(self):
        return int(self.second // 3600)

    @property
    def minutes(self):
        return int((self.second // 60) % 60)

    @property
    def seconds(self):
        return int(self.second % 60)

    def __mul__(self, other):
        return MyTime(self.second * other)

    def __truediv__(self, other):
        return MyTime(self.second / other)

    def __add__(self, other):
        return MyTime(self.second + other.second)

    def get_formatted_str(self):
        milliseconds = int((self.second % 1) * 10)
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}.{milliseconds}'

    def __str__(self):
        return f'{self.second}s'

    def __eq__(self, other):
        return self.second == other.second

    def __lt__(self, other):
        return self.second < other.second

    def __gt__(self, other):
        return self.second > other.second

    def __le__(self, other):
        return self.second <= other.second

    def __ge__(self, other):
        return self.second >= other.second

    def __ne__(self, other):
        return self.second != other.second


class MyTimeInterval():

    def __init__(self, start_seconds: MyTime, end_seconds: MyTime):
        self.start = start_seconds
        self.end = end_seconds

    def is_inside(self, seconds: MyTime):
        return self.start <= seconds <= self.end

    def intersects(self, other):
        return self.is_inside(other.start) or self.is_inside(other.end)


if __name__ == '__main__':
    a = MyTimeInterval(MyTime(10), MyTime(20))
    print(a.is_inside(MyTime(15)))
    print(a.intersects(MyTimeInterval(MyTime(5), MyTime(15))))

    assert MyTime(10) * 2 == MyTime(20)
    assert MyTime(10) / 2 == MyTime(5)
    assert MyTime(10) + MyTime(10) == MyTime(20)
    assert MyTime(10) < MyTime(20)
    assert MyTime(10) > MyTime(5)
    assert MyTime(10) <= MyTime(10)
    assert MyTime(10) >= MyTime(10)
    assert MyTime(10) != MyTime(5)
    assert MyTime(10) == MyTime(10)
    assert MyTimeInterval(MyTime(10), MyTime(20)).is_inside(MyTime(15))
    assert MyTimeInterval(MyTime(10), MyTime(20)).intersects(MyTimeInterval(MyTime(5), MyTime(15)))