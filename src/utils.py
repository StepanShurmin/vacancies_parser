def filter_vacancies(vacancy_list):
    """
    Фильтрует вакансии из HeadHunter и SuperJob и возвращает отфильтрованный список."""
    return sorted(vacancy_list, key=lambda x: x.name)


def get_top_vacancies(vacancy_list, n):
    """Извлекает первые N вакансий из списка."""
    return vacancy_list[:n]


def sort_by_salary_from(vacancy_list):
    """Сортирует список вакансий по зарплате от большего к меньшему."""
    return sorted(vacancy_list, reverse=True)


def print_vacancies(vacancy_list):
    """Выводит информацию о вакансиях в консоль."""
    for vacancy in vacancy_list:
        print(
            f"{vacancy.name.capitalize()}\n"
            f"з/п от {vacancy.salary_from} до {vacancy.salary_to} {vacancy.currency}\n"
            f"{vacancy.url}\n"
            f"{vacancy.description}\n"
        )
