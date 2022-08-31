"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time

# start_time = time.time()
# end_time = time.time()
# difference = e - s


def def_benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs})")
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Выполнено {func.__name__}\nВремя окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {end_time - start_time}")
        return result
    return wrapper


def class_benchmark(cls):
    call_attr = {k: v for k, v in cls.__dict__.items() if callable(v) and k[0] != '_'}
    for name, value in call_attr.items():
        decorated = def_benchmark(value)
        setattr(cls, name, decorated)
    return cls


@class_benchmark
class A:
    def __init__(self):
        print('init')

    def hello(self):
        print('hello')


a = A()
b = A()


a.hello()
b.hello()
