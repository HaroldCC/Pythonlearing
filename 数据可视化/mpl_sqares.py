import matplotlib.pyplot as plt

'''
######未提供输入值，图形会有些许偏差######
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)
'''
# 提供输入值版本
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("平方数", fontsize=24)
plt.xlabel("值", fontsize=14)
plt.ylabel("平方值", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
