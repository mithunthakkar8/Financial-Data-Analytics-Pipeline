# as can be seen from running the below code, there is no standard format in which data is reported by the company 
# net sales is reported differently in 4 different filings. 
# Because of this, there is no point using edgar for this project. Edgar data can only be used for data science/analysis purposes 
# and not for data engineering purposes because there will be required good bit of manual intervention and data preprocessing
# before this data can be displayed in the front end or even for storing in a database. 


import edgar
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

edgar.set_identity("Mithun Thakkar mithun.thakkar8@gmail.com")

Amazon = edgar.Company('1018724') # Amazon CIK
print(Amazon)
filings = Amazon.get_filings()
help(filings)

# get latest filing data
TenK = Amazon.get_filings(form='10-K').latest(1).obj()
financials = TenK.financials
BS_= financials.get_balance_sheet().get_dataframe()
IS_= financials.get_income_statement().get_dataframe()
CF_= financials.get_cash_flow_statement().get_dataframe()
print(BS_)
print(IS_.transpose())

# use the label in the index to fetch data 
IS_.loc['Total net sales']


# get data relating latest 10 fillings
TenKs = [x for x in Amazon.get_filings(form = '10-K').latest(10)]
print(TenKs[2].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[5].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[6].obj().financials.get_income_statement().get_dataframe().head())





print(financials.cashflow)
financials



