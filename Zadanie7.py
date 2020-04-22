class Parzysta:
    
    def __init__(self, slowo):
        self.slowo = slowo
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        index = self.index
        self.index += 2
        if (self.index > len(self.slowo)+1):
            raise StopIteration
        else:
            return self.slowo[index]

slowo = Parzysta('Hejnal')
print(next(slowo))
print(next(slowo))
print(next(slowo))

