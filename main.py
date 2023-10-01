
from utils import get_df,get_hvplot

import panel as pn
from datetime import datetime
from datetime import date
pn.extension('bokeh', template='bootstrap')
import hvplot.pandas

tickers = ['AAPL', 'META', 'GOOG', 'IBM', 'MSFT','NKE','DLTR','DG']

ticker = pn.widgets.Select(name='Ticker', options=tickers)
window = pn.widgets.IntSlider(name='Window Size', value=50, start=1, end=200, step=5)

# Create a DatePicker widget with a minimum date of 2000-01-01
date_start = pn.widgets.DatePicker(
    name ="Start Date",
    description='Select a Date',
    start= date(2000, 1, 1)
)

date_end = pn.widgets.DatePicker(
    name ="End Date",# value=datetime(2000, 1, 1),
    description='Select a Date',
    end= date(2023, 9, 1)
)

date_start.value = date(2010,1,1)
date_end.value = date.today()

pn.Row(
    pn.Column( ticker, window , date_start , date_end),
    # pn.panel(pn.bind(get_hvplot, ticker, "2010-01-01","2023-09-01","1d")) #, sizing_mode='stretch_width')
    pn.panel(pn.bind(get_hvplot, ticker, date_start , date_end,"1d",window)) #, sizing_mode='stretch_width')
).servable(title="Under Valued Screener- Linear Regression")

