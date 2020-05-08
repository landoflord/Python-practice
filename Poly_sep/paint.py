import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import matplotlib.path as mpath



def function_points_generator (points, function_from_catalog, ind):
    """ Генератор массивов np.array для f=0 и f=1 по для функции из каталога.
    """
    f_0 = []
    f_1 = []
    func_id = function_from_catalog.split('#')[1].strip()
    func_values =  function_from_catalog.split('#')[0].split(';')
    if ind:
        func_values = transform_for_painting(func_values)
    n = len(func_values)
    for i in range(n):
        if func_values[i] == '1':
            f_1.append(points[i])
        else:
            f_0.append(points[i])
    return np.array(f_0), np.array(f_1), func_id

def transform_for_painting(func_values):
    """ Функция преобразовывает значения исходной функции для рисования иначе точка (0;0;0) будем ближней левой 
    """
    func_values_new = [
        func_values[8],
        func_values[10],
        func_values[0],
        func_values[2],
        func_values[12],
        func_values[14],
        func_values[4],
        func_values[6],
        func_values[9],
        func_values[11],
        func_values[1],
        func_values[3],
        func_values[13],
        func_values[15],
        func_values[5],
        func_values[7]]
    return func_values_new

def cube_painting(line):
    """ Функций рисования куба
    """
    points = np.array([[0, 0, 0],
                    [0, 0, 3],
                    [0, 3, 0],
                    [0, 3, 3],
                    [3, 0, 0],
                    [3, 0, 3],
                    [3, 3, 0],
                    [3, 3, 3],
                    [2, 2, 5],
                    [2, 2, 8],
                    [2, 5, 5],
                    [2, 5, 8],
                    [5, 2, 5],
                    [5, 2, 8],
                    [5, 5, 5],
                    [5, 5, 8]])

    # Увеличение переменной X3 для того чтобы куб визуально отображался как куб а не параллелипипед
    n = points.shape[0]
    for i in range(n):
        points[i] = [points[i][0],points[i][1],points[i][2]*(2/1.5)] 

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlim(0,8)
    ax.set_ylim(0,8)
    ax.set_zlim(0,8)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('X3')
    
    plt.axis('off')


    # Рисуем стороны и ребра. Задаем линии движения
    verts = [[points[0],points[1]],[points[0],points[2]],
    [points[0],points[4]],[points[1],points[3]],
    [points[1],points[5]],[points[2],points[3]],
    [points[2],points[6]],[points[3],points[7]],
    [points[4],points[5]],[points[4],points[6]],
    [points[5],points[7]],[points[6],points[7]],
    [points[8],points[9]],[points[8],points[10]],
    [points[8],points[12]],[points[9],points[11]],
    [points[9],points[13]],[points[10],points[11]],
    [points[10],points[14]],[points[11],points[15]],
    [points[12],points[13]],[points[12],points[14]],
    [points[13],points[15]],[points[14],points[15]],
    [points[2],points[10]]]

    ax.add_collection3d(Poly3DCollection(verts, 
    facecolors='black', linewidths=1, edgecolors='black', alpha=.25))
    
    (f_0, f_1, func_id) = function_points_generator(points, line, True)
    if f_0.size !=0:
        ax.scatter3D(f_0[:, 0], f_0[:, 1], f_0[:, 2], marker='o', c= 'white', s= 70, linewidths=1,edgecolors='black', alpha = 1)
    if f_1.size !=0:
        ax.scatter3D(f_1[:, 0], f_1[:, 1], f_1[:, 2], marker='o', c= 'black', s= 70, linewidths=1,edgecolors='black', alpha = 1)
    plt.suptitle(f'Номер в каталоге Никонова В. Г.\n {func_id}', fontsize=10)
    plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '\\Pictures_for_catalog'+ '\\' + func_id + '.png', dpi=fig.dpi)
    plt.close(fig)
    
def main():
    with open (function_values_path) as func_values:
        lines = func_values.readlines()
        for line in lines:
            cube_painting(line)


if __name__ == "__main__":
    function_values_path = os.path.dirname(os.path.realpath(__file__))+ '\\' + 'functions.txt'
    main()



