#  입력 엑셀파일의 컬럼명 가정: title, review, category

import pandas as pd
import numpy as np
from df_xlsx_processing import export_xlsx
from tqdm import tqdm
import re
from konlpy.tag import Okt
import warnings
warnings.filterwarnings('ignore')

c_df = pd.read_csv('./dataset/origin_Csite_crawlingdata.csv', encoding='cp949')
i_df = pd.read_excel('./dataset/Isite_online.xlsx', engine='openpyxl')

c_res_df = export_xlsx.export_class101(c_df)
i_res_df = export_xlsx.export_idus(i_df)

