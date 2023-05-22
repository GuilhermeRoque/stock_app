import pandas as pd
import plotly.express as px


class PlotView:
    def __init__(self, df: pd.DataFrame):
        df = df.copy()
        df['date'] = df['date'].dt.strftime("%b-%Y")
        self.fig_bar_net_absolute_yield = px.bar(df, x='date', y='net_absolute_yield')
        self.fig_bar_net_absolute_yield.update_layout(xaxis_title='Month-Year', yaxis_title='Net Yield')
        df = df.set_index('date').stack().reset_index().rename(columns={'level_1': 'data', 0: 'value'})
        self.fig_line_complete = px.line(df, x='date', y='value', color='data')

    def show(self):
        self.fig_bar_net_absolute_yield.show()
        self.fig_line_complete.show()