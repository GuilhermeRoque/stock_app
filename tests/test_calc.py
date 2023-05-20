import os
import unittest
from stock_calculator import calculator
from stock_calculator.stock_transactions import StockTransactionsColumnsEnum, \
    StockTransactionsOperationsEnum, StockTransactionsFactory


class Test(unittest.TestCase):
    FILE_DIR = os.path.join(os.getcwd(), 'tests', 'sample.csv')

    def test(self):
        df = StockTransactionsFactory.read_from_csv(filepath_or_buffer=self.FILE_DIR)
        average_price = 0
        average_amount = 0
        for index, row in df.iterrows():
            if row[StockTransactionsColumnsEnum.operation] != StockTransactionsOperationsEnum.purchase:
                continue
            average_price = calculator.calc_average_price(
                price=row[StockTransactionsColumnsEnum.price],
                amount=row[StockTransactionsColumnsEnum.amount],
                brokerage_fee=row[StockTransactionsColumnsEnum.fee],
                average_price=average_price,
                average_amount=average_amount
            )
            average_amount = calculator.calc_average_purchase_amount(
                amount=row['amount'],
                average_amount=average_amount
            )
            print(f"index={index} average_price={average_price}, average_amount={average_amount}")

        self.assertEqual(average_price, 26.70625)
        self.assertEqual(average_amount, 400)


if __name__ == '__main__':
    unittest.main()
