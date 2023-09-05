price = [1, 2, 3, 9, 8]

price_iter = price.__iter__()

print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())


class InfiniteNaturalNumbers:
    def __init__(self) -> None:
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


values = iter(InfiniteNaturalNumbers())

print(f"InfinitNaturalNumbers: {next(values)}")

#generator function
def return_values():
    yield 1
    yield 2
    yield "three"

values = return_values()
print(values.__next__())
print(values.__next__())
print(values.__next__())