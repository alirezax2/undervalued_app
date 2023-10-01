
from utils import get_df,get_hvplot

import panel as pn

pn.extension('bokeh', template='bootstrap')
import hvplot.pandas

tickers = ['AAPL', 'META', 'GOOG', 'IBM', 'MSFT']

ticker = pn.widgets.Select(name='Ticker', options=tickers)
window = pn.widgets.IntSlider(name='Window Size', value=6, start=1, end=51, step=5)

pn.Row(
    pn.Column( ticker, window),
    pn.panel(pn.bind(get_hvplot, ticker, "2010-01-01","2023-09-01","1d")) #, sizing_mode='stretch_width')
).servable()

