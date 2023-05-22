import abc

from stock_calculator.stock_transactions import StockTransactionsDataFrame


class CalculatorBase(abc.ABC):
    def __init__(self, df_stock: StockTransactionsDataFrame):
        self.df_stock = df_stock

    @abc.abstractmethod
    def get_average_price(self, previous_average_price=0, previous_average_amount=0):
        pass

    @abc.abstractmethod
    def get_average_amount(self) -> int:
        pass

    @abc.abstractmethod
    def get_measured_result(self, average_price: float = None):
        pass

    @abc.abstractmethod
    def get_measured_loss(self):
        pass

    @abc.abstractmethod
    def get_taxes(self, measured_result: float = None):
        pass
