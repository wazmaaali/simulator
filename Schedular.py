
import Constants as Constants
import heapq

#Maintain global time

class Schedular:
    def __init__(self):
        self.event_queue=[]
    
    #This heapq save the event according to time in chronological order
    def schedule_event(self, event):
        heapq.heappush(self.event_queue, (event.arrival_time, event))
        event.arrival_event()
    
    def next_event(self):
        if self.event_queue:
            next_event =  heapq.heappop(self.event_queue)[1]
            Constants.GLOBAL_TIME = next_event.arrival_time
            # event.departure_event()
            return next_event
        return None