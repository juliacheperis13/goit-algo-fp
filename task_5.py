import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def bfs_traversal(root, initial_color):
    if not root:
        return []

    result = []
    queue = [root]
    current_color = initial_color

    while queue:
        current_node = queue.pop(0)  # Dequeue the front element
        result.append(current_node.val)
        current_node.color = current_color
        current_color = lighten_color(current_color)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return result


def dfs_traversal(root, initial_color):
    result = []
    if not root:
        return result

    current_color = initial_color

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        nonlocal current_color
        node.color = current_color
        current_color = lighten_color(current_color)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def lighten_color(hex_color, factor=1.4):
    if not (hex_color.startswith("#") and len(hex_color) == 7):
        raise ValueError("Invalid hex color format")

    rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    lightened_rgb = tuple(int(min(255, channel * factor)) for channel in rgb)
    lightened_hex_color = "#{:02X}{:02X}{:02X}".format(*lightened_rgb)

    return lightened_hex_color


def bfs_traversal_draw():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    original_color = "#331429"
    bfs_traversal(root, original_color)
    draw_tree(root)


def dfs_traversal_draw():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    original_color = "#d2691e"
    dfs_traversal(root, original_color)
    draw_tree(root)


if __name__ == "__main__":
    bfs_traversal_draw()
    dfs_traversal_draw()
