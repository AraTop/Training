# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def mvmntobjbfld(self, field, x, y, path, fly, crawl, starting_speed = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит"""

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly: 
            starting_speed *= 1.2 
            if path == 'UP':  
                new_y = x + starting_speed   
                new_x = y 
            elif path == 'DOWN':
                new_y = y - points_per_action  
                new_x = x  
            elif path == 'LEFT': 
                new_y = y  
                new_x = x - points_per_action 
            elif path == 'RIGHT':  
                new_y = y  
                new_x = x + points_per_action
        if crawl:
            points_per_action *= 0.5
            if crawl == 'UP':  
                new_y = y + points_per_action  
                new_x = x  
            elif crawl == 'DOWN':  
                new_y = y - points_per_action  
                new_x = x 
            elif crawl == 'LEFT':  
                new_y = y  
                new_x = x - points_per_action 
            elif crawl == 'RIGHT':  
                new_y = y  
                new_x = x + points_per_action  

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...