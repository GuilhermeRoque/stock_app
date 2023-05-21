from enum import StrEnum
import pandas as pd


class StockTransactionsOperationsEnum(StrEnum):
    purchase = "Compra"
    sale = "Venda"


class StockTransactionsColumnsEnum(StrEnum):
    operation = "operation"
    price = "price"
    amount = "amount"
    fee = "fee"


class StockTransactionsDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns = list(StockTransactionsColumnsEnum)

    @property
    def operation(self):
        return self[StockTransactionsColumnsEnum.operation]

    @property
    def price(self):
        return self[StockTransactionsColumnsEnum.price]

    @property
    def amount(self):
        return self[StockTransactionsColumnsEnum.amount]

    @property
    def fee(self):
        return self[StockTransactionsColumnsEnum.fee]


class StockTransactionsFactory:
    @staticmethod
    def read_from_csv(filepath_or_buffer: str) -> StockTransactionsDataFrame:
        df = pd.read_csv(filepath_or_buffer=filepath_or_buffer)
        return StockTransactionsDataFrame(df)
