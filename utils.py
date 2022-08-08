import json
from candidates import Candidate

def load_candidates(file):
    """
    Загружает список с данными кандидатов
    :param file: json файл
    :return: удобочитаемый список для python
    """
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def get_all(file):
    """
    Возвращает список с экземплярами класса Candidate с данными
    :param file: список со словарями данных по кандидатам
    :return: списко экземпляров
    """
    peoples = []
    for i in file:
        people = Candidate(i['pk'], i['name'], i['picture'], i['position'], i['gender'], i['age'], i['skills'].lower())
        peoples.append(people)
    return peoples

def get_by_pk(num, file):
    """
    Возвращает экземпляр класса Candidate по вводимому пользователю номеру
    :param num: вводимый номер
    :param file: список экземпляров класса Candidate
    :return: данные экземпляра класса
    """
    for i in file:
        if num == i.pk:
            return i

def get_by_skill(skill_name, file):
    """
    Возвращает информацию всех кандидатов содержащих вводимый пользователем скилл
    :param skill_name: искомый скилл среди кандидатов
    :param file: список экземпляров класса Candidate
    :return: удобочитаемая инфа по кандидатам
    """
    people = []
    for i in file:
        if skill_name in i.skills:
            people.append(i)
    return people
