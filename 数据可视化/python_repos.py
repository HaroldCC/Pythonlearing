import requests

import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
'''
我们调用get() 并将URL传递给它，再将响应对象存储在 变量r 中。
响应对象包含一个名为status_code 的属性，
它让我们知道请求是否成功了（状态码200表示请求成功）。
'''
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
'''
这个API返回JSON格式的信息，
因此我们使用方法json() 将这些信息转换为一个Python字典.
'''
response_dict = r.json()
print("储存库总量：", response_dict['total_count'])

# 搜索有关仓库的信息
repo_dicts = response_dict['items']
print("返回的存储库：", len(repo_dicts))

'''
# 输出仓库信息
repo_dict = repo_dicts[0]

print("\n关于每个存储库的选定信息:")
for repo_dict in repo_dicts:
    print('名称：', repo_dict['name'])

    # 项目所有者是用一个字典表示的，我们使用键owner来访问 表示所有者的字典，
    # 再使用键key 来获取所有者的登录名。
    print('作者：', repo_dict['owner']['login'])
    print('收藏：', repo_dict['stargazers_count'])
    print('仓库：', repo_dict['html_url'])
    print('创造：', repo_dict['created_at'])
    print('最新：', repo_dict['updated_at'])
    print('描述：', repo_dict['description'])
'''

# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("项目数：", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 下行代码由于有些description为空，所以会导致不成功
        # 因此，需要用str()转换为字符串
        # 或者判断进行填充
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'GitHub上最著名的Python项目'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
