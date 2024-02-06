import matplotlib.pyplot as plt
import networkx as nx
import uuid
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


def lighten_color(hex_color, increment=15):
    """Returns a lighter shade of the given hex color."""
    color = int(hex_color[1:], 16)
    r = min((color >> 16) + increment, 255)
    g = min(((color >> 8) & 0x00FF) + increment, 255)
    b = min((color & 0x0000FF) + increment, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


def bfs_colorization(root, main_color='#1296F0'):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        current_node.color = main_color = lighten_color(main_color)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

    return root




def dfs_colorization(node, main_color='#1296F0'):
    def inner(node):
        if node is not None:
            nonlocal main_color
            node.color = main_color = lighten_color(main_color)
            inner(node.left)
            inner(node.right)

    inner(node)
    return root


draw_tree(bfs_colorization(root), 'BFS')
draw_tree(dfs_colorization(root), 'DFS')
