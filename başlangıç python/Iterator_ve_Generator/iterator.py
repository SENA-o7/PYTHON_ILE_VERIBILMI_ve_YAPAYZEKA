class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        if self.start % 2 != 0:
            self.start += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current = self.start
        self.start += 2
        return current


even_numbers = EvenNumbers(1, 32)


for num in even_numbers:
    print(num)