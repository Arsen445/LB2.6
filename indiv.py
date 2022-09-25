#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    trains = []
    while True:
        print("Напишите Help для справк по программе")
        print("введите комаду")
        command = input()

        if command == "Help" or command == "help" or command == "HELP":
            print("Список команд:\n")
            print("[add - добавить рейс]")
            print("[list - вывести список рейсов]")
            print("[select <номер> - запросить рейсы с номером]")
            print("[help - отобразить справку]")
            print("[exit - завершить работу с программой]")

        elif command == ("add"):
            print("сколько поездов в расписании?")
            kol = int(input())
            k = 0
            for m in range(int(kol)):
                k = k + 1
                d = input("Введите пункт для "+str(k)+" поезда:  ")
                t = int(input("Введите время поезда:  "))
                n = int(input("Введите номер поезда:  "))
                train = {
                    'd': d,
                    'n': n,
                    't': t,
                }
                trains.append(train)
                if len(trains) > 1:
                    trains.sort(key=lambda item: item.get('n', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 5,
                '-' * 20,
                '-' * 14,
                '-' * 16
            )
            print(line)
            print(
                '| {:^5} | {:^20} | {:^14} | {:^16} |'.format(
                    "№",
                    "Едет в",
                    "№ поезда",
                    "Время отпр-ния"
                )
            )
            print(line)
            # Вывести данные о всех поездах.
            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>5} | {:<20} | {:<14} | {:>16} |'.format(
                        idx,
                        train.get('d', ''),
                        train.get('n', 0),
                        train.get('t', '')
                    )
                )
            print(line)

        elif command == 'exit':
            break

        elif command.startswith('select '):
                # Переменная равная введенному номеру
                selected_num = command[7:]
                # Инициализировать счетчик.
                count = 0
                # Проверить сведения работников из списка.
                for train in trains:
                    if train.get('num', 0) == selected_num:
                        count += 1
                        print(
                            '{:>4}: {} {}'.format(
                                count, train.get('num', 0),
                                train.get('num', 0)
                            )
                        )

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
