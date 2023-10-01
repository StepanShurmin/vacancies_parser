def filter_vacancies(vacancy_list: list) -> list:
    """
    Фильтрует вакансии из HeadHunter и SuperJob и возвращает отфильтрованный список.
    Аргументы: vacancy_list: Список вакансий для фильтрации.
    Возвращает: отфильтрованный список вакансий.
    """
    return sorted(vacancy_list, key=lambda x: x.name)


def get_top_vacancies(vacancy_list: list, n: int) -> list:
    """
    Извлекает первые N вакансий из списка.
    Аргументы: vacancy_list: Список вакансий,
    n: количество вакансий для извлечения.
    Возвращает: список первых N вакансий.
    """
    return vacancy_list[:n]


def sort_by_salary_from(vacancy_list: list) -> list:
    """
    Сортирует список вакансий по зарплате от большего к меньшему.
    Аргументы: vacancy_list: Список вакансий.
    Возвращает: отсортированный список вакансий.
    """
    return sorted(vacancy_list, reverse=True)


def print_vacancies(vacancy_list: list) -> None:
    """
    Выводит информацию о вакансиях в консоль.
    Аргументы: vacancy_list: Список вакансий.
    """
    for vacancy in vacancy_list:
        print(
            f"{vacancy.name.capitalize()}\n"
            f"з/п от {vacancy.salary_from} до {vacancy.salary_to} {vacancy.currency}\n"
            f"{vacancy.url}\n"
            f"{vacancy.description}\n"
        )
