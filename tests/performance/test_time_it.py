import timeit
import unittest
import pandas as pd
from stock_calculator.calculator_simple import StockCalculatorSimple
from stock_calculator.calculator_batch import StockCalculatorBatch
from stock_calculator.stock_transactions import StockTransactionsDataFrameFactory, \
    StockTransactionsDataFrame
from tests import definitions


class TestTimeIt(unittest.TestCase):

    def test_average_price(self):
        df = StockTransactionsDataFrameFactory.read_from_csv(filepath=definitions.FILE_DIR)
        df = df._df
        df_slice = df.copy()

        for i in range(0, 10_000):
            df = pd.concat([df, df_slice])
        df = df.reset_index()

        df = StockTransactionsDataFrame(df=df)

        def calc_simple():
            stock_calculator_simple = StockCalculatorSimple(df_stock=df)
            stock_calculator_simple.get_average_price()

        def calc_batch():
            stock_calculator_batch = StockCalculatorBatch(df_stock=df)
            stock_calculator_batch.get_average_price()

        execution_number = 10
        result_loop = timeit.timeit(calc_simple, number=execution_number)
        result_batch = timeit.timeit(calc_batch, number=execution_number)

        print(f"Time took for calc with pandas {result_batch}\n"
              f"Time took for calc without pandas {result_loop}\n"
              f"Calc with pandas is {result_loop / result_batch} faster!\n")
