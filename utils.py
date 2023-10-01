import pandas as pd
import yfinance as yf
import panel as pn

def get_df(ticker, startdate , enddate , interval="1d"):
    # interval="1d"
    # get_df(ticker ="PG", startdate="2000-01-01" , enddate="2023-09-01" , interval="1d")
    DF = yf.Ticker(ticker).history(start=startdate,end=enddate,interval=interval)
    DF['SMA50'] = DF.Close.rolling(window=50).mean()
    DF = DF.reset_index()
    return DF 

def get_hvplot(ticker , startdate , enddate , interval):
    DF = get_df(ticker , startdate=startdate , enddate=enddate , interval=interval)

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

    # # Step 5: Overlay scatter plot and linear regression line
    # return (scatter_plot * line_plot).opts(width=800, height=600, show_grid=True, gridstyle={ 'grid_line_color': 'gray'})
    # grid_style = {'grid_line_color': 'black'}#, 'grid_line_width': 1.5, 'ygrid_bounds': (0.3, 0.7),'minor_xgrid_line_color': 'lightgray', 'xgrid_line_dash': [4, 4]}
    return (scatter_plot * line_plot).opts(width=800, height=600, show_grid=True)
