
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
#for i in rev:
#    print(i)
print(rev.__next__())
print(rev.__next__())
print(rev.__next__())
print(rev.__next__())
print(rev.__next__())
