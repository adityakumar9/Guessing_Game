import random
P1 = random.randint(1,9)
#print(P1)
P2 = 0
count = []
class Guassgame:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def gameRule(self, c):
        self.c = c
        while True:
            if self.a == self.b:
                print("Exactly Right")
                break
            self.b = int(input("Gauss a Number: "))
            if self.a > self.b:
                print("To Low")
                count.append(str(self.b))
            elif self.a < self.b:
                print("To High")
                count.append(str(self.b))

Guassing = Guassgame(P1, P2)
Guassing.gameRule(count)
print(f"Number of Guesses: {len(count)}")

