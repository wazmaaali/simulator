



class Events:
    def __init__(self,arrival_time = None,departure_time = None,packet =None):
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.packet = packet
        
        
    def arrival_event(self,packet):
        print("Packet arrival event recieved of packet size: ",packet.size," at time= ",packet.arrival_time)
    def departure_event(slef,packet):
        print("Packed departure event recieved of packet size: ",packet.size)
       
            
