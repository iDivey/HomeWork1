class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start - 1
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.end:
            raise StopIteration()
        if self.i % 2 == 0:
            return self.i
            self.i += 2
        if self.i % 2 != 0:
            self.i += 1
            return self.i


en = EvenNumbers(10, 25)
for i in en:
    print(i)
