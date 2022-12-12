class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step
    def increment(self):
        self.count += self.step

class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class SingleCounter(Singleton, Counter):
    pass

c1 = SingleCounter()
c2 = SingleCounter()
c3 = Counter()

print(c1 == c2 == c3)   # False
print(c1 == c2)         # True
