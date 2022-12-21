from random import randint
from typing import Callable
import click
from pizza import Pizza
from utils import get_menu_from_file


@click.group()
def cli() -> None:
    """ Группировка команд """
    pass


@cli.command()
def menu() -> None:
    """ Выводит меню в консоль """
    # Читаем меню из файла
    pizzas_menu = get_menu_from_file('pizza_menu_config.json')
    for pizza in pizzas_menu['menu'].values():
        print(f"- {pizza['name']} {pizza['icon']}: {', '.join(pizza['recipe'])}")
    print(f'Доступные размер пицц: {Pizza.get_available_sizes()}')


def log(text, time_interval) -> Callable:
    """
    Декоратор для логирования
    с аргументами под форматирование и временной интервал
    """
    def log_decorator(func) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            for pizza in args:
                print(text.format(pizza, randint(*time_interval)))
            func(*args, **kwargs)
        return wrapper
    return log_decorator


@log('🍳 приготовили {} за {} минут!', (10, 45))
def bake(pizza: Pizza) -> None:
    """Готовит пиццу"""


@log('🛴 доставили {} за {} минут!', (30, 75))
def deliver(pizza: Pizza) -> None:
    """Доставляет пиццу"""


@log('🏠 забрали {} за {} минут!', (3, 30))
def pickup(pizza: Pizza) -> None:
    """Самовывоз"""


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza, size='L', delivery=False) -> None:
    """Готовит и доставляет пиццу"""
    # Запрашиваем меню
    pizza_menu = get_menu_from_file('pizza_menu_config.json')
    # Ищем в меню по ключу данные о пицце
    try:
        choosen_pizza = pizza_menu['menu'][pizza.lower()]
    except KeyError as key_exc:
        raise KeyError('Такой пиццы нет в меню') from key_exc
    pizza_for_order = Pizza(choosen_pizza['name'],
                            choosen_pizza['icon'],
                            choosen_pizza['recipe'],
                            size)
    bake(pizza_for_order)
    if delivery:
        deliver(pizza_for_order)
    else:
        pickup(pizza_for_order)


if __name__ == '__main__':
    cli()
