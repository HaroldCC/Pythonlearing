# 15-2
'''
import matplotlib.pyplot as plt

# 前五个数的立方
input_numbers = [1, 2, 3, 4, 5]
cubic_numbers = [x**3 for x in input_numbers]

plt.scatter(input_numbers, cubic_numbers, s=40)

# 坐标轴标签和图表标题
plt.title("数的立方", fontsize=24)
plt.xlabel("数", fontsize=14)
plt.ylabel("立方值", fontsize=14)

plt.show()

# 前五千个数的立方
x_numbers = list(range(1, 5001))
y_numbers = [x**3 for x in x_numbers]

plt.scatter(x_numbers, y_numbers, c=y_numbers, cmap = plt.cm.Reds,
            s=40)

plt.show()
'''
# 15-3
'''
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    """
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=10)
    """
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolor='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_runing = input("再次生成？(y/n):")
    if keep_runing == 'n':
        break
'''
# 15-4 将会走的更远，如果删除-1，将只会向一方延伸
'''
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolor='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_runing = input("再次生成？(y/n):")
    if keep_runing == 'n':
        break
'''
# 15-6
