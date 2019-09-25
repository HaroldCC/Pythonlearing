# pass
import json

import pygal

# 将数据加载到列表
filename = 'C:\\Users\\19211\\Desktop\\python\\.vscode\\gdp_json.json'
with open(filename) as f:
    gdp_date = json.load(f)

# 创建国家GDP字典
world_gdp = {}
for gdp_dict in gdp_date:
    if gdp_dict['Year'] == '2010':
        country_name = gdp_dict['Country Name']
        print(country_name)