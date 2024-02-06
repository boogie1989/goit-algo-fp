import matplotlib.pyplot as plt
import numpy as np


def draw_pifagoras_tree(ax, x1, y1, angle, depth, length):
    if depth == 0:
        return

    x2 = x1 + length * np.cos(np.radians(angle))
    y2 = y1 - length * np.sin(np.radians(angle))

    ax.plot([x1, x2], [y1, y2], color="brown")

    draw_pifagoras_tree(ax, x2, y2, angle - 45, depth - 1, length * 0.7)
    draw_pifagoras_tree(ax, x2, y2, angle + 45, depth - 1, length * 0.7)


def create_pifagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')

    start_x = 0
    start_y = 0
    start_angle = -90
    start_length = 100

    draw_pifagoras_tree(ax, start_x, start_y, start_angle, depth, start_length)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    recursion_depth = int(input("Введіть рівень рекурсії: "))
    create_pifagoras_tree(recursion_depth)
