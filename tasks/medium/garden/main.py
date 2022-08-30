from tasks.medium.garden.gardener import Gardener
from tasks.medium.garden.tomato import Tomato
from tasks.medium.garden.tomato_bush import TomatoBush

if __name__ == '__main__':
    tomato_bush_1 = TomatoBush(Tomato(0), Tomato(1), Tomato(0))
    tomato_bush_2 = TomatoBush(Tomato(0), Tomato(0), Tomato(1), Tomato(1))
    gardener = Gardener('Emi', tomato_bush_1, tomato_bush_2)
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.harvest()
