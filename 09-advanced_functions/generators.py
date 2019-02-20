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

    def __iter__(self):
        return self


print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)
