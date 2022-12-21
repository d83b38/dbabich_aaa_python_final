from utils import get_menu_from_file


class Pizza:
    """
    Класс для пицц
    """
    # доступные размеры для всех пицц в виде private атрибута
    __allowed_sizes: list[str] = get_menu_from_file('pizza_menu_config.json')['allowed_sizes']

    @classmethod
    def get_available_sizes(cls) -> list[str]:
        """ Запрос допустимых размеров пицц """
        return cls.__allowed_sizes

    def __init__(self, name, icon, recipe, size) -> None:
        self.name = name
        self.icon = icon
        self.size = size
        self.recipe = recipe

    def __setattr__(self, key, value) -> None:
        """ Ограничения по размеру при создании экземпляров """
        if key == 'size' and value not in self.__allowed_sizes:
            raise ValueError(f'Для пицц доступны только {self.__allowed_sizes} размеры')
        self.__dict__[key] = value

    def dict(self) -> dict[str, str]:
        """ Запрос рецепта экземпляра пиццы """
        returned_recipe = {}
        for idx, value in enumerate(self.recipe):
            returned_recipe[f'ingredient_{idx+1}'] = value
        return returned_recipe

    def __eq__(self, other) -> bool:
        """ Экзамеляры пицц равны только если название, рецепт и размер совпадают """
        return self.name == other.name\
            and set(self.recipe) == set(other.recipe)\
            and self.size == other.size

    def __str__(self) -> str:
        return f'{self.icon} {self.name} size {self.size}'
