class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = [*args]

    def work(self):
        for args in self.plants:
            args.grow_all()

    def harvest(self):
        if all([args.all_are_ripe for args in self.plants]):
            result = []
            for i in self.plants:
                result += i.give_away_all()
            return result
        else:
            return None, print("Томаты еще не созрели")
