# 锡特卡2014年7月份天气图
'''
import csv

from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = 'C:\\Users\\19211\\Desktop\\python\\.vscode\\数据可视化\\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("2014年7月日最高温", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("温度（F）", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''

'''
# 锡特卡2014年天气图
import csv

from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = 'C:\\Users\\19211\\Desktop\\python\\.vscode\\数据可视化\\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
"""实参alpha 指定颜色的透明度。Alpha 值为0表示完全透明，
1（默认设置）表示完全不透明。"""
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
"""向fill_between() 传递了一个 x 值系列：列表dates ，
还传递了两个 y 值系列：highs 和lows 。
实参facecolor 指定了填充区域的颜色。"""
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("2014年日最高温和最低温", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("温度（F）", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''

# 捕获异常
import csv

from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = 'C:\\Users\\19211\\Desktop\\python\\.vscode\\数据可视化\\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")

            high = int(row[1])

            low = int(row[3])
        except ValueError:
            print(current_date, '无数据！')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
'''实参alpha 指定颜色的透明度。Alpha 值为0表示完全透明，
1（默认设置）表示完全不透明。'''
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
'''向fill_between() 传递了一个 x 值系列：列表dates ，
还传递了两个 y 值系列：highs 和lows 。
实参facecolor 指定了填充区域的颜色。'''
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("2014年日最高温和最低温\n加利福尼亚死亡谷", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("温度（F）", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
