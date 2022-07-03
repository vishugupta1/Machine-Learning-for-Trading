""""""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""MC2-P1: Market simulator.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
All Rights Reserved  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or edited.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT honor code violation.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Student Name: Vishu Gupta (replace with your name)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT User ID: vgupta359 (replace with your User ID)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT ID: 903717362 (replace with your GT ID)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""

import datetime as dt
import os

import numpy as np

import pandas as pd
from util import get_data, plot_data

def author():
  return 'vgupta359' # replace tb34 with your Georgia Tech username.


def compute_portvals(  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    orders_file="./orders/orders.csv",
    start_val=1000000,
    commission=9.95,
    impact=0.005,
):  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Computes the portfolio values.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param orders_file: Path of the order file or the file object  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type orders_file: str or file object  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param start_val: The starting value of the portfolio  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type start_val: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type commission: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type impact: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: pandas.DataFrame  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # this is the function the autograder will call to test your code  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # code should work correctly with either input  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # TODO: Your code here
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # In the template, instead of computing the value of the portfolio, we just  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # read in the value of IBM over 6 months  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # start_date = dt.datetime(2008, 1, 1)
    # end_date = dt.datetime(2008, 6, 1)
    # portvals = get_data(["IBM"], pd.date_range(start_date, end_date))
    # portvals = portvals[["IBM"]]  # remove SPY
    # rv = pd.DataFrame(index=portvals.index, data=portvals.values)

    # References:
    # https://www.adamsmith.haus/python/answers/how-to-sort-a-pandas-dataframe-by-date-in-python#:~:text=Use%20pandas.,sort%20a%20DataFrame%20by%20date
    # https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58


    current_value = start_val
    df = pd.read_csv(orders_file)
    df = df.sort_values(by='Date')

    syms = []
    for symbol in df['Symbol']:
        if symbol not in syms:
            syms.append(symbol)

    dts = []
    for date in df['Date']:
        if date not in dts:
            dts.append(date)
    dates = pd.date_range(dts[0], dts[-1])

    data = get_data(syms, dates, False)
    #data = data.loc[dts]
    # print(df)
    # print(data)

    # df_dates = df['Date']
    # df_symbol = df['Symbol']
    # df_order = df['Order']
    # df_shares = df['Shares']

    temp = []
    for symbol in syms:
        temp1 = [symbol, 0, 0]
        temp.append(temp1)

    keeptrack = pd.DataFrame(temp, columns=['Symbols', 'Shares', 'Avg Price'])
    symbols_keys = keeptrack.loc[:,'Symbols']
    keeptrack = keeptrack.set_index('Symbols')
    #print(keeptrack)

    sol = []
    for date in dts:
        temp1 = [date, 0]
        sol.append(temp1)
    solution = pd.DataFrame(sol, columns=['date', 'value'])
    #print(solution)
    solution = solution.set_index('date')

    # iterate through each day
    # print(df)
    for i in range(len(df)):
        share = df.loc[i,'Shares']
        symbol = df.loc[i,'Symbol']
        order = df.loc[i,'Order']
        date = df.loc[i,'Date']
        price = data.loc[date,symbol]
        costorgain = price*share
        if(order == 'BUY'):
            current_value=current_value-costorgain
            keeptrack.at[symbol,'Shares'] = keeptrack.loc[symbol,'Shares']+share
            total = current_value+GetValueOfStocks(keeptrack,data,date,symbols_keys)
            solution.at[date,'value'] = total
        else:
            current_value = current_value+costorgain
            keeptrack.at[symbol, 'Shares'] = keeptrack.loc[symbol, 'Shares'] - share
            total = current_value+GetValueOfStocks(keeptrack,data,date,symbols_keys)
            solution.at[date, 'value'] = total

    #print(solution)
    portvals = solution
    return portvals  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 

def GetValueOfStocks(keeptrack, prices, date, symbols_keys):
    total = 0
    #print(keeptrack,prices,date)
    for symbol in symbols_keys:
        shares = keeptrack.loc[symbol,'Shares']
        price = prices.loc[date, symbol]
        total = total + (price*shares)
    #print(total)
    return total




def test_code():
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Helper function to test code  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # this is a helper function you can use to test your code  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # note that during autograding his function will not be called.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Define input parameters  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    of = "./orders/orders2.csv"  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    sv = 1000000  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Process orders  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    portvals = compute_portvals(orders_file="./orders/orders-01.csv", start_val=sv)
    if isinstance(portvals, pd.DataFrame):  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    else:  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        "warning, code did not return a DataFrame"  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Get portfolio stats  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    start_date = dt.datetime(2008, 1, 1)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    end_date = dt.datetime(2008, 6, 1)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.2,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.01,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.02,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        1.5,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    ]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.2,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.01,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.02,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        1.5,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    ]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Compare portfolio against $SPX  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Date Range: {start_date} to {end_date}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
if __name__ == "__main__":
    test_code()
