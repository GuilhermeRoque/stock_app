import os.path

import pandas as pd
import plotly.express as px
import plotly.io as pio


class PlotView:
    DEFAULT_PATH_BAR_CHART_PNG = "monthly_net_yield.png"
    DEFAULT_PATH_LINE_CHART_PNG = "monthly_report.png"
    DEFAULT_PATH_BAR_CHART_HTML = "monthly_net_yield.html"
    DEFAULT_PATH_LINE_CHART_HTML = "monthly_report.html"

    def __init__(self, df: pd.DataFrame, base_path: str):
        df = df.copy()
        df['date'] = df['date'].dt.strftime("%b-%Y")
        self.fig_bar_net_absolute_yield = px.bar(df, x='date', y='net_absolute_yield')
        self.fig_bar_net_absolute_yield.update_layout(xaxis_title='Month-Year', yaxis_title='Net Yield')
        df = df.set_index('date').stack().reset_index().rename(columns={'level_1': 'data', 0: 'value'})
        self.fig_line_complete = px.line(df, x='date', y='value', color='data')
        self.base_path = base_path

    def export(
            self,
            path_bar_chart_png: str = None,
            path_line_chart_png: str = None,
            path_bar_chart_html: str = None,
            path_line_chart_html: str = None
    ):
        path_bar_chart_png = path_bar_chart_png or self.DEFAULT_PATH_BAR_CHART_PNG
        path_line_chart_png = path_line_chart_png or self.DEFAULT_PATH_LINE_CHART_PNG
        path_bar_chart_png = os.path.join(self.base_path, path_bar_chart_png)
        path_line_chart_png = os.path.join(self.base_path, path_line_chart_png)

        pio.write_image(self.fig_bar_net_absolute_yield, path_bar_chart_png)
        pio.write_image(self.fig_line_complete, path_line_chart_png)

        path_bar_chart_html = path_bar_chart_html or self.DEFAULT_PATH_BAR_CHART_HTML
        path_line_chart_html = path_line_chart_html or self.DEFAULT_PATH_LINE_CHART_HTML
        path_bar_chart_html = os.path.join(self.base_path, path_bar_chart_html)
        path_line_chart_html = os.path.join(self.base_path, path_line_chart_html)

        self.fig_bar_net_absolute_yield.write_html(path_bar_chart_html)
        self.fig_line_complete.write_html(path_line_chart_html)