import networkx as nx
import matplotlib.pyplot as plt
import heapq

G = nx.DiGraph()

G.add_node("A", pos=(0, 0))
G.add_node("B", pos=(1, 0))
G.add_node("C", pos=(2, 0))
G.add_node("D", pos=(1, 1))
G.add_node("E", pos=(1, -1))


G.add_edge("A", "B", weight=8)
G.add_edge("B", "C", weight=4)
G.add_edge("B", "D", weight=5)
G.add_edge("B", "E", weight=7)

def dijkstra(graph, start):
    
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)
   
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
       
    return shortest_paths


# Visualization
start_vertex = "A"
shortest_distances = dijkstra(G, start_vertex)
print(f"The shortest distances fron vertex {start_vertex}: {shortest_distances}")

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12, font_weight="bold", arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()