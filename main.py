import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

def calculate_and_draw_cubes():
    # 詢問容器的尺寸
    container_x = float(input("請輸入容器的長度(X)："))
    container_y = float(input("請輸入容器的寬度(Y)："))
    container_z = float(input("請輸入容器的高度(Z)："))

    # 詢問立方體的尺寸
    cube_x = float(input("請輸入立方體的長度(X)："))
    cube_y = float(input("請輸入立方體的寬度(Y)："))
    cube_z = float(input("請輸入立方體的高度(Z)："))

    # 計算容器中可以放入的立方體數量
    number_of_cubes_x = int(container_x // cube_x)
    number_of_cubes_y = int(container_y // cube_y)
    number_of_cubes_z = int(container_z // cube_z)
    number_of_cubes = number_of_cubes_x * number_of_cubes_y * number_of_cubes_z

    # 輸出結果
    print("容器中最多可以放入 {} 個立方體。".format(int(number_of_cubes)))
    print("在X軸方向上最多可以放入 {} 個立方體。".format(int(number_of_cubes_x)))
    print("在Y軸方向上最多可以放入 {} 個立方體。".format(int(number_of_cubes_y)))
    print("在Z軸方向上最多可以放入 {} 個立方體。".format(int(number_of_cubes_z)))

    # 建立一個 3D 座標系統
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 繪製立方體
    for x in range(number_of_cubes_x):
        for y in range(number_of_cubes_y):
            for z in range(number_of_cubes_z):
                r = random.random()
                g = random.random()
                b = random.random()
                ax.bar3d(x*cube_x, y*cube_y, z*cube_z, cube_x, cube_y, cube_z, color=(r, g, b), shade=True)
    
    # 繪製一個半透明的容器立方體
    ax.bar3d(0, 0, 0, container_x, container_y, container_z, color=(0.7, 0.7, 0.7, 0.2), shade=True)
    

    # 設置圖表的標題和軸標籤
    ax.set_title("容器中的立方體")
    ax.set_xlabel("在X軸方向上最多可以放入 {} 個立方體。".format(int(number_of_cubes_x)))
    ax.set_ylabel("在Y軸方向上最多可以放入 {} 個立方體。".format(int(number_of_cubes_y)))
    ax.set_zlabel("在Z軸方向上最多可以放入 {} 個立方體。".format(int(number_of_cubes_z)))


    # 鎖定 XYZ 軸比例
    ax.set_box_aspect([container_x, container_y, container_z])

    # 顯示圖形
    plt.show()

calculate_and_draw_cubes()
