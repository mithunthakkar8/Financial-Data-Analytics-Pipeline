"""
ETL Pipeline for Sandfire Resources Reports
---------------------------------------------
- Downloads and extracts tables from financial reports (10K and 6F) on edgar SEC.
- Transforms and cleans the data.
- Loads the data into PostgreSQL data warehouse.

Author: Mithun Thakkar
Date: 2025-02-23
"""

import edgar
from datetime import datetime

edgar.set_identity("Mithun Thakkar mithun.thakkar8@gmail.com")

SCCO = edgar.Company('0001001838') # SCCO CIK
print(SCCO)
filings = SCCO.get_filings()
# help(filings)


# get data relating latest 10 10-K fillings
TenKs = [x for x in SCCO.get_filings(form = '10-K').latest(10)]

filings = edgar.get_filings(year = [2021,2022,2023,2024,2025], form = ['10-K','10-Q'], amendments=True).filter(cik=1001838)
filings[0].obj().financials.get_income_statement().get_dataframe().head()
filings[0].obj().financials.get_balance_sheet().get_dataframe().head()
filings[0].obj().financials.get_cash_flow_statement().get_dataframe()


print(TenKs[0].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[1].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[2].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[3].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[4].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[5].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[6].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[7].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[8].obj().financials.get_income_statement().get_dataframe().head())
print(TenKs[9].obj().financials.get_income_statement().get_dataframe().head())

TenQs = [x for x in SCCO.get_filings(form = '10-Q').latest(10)]
print(TenQs[0].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[1].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[2].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[3].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[4].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[5].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[6].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[7].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[8].obj().financials.get_income_statement().get_dataframe().head())
print(TenQs[9].obj().financials.get_income_statement().get_dataframe().head())

# Get filings for 2020 quarters 1 and 2
filings = SCCO.get_filings(2020, quarter=[1,2])






print(financials.cashflow)
financials






# import pdfplumber
# import pandas as pd

# # Path to your PDF file
# report_path = "C:/Users/mithu/Sync/Projects/Financial Data Analytics Pipeline/Sandfire_Reports/December 2024 QuarterlyReport.pdf"

# # Open the PDF
# with pdfplumber.open(report_path) as pdf:
#     tables = []
#     for page in pdf.pages:
#         table = page.extract_table()  # Extract tables
#         print(pd.DataFrame(table))
#         if table:
#             tables.append(pd.DataFrame(table))  # Convert to DataFrame


























































