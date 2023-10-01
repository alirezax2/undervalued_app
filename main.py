
from utils import get_df,get_hvplot

import panel as pn
from datetime import datetime
pn.extension('bokeh', template='bootstrap')
import hvplot.pandas

tickers = ['AAPL', 'META', 'GOOG', 'IBM', 'MSFT','NKE']

ticker = pn.widgets.Select(name='Ticker', options=tickers)
window = pn.widgets.IntSlider(name='Window Size', value=6, start=1, end=51, step=5)

# Create a DatePicker widget with a minimum date of 2000-01-01
date_start = pn.widgets.DatePicker(
    name ="Start Date", value=datetime(2000, 1, 1),
    description='Select a Date',
    # min= datetime(2000, 1, 1)
)

date_end = pn.widgets.DatePicker(
    name ="End Date",# value=datetime(2000, 1, 1),
    description='Select a Date',
    min= datetime(2000, 1, 1)
)


pn.Row(
    pn.Column( ticker, window , date_start , date_end),
    pn.panel(pn.bind(get_hvplot, ticker, "2010-01-01","2023-09-01","1d")) #, sizing_mode='stretch_width')
).servable()

