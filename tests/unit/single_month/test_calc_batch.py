from stock_calculator.calculator_batch import StockCalculatorBatch
from tests.unit.single_month.test_base import TestBase


class TestCalcBatch(TestBase):

    def _get_calculator(self, df_stock):
        return StockCalculatorBatch(df_stock=df_stock)
