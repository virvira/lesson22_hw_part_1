# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move_unit_by_field(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, crawl: bool, speed: int = 1):
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y_coord = y_coord + speed
                new_x_coord = x_coord
            elif direction == 'DOWN':
                new_y_coord = y_coord - speed
                new_x_coord = x_coord
            elif direction == 'LEFT':
                new_y_coord = y_coord
                new_x_coord = x_coord - speed
            elif direction == 'RIGHT':
                new_y_coord = y_coord
                new_x_coord = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y_coord = y_coord + speed
                new_x_coord = x_coord
            elif direction == 'DOWN':
                new_y_coord = y_coord - speed
                new_x_coord = x_coord
            elif direction == 'LEFT':
                new_y_coord = y_coord
                new_x_coord = x_coord - speed
            elif direction == 'RIGHT':
                new_y_coord = y_coord
                new_x_coord = x_coord + speed

            field.set_unit(x=new_x_coord, y=new_y_coord, unit=self)
