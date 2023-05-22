import dataclasses

import numpy as np
import pandas as pd

from stock_calculator.calculator_base import CalculatorBase
from stock_calculator.stock_transactions import StockTransactionsDataFrame


@dataclasses.dataclass
class StockTransactionsCalculatorDate:
    calculator: CalculatorBase
    date: pd.Timestamp


@dataclasses.dataclass
class MonthlyParse:
    gross_absolute_yield: float = 0
    net_absolute_yield: float = 0
    taxes: float = 0
    date: pd.Timestamp = None
    total_purchase_value = None
    total_sales_value = None


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
                calculator=calculator,
            )
            self.calculators_date.append(calculator_date)

    def parse_monthly(self) -> pd.DataFrame:
        result_measured = []
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
            date_parse = dict(
                date=calculator_date.date,
                gross_absolute_yield=measured_result,
                taxes=taxes
            )
            result_measured.append(date_parse)

        df_measured_results = pd.DataFrame(result_measured)
        df_measured_results['net_absolute_yield'] = df_measured_results['gross_absolute_yield'] - df_measured_results['taxes']
        df_total_values = self.df_stock.get_total_values_by_date()
        df_merged = pd.merge(
            left=df_measured_results,
            right=df_total_values
        )
        df_merged = df_merged.replace({np.nan: None})
        return df_merged


