import pytest
from unittest.mock import Mock
from unittest.mock import patch
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        """
        Проверяет, что метод set_buns устанавливает булочку.
        """
        mock_bun = Mock()
        mock_bun.name = 'Краторная булка N-200i'
        mock_bun.price = 1255
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, 'Булочка не установлена'

    def test_add_ingredient(self):
        """
        Проверяет, что метод add_ingredient добавляет ингредиент в список.
        """
        mock_ingredient = Mock()
        mock_ingredient.type = 'SAUCE'
        mock_ingredient.name = 'Соус Spicy-X'
        mock_ingredient.price = 90
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient], 'Ингредиент не добавлен в список'

    @pytest.mark.parametrize('value', [1, 'Соус Spicy-X'])
    def test_remove_ingredient(self, value):
        """
        Проверяет, что метод remove_ingredient по индексу удаляет ингредиент из списка
        и не удаляет ингредиент по его названию.
        """
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        try:
            burger.remove_ingredient(value)
            assert burger.ingredients == [mock_ingredient_1], 'Ингредиент не удалён из списка'
        except TypeError:
            assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2], 'Ингредиент удалён по назваанию'

    def test_move_ingredient(self):
        """
        Проверяет, что метод move_ingredient при указании разных индексов
        перемещает ингредиент: удаляет и добавляет его на новое место в списке.
        """
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1], 'Ингредиент не перемещён'

    def test_negative_move_ingredient(self):
        """
        Проверяет, что метод move_ingredient при указании одинаковых индексов
        не перемещает ингредиент: удаляет и добавляет его на то же место в списке.
        """
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.move_ingredient(0, 0)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2], 'Ингредиент перемещён'

    def test_get_price(self):
        """
        Проверяет, что метод get_price считает и возвращает цену бургера.
        """
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1255

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 90

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 4400

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        price = 2 * mock_bun.get_price() + mock_ingredient_1.get_price() + mock_ingredient_2.get_price()
        assert burger.get_price() == price, 'Неверная цена бургера'

    @patch('praktikum.burger.Burger.get_price', return_value=7000)
    def test_get_receipt(self, mock_get_price):
        """
        Проверяет, что метод get_receipt формирует
        и возвращает чек с информацией о бургере.
        """
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = 'SAUCE'
        mock_ingredient_1.get_name.return_value = 'Соус Spicy-X'

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = 'FILLING'
        mock_ingredient_2.get_name.return_value = 'Мини-салат Экзо-Плантаго'

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]

        expected_receipt = (
            '(==== Краторная булка N-200i ====)\n'
            '= sauce Соус Spicy-X =\n'
            '= filling Мини-салат Экзо-Плантаго =\n'
            '(==== Краторная булка N-200i ====)\n'
            '\n'
            'Price: 7000'
        )
        assert burger.get_receipt() == expected_receipt, 'Неверный чек с информацией о бургере'
