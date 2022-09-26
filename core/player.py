

class Player:

    def __init__(self, size):
        self.position_x = 0
        self.position_y = 0


    def move(self, direction):
        if direction == 'Up':
            self.position_x -= 1
        elif direction == 'Down':
            self.position_x += 1
        elif direction == 'Left':
            self.position_y -= 1
        elif direction == 'Right':
            self.position_y += 1


