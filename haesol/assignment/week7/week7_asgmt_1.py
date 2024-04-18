class math:
    def __init__(self, x=1, y=1):
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

    def pow(self):
        return self.x ** self.y

    def root(self):
        return self.x ** (1/self.y)


a = math(10, 2)
print(a.add())
print(a.div())
print(a.mul())
print(a.sub())
print(a.pow())
print(a.root())
