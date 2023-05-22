import abc
import unittest

from stock_calculator.calculator_base import CalculatorBase
from stock_calculator.calculator_monthly import CalculatorMonthly
from stock_calculator.stock_transactions import StockTransactionsDataFrameFactory
from tests.mocks.multiple_months import definitions


class TestBaseMonthly(unittest.TestCase, abc.ABC):

    def setUp(self) -> None:
        self.df = StockTransactionsDataFrameFactory.read_from_csv(filepath=definitions.FILE_DIR)
        self.calculator_type = self._get_calculator()
        self.calculator = CalculatorMonthly(df_stock=self.df, calculator_type=self.calculator_type)

    def test_average_price_monthly(self):
        average_price_calc = self.calculator.parse_monthly().to_dict(orient='list')
        self.assertEqual(definitions.EXPECTED_MONTHLY_PARSE, average_price_calc)

    # def test_average_amount_monthly(self):
    #     average_amount_batch_calc = self.calculator.get_average_purchase_amount()
    #     self.assertEqual(definitions.EXPECTED_AVERAGE_PURCHASE_AMOUNT, average_amount_batch_calc)
    #
    # def test_measured_result_monthly(self):
    #     measured_result = self.calculator.get_measured_result()
    #     self.assertAlmostEqual(definitions.EXPECTED_MEASURED_RESULT, measured_result)
    #
    # def test_measured_loss_monthly(self):
    #     measured_loss = self.calculator.get_measured_loss()
    #     self.assertEqual(definitions.EXPECTED_MEASURED_LOSS, measured_loss)
    #
    # def test_taxes_monthly(self):
    #     taxes = self.calculator.get_taxes()
    #     self.assertAlmostEqual(definitions.EXPECTED_TAXES, taxes)

    @abc.abstractmethod
    def _get_calculator(self) -> type[CalculatorBase]:
        pass


if __name__ == '__main__':
    unittest.main()
