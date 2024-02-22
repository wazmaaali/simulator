import Events as Events
import Schedular as Schedular
import Network as Network
import Packet as Packet

import os
import random
import time

class Simulator:
    def __init__(self,schedular,network,model,n,m=None):
        self.schedular = schedular
        print("here")
        self.network =network
        self.model = model
        self.n = n
        self.m = m
        # self.run_event()
        self.generate_events(100)
        
    def generate_events(self,num_events):
        net = self.network_topology()
        nodes_list = list(net.nodes())

        packet= Packet.Packet(nodes_list[0],nodes_list[30],1024)

        for i in range(num_events):
            random.seed(os.urandom(10))
            # Generate an exponential arrival time
            arrival_time = random.expovariate(random.randint(1, 10))
            # Generate an exponential departure time
            dep_time = arrival_time + random.expovariate(random.randint(1, 10))
            
            print(f"Iteration {i}, Arrival Time: {arrival_time:.2f}, Departure Time: {dep_time:.2f}")
            # Small sleep to ensure the time-based seed changes between iterations
            time.sleep(0.1)
            packet.arrival_time = arrival_time
            _event = Events.Events(arrival_time,dep_time,packet)
            self.schedular.schedule_event(_event)
            self.process_packet_arrival(_event, net,packet)
            self.schedular.next_event() #next event called after first event has been processed in order to keep a check of global time
    
    def run_event(self):
               
        while True:
            current_event = self.schedular.next_event()
            if current_event is None:  # No more events to process
                break
            self.generate_events(100)

        
    def process_packet_arrival(self,event, network,packet):
        path=self.network.dijkstra(network,packet.source,packet.dest)
        
        if path:
            event.departure_event(packet)
            print(f"Packet from {packet.source} to {packet.dest} will take path: {path}")
        else:
            print(f"No path found from {packet.source} to {packet.dest}")
            
    def network_topology(self):
        if self.model == "B":
            return self.network.BarabsiAlbertModel(self.n, self.m)
        elif self.model == "W":
            return self.network.WaxmanModel(self.n)
        else:
            print("None")
        
            
            
if __name__ == "__main__":
    a=Schedular.Schedular()
    b= Network.Network()
    model = "B"
    nodes=100
    num_edges = 2
    c = Simulator(a,b,model,nodes,num_edges) 
