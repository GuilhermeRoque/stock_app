import os
from stock_calculator.calculator_batch import StockCalculatorBatch

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_PATH = os.path.join(CURRENT_DIR, 'artifacts')
TESTS_PATH = os.path.join(CURRENT_DIR, 'tests')
MOCKS_PATH = os.path.join(TESTS_PATH, "mocks")
MOCK_MULTIPLE_MONTHS_PATH = os.path.join(MOCKS_PATH, "multiple_months", "sample.csv")
MOCK_SINGLE_MONTH_PATH = os.path.join(MOCKS_PATH, "single_month", "sample.csv")

# CHANGE THESE TO RUN MAIN WITH OTHER CONFIG
CALCULATOR_TYPE = StockCalculatorBatch
INPUT_CSV_FILE = MOCK_MULTIPLE_MONTHS_PATH
DESTINATION_FOLDER_PATH = ARTIFACTS_PATH
