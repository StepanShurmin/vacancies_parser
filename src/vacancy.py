class Vacancy:
    def __init__(
        self, name: str, url: str, salary_from: float, salary_to: float, currency: str, description: str
    ) -> None:
        """Инициализация класса Vacancy."""
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Vacancy."""
        return f"Вакансия (название = '{self.name}', зп = '{self.salary_from}' - {self.salary_to} {self.currency})"

    def __eq__(self, other) -> bool:
        """
        Проверяет, является ли объект Vacancy равным другому объекту Vacancy.
        Аргументы: other (Vacancy): Другой объект Vacancy для сравнения.
        Возвращает: bool.
        """
        return self.salary_from == other.salary_from

    def __lt__(self, other) -> bool:
        """
        Проверяет, является ли объект Vacancy меньше другого объекта Vacancy.
        Аргументы: other (Vacancy): Другой объект Vacancy для сравнения.
        Возвращает: bool.
        """
        return self.salary_from < other.salary_from

    def __gt__(self, other) -> bool:
        """
        Проверяет, является ли объект Vacancy больше другого объекта Vacancy.
        Аргументы: other (Vacancy): Другой объект Vacancy для сравнения.
        Возвращает: bool.
        """
        return self.salary_from > other.salary_from
