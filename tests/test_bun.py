from praktikum.bun import Bun


class TestBun:
    def test_get_name(self):
        """
        Проверяет, что метод get_name возвращает название булочки.
        """
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_name() == 'Краторная булка N-200i', 'Не получено название булочки'

    def test_get_price(self):
        """
        Проверяет, что метод get_price возвращает цену булочки.
        """
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255, 'Не получена цена булочки'
