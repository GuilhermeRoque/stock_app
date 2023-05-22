import numpy as np
import pandas as pd

from stock_calculator.calculator_base import CalculatorBase
from stock_calculator.stock_transactions import StockTransactionsDataFrame


class StockCalculatorBatch(CalculatorBase):

    def get_average_price(self, previous_average_price=0, previous_average_amount=0):

        amount_complete = self._get_amount_and_update_with_operation()
        average_amount = amount_complete.cumsum() + previous_average_amount
        df_stock = self.df_stock.filter_purchase_operations()
        if df_stock.is_empty():
            return previous_average_price

        price = df_stock.get_price()

        amount = df_stock.get_amount()

        average_amount_shift = average_amount.shift(1)
        average_amount_shift.iloc[0] = previous_average_amount

        average_amount = average_amount.loc[amount.index].copy()
        average_amount_shift = average_amount_shift.loc[amount.index].copy()

        brokerage_fee = df_stock.get_fee()

        x = price * amount + brokerage_fee
        y = x / average_amount
        z = average_amount_shift / average_amount

        average_price = np.zeros(len(y))
        average_price[0] = y.iloc[0]

        y = np.array(y)
        z = np.array(z)
        z = np.flip(z)
        z = np.cumprod(z)
        z = np.flip(z)
        z = np.append(z, 1)
        y = np.insert(y, 0, previous_average_price)

        result = z * y
        result = result.sum()

        return result

    def get_average_amount(self) -> int:
        amount = self._get_amount_and_update_with_operation()
        return amount.sum()

    def get_average_amount_each_entry(self) -> pd.Series:
        amount = self._get_amount_and_update_with_operation()
        return amount.cumsum()

    def _get_amount_and_update_with_operation(self):
        amount = self.df_stock.get_amount()
        is_sales = self.df_stock.is_sales_operations()
        amount.loc[is_sales] *= -1
        return amount

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

    def get_taxes(self, measured_result: float = None):
        measured_result = measured_result or self.get_measured_result()
        if measured_result > 0:
            return measured_result * 0.15
        return 0
