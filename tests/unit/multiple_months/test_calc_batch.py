from stock_calculator.calculator_batch import StockCalculatorBatch
from tests.unit.multiple_months.test_base import TestBaseMonthly


class TestCalcMonthlyBatch(TestBaseMonthly):

    def _get_calculator(self):
        return StockCalculatorBatch
