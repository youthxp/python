import tushare as ts
import pandas as pd
import time
from multiprocessing.dummy import Pool









if __name__ == '__main__':
    '''
    测试
    '''
    t1 = time.perf_counter()
    con = ts.get_apis()
    df = ts.get_stock_basics()
    t = time.perf_counter() - t1
    print(df)
