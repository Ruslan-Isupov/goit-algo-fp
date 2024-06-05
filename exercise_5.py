import uuid
import heapq
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
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def build_heap_tree(heap, index=0):
  if index >= len(heap):
    return None
  node = Node(heap[index])
  left_index = 2 * index + 1
  right_index = 2 * index + 2
  node.left = build_heap_tree(heap, left_index)
  node.right = build_heap_tree(heap, right_index)
  return node

def generate_color(step, total_steps):
  base_color = [70, 130, 180] 
  lighten_factor = step / total_steps
  new_color = [min(255, int(c + (255 - c) * lighten_factor)) for c in base_color]
  return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'

def dfs_visualize(root, total_steps):
  visited = set()
  stack = [root]
  colors = {}
  step = 0

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      colors[node.id] = generate_color(step, total_steps)
      step += 1

      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)

  return colors

def bfs_visualize(root, total_steps):
  visited, queue = set(), [root]
  colors = {}
  step = 0

  while queue:
    node = queue.pop(0)
    if node not in visited:
      visited.add(node)
      colors[node.id] = generate_color(step, total_steps)
      step += 1

      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  return colors

def count(node):
  if node is None:
    return 0
  return 1 + count(node.left) + count(node.right)  

heap = [1, 4, 6, 8, 9, 2, 3, 28, 5, 3, 6]
heapq.heapify(heap)
heap_tree_root = build_heap_tree(heap)

total_steps = count(heap_tree_root)

# DFS visualization
dfs_colors = dfs_visualize(heap_tree_root, total_steps)
draw_tree(heap_tree_root, dfs_colors)

# BFS visualization
bfs_colors = bfs_visualize(heap_tree_root, total_steps)
draw_tree(heap_tree_root, bfs_colors)