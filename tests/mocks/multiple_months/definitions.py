import os
from pandas import Timestamp

from stock_calculator.calculator_monthly import MonthlyParse

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(CURRENT_DIR, 'sample.csv')
EXPECTED_MONTHLY_PARSE = [
    MonthlyParse(average_price=30.198888888888888,
                 measured_result=-274.7777777777773,
                 taxes=0.0,
                 date=Timestamp('2020-01-31 00:00:00')),
    MonthlyParse(average_price=30.925694444444446,
                 measured_result=-113.13888888888894,
                 taxes=0.0,
                 date=Timestamp('2020-02-29 00:00:00')),
    MonthlyParse(average_price=31.135011363636366,
                 measured_result=-2240.002272727273,
                 taxes=0.0,
                 date=Timestamp('2020-03-31 00:00:00')),
    MonthlyParse(average_price=28.64500811688312,
                 measured_result=0,
                 taxes=0.0,
                 date=Timestamp('2020-04-30 00:00:00')),
    MonthlyParse(average_price=28.64500811688312,
                 measured_result=8873.995129870129,
                 taxes=1331.0992694805193,
                 date=Timestamp('2020-05-31 00:00:00')),
    MonthlyParse(average_price=27.92334054834055,
                 measured_result=-3544.0064935064956,
                 taxes=0.0,
                 date=Timestamp('2020-06-30 00:00:00'))
]