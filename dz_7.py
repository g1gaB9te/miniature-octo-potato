class ReverseIterator:
    def __init__(self, itera):
        self.itera = itera
        self.king = len(itera)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.king == 0:
            raise StopIteration
        self.king -= 1
        return self.itera[self.king]

reverse = ReverseIterator([1, 2, 3, 4, 5]) 
for num in reverse:
    print(num)