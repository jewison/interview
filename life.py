import numpy as np
import copy
import os


# 临近点的个数
def near_num(array, point):
    num = -array[point[0]][point[1]]
    around = [-1, 1, 0]
    # 遍历这个细胞周围的细胞
    for i in around:
        for j in around:
            if array[point[0] + i][point[1] + j] == 1:
                num += 1
    return num


# 刷新
def refresh(game_map):
    copy_map = copy.copy(game_map)
    # 遍历地图的每一个细胞
    for x in range(copy_map.shape[0] - 1):
        for y in range(copy_map.shape[1] - 1):
            # 游戏生存规则
            num = near_num(copy_map, [x, y])
            if num > 3:
                game_map[x][y] = 0
            elif num == 3:
                game_map[x][y] = 1
            elif num == 0 or num == 1:
                game_map[x][y] = 0
    return game_map


# 输出
def output(game_map):
    # 遍历地图，如果有细胞标记M
    for line in game_map:
        out_line = " "
        for point in line:
            if point == 1:
                out_line += "M"
            else:
                out_line += " "
            out_line += " "
        print(out_line)
    return "done"


# 地图的尺寸
size = 100
# 初始的细胞数
start_num = 1800
mid = int(size / 2)
# 初始化地图函数
game_map = np.zeros([size, size])
# 随机生成输出初始数量的细胞，并生成坐标
start_point_x = np.random.randint(0, size, size=start_num)
start_point_y = np.random.randint(0, size, size=start_num)
for i in range(len(start_point_x)):
    game_map[start_point_x[i]][start_point_y[i]] = 1

while True:
    # 生存设置为0
    alive = 0
    # 清屏
    os.system("cls")
    # 输出
    output(game_map)
    for line in game_map:
        for point in line:
            if point == 1:
                alive += 1
    print(alive)
    # 刷新新的地图函数
    game_map = refresh(game_map)
