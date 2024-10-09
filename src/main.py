# -*- coding: utf-8 -*-
from src.reports import spending_by_category
from src.services import search_transaction_by_mobile_phone, testing
from src.utils import get_excel
from src.views import final_list


def main():
    '''Итоговая функция, которая запускает весь функционал программы'''
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о главной странице")
    print("2. Воспользоваться поиском по телефонным номерам")
    print("3. Получить информацию о тратах по категории")

    choice = input("Пользователь: ")
    if choice not in ["1", "2", "3"]:
        return "Неверный ввод. Пожалуйста, выберите пункт 1, 2 или 3."
    if choice == "1":
        print("Добро пожаловать на главную страницу")
        print(final_list('01.11.2021 23:50:17'), sep='\n')
        return
    elif choice == "2":
        print("Поиск по телефонным номерам")
        print(search_transaction_by_mobile_phone(testing))
        return
    else:
        print("информация о тратах по категории")
        print(*spending_by_category(get_excel('dataframe'), "Фастфуд", '17.01.2018'), sep="\n")
        return


if __name__ == "__main__":
     main()