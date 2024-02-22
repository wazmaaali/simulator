# nodes 
# ids 
# connection 
import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq
class Network:
    def __init__(self):
        self.graph = None
        
    def BarabsiAlbertModel(self, n, m):
        """
         Parameters:
        - n: Number of nodes
        - m: Number of edges to attach from a new node to existing nodes
        - seed: Seed for random number generator (optional)
        """
        self.graph = nx.barabasi_albert_graph(n, m)
        print(f"Generated Barabási-Albert topology with {n} nodes and {m} edges per new node.")
        return self.generate_network_topology()
        
    def WaxmanModel(self, n):
        """
        Generates a network topology using the Waxman model.
        
        Parameters:
        - n: Number of nodes
        - alpha: Model parameter
        - beta: Model parameter
        - L: Maximum distance between nodes (optional, defaults to the maximum distance in the domain)
        - domain: Tuple specifying the domain rectangle (xmin, ymin, xmax, ymax)
        - seed: Seed for random number generator (optional)
        """
        self.graph = nx.waxman_graph(n)
        print(f"Generated Waxman topology with {n} nodes.")
        return self.generate_network_topology()

    def generate_network_topology(self):
        nodes = {node_id: Node(node_id) for node_id in self.graph.nodes()}
        bandwidth_range = (100, 1000)  # Mbps
        latency_range = (5, 50)  # mi
        for node1, node2 in self.graph.edges():
            bandwidth = random.randint(*bandwidth_range)
            latency = random.randint(*latency_range)
            link = Link(nodes[node1], nodes[node2], bandwidth, latency)
            nodes[node1].add_link(link)
            nodes[node2].add_link(link)  # Assuming bidirectional links        
        return self.graph
        
    
    
    def display_graph(self):
        """
        Displays the generated network graph. Requires matplotlib.
        """
        if self.graph:
            nx.draw(self.graph, with_labels=True, node_size=700, node_color="lightblue")
            plt.show()
        else:
            print("No network topology has been generated yet.")
            

    import heapq

    def dijkstra(self,network, start, goal):
        # Initial distances are set to infinity
        distances = {node: float('infinity') for node in network.nodes()}

        # The distance to the start is 0
        distances[start] = 0
        # Priority queue for the nodes to visit
        pq = [(0, start, [])]  # (distance, node, path)
        
        while pq:
            # Pop the node with the smallest distance
            current_distance, current_node, path = heapq.heappop(pq)
            
            # Early termination if we reach the goal
            if current_node == goal:
                return path + [current_node]
            
            # Skip if we found a better path already
            if current_distance > distances[current_node]:
                continue
            

            for neighbor in network.neighbors(current_node):
                cost = 1
                distance = current_distance + cost
                
                # Only consider this new path if it's better than any known path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor, path + [current_node]))

        return None  # Goal not reachable




class Link:
    def __init__(self, node1, node2, bandwidth, latency):
        self.node1 = node1
        self.node2 = node2
        self.bandwidth = bandwidth
        self.latency = latency

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.links = []  # Links connected to this node
    
    def add_link(self, link):
        self.links.append(link)  