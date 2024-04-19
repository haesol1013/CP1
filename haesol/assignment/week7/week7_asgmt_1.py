class math:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y


a = math(10, 5)
print(a.add())
print(a.div())
print(a.mul())
print(a.sub())
