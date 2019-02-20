class PrimeUntil:
    def __init__(self, end):
        self.end = end
        self.start = 2

    def __next__(self):
        while self.start < self.end:
            for n in range(self.start, self.end):
                for i in range(2, n):
                    if n % i == 0:
                        break
                    else:
                        self.start = n + 1
                        return n
        raise StopAsyncIteration()


g = PrimeUntil(100)
print(next(g))
print(next(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
