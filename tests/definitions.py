import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(TEST_DIR, 'mocks/sample.csv')
EXPECTED_AVERAGE_PRICE = 26.70625
EXPECTED_AVERAGE_PURCHASE_AMOUNT = 400
EXPECTED_AVERAGE_AMOUNT = 200
EXPECTED_MEASURED_RESULT_AFTER_FIRST_SALE = -26.125
EXPECTED_MEASURED_RESULT_AFTER_SECOND_SALE = 59.875
EXPECTED_MEASURED_RESULT = 33.75
EXPECTED_MEASURED_LOSS = 0
EXPECTED_TAXES = 5.0625
