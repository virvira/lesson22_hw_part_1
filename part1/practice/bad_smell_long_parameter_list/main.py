# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, x_coord, y_coord, direction):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.direction = direction

    def move_with_choosing_speed(self, speed):
        if self.direction == 'UP':
            new_y = self.y_coord + speed
            new_x = self.x_coord
        elif self.direction == 'DOWN':
            new_y = self.y_coord - speed
            new_x = self.x_coord
        elif self.direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - speed
        elif self.direction == 'RIGHT':
            new_y = self.y_coord
            new_x = self.x_coord + speed

        return new_x, new_y

    def move(self, field, is_fly, crawl, speed=1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
        if crawl:
            speed *= 0.5

        new_x, new_y = self.move(speed)

        field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
