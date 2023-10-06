import pandas as pd
import yfinance as yf
import panel as pn

@pn.cache
def get_df(ticker, startdate , enddate , interval="1d",window=50):
    # interval="1d"
    # get_df(ticker ="PG", startdate="2000-01-01" , enddate="2023-09-01" , interval="1d")
    DF = yf.Ticker(ticker).history(start=startdate,end=enddate,interval=interval)
    DF['SMA'] = DF.Close.rolling(window=window).mean()
    DF = DF.reset_index()
    return DF 

def get_income_statement_df(ticker):
    yfobj = yf.Ticker(ticker)
    df= yfobj.financials.T
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    return df

def get_income_hvplot(ticker):
    DF = get_income_statement_df(ticker)
    plt1 = DF.hvplot.line(y='Total Revenue') * DF.hvplot.scatter(y='Total Revenue').opts(color="red") 
    plt1.opts(width=600, height=450, show_grid=True)
    plt2 = DF.hvplot.line(y='Gross Profit') * DF.hvplot.scatter(y='Gross Profit').opts(color="red") 
    plt2.opts(width=600, height=450, show_grid=True)
    plt3 = DF.hvplot.line(y='Net Income') * DF.hvplot.scatter(y='Net Income').opts(color="red")
    plt3.opts(width=600, height=450, show_grid=True)
    return pn.Column(plt1 , plt2 , plt3 )

def get_hvplot(ticker , startdate , enddate , interval,window):
    DF = get_df(ticker , startdate=startdate , enddate=enddate , interval=interval,window=window)

    import hvplot.pandas  # Ensure hvplot is installed (pip install hvplot)
    from sklearn.linear_model import LinearRegression
    import holoviews as hv
    hv.extension('bokeh')
    # Assuming your dataframe is named 'df' with columns 'Date' and 'Close'
    # If not, replace 'Date' and 'Close' with your actual column names.

    # Step 1: Create a scatter plot using hvplot
    scatter_plot = DF.hvplot(x='Date', y='Close',  kind='scatter',title=f'{ticker} Close vs. Date')

    # Step 2: Fit a linear regression model
    DF['Date2'] = pd.to_numeric(DF['Date'])
    X = DF[['Date2']]
    y = DF[['Close']] #.values
    model = LinearRegression().fit(X, y)

    # # Step 3: Predict using the linear regression model
    DF['Predicted_Close'] = model.predict(X)

    # # Step 4: Create a line plot for linear regression
    line_plot = DF.hvplot(x='Date', y='Predicted_Close', kind='line',line_dash='dashed', color='red')
    line_plot_SMA = DF.hvplot(x='Date', y='SMA', kind='line',line_dash='dashed', color='orange')

    # # Step 5: Overlay scatter plot and linear regression line
    # return (scatter_plot * line_plot).opts(width=800, height=600, show_grid=True, gridstyle={ 'grid_line_color': 'gray'})
    # grid_style = {'grid_line_color': 'black'}#, 'grid_line_width': 1.5, 'ygrid_bounds': (0.3, 0.7),'minor_xgrid_line_color': 'lightgray', 'xgrid_line_dash': [4, 4]}
    return (scatter_plot * line_plot *line_plot_SMA).opts(width=800, height=600, show_grid=True)
