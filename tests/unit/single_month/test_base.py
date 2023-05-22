import abc
import unittest

from stock_calculator.calculator_base import CalculatorBase
from stock_calculator.stock_transactions import StockTransactionsDataFrameFactory, StockTransactionsDataFrame
from tests.mocks.single_month import definitions


class TestBase(unittest.TestCase, abc.ABC):

    def setUp(self) -> None:
        df = StockTransactionsDataFrameFactory.read_from_csv(filepath=definitions.FILE_DIR)
        self.calculator = self._get_calculator(df_stock=df)

    def test_average_price(self):
        average_price_batch_calc = self.calculator.get_average_price()
        self.assertEqual(definitions.EXPECTED_AVERAGE_PRICE, average_price_batch_calc)

    def test_average_amount(self):
        average_amount_batch_calc = self.calculator.get_average_amount()
        self.assertEqual(definitions.EXPECTED_AVERAGE_AMOUNT, average_amount_batch_calc)

    def test_measured_result(self):
        measured_result = self.calculator.get_measured_result()
        self.assertAlmostEqual(definitions.EXPECTED_MEASURED_RESULT, measured_result)

    def test_measured_loss(self):
        measured_loss = self.calculator.get_measured_loss()
        self.assertEqual(definitions.EXPECTED_MEASURED_LOSS, measured_loss)

    def test_taxes(self):
        taxes = self.calculator.get_taxes()
        self.assertAlmostEqual(definitions.EXPECTED_TAXES, taxes)

    @abc.abstractmethod
    def _get_calculator(self, df_stock: StockTransactionsDataFrame) -> CalculatorBase:
        pass


if __name__ == '__main__':
    unittest.main()
