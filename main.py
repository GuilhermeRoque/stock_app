from presentation.plot_view import PlotView
from stock_calculator.calculator_batch import StockCalculatorBatch
from stock_calculator.calculator_monthly import CalculatorMonthly
from stock_calculator.stock_transactions import StockTransactionsDataFrameFactory
from tests.mocks.multiple_months import definitions

if __name__ == '__main__':
    df = StockTransactionsDataFrameFactory.read_from_csv(filepath=definitions.FILE_DIR)
    calculator_type = StockCalculatorBatch
    calculator = CalculatorMonthly(df_stock=df, calculator_type=calculator_type)
    df_result = calculator.parse_monthly()

    plot_view = PlotView(df=df_result)
    plot_view.show()
