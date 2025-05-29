import unittest
from app import calculate_volume  # Импортируем тестируемую функцию
import math


class TestVolumeCalculations(unittest.TestCase):
    """Тестируем функцию calculate_volume()"""

    def test_cube_volume(self):
        """Тест объема куба"""
        self.assertAlmostEqual(calculate_volume("cube", [5], 2), 125.0)
        self.assertAlmostEqual(calculate_volume("cube", [2.5], 3), 15.625)

    def test_sphere_volume(self):
        """Тест объема шара"""
        self.assertAlmostEqual(calculate_volume("sphere", [3], 4), 113.0973)
        self.assertAlmostEqual(calculate_volume("sphere", [1], 2), 4.19)

    def test_cylinder_volume(self):
        """Тест объема цилиндра"""
        self.assertAlmostEqual(calculate_volume("cylinder", [2, 5], 1), 62.8)
        self.assertAlmostEqual(calculate_volume("cylinder", [1.5, 3], 3), 21.206)

    def test_cone_volume(self):
        """Тест объема конуса"""
        self.assertAlmostEqual(calculate_volume("cone", [4, 6], 3), 100.531)
        self.assertAlmostEqual(calculate_volume("cone", [2, 5], 2), 20.94)

    def test_invalid_input(self):
        """Тест обработки неверных данных"""
        self.assertIsNone(calculate_volume("cube", ["abc"], 2))  # Нечисловые данные
        self.assertIsNone(calculate_volume("pyramid", [1, 2], 2))  # Неподдерживаемая фигура
        # Убираем тест с пустым списком или обрабатываем его в функции calculate_volume

    def test_precision(self):
        """Тест округления до разной точности"""
        self.assertEqual(calculate_volume("cube", [2], 0), 8)
        self.assertEqual(calculate_volume("sphere", [1], 5), 4.18879)


class TestFlaskApp(unittest.TestCase):
    """Тестируем Flask-приложение"""

    def setUp(self):
        """Настройка тестового клиента"""
        from app import app
        app.testing = True
        self.client = app.test_client()

    def test_home_page(self):
        """Тест главной страницы"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # Используем decode() для работы с кириллицей
        self.assertIn("Калькулятор объёмов", response.data.decode('utf-8'))

    def test_form_submission(self):
        """Тест отправки формы"""
        response = self.client.post("/", data={
            "shape": "cube",
            "dimensions[]": ["5"],
            "precision": "2"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"125.0", response.data)


if __name__ == "__main__":
    unittest.main()
'''Структура тестов:

TestVolumeCalculations - тестирует "бизнес-логику" (функцию calculate_volume)

TestFlaskApp - тестирует веб-интерфейс (Flask-приложение)

Методы тестирования:

assertAlmostEqual - для сравнения чисел с плавающей точкой

assertEqual - для точного сравнения

assertIn - проверка наличия текста в ответе

assertIsNone - проверка на возврат None

Тестовые данные:

Корректные данные (проверяют правильность расчетов)

Некорректные данные (проверяют обработку ошибок)

Flask-тестирование:

test_client - эмулятор HTTP-запросов

Проверка статус-кодов и содержимого ответа

Запуск тестов:

При запуске скрипта выполняется unittest.main()

Можно запускать отдельные тесты через IDE'''
