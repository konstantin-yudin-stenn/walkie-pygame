

class Room:

    def __init__(self, x=0, y=0):
        self.x = str(x)
        self.y = str(y)
        self.status = '0'

    def __str__(self):
        return str(self.status)


class Field:

    def __init__(self, size):
        self.size = size
        self.field = [[Room(i, j) for j in range(self.size)] for i in range(self.size)]

    def __getitem__(self, item):
        return self.field[item]

    def __str__(self):
        res = ''
        for corridor in self.field:
            for room in corridor:
                res += str(room) + '  '
            res += '\n'
        return res
