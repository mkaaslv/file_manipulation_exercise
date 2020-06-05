"""Data, Data Everywhere"""

import csv


def get_sales_dict(filename: str) -> dict:
    """
       Get the results and store them in the dictionary.

       Results are following the format 'Product id - sales(price*quantity).
       You have to return a dict, where the names of the competitors
       are keys and the results are values (as ints).

       :param filename: is the path to the file with the results.
       :return: a dict containing names as keys and results as values (as ints).
       """
    pass


def find_average_price(filename: str) -> int:
    """
    Find average products price. Round down to integer.

    :param filename:
    :return:
    """
    pass


def find_average_quantity(filename: str) -> int:
    """
    Find average products quantity. Round up to integer.

    :param filename:
    :return:
    """
    pass


def get_total_quantity(filename: str) -> int:
    """
    Get total quantity of all products.

    :param filename:
    :return:
    """


def get_total_price(filename: str) -> int:
    """
    Get total quantity of all products.

    :param filename:
    :return:
    """


def get_sales_above(price: int, sales_dict: dict) -> list:
    """
    Get products above certain price and put them in a list.

    :param price:
    :param sales_dict:
    :return:
    """
    pass


def get_certain_product_info(product_id, sales_dict: dict) -> str:
    """
    Get info about certain product.

    :param sales_dict:
    :return:
    """


def find_top_most_profitable(top: int, sales_dict: dict, file_to_write: str) -> None:
    """
    Find top most profitable product(s) and write them to csv file.

    The csv file must look like this:

    rank,product_id,sales
    ex.
    1,p3,500
    2,p1,350
    ...

    :param top:
    :param file_to_write:
    :param sales_dict:
    :return:
    """
