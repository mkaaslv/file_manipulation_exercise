"""Tests for top sales finder."""

from top_sales_finder import *

sales = {
    "p1": 420,
    "p2": 196,
    "p3": 20,
    "p4": 120
}


def test_get_sales_dict():
    """Test reads file right."""

    assert get_sales_dict("test_data.csv") in sales


def test_get_sales_above():
    """Test get_sales_above."""

    assert get_sales_above(20, sales) is ["p1", "p2", "p3"]
    assert get_sales_above(150, sales) is ["p1", "p2"]
    assert get_sales_above(500, sales) is []


def test_get_certain_product_info():
    """Test get_certain_product."""

    assert get_certain_product_info("p3", sales) is "p3, 20"
    assert get_certain_product_info("p1", sales) is "p1, 420"
    assert get_certain_product_info("p5", sales) is ""


def test_find_average():
    """Test find average price and quantity."""

    assert find_average_price("test_data.csv") is 9
    assert find_average_quantity("test_data.csv") is 4


def test_get_total():
    """Test get total price or quantity."""

    assert get_total_price("test_data.csv") is 84
    assert get_total_quantity("test_data.csv") is 40


def test_find_top_most_profitable():
    """Test most profitable."""

    find_top_most_profitable(1, sales, "top_sales.csv")
    test_file("top_sales.csv", 1)

    find_top_most_profitable(3, sales, "top_sales.csv")
    test_file("top_sales.csv", 3)

    find_top_most_profitable(5, sales, "top_sales.csv")
    test_file("top_sales.csv", 5)


def test_file(filename: str, top: int):
    """Test if files are correct."""
    file_lines = ["rank,product_id,sales", "1,p1,420", "2,p2,196", "3,p4,120", "4,p3,20"]

    with open(filename, "r") as open_file:
        assert len(open_file.readlines()) == top + 1

        for i in range(len(file_lines)):
            for line in open_file:
                assert line == file_lines[i]
