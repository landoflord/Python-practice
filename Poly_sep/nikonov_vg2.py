import sys

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


from itertools import product


def get_name_values(line):
    func_temp, name = line.split('#')
    func = [int(i) for i in func_temp.split(';')]

    return name, func


def get_4d_to_3d_coordinates(point):
    return [i + point[3] * 1.5 for i in point[:-1]]


def draw_point(ax, point, res, show_point_title=False):
    values = get_4d_to_3d_coordinates(point)

    if show_point_title:
        ax.text(values[0], values[1], values[2], f'({point[0]}, {point[1]}, {point[2]}, {point[3]})', ha='center',
            va='bottom')

    if res == 0:
        ax.scatter(values[0], values[1], values[2], linewidths=2, alpha=1, s=100, edgecolors='black', c='white')

    else:
        ax.scatter(values[0], values[1], values[2], linewidths=2, alpha=1, s=100, c='k')


def get_edges(cube):
    vertices = [[0, 1, 3, 2, 0], [4, 6, 7, 5, 4], [0, 2, 6, 4, 0], [0, 1, 5, 4, 0], [2, 3, 7, 6, 2]]

    points = [get_4d_to_3d_coordinates(point[0]) for point in cube]

    return [[points[vertices[ix][iy]] for iy in range(len(vertices[0]))] for ix in range(len(vertices))]


def draw_edges(ax, cube):
    ax.add_collection3d(Line3DCollection(get_edges(cube), colors='k', linewidths=.5, linestyles=':'))


def draw_cube(ax, cube):
    draw_edges(ax, cube)

    for point in cube:
        draw_point(ax, point[0], point[1])


def draw_cubes(ax, points, res):
    d = [(c, v) for (c, v) in zip(points, res)]
    cube_before, cube_after = d[::2], d[1::2]

    draw_cube(ax, cube_before)
    draw_cube(ax, cube_after)


def draw_x4(ax, point):
    x4 = [[point, get_4d_to_3d_coordinates(point)]]

    ax.add_collection3d(Line3DCollection(x4, colors='k', linewidths=.3))


def draw_plot(lines):
    x4_end_point = [.0, 1.0, .0, 1]
    points = [i for i in product((0, 1), repeat=4)]

    for line in lines:
        name, val = get_name_values(line)

        fig = plt.figure(figsize=(7, 7))
        ax = plt.axes(projection="3d")

        ax.set_xlabel('X1', fontsize=30)
        ax.set_xticklabels([])
        ax.set_ylabel('X2', fontsize=30)
        ax.set_yticklabels([])
        ax.set_zlabel('X3', fontsize=30)
        ax.set_zticklabels([])

        plt.suptitle(f'Номер в каталоге Никонова В. Г.\n№ {name}', fontsize=30)

        draw_cubes(ax, points, val)

        draw_x4(ax, x4_end_point)

        plt.axis('off')

        plt.savefig(name + '.png', dpi=fig.dpi)

        plt.show()
        plt.close(fig)


if __name__ == '__main__':
    content = []

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            content = [line.rstrip() for line in f]
    else:
        content.append('0;0;1;0;1;0;0;0;1;0;0;0;0;0;0;1#4.4.1.4')

    draw_plot(content)
