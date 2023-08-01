from abc import ABC, abstractmethod


class ApiJobSites(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями."""

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_formatted_vacancies(self):
        pass


class FILESaver(ABC):
    """Абстрактный класс для работы с полученными данными с сайтов с вакансиями."""

    @abstractmethod
    def save_data(self, json_file):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass
