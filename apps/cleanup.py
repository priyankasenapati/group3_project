# Run this file to create tables in postgresql
# Import dependencies
import pandas as pd
from tabula import read_pdf
import numpy as np
from datetime import datetime
from sqlalchemy import create_engine, func
import psycopg2
from config import db_password

#####################################################
# US Divorce Rates by States Dataset
df = read_pdf(r"data_extraction\state-divorce-rates-90-95-99-18.pdf")
divorce = df.copy()
# Drop columns with null values
divorce = divorce.dropna(axis=1, how='all')
# Set column names
divorce.columns = divorce.iloc[0]
divorce = divorce.drop(divorce.index[0])
# Set 'State_name' column
divorce = divorce.rename(columns={np.nan: 'State_name'})
# Column '2005' and '2004' are grouped together
# Split column '2005 2004'
divorce[['2005', '2004']] = divorce['2005 2004'].str.split(expand=True)
# Drop column '2005 2004'
divorce = divorce.drop(columns='2005 2004')
# List of states
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
# Create 'State' column
divorce['State'] = states
# Reorder columns
divorce = divorce[['State', 'State_name', '2018', '2017', '2016', '2015',
                   '2014', '2013', '2012', '2011', '2010', '2009', '2008',
                   '2007', '2006', '2005', '2004', '2003', '2002', '2001',
                   '2000', '1999', '1995', '1990']]
# Convert object columns to float
divorce[['2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011',
         '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003',
         '2002', '2001', '2000', '1999', '1995', '1990']] \
       = divorce[['2018', '2017', '2016', '2015', '2014', '2013', '2012',
                  '2011', '2010', '2009', '2008', '2007', '2006', '2005',
                  '2004', '2003', '2002', '2001', '2000', '1999', '1995',
                  '1990']].apply(pd.to_numeric, errors='coerce')
# Create pivot table
divorce_pivot = pd.pivot_table(divorce, index=['State', 'State_name'])
divorce_pivot.columns = pd.to_datetime(divorce_pivot.columns, format='%Y').year
divorce_pivot
# Save to csv
divorce_pivot.to_csv(r'data_extraction\cleaned_data\divorce_by_state.csv')


#######################################################
# # US Marriage Rates by State: Dataset
df = read_pdf(r"data_extraction\state-marriage-rates-90-95-99-18.pdf")
# Copy dataframe
marriage = df.copy()
# Drop columns with null values
marriage = marriage.dropna(axis=1, how='all')
# Set column names
marriage.columns = ['State_name', '2018', '2017', '2016', '2015', '2014',
                    '2013', '2012', '2011', '2010', '2009', '2008_2007_2006',
                    '2005', '2004', '2003', '2002', '2001', '2000', '1999',
                    '1995', '1990']
marriage = marriage.drop(marriage.index[0])

# Column '2008','2007' and '2006' are grouped together
# Split column '2008_2007_2006'
marriage[['2008', '2007', '2006']] \
       = marriage['2008_2007_2006'].str.split(expand=True)
# Drop column '2008_2007_2006'
marriage = marriage.drop(columns='2008_2007_2006')
# Create 'State' column
marriage['State'] = states
# Reorder columns
marriage = marriage[['State', 'State_name', '2018', '2017', '2016', '2015',
                     '2014', '2013', '2012', '2011', '2010', '2009', '2008',
                     '2007', '2006', '2005', '2004', '2003', '2002', '2001',
                     '2000', '1999', '1995', '1990']]
# Convert object columns to float
marriage[['2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011',
          '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003',
          '2002', '2001', '2000', '1999', '1995', '1990']] \
       = marriage[['2018', '2017', '2016', '2015', '2014', '2013', '2012',
                   '2011', '2010', '2009', '2008', '2007', '2006', '2005',
                   '2004', '2003', '2002', '2001', '2000', '1999', '1995',
                   '1990']].apply(pd.to_numeric, errors='coerce')
# Create pivot table
marriage_pivot = pd.pivot_table(marriage, index=['State', 'State_name'])
marriage_pivot.columns \
       = pd.to_datetime(marriage_pivot.columns, format='%Y').year
# Save to csv
marriage_pivot.to_csv(r'data_extraction\cleaned_data\marriage_by_state.csv')


####################################################
# # US Marriage and Divorce Rate over the years
df1, df2 \
       = read_pdf(r'data_extraction\national-marriage-divorce-rates-00-18.pdf',
                  pages='all', multiple_tables=True)
national_marriage = df1.copy()
national_divorce = df2.copy()


# ## National Marriage Rate
# Rename columns and drop the first 3 rows
national_marriage.columns = ['year', 'Marriages', 'Population',
                             'Rate per 1,000 total population']
national_marriage = national_marriage \
       .drop(national_marriage.index[0:3]).reset_index(drop=True)
# Correct Year column
years = []
for year in national_marriage['year']:
    first_year = year[:4]
    years.append(first_year)
national_marriage = national_marriage.drop(columns='year')
national_marriage['year'] = years
# Reorder column
national_marriage = national_marriage[['year', 'Marriages', 'Population',
                                       'Rate per 1,000 total population']]
# Save to csv file
national_marriage.to_csv(r'data_extraction\cleaned_data\us_marriage_rate.csv',
                         index=False)


# ## National Divorce Rate
# Rename columns and drop the first 3 rows
national_divorce.columns = ['year', 'Divorces & annulments', 'Population',
                            'Rate per 1,000 total population']
national_divorce = national_divorce.drop(national_divorce.index[0:3]) \
       .reset_index(drop=True)
# Correct Year column
years = []
for year in national_divorce['year']:
    first_year = year[:4]
    years.append(first_year)
national_divorce = national_divorce.drop(columns='year')
national_divorce['year'] = years
# Reorder column
national_divorce \
       = national_divorce[['year', 'Divorces & annulments', 'Population',
                           'Rate per 1,000 total population']]
# Save to csv file
national_divorce.to_csv(r'data_extraction\cleaned_data\us_divorce_rate.csv',
                        index=False)


##################################################
# # Divorce Rate by Occupation
url = 'https://docs.google.com/spreadsheets/d/1-JVVCiuXBZEpU6_5HsZLYyblVClpEW0ucYBafkNbaYI/pubhtml#'  # noqa
html_tables = pd.read_html(url, header=1, index_col=0)
df_occupation = html_tables[0]
# Rename
df_occupation = df_occupation.rename(columns={"OCC": "occ"})
# Delete duplicates
df_occupation = df_occupation.drop_duplicates(subset='occ')
# Save to csv file
df_occupation \
       .to_csv(r'data_extraction\cleaned_data\divorce_by_occupation.csv',
               index=False)


############################################################
# # Marriage and Divorce Rate by Race

dfs = read_pdf(r'data_extraction\nihms777225.pdf',
               pages='all', multiple_tables=True)

# Marriage rate by Race
marriage_race = dfs[0].iloc[:7].reset_index(drop=True)
marriage_race.columns = marriage_race.iloc[0]
marriage_race = marriage_race.drop(marriage_race.index[0])
marriage_race = marriage_race.dropna(axis=1, how='all')
# Column 'American Indian/Native Alaskan Hispanic, Total' are grouped together
# Split column 'American Indian/Native Alaskan Hispanic, Total'
marriage_race[['American Indian/Native Alaskan', 'Hispanic, Total']] \
       = marriage_race['American Indian/Native Alaskan Hispanic, Total'] \
       .str.split(expand=True)
# Drop column 'American Indian/Native Alaskan Hispanic, Total'
marriage_race = marriage_race \
       .drop(columns='American Indian/Native Alaskan Hispanic, Total')
races = ['White', 'Black', 'Asian/Pacific Islander',
         'American Indian/Native Alaskan', 'Hispanic, Total',
         'Hispanic, U.S. born', 'Hispanic, foreign born']
# Unpivot table
melt_marriage_race = pd.melt(marriage_race, id_vars=['Age'], value_vars=races)
melt_marriage_race.columns = ['Age', 'Race', 'Marriage_Rate']
# Pivot table
pivot_marriage_race \
       = pd.pivot_table(melt_marriage_race, values='Marriage_Rate',
                        index=['Age'], columns=['Race'], aggfunc=np.sum)
# Save to csv file
pivot_marriage_race \
       .to_csv(r'data_extraction\cleaned_data\marriage_rate_by_race.csv',
               index=False)


# ## Divorce Rate by Race
# DIVORCE rate by Race
divorce_race = dfs[0].iloc[8:].reset_index(drop=True)
divorce_race.columns = divorce_race.iloc[0]
divorce_race = divorce_race.drop(divorce_race.index[0])
divorce_race = divorce_race.dropna(axis=1, how='all')
# Column 'American Indian/Native Alaskan Hispanic, Total' are grouped together
# Split column 'American Indian/Native Alaskan Hispanic, Total'
divorce_race[['American Indian/Native Alaskan', 'Hispanic, Total']] \
       = divorce_race['American Indian/Native Alaskan Hispanic, Total'] \
       .str.split(expand=True)
# Drop column 'American Indian/Native Alaskan Hispanic, Total'
divorce_race = divorce_race. \
       drop(columns='American Indian/Native Alaskan Hispanic, Total')
# Unpivot table
melt_divorce_race = pd.melt(divorce_race, id_vars=['Age'], value_vars=races)
melt_divorce_race.columns = ['Age', 'Race', 'Divorce_Rate']
melt_divorce_race.head()
# Pivot table
pivot_divorce_race = pd.pivot_table(melt_divorce_race, values='Divorce_Rate',
                                    index=['Age'], columns=['Race'],
                                    aggfunc=np.sum)

# Save to csv
pivot_divorce_race.to_csv(r'data_extraction\cleaned_data\divorce_rate_by_race.csv',  # noqa
                          index=True)

#####################################################
# Save to postgreSQL
# Set up database
try:
    db_string = f'postgres://postgres:{db_password}@127.0.0.1:5432/divorce_prediction'  # noqa
except:
    print('Error creating connection string')

# Create database engine
engine = create_engine(db_string)
# Save occupation dataframe to database
national_marriage.to_sql("national_marriage", engine,
                         if_exists='replace', index=False)
national_divorce.to_sql("national_divorce", engine,
                        if_exists="replace", index=False)
df_occupation.to_sql('divorce_by_occupation', engine,
                     if_exists="replace", index=False)

# Set primary key
engine.execute('ALTER TABLE national_marriage ADD PRIMARY KEY (year);')
engine.execute('ALTER TABLE national_divorce ADD PRIMARY KEY (year);')
engine.execute('ALTER TABLE divorce_by_occupation ADD PRIMARY KEY (occ);')
