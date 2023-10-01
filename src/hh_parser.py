import time

import requests

from src.abstract_classes import ApiJobSites


class HeadHunterAPI(ApiJobSites):
    """Класс для запроса вакансий через HH API."""

    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword):
        """
        Инициализация класса HeadHunterAPI.
        Аргументы: keyword (str): Ключевое слово для поиска вакансий.
        """
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15"
        }
        self.params = {"per_page": 10, "page": None, "text": keyword, "archive": False, "only_with_salary": True}
        self.keyword = keyword
        self.vacancies = []

    def get_request(self) -> list[dict]:
        """
        Отправляет запрос к HH API для получения вакансий.
        Возвращает: cписок словарей с информацией о вакансиях.
        """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            print(f"Ошибка получения вакансий! Статус-код: {response.status_code}")

    def get_vacancies(self, page_count=5) -> None:
        """
        Получает вакансии через HH API.
        Аргументы: page_count (int): Количество страниц для получения. По умолчанию 5.
        """
        self.vacancies = []
        for page in range(page_count):
            time.sleep(1)
            page_vacancies = []
            self.params["page"] = page
            print(f"{self.__class__.__name__} загрузка страницы {page + 1} HH -", end=" ")
            try:
                page_vacancies = self.get_request()
            except Exception as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f"Загружено вакансий: {len(page_vacancies)}")
            if len(page_vacancies) == 0:
                print(f"Не удалось загрузить страницу {page + 1}")
                break

    def get_formatted_vacancies(self) -> list[dict]:
        """
        Возвращает отформатированные данные о вакансиях.
        Возвращает: список словарей с отформатированной информацией о вакансиях.
        """
        formatted_vacancies = []

        for vacancy in self.vacancies:
            formatted_vacancy = {
                "name": vacancy["name"].lower(),
                "url": vacancy["alternate_url"],
                "salary_from": vacancy["salary"]["from"] if vacancy["salary"]["from"] is not None else 0,
                "salary_to": vacancy["salary"]["to"]
                if vacancy["salary"]["to"] is not None
                else vacancy["salary"]["from"],
                "currency": vacancy["salary"]["currency"] if vacancy["salary"] else "",
                "description": vacancy["snippet"]["requirement"]
                if vacancy["snippet"]["requirement"] is not None
                else "",
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies
