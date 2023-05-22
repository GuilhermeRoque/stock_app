import numpy as np

from stock_calculator.calculator_base import CalculatorInterface
from stock_calculator.stock_transactions import StockTransactionsDataFrame


class StockCalculatorBatch(CalculatorInterface):
    def __init__(self, df_stock: StockTransactionsDataFrame):
        self.df_stock = df_stock

    def get_average_price(self):
        df_stock = self.df_stock.filter_purchase_operations()
        price = df_stock.get_price()
        amount = df_stock.get_amount()
        brokerage_fee = df_stock.get_fee()

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

    def get_average_purchase_amount(self) -> int:
        df_stock = self.df_stock.filter_purchase_operations()
        return df_stock.get_amount().sum()

    def get_measured_result(self, average_price: float = None):
        average_price = average_price or self.get_average_price()
        df_stock = self.df_stock.filter_sales_operations()
        price = df_stock.get_price()
        amount = df_stock.get_amount()
        fee = df_stock.get_fee()
        measured_result = (price - average_price) * amount - fee
        return measured_result.sum()

    def get_measured_loss(self):
        measured_result = self.get_measured_result()
        if measured_result < 0:
            return measured_result * -1
        return 0

    def get_taxes(self):
        measured_result = self.get_measured_result()
        if measured_result > 0:
            return measured_result * 0.15
        return 0
