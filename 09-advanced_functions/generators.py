class FirstHundredGenerator:
    def __init__(self):
        self.num = 0

    def __next__(self):
        if self.num < 100:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration()


g = FirstHundredGenerator()

print(next(g))
print(next(g))
print(next(g))
