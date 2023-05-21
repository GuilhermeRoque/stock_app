import numpy as np
import pandas as pd


def calc_average_price_batch(
        price: pd.Series,
        amount: pd.Series,
        brokerage_fee: pd.Series,
) -> float:
    x = price * amount + brokerage_fee
    average_amount = amount.cumsum()
    previous_average_amount = average_amount.shift(1).fillna(0)
    y = x / average_amount
    z = previous_average_amount / average_amount

    average_price = np.zeros(len(y))
    average_price[0] = y.iloc[0]

    y = np.array(y)
    z = np.array(z)
    z = z[1:]
    z = np.flip(z)
    z = np.cumprod(z)
    z = np.flip(z)
    z = np.append(z, 1)
    result = z * y
    result = result.sum()

    return result


def calc_average_price_batch_loop(
    price: pd.Series,
    amount: pd.Series,
    brokerage_fee: pd.Series,
) -> float:
    average_price = 0
    average_amount = 0
    for i in range(0, len(price)):
        average_price = calc_average_price(
            price=price[i],
            amount=amount[i],
            brokerage_fee=brokerage_fee[i],
            average_price=average_price,
            average_amount=average_amount
        )
        average_amount = calc_average_purchase_amount(
            amount=amount[i],
            average_amount=average_amount
        )
    return average_price

def calc_average_purchase_amount_batch(amount: pd.Series):
    return amount.sum()


def calc_average_price(
        price: float,
        amount: int,
        brokerage_fee: float,
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
    previous_average_amount = average_amount
    average_amount = calc_average_purchase_amount(
        amount=amount,
        average_amount=average_amount
    )
    x = price * amount + brokerage_fee
    average_price = (average_price * previous_average_amount + x) / average_amount
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
