import os
import django
import sys
import pandas as pd
import logging

# 添加项目根目录到 Python 路径
project_root = 'f:\\zyy_wto\\webgis'
if project_root not in sys.path:
    sys.path.append(project_root)
# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webgis.settings')
django.setup()

# 现在可以导入 Django 模型
from wto.models import TradeYearIndex_, Country, ProductSector

# 读取 Excel 文件
df = pd.read_excel('F:/zyy_wto/data/WtoData_export_i.xlsx')
df.fillna(0, inplace=True)  # 将所有的 nan 值替换为 0

# 获取年份列名
year_columns = [2022,2021,2020,2019,2018,2017,2016,2015]

for index, row in df.iterrows():
    # 提取数据
    reporting_country_name = row['Reporting Economy']

    # 根据国家名称和产品/部门名称获取相应的对象或创建新对象
    reporting_country, _ = Country.objects.get_or_create(name=reporting_country_name)
   
    for year_col in year_columns:
        year = int(year_col)
        export_value_y = row[year_col]
        # import_value_y = row[year_col]  # 如果你也需要导入值

        # 创建或更新 TradeYearData 对象
        TradeYearIndex_I.objects.create(
            reporting_country=reporting_country,
            year=year,
            import_value_i=export_value_y,
            # import_value_y=import_value_y,
        )