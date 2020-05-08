import sys

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

from itertools import product


def get_name_values(line):
    func_temp, name = line.split('#')
    func = [int(i) for i in func_temp.split(';')]

    return name, func


def get_4d_to_3d_coordinates(point):
    return [i + point[3] * 1.5 for i in point[:-1]]


def draw_point(ax, point, res):
    values = get_4d_to_3d_coordinates(point)

    ax.text(values[0], values[1], values[2], f'({point[0]}, {point[1]}, {point[2]}, {point[3]})', ha='center',
            va='bottom')

    color = 'black'
    marker = 'o'
    size = 70
    alpha = 1
    linewidths=1
    edgecolors='black'

    if res == 0:
        color = 'white'
        marker = 'o'
        size = 70
        alpha = 1
        linewidths=1
        edgecolors='black'


    ax.scatter(values[0], values[1], values[2], c=color, marker=marker, s=size, alpha = alpha, linewidths = linewidths, edgecolors = edgecolors)


def get_edges(cube):
    points = [get_4d_to_3d_coordinates(point[0]) for point in cube]

    return [
        [points[0], points[1], points[5], points[4]],
        [points[0], points[1], points[3], points[2]],
        [points[1], points[3], points[7], points[5]],
        [points[4], points[5], points[7], points[6]],
        [points[2], points[3], points[7], points[6]],
        [points[0], points[2], points[6], points[4]],
    ]


def draw_edges(ax, cube):
    ax.add_collection3d(Poly3DCollection(get_edges(cube), facecolors='black', linewidths=1, edgecolors='black', alpha=.25))


def draw_cube(ax, cube):
    for point in cube:
        draw_point(ax, point[0], point[1])

    draw_edges(ax, cube)


def draw_cubes(ax, points, res):
    d = [(c, v) for (c, v) in zip(points, res)]
    cube_before, cube_after = d[::2], d[1::2]

    draw_cube(ax, cube_before)
    draw_cube(ax, cube_after)


def draw_x4(ax, point):
    point_after = get_4d_to_3d_coordinates(point)

    xyz = [[coord_new, coord] for [coord_new, coord] in zip(point_after, point)]

    ax.plot3D(xyz[0], xyz[1], xyz[2])
    #ax.text(xyz[0][0] - 1, xyz[1][0] - 1, xyz[2][0] - 1, 'X4', (1, 1, 1), fontsize=30)


def draw_plot(lines):
    x4_end_point = [.0, 1.0, .0, 1]
    

    for line in lines:
        name, val = get_name_values(line)
        points = [i for i in product((0, 1), repeat=4)]

        fig = plt.figure(figsize=(18, 18))
        ax = plt.axes(projection="3d")

        #ax.set_xlabel('X1', fontsize=30)
        ax.set_xticklabels([])
        #ax.set_ylabel('X2', fontsize=30)
        ax.set_yticklabels([])
        #ax.set_zlabel('X3', fontsize=30)
        ax.set_zticklabels([])

        plt.suptitle(f'Номер в каталоге Никонова В. Г.\n№ {name}', fontsize=30)

        draw_cubes(ax, points, val)

        draw_x4(ax, x4_end_point)
        plt.axis('off')
        plt.savefig(name + '.png', dpi=fig.dpi)
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    content = []

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            content = [line.rstrip() for line in f]
    else:
        content.append('0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0#0.0.1.1')

    draw_plot(content)
