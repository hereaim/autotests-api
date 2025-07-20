from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, используемый для генерации случайных данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайную строку текста.
        :return: Сгенерированная строка текста.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4
        :return: Сгенерированный UUID4
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайную электронную почту.
        :return: Сгенерированная электронная почта.
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерирует случайную строку предложения.
        :return: Сгенерированная строка предложения.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайную строку пароля.
        :return: Сгенерированная строка пароля.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.
        :return: Сгенерированная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.
        :return: Сгенерированное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество.
        :return: Сгенерированное отчество.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует случайное время.
        :return: Сгенерированное время.
        """
        return f"{self.faker.random_int(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число.
        :param start: Начальное значение (по умолчанию 1).
        :param end: Конечное значение (по умолчанию 100).
        :return: Сгенерированное целое число.
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует случайное максимальное значение баллов.
        :return: Сгенерированное максимальное значение баллов.
        """
        return self.faker.random_int(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайное минимальное значение баллов.
        :return: Сгенерированное минимальное значение баллов.
        """
        return self.faker.random_int(1, 49)


fake = Fake(faker=Faker())
