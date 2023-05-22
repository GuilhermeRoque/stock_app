import dataclasses

import pandas as pd

from stock_calculator.calculator_base import CalculatorBase
from stock_calculator.stock_transactions import StockTransactionsDataFrame


@dataclasses.dataclass
class StockTransactionsCalculatorDate:
    calculator: CalculatorBase
    date: pd.Timestamp


@dataclasses.dataclass
class MonthlyParse:
    average_price: float = 0
    measured_result: float = 0
    taxes: float = 0
    date: pd.Timestamp = None


class CalculatorMonthly:
    def __init__(self, df_stock: StockTransactionsDataFrame, calculator_type: type[CalculatorBase]):
        self.df_stock = df_stock.offset_dates_to_months()
        self.calculator_type = calculator_type
        self.calculator = calculator_type(df_stock=self.df_stock)
        self.calculators_date = []

        dates = self.df_stock.get_unique_dates()
        for date in dates:
            df_at_date = self.df_stock.filter_by_date(date=date)
            calculator = self.calculator_type(df_stock=df_at_date)
            calculator_date = StockTransactionsCalculatorDate(
                date=date,
                calculator=calculator
            )
            self.calculators_date.append(calculator_date)

    def parse_monthly(self) -> list[MonthlyParse]:
        result = []
        average_price = 0
        average_amount = 0
        for calculator_date in self.calculators_date:
            average_price = calculator_date.calculator.get_average_price(
                previous_average_price=average_price,
                previous_average_amount=average_amount
            )
            average_amount = calculator_date.calculator.get_average_amount() + average_amount
            measured_result = calculator_date.calculator.get_measured_result(average_price=average_price)
            taxes = calculator_date.calculator.get_taxes(measured_result=measured_result)
            date_parse = MonthlyParse(
                date=calculator_date.date,
                average_price=average_price,
                measured_result=measured_result,
                taxes=taxes
            )
            result.append(date_parse)

        return result


