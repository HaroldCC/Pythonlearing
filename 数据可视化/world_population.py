import json

import pygal

# 改变基色
from pygal.style import RotateStyle

# 亮色
from pygal.style import LightColorizedStyle

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'C:\\Users\\1921189869\\Desktop\\python\\.vscode\\数据可视化\\population_data.json'
with open(filename) as f:
    pop_date = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_date:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # 因为文件中的键和值都是字符串，因此要将字符串转换为数字
        # 由于字符串中存在小数，int()不能直接将小数字符串转换为整数
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 为地图样式提供一种基色,RotateStyle()参数以#开头的十六进制颜色
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10-1bm', cc_pops_2)
wm.add('>1bm', cc_pops_3)

wm.render_to_file('world_population.svg')
