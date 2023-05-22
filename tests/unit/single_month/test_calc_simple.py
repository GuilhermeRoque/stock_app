from stock_calculator.calculator_simple import StockCalculatorSimple
from tests.unit.single_month.test_base import TestBase


class TestCalcLoop(TestBase):

    def _get_calculator(self, df_stock):
        return StockCalculatorSimple(df_stock=df_stock)
