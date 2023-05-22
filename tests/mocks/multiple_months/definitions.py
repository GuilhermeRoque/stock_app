import os
from pandas import Timestamp

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(CURRENT_DIR, 'sample.csv')

EXPECTED_MONTHLY_PARSE = {
    'date': [
        Timestamp('2020-01-31 00:00:00'),
        Timestamp('2020-02-29 00:00:00'),
        Timestamp('2020-03-31 00:00:00'),
        Timestamp('2020-04-30 00:00:00'),
        Timestamp('2020-05-31 00:00:00'),
        Timestamp('2020-06-30 00:00:00')
    ],
    'gross_absolute_yield': [
        -274.7777777777773,
        -113.13888888888894,
        -2240.002272727273,
        0.0,
        8873.995129870129,
        -3544.0064935064956
    ],
    'taxes': [
        0.0,
        0.0,
        0.0,
        0.0,
        1331.0992694805193,
        0.0
    ],
    'net_absolute_yield': [
        -274.7777777777773,
        -113.13888888888894,
        -2240.002272727273,
        0.0,
        7542.89586038961,
        -3544.0064935064956
    ],
    'purchase': [
        143.76,
        100.64,
        71.43,
        58.18,
        None,
        22.1
    ],
    'sale': [
        28.85,
        60.83,
        40.0,
        None,
        152.97,
        48.3
    ]
}