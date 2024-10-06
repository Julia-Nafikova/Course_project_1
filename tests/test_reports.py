# -*- coding: utf-8 -*-
from src.reports import spending_by_category


def test_spending_by_category_with_date(sample_data):
    # Тестирование функции с указанной датой и категорией "Продукты"
    result = spending_by_category(sample_data, "Продукты", "30.12.2021")
    assert len(result) == 3


def test_spending_by_category_no_date(sample_data):
    result = spending_by_category(sample_data, "Продукты")
    assert len(result) == 3  # Ожидаем три строки, соответствующие категории "Продукты"


def test_spending_by_category_future_date(sample_data):
    # Тестирование функции с будущей датой
    result = spending_by_category(sample_data, "Продукты", "01.01.2023")
    assert (
        len(result) == 0
    )  # Ожидается 0 строк, так как нет операций с категорией "Продукты" за последние три месяца от будущей даты


def test_spending_by_category_no_transactions(sample_data):
    # Тестирование функции с категорией, для которой нет транзакций
    result = spending_by_category(sample_data, "Здоровье", "30.12.2021")
    assert len(result) == 0  # Ожидается 0 строк, так как нет транзакций с категорией "Здоровье"
