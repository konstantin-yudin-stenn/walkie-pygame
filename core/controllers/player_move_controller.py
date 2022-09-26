class CantMoveException(Exception):
    pass


class PlayerMoveController:

    @staticmethod
    def move(field, direction):
        player_x = player_y = None
        for row in field:
            for room in row:
                if room.status == 'P':
                    player_x, player_y = room.x, room.y
        if not player_x or not player_y:
            raise CantMoveException('Игрок не найден на поле')

        if direction == 'up':
            if int(player_x) > 0:
                return int(player_x) - 1, int(player_y)

        elif direction == 'down':
            if int(player_x) < field.size - 1:
                return int(player_x) + 1, int(player_y)

        elif direction == 'left':
            if int(player_y) > 0:
                return int(player_x), int(player_y) - 1

        elif direction == 'right':
            if int(player_y) < field.size - 1:
                return int(player_x), int(player_y) + 1

        return int(player_x), int(player_y)



