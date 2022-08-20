'''
Парсер билетов на Яндекс.Даче
Билеты быстро разбирают и решил сделать парсер для сайта.
Поскольку это Яндекс, то спарсить содержимое простыс супом
не получилось, поскольку сайт динамический.
Пришлось работать через Selenium.
На даном этапе необходимы задачи выполнены, позже доделаю в бота.
Парсер выдает доступные ивенты, пользователь вводит (можно даже частично,
реализовано вхождение в текст) необходимый ивент и скрипт выдает
дату и количество билетов. Потом можно прикрутить телебота для
отправки сообщения когда билеты доступны, но пока нет времени на это.
'''

import requests
import time as t

from selenium import webdriver
from selenium.webdriver.common.by import By

def driver_init():
    driver = webdriver.Chrome()
    driver.get('https://plus.yandex.ru/dacha')
    return driver

def events(articles):
    for article in articles:
        event = article.find_element(By.TAG_NAME, 'h4').text
        date = article.find_element(By.CLASS_NAME, 'dacha-event-card__date').text
        print(f'------------------ Мероприятие ------------------')
        print(date)
        print(event)

def check_tickets(articles, event):
    for article in articles:
        events = article.find_element(By.TAG_NAME, 'h4')
        date = article.find_element(By.CLASS_NAME, 'dacha-event-card__date').text
        tickets = article.find_element(By.CLASS_NAME, 'dacha-event-card__button-wrapper').find_element(By.CLASS_NAME, 'dacha-event-card__description').text
        if event.lower() in events.text.lower():
            if tickets == "Билетов нет. Следите за обновлениями":
                print(date)
                print(events.text)
                print('Билетов нет. Следите за обновлениями')
                return
            else:
                print('-----------------Ваше мероприятие-----------------')
                print(date)
                print(events)
                print('---------------------Остаток билетов---------------------')
                print(tickets)
                return
    print('Такого мероприятия не существует, выберите другое')


if __name__ == '__main__':
    while True:
        driver = driver_init()
        articles = driver.find_elements(By.TAG_NAME, 'article')
        events(articles)
        print()
        event = input('Выберите мероприятие: ')
        check_tickets(articles, event)
        driver.close()
        t.sleep(10)

'''
Дальше идет код телеграм-бота TODO приложения для записи повседневных дел,
который я написал самостоятельно проходя интенсив скилбокса.
Его можно переделать для отправки сообщения, если билет появился на сайте
Будет время допилю этот код)
'''
# from random import choice
#
# import telebot
#
# token = ''
#
# bot = telebot.TeleBot(token)
#
#
# RANDOM_TASKS = ['Поспать', 'Выучить Python', 'Сходить на работу', 'Посмотреть 4 сезон Рик и Морти', 'Досмотреть Элементарно, наконец-то!']
# COMMANDS = ['/show', '/print', '/показать', '/todo', 'add', '/добавить', '/random', '/help', '/помощь', '/snail']
#
# todos = dict()
#
# splitted = []
#
# HELP = '''
# Список доступных команд:
# /show {дата(ы)}, /print {дата(ы)}, /показать {дата(ы)}  - напечать все задачи на заданную дату
# /todo {дата} {@категория} {задача}, /add {дата} {@категория} {задача}, /добавить {дата} {@категория} {задача} - добавить задачу на необходимую дату
# /random - добавить на сегодня случайную задачу
# /help, /помощь - напечатать FAQ по командам бота
# /snail {высота столба} {количество дней} - узнать доберется ли таки улитка до конца столба (вводите высоту и количество дней после команды через пробел )
# '''
# # Создал функцию - не знаю зачем, но пару раз импользовал
#
# def split_(message):
#     return message.text.split(maxsplit=2)
#
# # Онли фанкшн
#
# def add_todo(date, task, category):
#     date = date.lower()
#     if todos.get(date) is not None:
#         if category != '':
#             todos[date].append(task + ' ' + category)
#         else:
#             todos[date].append(task)
#     elif category != '':
#         todos[date] = [task + ' ' + category]
#     else:
#         todos[date] = [task]
#
# # Стартовая командОчка
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     print(message.entities[0].type)
#     bot.send_message(message.chat.id, f'Привет, выбери одну из команд)\n{HELP}')
#
# # Помагаемся
#
# @bot.message_handler(commands=['help', 'помощь'])
# def help(message):
#     bot.send_message(message.chat.id, HELP)
#
# # Рандомируем задачки
#
# @bot.message_handler(commands=['random'])
# def random(message):
#     task = choice(RANDOM_TASKS)
#     add_todo('сегодня', task, '@рандомная задача')
#     bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')
#
# # Добавляем задачки
#
# @bot.message_handler(commands=['add', 'todo', 'добавить'])
# def add(message):
#     splitt = message.text.split()
#     temp = []
#     temp_2 = []
#     for word in splitt:
#         if '@' in word[0]:
#             exist = True
#             break
#         else:
#             exist = False
#     if exist:
#         for word in splitt:
#             if '@' in word[0]:
#                 temp[:] = splitt[splitt.index(word):]
#                 temp_2[:] = splitt[2:splitt.index(word)]
#         task = ' '.join(temp_2)
#         date = splitt[1]
#         category = ' '.join(temp)
#         if len(task) >= 3:
#             add_todo(date, task, category)
#             bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date} в категорию {category}')
#         else:
#             bot.send_message(message.chat.id, 'Слишком короткая задача!')
#
#     elif len(split_(message)) == 3:
#         task = split_(message)[2]
#         date = split_(message)[1]
#         category = ''
#         if len(task) >= 3:
#             add_todo(date, task, category)
#             bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')
#         else:
#             bot.send_message(message.chat.id, 'Слишком короткая задача!')
#     else:
#         bot.send_message(message.chat.id, 'Введите команду, дату и задачу!')
#
# # Команда "Шоу" - показать, так сказать
#
# @bot.message_handler(commands=['show', 'print', 'показать'])
# def show(message):
#     dates = message.text.split()[1:]
#     if len(dates) >= 1:
#         for date in dates:
#             tasks = ''
#             if date in todos:
#                 bot.send_message(message.chat.id, f'Задачи на {date}:')
#                 for task in todos[date]:
#                     tasks += f'[ ] {task}\n'
#                 bot.send_message(message.chat.id, tasks)
#             else:
#                 bot.send_message(message.chat.id, f'Такой даты: {date} - нет :(')
#     else:
#         bot.send_message(message.chat.id, 'Введите дату после команды')
#
#
# # Решаем ту самую задачу про улитку;)
#
# @bot.message_handler(commands=['snail'])
# def snail(message):
#     if len(message.text.split()) == 3:
#         dvizh = 0
#         day = 1
#         stolb = int(message.text.split()[1])
#         days = int(message.text.split()[2])
#         bot.send_message(message.chat.id, f'Проверка сможет ли улитка добраться до вершины столба?\nВысота столба: {stolb}\nдней на подъем: {days}')
#         if stolb - days <= 2:
#             while day <= days:
#                 dvizh = dvizh + 3
#                 if dvizh > stolb:
#                     bot.send_message(message.chat.id, f'В {day}-й день улитка должна была пройти 3 метра, но столб был очень короткий, а улитка '
#                           f'быстрая и она меньше чем за день дошла до вершины столба в {stolb} метра')
#                     break
#                 else:
#                     bot.send_message(message.chat.id, f'В {day}-й день улитка прошла 3 метра и остановилась на отметке {dvizh} метра')
#                     if (dvizh < stolb) & (day < days):
#                         dvizh = dvizh - 2
#                         bot.send_message(message.chat.id, f'Ночью улитка спустилась на 2 метра и теперь она на отметке {dvizh} метра')
#                         day += 1
#                     elif dvizh >= stolb:
#                         bot.send_message(message.chat.id, f'И наконец-то дошла до крайней точки высоты в {stolb} метров')
#                         break
#         else: bot.send_message(message.chat.id, f'Выделенного колличества в размере {days} дней не хватит чтобы улитка дошла до конечной точки столба в {stolb} метров')
#     else:
#         bot.send_message(message.chat.id, 'Введите длинну столба и количество дней после команды')
#
#
# # Направляемся в нужное русло, когда ничего не понятно
#
# @bot.message_handler(content_types=["text"])
# def hello(message):
#     if message.text not in COMMANDS:
#         bot.send_message(message.chat.id, f'Привет, выбери одну из команд)\n{HELP}')
#
#
# bot.polling(none_stop=True)