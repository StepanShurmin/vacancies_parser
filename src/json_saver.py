import json

from src.abstract_classes import FILESaver
from src.vacancy import Vacancy


class JSONSaver(FILESaver):
    def __init__(self, keyword, vacancies_json) -> None:
        """
        Инициализация класса JSONSaver.
        Аргументы: keyword (str): Ключевое слово для поиска вакансий.
        vacancies_json (str): JSON-строка с данными о вакансиях.
        """
        self.keyword = keyword
        self.filename = "vacancies_JSON.json"
        self.save_data(vacancies_json)
        self.vacancy_list = []

    def save_data(self, vacancies_json) -> None:
        """
        Сохраняет данные в JSON-файл.
        Аргументы: vacancies_json (str): JSON-строка с данными о вакансиях.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies_json, file, indent=4, ensure_ascii=False)

    def add_vacancy(self) -> list:
        """
        Добавляет вакансии в список vacancy_list.
        Возвращает: list[Vacancy]: Список объектов Vacancy.
        """
        with open(self.filename, "r") as file:
            vacancies = json.load(file)

        for vacancy in vacancies:
            new_vacancy = Vacancy(
                vacancy["name"],
                vacancy["url"],
                vacancy["salary_from"],
                vacancy["salary_to"],
                vacancy["currency"],
                vacancy["description"],
            )
            self.vacancy_list.append(new_vacancy)
        return self.vacancy_list

    def del_vacancy(self) -> None:
        """Удаляет данные о вакансиях из JSON-файла."""
        with open(self.filename, "w") as file:
            json.dump("", file, indent=4, ensure_ascii=False)
