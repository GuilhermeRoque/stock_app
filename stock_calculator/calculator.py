import pandas as pd


def calc_average_price_batch(
        price: pd.Series,
        amount: pd.Series,
        brokerage_fee: pd.Series,
):
    pass


def calc_average_price(
        price: float | pd.Series,
        amount: int | pd.Series,
        brokerage_fee: float | pd.Series,
        average_price: float = 0,
        average_amount: int = 0
) -> float:
    """
    :param price: Stock purchase price (PC)
    :param amount: Stock amount (QC)
    :param brokerage_fee: Stock brokerage fee (TC)
    :param average_price: Stock average price, initially zero (PM)
    :param average_amount: Stock average amount, initially zero (QM)
    :return: New calculated average price (PM)
    """
    new_average_amount = calc_average_purchase_amount(
        amount=amount,
        average_amount=average_amount
    )
    average_price = (average_price * average_amount + price * amount + brokerage_fee) / new_average_amount
    return average_price


def calc_average_purchase_amount(
        amount: int,
        average_amount: int = 0
) -> int:
    """
    :param amount: Stock amount (QC)
    :param average_amount: Stock average amount, initially zero (QM)
    :return: New calculated average amount (QM)
    """
    average_amount = average_amount + amount
    return average_amount


def calc_measured_result(
        price: pd.Series,
        amount: pd.Series,
        average_price: float = 0,
        average_amount: int = 0
) -> pd.Series:
    """
    :param price: Stock sale price (PV)
    :param amount: Stock sale amount (QC)
    :param average_price: Stock average price, initially zero (PM)
    :param average_amount: Stock average amount, initially zero (QM)
    :return: New calculated average price (PM)
    """
    measured_result = (price - average_price) / (average_amount - amount)
    return measured_result


def calc_average_sale_amount(
        amount: pd.Series,
        average_amount: int = 0
) -> pd.Series:
    """
    :param amount: Stock amount (QV)
    :param average_amount: Stock average amount, initially zero (QM)
    :return: New calculated average amount (QM)
    """
    average_amount = average_amount - amount
    return average_amount
