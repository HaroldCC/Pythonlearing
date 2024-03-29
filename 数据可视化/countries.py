'''
Pygal中的地图制作工具要求数据为特定的格式：用国别码表示国家，
以及用数字表示人口数量。处理地理政治数据时，
经常需要用到几个标准化国别码集。
population_data.json中包含的是三个字母的国别码，
但Pygal使用两个字母的国别码。
我们需要想办法根据国家名获取两个字母的国别码。
Pygal使用的国别码存储在模块i18n （internationalization的缩写）中。
字典COUNTRIES 包含的键和值分别为两个字母的国别码和国家名。
要查看这些国别码，可从模块i18n 中导 入这个字典，
并打印其键和值
'''

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
