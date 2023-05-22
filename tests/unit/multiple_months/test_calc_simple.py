from stock_calculator.calculator_simple import StockCalculatorSimple
from tests.unit.multiple_months.test_base import TestBaseMonthly


class TestCalcMonthlySimple(TestBaseMonthly):

    def _get_calculator(self):
        return StockCalculatorSimple
