from __future__ import annotations
from enum import StrEnum
import pandas as pd


class StockTransactionsOperationsEnum(StrEnum):
    purchase = "purchase"
    sale = "sale"


OperationsEnumMapper = {
    "Compra": StockTransactionsOperationsEnum.purchase,
    "Venda": StockTransactionsOperationsEnum.sale
}


class StockTransactionsColumnsEnum(StrEnum):
    operation = "operation"
    price = "price"
    amount = "amount"
    fee = "fee"


class StockTransactionsDataFrame:
    def __init__(self, df: pd.DataFrame):
        self._df = df

    def filter_sales_operations(self) -> StockTransactionsDataFrame:
        df = self._df[self.is_sales_operations()].reset_index()
        return StockTransactionsDataFrame(df)

    def is_sales_operations(self):
        return self._df[StockTransactionsColumnsEnum.operation] == StockTransactionsOperationsEnum.sale

    def filter_purchase_operations(self) -> StockTransactionsDataFrame:
        df = self._df[self.is_purchase_operations()].reset_index()
        return StockTransactionsDataFrame(df)

    def is_purchase_operations(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.operation] == StockTransactionsOperationsEnum.purchase

    def get_price(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.price].copy()

    def get_amount(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.amount].copy()

    def get_fee(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.fee].copy()

    def copy(self):
        return self.__class__(self._df.copy())


class StockTransactionsDataFrameFactory:
    @staticmethod
    def read_from_csv(filepath: str):
        df = pd.read_csv(filepath_or_buffer=filepath)
        df.columns = list(StockTransactionsColumnsEnum)
        df[StockTransactionsColumnsEnum.operation] = df[StockTransactionsColumnsEnum.operation].map(
            OperationsEnumMapper)
        return StockTransactionsDataFrame(df)
