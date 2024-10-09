# -*- coding: utf-8 -*-
import pandas as pd
from src.logger import setup_logger

logger = setup_logger("utils", "logs/utils.log")


def get_excel(formatting):
    """Читает файл и форматирует в дф или словарь"""
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    logger.info("файл перекодирован в список словарей")
    if formatting == "dataframe":
        return get_excel_file
    elif formatting == "dict":
        return get_excel_file.to_dict(orient="records")
    else:
        logger.error("Возникла ошибка")
        raise ValueError("Invalid format specified. Use 'dataframe' or 'dict'.")


# print(get_excel('dataframe'))
