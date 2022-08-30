class TomatoBush:
    tomato_list = list

    def __init__(self, *args):
        self.tomato_list = [*args]

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomato_list])

    def give_away_all(self):
        for tomato in self.tomato_list:
            if tomato == 'Красный':
                self.tomato_list.clear()
            return self.tomato_list
