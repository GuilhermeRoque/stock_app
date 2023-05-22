from presentation.csv_view import CsvView
from presentation.plot_view import PlotView
from stock_calculator.calculator_monthly import CalculatorMonthly
from stock_calculator.stock_transactions import StockTransactionsDataFrameFactory
import definitions as main_definitions

if __name__ == '__main__':
    df = StockTransactionsDataFrameFactory.read_from_csv(filepath=main_definitions.MOCK_MULTIPLE_MONTHS_PATH)
    calculator_type = main_definitions.CALCULATOR_TYPE
    calculator = CalculatorMonthly(df_stock=df, calculator_type=calculator_type)
    df_result = calculator.parse_monthly()

    plot_view = PlotView(df=df_result, base_path=main_definitions.DESTINATION_FOLDER_PATH)
    plot_view.export()

    csv_view = CsvView(df=df_result, base_path=main_definitions.DESTINATION_FOLDER_PATH)
    csv_view.export()
