import os
import timeit
import unittest

import pandas as pd

from stock_calculator import calculator
from stock_calculator.stock_transactions import StockTransactionsColumnsEnum, \
    StockTransactionsOperationsEnum, StockTransactionsFactory


class Test(unittest.TestCase):
    FILE_DIR = os.path.join(os.getcwd(), 'tests', 'sample.csv')
    EXPECTED_AVERAGE_PRICE = 26.70625

    def test_for_loop(self):
        df = StockTransactionsFactory.read_from_csv(filepath_or_buffer=self.FILE_DIR)
        df = df[:3].copy()
        average_price = calculator.calc_average_price_batch_loop(
            price=df.price,
            amount=df.amount,
            brokerage_fee=df.fee
        )
        self.assertEqual(average_price, self.EXPECTED_AVERAGE_PRICE)

        average_price_batch_calc = calculator.calc_average_price_batch(
            price=df.price,
            amount=df.amount,
            brokerage_fee=df.fee
        )
        self.assertEqual(average_price_batch_calc, self.EXPECTED_AVERAGE_PRICE)

    def test_batch(self):
        df = StockTransactionsFactory.read_from_csv(filepath_or_buffer=self.FILE_DIR)
        df = df[:3].copy()

        average_price_batch_calc = calculator.calc_average_price_batch(
            price=df.price,
            amount=df.amount,
            brokerage_fee=df.fee
        )
        self.assertEqual(average_price_batch_calc, self.EXPECTED_AVERAGE_PRICE)

    def test_time_it(self):
        df = StockTransactionsFactory.read_from_csv(filepath_or_buffer=self.FILE_DIR)
        df = df[:3].copy()
        df_slice = df.copy()

        for i in range(0, 10_000):
            df = pd.concat([df, df_slice])
        df = df.reset_index()

        def calc_loop():
            average_price = calculator.calc_average_price_batch_loop(
                price=df.price,
                amount=df.amount,
                brokerage_fee=df.fee
            )

        def calc_batch():
            average_price = calculator.calc_average_price_batch(
                price=df.price,
                amount=df.amount,
                brokerage_fee=df.fee
            )
        execution_number = 10
        result_loop = timeit.timeit(calc_loop, number=execution_number)
        result_batch = timeit.timeit(calc_batch, number=execution_number)

        print(f"Calc with pandas is {result_loop/result_batch} faster!")

if __name__ == '__main__':
    unittest.main()
