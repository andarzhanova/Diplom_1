import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredient:

    def test_get_price(self):
        """
        Проверяет, что метод get_price возвращает цену ингредиента.
        """
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_price() == 90, 'Не получена цена ингредиента'

    def test_get_name(self):
        """
        Проверяет, что метод get_name возвращает название ингредиента.
        """
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_name() == 'Соус Spicy-X', 'Не получено название ингредиента'

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90, 'SAUCE'],
            [ingredient_types.INGREDIENT_TYPE_FILLING, 'Мини-салат Экзо-Плантаго', 4400, 'FILLING']
        ]
    )
    def test_get_type(self, type, name, price, expected_ingredient):
        """
        Проверяет, что метод get_type возвращает тип ингредиента.
        """
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient, 'Не получен тип ингредиента'
