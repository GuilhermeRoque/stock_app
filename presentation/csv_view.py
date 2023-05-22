import io
import os.path

import pandas as pd


class CsvView:
    DEFAULT_PATH = "monthly_parse_report.csv"

    def __init__(self, df: pd.DataFrame, base_path: str):
        self.buffer = io.StringIO()
        df['date'] = df['date'].dt.strftime("%b-%Y")
        df = df.rename(
            columns={
                "date": "Month-Year",
                "gross_absolute_yield": "Gross Yield",
                "taxes": "Taxes",
                "net_absolute_yield": "Net Yield",
                "purchase": "Total Purchase Value",
                "sale": "Total Sale Value"
            }
        )
        df.to_csv(path_or_buf=self.buffer, index=False)
        self.buffer.seek(0)
        self.base_path = base_path

    def export(self, path: str = None):
        path = path or self.DEFAULT_PATH
        path = os.path.join(self.base_path, path)
        with open(path, "w") as file:
            file.write(self.buffer.read())
