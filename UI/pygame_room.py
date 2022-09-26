import pygame


class Room(pygame.sprite.Sprite):
    def __init__(self, room, location):
        pygame.sprite.Sprite.__init__(self)
        self.status = room.status
        self.w_size = 25
        self.h_size = 25
        self.image = pygame.Surface((self.w_size, self.h_size))
        if self.status == 'P':
            self.image.fill((255, 0, 0))
        else:
            self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.location = location
        self.rect.center = (self.location[0], self.location[1])


    def update(self):
        """ TODO: update room color from incomed field_matrix """
        pass


class Rooms(pygame.sprite.Sprite):
    def __init__(self, field_matrix, field_ui):
        pygame.sprite.Sprite.__init__(self)
        self.list_of_rooms = []
        start_of_the_row = 100 + (field_ui.rect.h / 20)

        for row in field_matrix.field:
            start_of_the_column = 100 + (field_ui.rect.w / 20)
            for column in row:
                self.list_of_rooms.append(Room(room=column,
                                               location=(start_of_the_column, start_of_the_row)))
                start_of_the_column += field_ui.rect.w / 10
            start_of_the_row += field_ui.rect.h / 10



