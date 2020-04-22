  
class Wspak:
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

wyraz=Wspak("Ale po co ?")
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())

print("\n\n")

HaHa=Wspak("natsikebzU")
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())
print(HaHa.__next__())

