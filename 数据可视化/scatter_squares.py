import matplotlib.pyplot as plt

'''
###绘制单个点###
plt.scatter(2, 4, s=200)

# 设置图表标题并给坐标轴加上标签
plt.title("平方值", fontsize=24)
plt.xlabel("值", fontsize=14)
plt.ylabel("平方值", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''

'''
# ##绘制一系列点###
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# 设置图表标题并给坐标轴加上标签
plt.title("平方值", fontsize=24)
plt.xlabel("值", fontsize=14)
plt.ylabel("平方值", fontsize=14)

plt.show()
'''

# ##自动计算数据###
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)
# 删除数据点的轮廓
# plt.scatter(x_values, y_values, edgecolor='none', s=40)
# 改变颜色
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
'''
使用RGB颜色模式自定义颜色。
要指定自定义颜色，可传递参数c ，
并将其设置为一个元组，其中包含三个0~1之间的小数值，
它们分别表示红色、绿色和蓝色分量。
值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
'''
# 设置渐变色
'''将参数c 设置成了一个 y 值列表，
并使用参数cmap 告诉pyplot 使用哪个颜色映射。
这些代码将 y 值较小的点显示为浅蓝色，
并将 y 值较大的点显示为深蓝色
'''
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("平方值", fontsize=24)
plt.xlabel("值", fontsize=14)
plt.ylabel("平方值", fontsize=14)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

# 图表显示
# plt.show()

# 图表保存至文件
plt.savefig('squares_plot.png', bbox_inches='tight')
