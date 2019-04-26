import tushare as ts
import pandas as pd









if __name__ == '__main__':
   con = ts.get_apis()
   df = ts.get_stock_basics()
   print(df)