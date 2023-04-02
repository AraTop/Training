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
    def __init__(self, data):
        self.field = data.get("field")
        self.x_coord = data.get("x_coord")
        self.y_coord = data.get("y_coord")
        self.direction = data.get("direction")
        self.is_fly = data.get("is_fly")
        self.crawl = data.get("crawl")
        self.speed = data.get("speed")

    def move(self,direction):

        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if self.is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = self.y_coord + speed
                new_x = self.x_coord
            elif direction == 'DOWN':
                new_y = self.y_coord - speed
                new_x = self.x_coord
            elif direction == 'LEFT':
                new_y = self.y_coord
                new_x = self.x_coord - speed
            elif direction == 'RIGTH':
                new_y = self.y_coord
                new_x = self.x_coord + speed
        if self.crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = self.y_coord + speed
                new_x = self.x_coord
            elif direction == 'DOWN':
                new_y = self.y_coord - speed
                new_x = self.x_coord
            elif direction == 'LEFT':
                new_y = self.y_coord
                new_x = self.x_coord - speed
            elif direction == 'RIGTH':
                new_y = self.y_coord
                new_x = self.x_coord + speed

            self.field.set_unit(x=new_x, y=new_y, unit=self)
