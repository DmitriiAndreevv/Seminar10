class Minsrart:

    def __init__(self):
        self.sum = []

    def give_number(self, n):
        self.sum += [n]

    def res(self):
        if len(self.sum) == 0:
            return None
        else: return min(self.sum)

class Maxstart:

    def __init__(self):
        self.sum = []
    
    def give_number(self, n):
        self.sum += [n]

    def res(self):
        if len(self.sum) == 0:
            return None
        else: return max(self.sum)

class Averagestart:

    def __init__(self):
        self.sum = []

    def give_number(self, n):
        self.sum += [n]

    def res(self):
        if len(self.sum) == 0:
            return None
        else: return sum(self.sum)/len(self.sum)

val = [1, 2, 3, 6, 7, 8, 0, 4, 5, 9, -1, 1.5, 0.4, 3,5]

min1 = Minsrart()
max1 = Maxstart()
avg = Averagestart()

for i in val:
    min1.give_number(i)
    max1.give_number(i)
    avg.give_number(i)

print(min1.res())
print(max1.res())
print('{:.2}'.format
(avg.res()))