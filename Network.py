# nodes 
# ids 
# connection 
import matplotlib.pyplot as plt
import networkx as 
import random

class Network:
    def __init__(self):
        self.graph = None
        
    def BarabsiAlbertModel(self, n, m, seed=None):
        """
         Parameters:
        - n: Number of nodes
        - m: Number of edges to attach from a new node to existing nodes
        - seed: Seed for random number generator (optional)
        """
        self.graph = nx.barabasi_albert_graph(n, m, seed=seed)
        print(f"Generated Barabási-Albert topology with {n} nodes and {m} edges per new node.")
        generate_network_topology()
        
    def WaxmanModel(self, n, alpha=0.4, beta=0.1, L=None, domain=(0, 0, 1, 1), seed=None):
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
        self.graph = nx.waxman_graph(n, alpha=alpha, beta=beta, L=L, domain=domain, seed=seed)
        print(f"Generated Waxman topology with {n} nodes, alpha={alpha}, beta={beta}.")
        generate_network_topology()

    def generate_network_topology():
        nodes = {node_id: Node(node_id) for node_id in self.graph.nodes()}
        bandwidth_range = (100, 1000)  # Mbps
        latency_range = (5, 50)  # mi
        for node1, node2 in graph.edges():
            bandwidth = random.randint(*bandwidth_range)
            latency = random.randint(*latency_range)
            link = Link(nodes[node1], nodes[node2], bandwidth, latency)
            nodes[node1].add_link(link)
            nodes[node2].add_link(link)  # Assuming bidirectional links
        
    return nodes
        
    
    
    def display_graph(self):
        """
        Displays the generated network graph. Requires matplotlib.
        """
        if self.graph:
            nx.draw(self.graph, with_labels=True, node_size=700, node_color="lightblue")
            plt.show()
        else:
            print("No network topology has been generated yet.")


class Packet:
    def __init__(self, source, dest, size, arrival_time):
        self.source = source
        self.dest = dest
        self.size = size
        self.arrival_time = arrival_time

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