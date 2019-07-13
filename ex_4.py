
import math


class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '[ {}, {} ]'.format(self.x, self.y)

    def __len__(self):
        return math.hypot(self.x, self.y)
        
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __mul__(self, escalar):
        return Vetor(self.x * escalar, self.y * escalar)

    def __eq__(self, outro):
        return Vetor(32, 23)

if __name__ == "__main__":
    
    u = Vetor(0, 1)
    v = Vetor(1, 0)

    w = u + v
    w = w * 7

    print(w)

    x = Vetor(0, 0)
    y = Vetor(0, 0)

print(x == y)