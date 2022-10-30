import sqlite3
import pandas as pd

con = sqlite3.connect('comp_data.db')
wb = pd.ExcelFile('components.xlsx')
for sheet in wb.sheet_names:
    df = pd.read_excel('components.xlsx', sheet_name='components')
    df.to_sql(sheet, con, index=True, if_exists="replace", )

con.commit()
con.close()
