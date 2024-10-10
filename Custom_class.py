class Rectangle:
    def __init__(self, length: int, width: int):
        self.values = [{'length': length}, {'width': width}]
    
    def __iter__(self):
        return iter(self.values)
rect = Rectangle(10, 5)

for item in rect:
    print(item)