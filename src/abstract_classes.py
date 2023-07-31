from abc import ABC, abstractmethod


class ApiJobSites(ABC):
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
    @abstractmethod
    def save_data(self, json_file):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass
