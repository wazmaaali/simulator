
class Packet:
    def __init__(self, source, dest, size, arrival_time=None):
        self.source = source
        self.dest = dest
        self.size = size
        self.arrival_time = arrival_time