from __future__ import annotations
from enum import StrEnum
import pandas as pd


class StockTransactionsOperationsEnum(StrEnum):
    purchase = "purchase"
    sale = "sale"


class StockTransactionsColumnsEnum(StrEnum):
    operation = "operation"
    price = "price"
    amount = "amount"
    fee = "fee"
    ticker = "ticker"
    date = "date"


class StockTransactionsDataFrame:
    def __init__(self, df: pd.DataFrame):
        self._df = df

    def filter_sales_operations(self) -> StockTransactionsDataFrame:
        df = self._df[self.is_sales_operations()].copy()
        return StockTransactionsDataFrame(df)

    def is_sales_operations(self):
        return self._df[StockTransactionsColumnsEnum.operation] == StockTransactionsOperationsEnum.sale

    def filter_purchase_operations(self) -> StockTransactionsDataFrame:
        df = self._df[self.is_purchase_operations()].copy()
        return StockTransactionsDataFrame(df)

    def is_purchase_operations(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.operation] == StockTransactionsOperationsEnum.purchase

    def get_price(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.price].copy()

    def get_unique_dates(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.date].drop_duplicates()

    def filter_by_date(self, date: pd.Timestamp) -> StockTransactionsDataFrame:
        return StockTransactionsDataFrame(self._df[self.is_date(date=date)].copy())

    def is_date(self, date: pd.Timestamp):
        return self._df[StockTransactionsColumnsEnum.date] == date

    def get_amount(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.amount].copy()

    def get_operation(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.operation].copy()

    def get_fee(self) -> pd.Series:
        return self._df[StockTransactionsColumnsEnum.fee].copy()

    def get_index(self) -> pd.Series:
        return self._df.index.copy()

    def offset_dates_to_months(self) -> StockTransactionsDataFrame:
        df = self._df.copy()
        df = df.sort_values(by=StockTransactionsColumnsEnum.date)
        df.loc[
            df[StockTransactionsColumnsEnum.date].notna(), StockTransactionsColumnsEnum.date
        ] += pd.offsets.MonthEnd(0)
        return StockTransactionsDataFrame(df)

    def copy(self):
        return StockTransactionsDataFrame(self._df.copy())

    def is_empty(self):
        return self._df.empty

ColumnsEnumMapper = {
    "Operação": StockTransactionsColumnsEnum.operation,
    "Preço": StockTransactionsColumnsEnum.price,
    "Quantidade": StockTransactionsColumnsEnum.amount,
    "Taxa de corretagem": StockTransactionsColumnsEnum.fee,
    "Data da operação": StockTransactionsColumnsEnum.date,
    "Ação": StockTransactionsColumnsEnum.ticker
}

OperationsEnumMapper = {
    "Compra": StockTransactionsOperationsEnum.purchase,
    "Venda": StockTransactionsOperationsEnum.sale
}


class StockTransactionsDataFrameFactory:

    @staticmethod
    def read_from_csv(filepath: str):
        df = pd.read_csv(filepath_or_buffer=filepath)
        df = df.rename(columns=ColumnsEnumMapper)
        df = df.reindex(columns=list(StockTransactionsColumnsEnum))
        df[StockTransactionsColumnsEnum.date] = pd.to_datetime(df[StockTransactionsColumnsEnum.date])
        df[StockTransactionsColumnsEnum.operation] = df[StockTransactionsColumnsEnum.operation].map(
            OperationsEnumMapper)
        return StockTransactionsDataFrame(df)
